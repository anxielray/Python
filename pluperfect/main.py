def is_pluperfect(n):
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))

num = int(input("Enter a number to check if it's pluperfect: "))
print(f"{num} is {'a' if is_pluperfect(num) else 'not a'} pluperfect number.")

