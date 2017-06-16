import os
import shutil
from ._metview import ffi, lib


def dict_to_request(verb, d):
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
    'retrieve': 'RETRIEVE',
    'mcoast': 'MCOAST',
    'read': 'READ',
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
            lib.p_push_request(dict_to_request(service_function_verbs[name], n))
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
        else:
            return None

    return wrapped


lib.p_init()


lib.p_push_number(5)
lib.p_push_number(4)


pr       = make('print')
low      = make('lowercase')
ds       = make('describe')
waitmode = make('waitmode')
plot     = make('plot')
retrieve = make('retrieve')
read     = make('read')


####################### User Program ###############

# call Metview's 'print' function with any number of arguments
pr('Start ', 7, 1, 3, ' Finished!')
pr(6, 2, ' Middle ', 6)

# call Metview's 'lowercase' string function
a = low('MetViEw')
print('output LOWERCASE function: %s\n' % a)


gg = read({'SOURCE' : 'test.grib', 'GRID' : '80'})
regidded_grib = shutil.copyfile(gg, 'test_gg_grid.grib')
grib_path = read(regidded_grib)
print('Regridded grib file path: %s\n' % grib_path)

lib.p_push_grib(grib_path.encode('utf-8'))
lib.p_call_function('plot'.encode('utf-8'), 1)




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
