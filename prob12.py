'''
This is too slow.  Factoring would be much faster than getting divisors this way, but then, given the factors, how do we could the divisors?

If the factors are 1, 2, 2, 7, then the divisors are:
    1
    2
    7
    2*2
    2*7
    2*2*7

If the factors are 1, 2, 2, 3, 3, then the divisors are:
    1, 2, 3, 2*2, 2*3, 2*2*3, 2*3*3, 3*3, 2*2*3*3

TODO: Think of how to express that.
'''

import math

def get_factors(n):
    factors = [1]
    while n % 2 == 0:
        factors.append(2)
        n /= 2
    for f in range(3, int(math.sqrt(n))+1):
        while n % f == 0:
            factors.append(f)
            n /= f
    return factors

def count_divisors(factors):
    num_divisors = 1
    for v in set(factors):
        num_divisors *= (factors.count(v) + 1)
    return num_divisors

if __name__ == "__main__":
    maxd = 0
    n = 1
    while maxd <= 500:
        x = sum(range(1,n+1))

        factors = get_factors(x)

        num_divisors = count_divisors(factors)

        if num_divisors > maxd:
            print("The first triangle number with {} divisors is the {}th number, {}".format(num_divisors, n, x))
            maxd = num_divisors
        n += 1
