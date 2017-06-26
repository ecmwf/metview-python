import os
import shutil
from ._metview import ffi, lib



class Request(dict):
    verb = "UNKNOWN"

    def __init__(self, req):
        self.verb = ffi.string(lib.p_get_req_verb(req)).decode('utf-8')
        n = lib.p_get_req_num_params(req)
        for i in range(0,n):
            param = ffi.string(lib.p_get_req_param(req, i)).decode('utf-8')
            val   = ffi.string(lib.p_get_req_value(req, param.encode('utf-8'))).decode('utf-8')
            self[param] = val
        #self['_MACRO'] = 'BLANK'
        #self['_PATH']  = 'BLANK'
        #print(self)

    def __str__(self):
        return "VERB: " + self.verb + super().__str__()

    

def dict_to_request(d, verb='NONE'):

    # get the verb from the request if not supplied by the caller
    if verb=='NONE' and isinstance(d, Request):
        verb = d.verb

    r = lib.p_new_request(verb.encode('utf-8'))
    for k, v in d.items():
        if isinstance(v, list):
            for v1 in v:
                if isinstance(v1, str):
                    v1 = v1.encode('utf-8')
                lib.p_add_value(r, k.encode('utf-8'), v1)
        elif isinstance(v, str):
            lib.p_set_value(r, k.encode('utf-8'), v.encode('utf-8'))
        else:
            lib.p_set_value(r, k.encode('utf-8'), v)
    return r




# we can actually get these from Metview, but for testing we just have a dict
service_function_verbs = {
    'retrieve' : 'RETRIEVE',
    'mcoast'   : 'MCOAST',
    'mcont'    : 'MCONT',
    'read'     : 'READ',
}


def push_bytes(b):
    lib.p_push_string(b)


def push_str(s):
    push_bytes(s.encode('utf-8'))


def _call_function(name, *args):
    for n in args:
        if isinstance(n, int):
            lib.p_push_number(n)
        if isinstance(n, str):
            push_str(n)
        if isinstance(n, dict):
            lib.p_push_request(dict_to_request(n, service_function_verbs[name]))
    lib.p_call_function(name.encode('utf-8'), len(args))


def make(name):

    def wrapped(*args):
        err = _call_function(name, *args)
        #if err:
        #   throw Exce....

        rt = lib.p_result_type()
        if rt == 0: 
            return lib.p_result_as_number()
        elif rt == 1:
            return ffi.string(lib.p_result_as_string()).decode('utf-8')
        elif rt == 2:
            return ffi.string(lib.p_result_as_grib_path()).decode('utf-8')
        elif rt == 3:
            return_req = lib.p_result_as_request()
            return Request(return_req)
        else:
            return None

    return wrapped


lib.p_init()

pr       = make('print')
low      = make('lowercase')
ds       = make('describe')
waitmode = make('waitmode')
plot     = make('plot')
retrieve = make('retrieve')
read     = make('read')
mcont    = make('mcont')


####################### User Program ###############

# perform a MARS retrieval
# - defined a request
# - set waitmode to 1 to force synchronisation
# - the return is a path to a temporary file, so copy it before end of script
# req = { 'PARAM' : 't',
#         'LEVELIST' : ['1000', '500'],
#         'GRID' : ['2', '2']}
# waitmode(1)
# g = retrieve(req)
# print(g)
# copyfile(g, './result.grib')
