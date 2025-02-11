def find_factorial(n):
    result = 1
    for i in range(n):
        result *= i
    return result

print(find_factorial(5))
