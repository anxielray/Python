string_int = "32"
string_float = "3.141"
string_bool = "True"

int_value = int(string_int)
float_value = float(string_float)
bool_value = bool(string_bool)

# Print the converted values along with their types
print(f"32 as an  integer is: {int_value}, and is of Type: {type(int_value)}")
print(f"3.141 as a Float: {float_value}, and is of Type: {type(float_value)}")
print(f"True as a Boolean: {bool_value}, and is of Type: {type(bool_value)}")