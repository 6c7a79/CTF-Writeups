from Cryptodome.Util.number import * 
flag = b'WH2025{??????????????????????????}'

pt = bytes_to_long(flag)
p = getPrime(2048)
q = getPrime(2048)
N = p * q 
e = 0x10001
ct = pow(pt,e,N)
print(f'p = {p}\nq = {q}\nct = {ct}')
