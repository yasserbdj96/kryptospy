#!/usr/bin/env python
# coding:utf-8
#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : yasserbdj96                                  |
#   |   Email   : yasser.bdj96@gmail.com                       |
#   |   Github  : https://github.com/yasserbdj96               |
#   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
# --+----------------------------------------------------------+--  
#   |        all posts #yasserbdj96 ,all views my own.         |
# --+----------------------------------------------------------+--
#   |                                                          |

#START{

try:
    from kryptospy import *
except:
    import os
    os.chdir("../")
    from kryptospy import *

# Example:1
#For encryption
p1=kryptospy("123","Example:1").enc()
print(p1)
    
#To decrypt
p2=kryptospy("123",p1).dec()
print(p2)

#}END.