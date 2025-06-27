from multiprocessing import Pool

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    numbers = list(range(0, 10))
    with Pool() as pool:
        prime_flags = pool.map(is_prime, numbers)
    primes = [num for num, is_p in zip(numbers, prime_flags) if is_p]
    print("Primes found:", primes)
