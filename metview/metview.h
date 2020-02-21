
struct MvRequest;
typedef struct MvRequest* MvRequest_p;

struct CList;
typedef struct CList* CList_p;

struct CVector;
typedef struct CVector* CVector_p;


struct Value;
typedef struct Value* Value_p;


int mp_init(int argc, char **argv);
void p_init();
const char* p_hello_world(int argc);
const char* p_call_function(const char* name, int arity);
void p_push_number(double n);
void p_push_string(const char *str);
void p_push_request(void *req);
void p_push_value(Value_p val);
void p_push_datestring(const char *str);
void p_push_list(CList_p lst);
void p_push_vector_from_double_array(double *vals, int size, double numpy_missing_value);
void p_push_vector_from_float32_array(float *vals, int size, float numpy_missing_value);
void p_push_nil();
int p_result_type(void);
const char *p_value_as_string(Value_p);
double p_value_as_number(Value_p);
char* p_value_as_datestring(Value_p);
CVector_p p_value_as_vector(Value_p, double numpy_missing_value);
int p_vector_count(CVector_p);
int p_vector_elem_size(CVector_p);
double *p_vector_double_array(CVector_p);
float *p_vector_float32_array(CVector_p);
const char *p_error_message(Value_p);
CList_p p_value_as_list(Value_p);
Value_p p_result_as_value();
int p_value_type(Value_p val);
CList_p p_new_list(int);
void p_add_value_from_pop_to_list(CList_p, int);
int p_list_count(CList_p);
Value_p p_list_element_as_value(CList_p, int);
MvRequest_p p_new_request(const char *verb);
void p_set_value(MvRequest_p req, const char *param, const char *value);
void p_add_value(MvRequest_p req, const char *param, const char *value);
void p_set_request_value_from_pop(MvRequest_p req, const char *param);
const char *p_get_req_verb(Value_p req);
int p_get_req_num_params(Value_p req);
const char *p_get_req_param(Value_p req, int i);
const char *p_get_req_value(Value_p req, const char *param);
void p_set_subvalue(Value_p, int, Value_p);
void p_set_subvalue_from_arg_stack(Value_p);
void p_set_temporary(Value_p val, int flag);
const char *p_data_path(Value_p val);
void p_destroy_value(Value_p val);
