from Cryptodome.Util.number import * 

p = getPrime(2048)
q = getPrime(2048)
N = p * q 
e = 3 
flag = b"WH2025{????????????????????}"
pt = bytes_to_long(flag)

ct = pow(pt,e,N)
print(f'p = {p}\nq = {q}\nct = {ct}')

