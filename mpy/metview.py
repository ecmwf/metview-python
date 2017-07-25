
import io
import os.path

from cffi import FFI


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding='utf-8').read()


try:
    ffi = FFI()
    ffi.cdef(read('metview.h'))
    lib = ffi.dlopen('libMvMacro.so')
    lib.p_init()
except:
    pass


class Request(dict):
    verb = "UNKNOWN"

    def __init__(self, req):
        if isinstance(req, dict):
            self.update(req)
            self.to_metview_style()
            if isinstance(req, Request):
                self.verb = req.verb
        else:
            self.verb = ffi.string(lib.p_get_req_verb(req)).decode('utf-8')
            n = lib.p_get_req_num_params(req)
            for i in range(0, n):
                param = ffi.string(lib.p_get_req_param(req, i)).decode('utf-8')
                val = ffi.string(lib.p_get_req_value(req, param.encode('utf-8'))).decode('utf-8')
                self[param] = val
            # self['_MACRO'] = 'BLANK'
            # self['_PATH']  = 'BLANK'

    def __str__(self):
        return "VERB: " + self.verb + super().__str__()

    # translate Python classes into Metview ones where needed
    def to_metview_style(self):
        for k, v in self.items():

            #if isinstance(v, (list, tuple)):
            #    for v_i in v:
            #        v_i = str(v_i).encode('utf-8')
            #        lib.p_add_value(r, k.encode('utf-8'), v_i)

            if isinstance(v, bool):
                conversion_dict = {True: 'on', False: 'off'}
                self[k] = conversion_dict[v]

    def push(self):
        r = lib.p_new_request(self.verb.encode('utf-8'))

        # to populate a request on the Macro side, we push each
        # value onto its stack, and then tell it to create a new
        # parameter with that name for the request. This allows us to
        # use Macro to handle the addition of complex data types to
        # a request
        for k, v in self.items():
            push_arg(v, 'NONAME')
            lib.p_set_request_value_from_pop(r, k.encode('utf-8'))

        lib.p_push_request(r)


#def dict_to_request(d, verb='NONE'):
#    # get the verb from the request if not supplied by the caller
#    if verb == 'NONE' and isinstance(d, Request):
#        verb = d.verb
#
#    r = lib.p_new_request(verb.encode('utf-8'))
#    for k, v in d.items():
#        if isinstance(v, (list, tuple)):
#            for v_i in v:
#                v_i = str(v_i).encode('utf-8')
#                lib.p_add_value(r, k.encode('utf-8'), v_i)
#        elif isinstance(v, (Fieldset, Bufr, Geopoints)):
#            lib.p_set_value(r, k.encode('utf-8'), v.push())
#        elif isinstance(v, str):
#            lib.p_set_value(r, k.encode('utf-8'), v.encode('utf-8'))
#        elif isinstance(v, bool):
#            conversion_dict = {True: 'on', False: 'off'}
#            lib.p_set_value(r, k.encode('utf-8'), conversion_dict[v].encode('utf-8'))
#        elif isinstance(v, (int, float)):
#            lib.p_set_value(r, k.encode('utf-8'), str(v).encode('utf-8'))
#        else:
#            lib.p_set_value(r, k.encode('utf-8'), v)
#    return r


#def push_dict(d, verb='NONE'):
#
#    for k, v in d.items():
#        if isinstance(v, (list, tuple)):
#            for v_i in v:
#                v_i = str(v_i).encode('utf-8')
#                lib.p_add_value(r, k.encode('utf-8'), v_i)
#        elif isinstance(v, (Fieldset, Bufr, Geopoints)):
#            lib.p_set_value(r, k.encode('utf-8'), v.push())
#        elif isinstance(v, str):
#            lib.p_set_value(r, k.encode('utf-8'), v.encode('utf-8'))
#        elif isinstance(v, bool):
#            conversion_dict = {True: 'on', False: 'off'}
#            lib.p_set_value(r, k.encode('utf-8'), conversion_dict[v].encode('utf-8'))
#        elif isinstance(v, (int, float)):
#            lib.p_set_value(r, k.encode('utf-8'), str(v).encode('utf-8'))
#        else:
#            lib.p_set_value(r, k.encode('utf-8'), v)
#    return r


def push_bytes(b):
    lib.p_push_string(b)


def push_str(s):
    push_bytes(s.encode('utf-8'))


def push_arg(n, name):

    nargs = 1

    if isinstance(n, int):
        lib.p_push_number(n)
    if isinstance(n, str):
        push_str(n)
    if isinstance(n, dict):
        Request(n).push()
    if isinstance(n, Fieldset):
        lib.p_push_grib(n.push())
    if isinstance(n, Bufr):
        lib.p_push_bufr(n.push())
    if isinstance(n, Geopoints):
        lib.p_push_geopoints(n.push())

    return nargs


def dict_to_pushed_args(d):

    # push each key and value onto the argument stack
    for k, v in d.items():
        push_str(k)
        push_arg(v, 'NONE')
        
    return 2 * len(d)  # return the number of arguments generated


class Fieldset:

    def __init__(self, fs):
        self.fs = fs

    def push(self):
        return self.fs

    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return sub(self, other)

    def __mul__(self, other):
        return prod(self, other)

    def __truediv__(self, other):
        return div(self, other)

    def __pow__(self, other):
        return power(self, other)


class Bufr:

    def __init__(self, bufr):
        self.bufr = bufr

    def push(self):
        return self.bufr


class Geopoints:

    def __init__(self, gpts):
        self.gpts = gpts
        #print('GC: ', self.url)

    def push(self):
        #print('GP: ', self.url)
        return self.gpts

    def __mul__(self, other):
        return prod(self, other)

    def __ge__(self, other):
        return greater_equal_than(self, other)

    def __gt__(self, other):
        return greater_than(self, other)

    def __le__(self, other):
        return lower_equal_than(self, other)

    def __lt__(self, other):
        return lower_than(self, other)

    def filter(self, other):
        return filter(self, other)


# we can actually get these from Metview, but for testing we just have a dict
# service_function_verbs = {
#     'retrieve': 'RETRIEVE',
#     'mcoast': 'MCOAST',
#     'mcont': 'MCONT',
#     'mobs': 'MOBS',
#     'msymb': 'MSYMB',
#     'read': 'READ',
#     'geoview': 'GEOVIEW',
#     'mtext': 'MTEXT',
#     'ps_output': 'PS_OUTPUT',
#     'obsfilter': 'OBSFILTER',
#     'filter': 'FILTER'
# }


def _call_function(name, *args, **kwargs):

    nargs = 0

    for n in args:
        actual_n_args = push_arg(n, name)
        nargs += actual_n_args

    merged_dict = {}
    merged_dict.update(kwargs)
    if len(merged_dict) > 0:
        dn = dict_to_pushed_args(Request(merged_dict))
        nargs += dn

    lib.p_call_function(name.encode('utf-8'), nargs)


def make(name):

    def wrapped(*args, **kwargs):
        err = _call_function(name, *args, **kwargs)
        #if err:
        #   throw Exce....

        rt = lib.p_result_type()
        # Number
        if rt == 0: 
            return lib.p_result_as_number()
        # String
        elif rt == 1:
            return ffi.string(lib.p_result_as_string()).decode('utf-8')
        # Fieldset
        elif rt == 2:
            return Fieldset(lib.p_result_as_grib())
        # Request dictionary
        elif rt == 3:
            return_req = lib.p_result_as_request()
            return Request(return_req)
        # BUFR
        elif rt == 4:
            return Bufr(lib.p_result_as_bufr())
        # Geopoints
        elif rt == 5:
            return Geopoints(lib.p_result_as_geopoints())
        else:
            return None

    return wrapped


ds = make('describe')
version_info = make('version_info')
low = make('lowercase')
mcoast = make('mcoast')
mcont = make('mcont')
mobs = make('mobs')
msymb = make('msymb')
met_plot = make('plot')
pr = make('print')
read = make('read')
write = make('write')
retrieve = make('retrieve')
waitmode = make('waitmode')
geoview = make('geoview')
mtext = make('mtext')
ps_output = make('ps_output')
png_output = make('png_output')
set_output = make('setoutput')
maxvalue = make('maxvalue')
minvalue = make('minvalue')
accumulate = make('accumulate')
add = make('+')
sub = make('-')
prod = make('*')
div = make('/')
power = make('^')
sqrt = make('sqrt')
interpolate = make('interpolate')
mcross_sect = make('mcross_sect')
grib_get_string = make('grib_get_string')
obsfilter = make('obsfilter')
filter = make('filter')
greater_equal_than = make('>=')
greater_than = make('>')
lower_equal_than = make('<=')
lower_than = make('<')
type = make('type')
count = make('count')
distance = make('distance')


def plot(*args, **kwargs):
    map_outputs = {
        'png': png_output,
        'ps': ps_output,
    }
    if 'output_type' in kwargs:
        output_function = map_outputs[kwargs['output_type'].lower()]
        kwargs.pop('output_type')
        return met_plot(output_function(kwargs), *args)
    else:
        return met_plot(*args)


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
