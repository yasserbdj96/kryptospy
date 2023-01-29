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
from kryptospy.fnc import *
import re

#start kryptospy class:
class kryptospy:
    #__init__:
    def __init__(self,password,text):
        #
        self.password=password

        #self.text=re.search("b'(.*)'",str(text.replace("'","__smbl_1__").encode('utf-8'))).group(1)
        self.text=text

        self.split_x="__::__"

    #
    def enc(self):
        text=self.text
        password=self.password
        #1:
        text=tobase64(text)

        #2:
        text=tobinary(text)
        ones=text.split("0")
        zeros=text.split("1")

        #3:
        ones_list=[]
        for i in range(len(ones)):
            if ones[i]!="":
                ones_list.append(ones[i])
    
        zeros_list=[]
        for i in range(len(zeros)):
            if zeros[i]!="":
                zeros_list.append(zeros[i])

        all_list=kryptospy.twolists(zeros_list,ones_list)

        zip_list=""
        for i in range(len(all_list)):
            zip_list+=str(len(all_list[i])-1)

        #4:
        word=zip_list #word = "1"
        count=1
        length=[]
        if len(word)>1:
            for i in range(1,len(word)):
                if word[i-1]==word[i]:
                    count+=1
                else :
                    length.append(word[i-1]+self.split_x+str(count))
                    count=1
            length.append(word[i-1]+self.split_x+str(count))
        else:
            i=0
            length.append(word[i-1]+self.split_x+str(count))
    
        chars=kryptospy.passwd(password)

        length_en_zip=""
        for i in range(len(length)):
            x,y=length[i].split(self.split_x)
            length_en_zip+=chars[int(x)][int(y)]

        #
        return length_en_zip

    #
    def dec(self):
        text=self.text
        password=self.password
        #4:
        chars=kryptospy.passwd(password)
        f=""
        for i in range(len(text)):
            for k, mm in enumerate(chars):
                try:
                    j = mm.index(text[i])
                except ValueError:
                    continue
                f+=str(k)*j
        text=f

        #3:
        text=[*text]
        binary=""
        for i in range(len(text)):
            if (i % 2)==0:
                binary+=str("0"*(int(text[i])+1))
            else:
                binary+=str("1"*(int(text[i])+1))
        #c="1"*(8-(len([*binary])%8))
        text=binary

        #2:
        
        text=frombinary(text)

        #1:
        text=fromb64(text)

        #
        return text
        #return eval(f"b'{kryptospy.fromb64(text)}'.decode('utf-8')").replace("__smbl_1__","'")

    def passwd(text):
        chars_list=[]
        t=True
        while t==True:
            text=tomd5(text)+tobase64(tomd5(text)).upper()+tobase64(tomd5(text)).lower()+tomd5(text).upper()
            x=[*text]
            for i in range(len(x)):
                if x[i] not in chars_list and x[i]!="=":
                    if len(chars_list)<56:
                        chars_list.append(x[i])
                    else:
                        t=False
        step=7
        return [chars_list[i::step] for i in range(step)]
    
    def twolists(list1, list2):
        newlist = []
        a1 = len(list1)
        a2 = len(list2)

        for i in range(max(a1, a2)):
            if i < a1:
                newlist.append(list1[i])
            if i < a2:
                newlist.append(list2[i])

        return newlist

#}END.