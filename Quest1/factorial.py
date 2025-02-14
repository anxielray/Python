# write a function displaying thr factorial of n


def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


if __name__ == "__main__":
    num = factorial(int(input("insert a number ")))

    if num is not None:
        print(f"factorial is {num}")
    else:
        print("No factorial us defined for negative Numbers")
