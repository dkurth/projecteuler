def nextTerm(t):
    if t % 2:
        return 3*t+1
    else:
        return t/2

def getChain(x):
    c = [str(x)]
    while x != 1:
        x = nextTerm(x)
        c.append(str(x))
    return c

if __name__ == "__main__":
    maxlen = 0
    maxval = 1
    for x in range(1, 1000000):
        chain = getChain(x)
        # print('|'.join(chain))
        # print('{} -> {} :: {}'.format(x, len(chain), chain)) #' => '.join(chain)))
        if len(chain) > maxlen:
            # print('{}: {}'.format(x, '|'.join(chain)))
            maxlen = len(chain)
            maxval = x

print('{} => {}'.format(maxval, maxlen))