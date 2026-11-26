import algorithms as alg


if __name__ == "__main__":
    assert alg.reverse_number(1234) == 4321
    assert alg.reverse_number(1200) == 21
    assert alg.gcd(48, 18) == 6
    assert alg.is_prime(17) is True
    assert alg.fibonacci(6) == 8
    assert alg.max_increasing_len([1, 3, 5, 2, 4]) == 3
    assert abs(alg.sqrt_newton(25, 1e-6) - 5.0) <= 1e-6
    assert alg.second_max([10, 20, 4, 45, 99]) == 45
    assert alg.count_primes_up_to(10) == 4
    print("Все базовые проверки пройдены успешно!")