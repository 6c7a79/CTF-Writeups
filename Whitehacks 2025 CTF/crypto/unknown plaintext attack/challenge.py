import os

BLOCK_SIZE = 64
KEY_LEN = 16

flag = b'WH25{REDACTED}'[5:-1]  # hah, you will never get my flag now!


def schedule(key: bytes):
    assert all(a < 0xfb for a in key) # 0xfb = 251
    return bytes((i * 2) % 0xfb for i in key) 


def pad(text):
    return text.ljust(BLOCK_SIZE, (BLOCK_SIZE - len(text)).to_bytes()) # pad the m to len of 64 with (BLOCK_SIZE - len(text)).to_bytes() where the range of (BLOCK_SIZE - len(text))<=48


def xor(a, b):
    return bytes(i ^ j for i, j in zip(a, b))


def encrypt(text, key):
    assert len(text) <= 48  # the len of REDACTED part of the flag is <= 48
    text = pad(text) 
    out = b''
    for i in range(0, BLOCK_SIZE, KEY_LEN):
        out += xor(text[i:i+16], key) # encrypt each 16 len blocks with the key
        key = schedule(key)

    return out


print(encrypt(flag, os.urandom(KEY_LEN)).hex())

