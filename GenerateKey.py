import math
import random


# primality testing
def miller_rabin_test(n):
    p = n - 1
    r = 0
    while p % 2 == 0:
        r += 1
        p /= 2
    b = random.randint(2, n - 2)
    if fastExpMod(b, int(p), n) == 1:
        return True
    for i in range(0,7):
        if fastExpMod(b, (2 ** i) * p, n) == n - 1:
            return True
    return False
    

# fast compute b^e (mod n)
def fastExpMod(b, e, n):
    result = 1
    e = int(e)
    while e != 0:
        if e % 2 != 0:
            e -= 1
            result = (result * b) % n
        e >>= 1
        b = (b * b) % n
    return result
    

# generate big prime numbers
def create_prime_num(keylength):
    while True:
        n = random.randint(0, keylength)
        if n % 2 != 0:
            found = True
            for i in range(0, 10):
                if miller_rabin_test(n):
                    pass
                else:
                    found = False
                    break
            if found:
                return n


# find public key e
def public_e(fn):
    while True:
        e = random.randint(0, fn)
        if math.gcd(e, fn) == 1:
            return e
 
 
# find private key d
def private_d(e, fn):
    d = 0
    while True:
        if (e * d) % fn == 1:
            return d
        d += 1