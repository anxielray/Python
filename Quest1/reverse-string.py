def reverse_string(s):
    return s[::-1]

def split_string(s):
    return s.split()

def join_string(s):
    return " ".join(s)

if __name__ == "__main__":
    str = input("Enter a string: ")
    print(join_string(reverse_string(split_string(str))))