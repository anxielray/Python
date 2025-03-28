import sys

def inter(s1, s2):
    seen = set()
    result = []
    
    for char in s1:
        if char in s2 and char not in seen:
            result.append(char)
            seen.add(char)
    
    print("".join(result))

if __name__ == "__main__":
    if len(sys.argv) == 3:
        inter(sys.argv[1], sys.argv[2])

