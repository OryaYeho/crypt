# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 10:07:41 2021

@author: oryay
"""

from skipjack import SkipJack


def encryptFile():
    BLOCK_SIZE = 8
    KEY = [0x00, 0x99, 0x88, 0x77, 0x66, 0x55, 0x44, 0x33, 0x22, 0x11]
    sj = SkipJack()
    with open('car.jpg','rb') as f_in:
        with open('cars_enc.jpg','wb') as f_out:
            block = f_in.read(BLOCK_SIZE) #b'\xff\xd8\xff\xe0\x00\x10JF'
            while block:
                block_encypt = sj.encrypt(int.from_bytes(block, "big"), KEY) #4997498391657805585
                block_encypt_bytes=block_encypt.to_bytes(BLOCK_SIZE,'big') #'EZ\xaeO0Yw\x11'
                f_out.write(block_encypt_bytes)
                block = f_in.read(BLOCK_SIZE)

def decryptFile():
    BLOCK_SIZE = 8
    KEY = [0x00, 0x99, 0x88, 0x77, 0x66, 0x55, 0x44, 0x33, 0x22, 0x11]
    sj = SkipJack()
    with open('cars_enc.jpg','rb') as f_in:
        with open('cars_dec.jpg','wb') as f_out:
            block_encypt = f_in.read(BLOCK_SIZE)  #'EZ\xaeO0Yw\x11'
            while block_encypt:
                block_encypt_int = int.from_bytes(block_encypt,'big') #4997498391657805585
                block_int = sj.decrypt(block_encypt_int, KEY) #18435766412179950150
                block = block_int.to_bytes(BLOCK_SIZE,'big')
                f_out.write(block)
                block_encypt = f_in.read(BLOCK_SIZE)

encryptFile()
decryptFile()
