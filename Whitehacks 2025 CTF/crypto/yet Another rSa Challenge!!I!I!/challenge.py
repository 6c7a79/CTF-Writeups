from Crypto.Util.number import getPrime

flag = b'REDACTED'
magicsauce = lambda text: REDACTED

plaintext = magicsauce(flag)
p = getPrime(256)
q = getPrime(256)
n = p * q
e = 65537
whoopsies = p + q

c = pow(plaintext, e, n)

print(f'{n=}')
print(f'{whoopsies=}')
print(f'{c=}')
