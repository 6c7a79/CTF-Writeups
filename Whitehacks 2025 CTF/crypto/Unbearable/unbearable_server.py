from flask import Flask, request
from secrets import token_bytes
from Cryptodome.Cipher import AES 
from Cryptodome.Util.Padding import pad

session_key = token_bytes(32) # generate a 32 bytes key
session_iv = token_bytes(16) # generate a 16 bytes iv
unbearable = Flask(__name__)

flag = b'WH2025{????????????????????}'

@unbearable.route('/encrypt',methods=['POST'])
def encrypt():
    try:
        data = bytes.fromhex(request.json['data']) # receive input data
        pt = data + flag # add flag to the back of the input data
        cipher = AES.new(session_key,AES.MODE_CBC,session_iv) 
        # encrypt use CBC mode, which use a fix iv once for the first block, key is also the same for each block.
        # so that two plaintexts that share the same first N blocks their corresponding ciphertexts will also share the same first N blocks
        # therefore we can craft a payload with size (block_size -1), and get back the ciphertext from the oracle 
        # then craft a payload with the guess char of the flag at the back and get back the ciphertext from the oracle
        # we can compare to see if the the first blocks matches, if match then the guess char is correct so we add the char at the back of the payload.
        # then we continue this brute force process until the last char of the flag is bruteforced which is '}'
        return {'data':cipher.encrypt(pad(pt,cipher.block_size)).hex()} # pad the data to block_size for encryption
    except:
        return 'Err 400, invalid request',400

unbearable.run("0.0.0.0",1337)
