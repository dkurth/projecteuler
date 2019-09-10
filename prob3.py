import math

n = 600851475143

factors = []
if n % 2 == 0:
    factors.append(2)

for f in range(3, int(math.sqrt(n))+1):
    if n % f == 0:
        factors.append(f)
        n /= f

print(factors)