def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev*10 + digit
        n //= 10
    return rev

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def is_prime(n):
    if n <= 1:
        return False
    else:
        d = 2

    while d**2 <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def fibonacci(n):
    if n == 0:
        return 0
    
    prev, curr, i = 0, 1, 1
    while i < n:
        nxt = prev + curr
        prev, curr = curr, nxt
        i += 1
    return curr

def max_increasing_len(arr):
    if len(arr) == 0:
        return 0
    
    cur, best, i = 1, 1, 1
    while i < len(arr):
        if arr[i] > arr[i-1]:
            cur += 1
        else:
            cur = 1
        best = max(best, cur)
        i += 1
    return best

def sqrt_newton(n, eps=1e-6):
    if n == 0:
        return 0.0

    x = n//2
    while abs(x**2 - n) > eps:
        x = 0.5*(x + n//x)
    return x

def second_max(arr):
    if len(arr) < 2:
        return None

    m1, m2, i = float("-inf"), float("-inf"), 0
    while i < len(arr):
        if arr[i] > m1:
            m2, m1 = m1, arr[i]
        elif m2 < arr[i] < m1:
            m2 = arr[i]
        i += 1
    return m2

def count_primes_up_to(n):
    cnt, num = 0, 2
    while num <= n:
        is_p, d = True, 2

        while d**2 <= num and is_p:
            if num % d == 0:
                is_p = False
            d += 1

        if is_p:
            cnt += 1
        num += 1
    return cnt