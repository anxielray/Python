def fibonacci(n):
    sequence = [0, 1]
    for _ in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

n = int(input("Enter the number of Fibonacci terms: "))
print("Fibonacci sequence:", fibonacci(n))

