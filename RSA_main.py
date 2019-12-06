from GenerateKey import create_prime_num, fastExpMod, public_e, private_d

def create_keys(keylength):
    p = create_prime_num(keylength)
    q = create_prime_num(keylength)
    n = p * q
    fn = (p - 1)*(q - 1)
    e = public_e(fn)
    d = private_d(e, fn)
    return (n, e, d)

def encrypt(P, e, n):
    return fastExpMod(P, e, n)

def decrypt(C, d, n):
    return fastExpMod(C, d, n)


if __name__ == "__main__":

    # generate public and private key
    key = create_keys(5000)
    n = key[0]
    e = key[1]
    d = key[2]
    
    # encrypt and decrypt
    p = 12345
    print('Plain Text: ', p)

    c = encrypt(p, e, n)
    print('Cipher Text: ', c)

    m = decrypt(c, d, n)
    print('Decrypted Message: ', m)