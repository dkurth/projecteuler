def is_palindrome(x):
    return str(x) == str(x)[::-1]

pals = []

for n in range(100, 1000):
    for m in range(n, 1000):
        p = n * m

        if is_palindrome(p):
            pals.append(p)

print(max(pals))