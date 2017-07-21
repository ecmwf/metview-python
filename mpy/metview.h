
struct MvRequest;
typedef struct MvRequest* MvRequest_p;

struct CGeopts;
typedef struct CGeopts* CGeopts_p;

struct CBufr;
typedef struct CBufr* CBufr_p;

struct CGrib;
typedef struct CGrib* CGrib_p;



int mp_init(int argc, char **argv);
void p_init();
const char* p_hello_world(int argc);
const char* p_call_function(const char* name, int arity);
void p_push_number(int n);
void p_push_string(const char *str);
void p_push_request(void *req);
void p_push_grib(CGrib_p fs);
void p_push_bufr(CBufr_p bufr);
void p_push_geopoints(CGeopts_p gpt);
int p_result_type(void);
char *p_result_as_string(void);
CGrib_p p_result_as_grib(void);
CBufr_p p_result_as_bufr(void);
CGeopts_p p_result_as_geopoints(void);
double p_result_as_number(void);
MvRequest_p p_result_as_request(void);
MvRequest_p p_new_request(const char *verb);
void p_set_value(MvRequest_p req, const char *param, const char *value);
void p_add_value(MvRequest_p req, const char *param, const char *value);
void p_set_request_value_from_pop(MvRequest_p req, const char *param);
char *p_get_req_verb(MvRequest_p req);
int p_get_req_num_params(MvRequest_p req);
char *p_get_req_param(MvRequest_p req, int i);
char *p_get_req_value(MvRequest_p req, const char *param);
