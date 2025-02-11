def find_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def gcd(a, b):
    while b:
        a,b = b, a%b
    return a

if __name__ == "__main__":
    print(find_factorial(5))
