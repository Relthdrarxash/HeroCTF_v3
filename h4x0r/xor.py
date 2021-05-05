#!/usr/bin/env python3
from os import urandom
from random import randint
from pwn import xor

input_img = open("flag.png.enc", "rb").read()
outpout_img = open("flag.png", "wb")

key = bytes.fromhex("5e37d56cc73b60b3") + bytes([randint(0, 9)])
outpout_img.write(xor(input_img, key))
print(key)
