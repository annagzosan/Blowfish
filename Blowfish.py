# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:04:50 2021

@author: user
"""

from Crypto.Cipher import Blowfish
from struct import pack
from Crypto import Random
import random


avg=0
bs = Blowfish.block_size
key ='This is the key'
iv = Random.new().read(bs)
#cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
cipher = Blowfish.new(key, Blowfish.MODE_ECB)
for j in range(0,35):
    print('Pair no: ', j+1)
    str1_=''
    str2_=''
    for i in range(0,48):
        str1_+=str((random.randint(0,1)))
    str2_=str1_.replace('0','1',1)
    str1= str.encode(str1_)
    str2= str.encode(str2_)
    plen1 = bs - divmod(len(str1),bs)[1]
    padding = [plen1]*plen1
    padding = pack('b'*plen1, *padding)
    msg1 = iv + cipher.encrypt(str1 + padding)
    plen2 = bs - divmod(len(str2),bs)[1]
    padding = [plen2]*plen2
    padding = pack('b'*plen2, *padding)
    msg2 = iv + cipher.encrypt(str2 + padding)
    counts=sum ( msg1[i] != msg2[i] for i in range(len(msg1)))
    avg+=counts
    print('Differences between the two cipher texts :',counts)
    print('_______________')

print('Average : ' , avg/35)


