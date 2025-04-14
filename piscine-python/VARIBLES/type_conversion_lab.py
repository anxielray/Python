string_int = "32"
string_float = "3.141"
string_bool = "True"

int_value = int(string_int)
float_value = float(string_float)
bool_value = bool(string_bool)

# Print the converted values along with their types
print(f"Integer: {int_value}, Type: {type(int_value)}")
print(f"Float: {float_value}, Type: {type(float_value)}")
print(f"Boolean: {bool_value}, Type: {type(bool_value)}")