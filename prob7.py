import math

def is_prime(n):
    r = math.sqrt(n)
    for p in primes:
        if p > r:
            return True
        elif n % p == 0:
            return False
    return True

if __name__ == "__main__":
    primes = [2]

    idx = 10001
    x = 3

    while len(primes) < idx:
        if is_prime(x):
            primes.append(x)
        x += 2

    print("The {}th prime is {}".format(len(primes), primes[-1]))
