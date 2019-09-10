a = b = 1
c = s = 0

while True:
    c = a + b
    if c > 4e6:
        break
    # print(c)
    if c % 2 == 0:
        s += c
    (a, b, c) = (b, c, 0)

print()
print (s)