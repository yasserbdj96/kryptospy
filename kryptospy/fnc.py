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
import base64
import hashlib

#tobase64:
def tobase64(data):
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')

#from base64:
def fromb64(data):
    return base64.b64decode(data.encode('utf-8')).decode('utf-8')

global n
n=8

#tobinary:
def tobinary(data):
    data='X'.join(format(ord(x), 'b') for x in data)
    data=data.split("X")
    for i in range(len(data)):
        data[i]=(n-len(data[i]))*"0"+data[i]
    v=""
    for i in range(len(data)):
        v+=data[i]
    return v

#frombinary:
def frombinary(data):
    binary_values=listit(n,data)
    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    return ascii_string

#listit:
def listit(n,data):
    binary_values=[]
    for i in range(0,len(data),n):
        binary_values.append(data[i:i+n])
    return binary_values

#tomd5:
def tomd5(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest()

#}END.