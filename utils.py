def find_factorial(n):
    result = 1
    for i in range(n):
        result *= i
    return result

if __name__ == "__main__":
    print(find_factorial(5))
