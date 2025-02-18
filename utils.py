def is_power_of_five(n):
    if n <= 0:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def gcd(a, b):
    while b:
        a,b = b, a%b
    return a

def euler_phi(n):
    res = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            res += 1
    return res - 1
