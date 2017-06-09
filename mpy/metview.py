
from ._metview import ffi, lib
print('ciao')

def dict_to_request(verb, d):
    r = p_new_request(verb)
    for k, v in d.items():
        print(k, v)
        if isinstance(v, list):
            for v1 in v:
                lib.p_add_value(r, k, v1)
        else:
            lib.p_set_value(r, k, v)
    return r


# we can actually get these from Metview, but for testing we just have a dict
service_function_verbs = {"retrieve" : "RETRIEVE",
                          "mcoast"   : "MCOAST"}


#lib.p_push_number(5)
#lib.p_push_number(4)
#lib.p_hello_world(2)


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
        #if isinstance(n, datetime::dateime)
        #    p_push_date(n.iso_format)
        #if isinstance(n, (list, tuple))
    print(len(args), type(len(args)))
    lib.p_call_function(name.encode('utf-8'), len(args))


#return decode_value(p_pop())

def make(name):

    def wrapped(*args):
        err = _call_function(name, *args)
        #if err:
        #   throw Exce....

        rt = lib.p_result_type()

        if rt == "string":
            return lib.p_result_as_string().decode('utf-8')
        elif rt == "number":
            return lib.p_result_as_number()
        elif rt == "grib":
            return lib.p_result_as_grib_path().decode('utf-8')
        else:
            return 0

    return wrapped

pr       = make("print")
low      = make("lowercase")
ds       = make("describe")
waitmode = make("waitmode")
plot     = make("plot")
retrieve = make("retrieve")

####################### User Program ###############

from shutil import copyfile

# call Metview's 'print' function with any number of arguments

pr("Start ", 7, 1, 3, " Finished!")

pr(6, 2, " Middle ", 6)


# call Metview's 'lowercase' string function
a = low("MetViEw")
print(a)


# perform a MARS retrieval
# - defined a request
# - set waitmode to 1 to force synchronisation
# - the return is a path to a temporary file, so copy it before end of script
req = { "PARAM" : "t",
        "LEVELIST" : ["1000", "500"],
        "GRID" : ["2", "2"]}
waitmode(1)
g = retrieve(req)
print(g)
copyfile(g, "./result.grib")


#coast = {"map_coastline_colour" : "red"}
#plot(coast)

#print(p)
