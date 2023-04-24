# assignment 2: calculate n factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = 5
result = factorial(n)
print(result)  # Output: 120

