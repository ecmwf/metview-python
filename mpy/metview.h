
int mp_init(int argc, char **argv);
void p_init();
const char* p_hello_world(int argc);
const char* p_call_function(const char* name, int arity);
void p_push_number(int n);
void p_push_string(const char *str);
void p_push_request(void *req);
void p_push_grib(const char *filename);
int p_result_type(void);
char *p_result_as_string(void);
char *p_result_as_grib_path(void);
double p_result_as_number(void);
void* p_new_request(const char *verb);
void p_set_value(void *req, const char *param, const char *value);
void p_add_value(void *req, const char *param, const char *value);
