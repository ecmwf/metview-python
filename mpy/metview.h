
struct MvRequest;

typedef struct MvRequest* MvRequest_p;


int mp_init(int argc, char **argv);
void p_init();
const char* p_hello_world(int argc);
const char* p_call_function(const char* name, int arity);
void p_push_number(int n);
void p_push_string(const char *str);
void p_push_request(void *req);
void p_push_grib(const char *filename);
void p_push_bufr(const char *filename);
int p_result_type(void);
char *p_result_as_string(void);
char *p_result_as_grib_path(void);
char *p_result_as_bufr_path(void);
double p_result_as_number(void);
MvRequest_p p_result_as_request(void);
MvRequest_p p_new_request(const char *verb);
void p_set_value(MvRequest_p req, const char *param, const char *value);
void p_add_value(MvRequest_p req, const char *param, const char *value);
char *p_get_req_verb(MvRequest_p req);
int p_get_req_num_params(MvRequest_p req);
char *p_get_req_param(MvRequest_p req, int i);
char *p_get_req_value(MvRequest_p req, const char *param);
