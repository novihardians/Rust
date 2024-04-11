def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    # else
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case


print(fibonacci_of(19))
# 4181

print("\n")

print([fibonacci_of(n) for n in range(19)]) # index 0 = F0 /// range(19) means fibonacci_of(18)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]

print("\n")

print([fibonacci_of(n) for n in range(20)]) # index 0 = F0 /// range(20) means fibonacci_of(19)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]