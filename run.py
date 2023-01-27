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
from kryptospy import *
import argparse

# INPUT ARG
ap = argparse.ArgumentParser()
ap.add_argument('-p', '--password', required=True)
ap.add_argument('-t', '--text', required=True)
ap.add_argument('-c', '--condition', required=True)
args = ap.parse_args()





try:
    #import os
    import sys
    #
    #CONDI = os.environ['CONDI'] if "CONDI" in os.environ else sys.argv[1]
    #PASSWD = os.environ['PASSWD'] if "PASSWD" in os.environ else sys.argv[2]
    #TEXT = os.environ['TEXT'] if "TEXT" in os.environ else sys.argv[3]

    CONDI=args.condition
    TEXT=args.text
    PASSWD=args.password

    if CONDI.upper()=="encode".upper():
        p1=kryptospy(PASSWD,TEXT).enc()
        print(p1)
    elif CONDI.upper()=="decode".upper():
        p2=kryptospy(PASSWD,TEXT).dec()
        print(p2)

except Exception as e:
    print(f"USAGE : python3 {sys.argv[0]} -c <CONDITION*> -p <PASSWORD*> -t <TEXT*>")
    print("CONDITION*: encode/decode")
    exit()
    #pass
#}END.



"""
text="yasserbdj96"
t2enc=kryptospy("123",text).enc()
t2dec=kryptospy("123",t2enc).dec()

print(t2enc)
print(t2dec)"""