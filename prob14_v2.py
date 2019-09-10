# faster version, with a memory

mem = {}
maxlen = 0
maxval = 1
maxchainval = 0
for i in range(1, 1000000): # i does not change
    n = i # a working copy of i
    chain = 0
    while i != 1:
        chain += 1
        if n in mem:
            chain += mem[n]
            break
        if n % 2:
            n = 3*n+1
        else:
            n = n/2
        if n > maxchainval:
            maxchainval = n
    mem[i] = chain
    if chain > maxlen:
        maxlen = chain
        maxval = i

print('{} => {}'.format(maxval, maxlen))
print("The largest value in any chain was {}".format(maxchainval)) # Wow, it's 56,991,483,520 when i goes up to 1 million.