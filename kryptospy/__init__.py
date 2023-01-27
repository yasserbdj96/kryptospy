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

#start kryptospy class:
class kryptospy:
    #__init__:
    def __init__(self,password,text):
        #
        self.password=password
        self.text=text

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
        o=ones[0]
        for i in range(len(ones)):
            if ones[i]!="":
                ones_list.append(ones[i])
    
        zeros_list=[]
        z=zeros[0]
        for i in range(len(zeros)):
            if zeros[i]!="":
                zeros_list.append(zeros[i])

        if o=="":
            all_list=[x for y in zip(zeros_list,ones_list) for x in y]
        elif z=="":
            all_list=[x for y in zip(ones_list,zeros_list) for x in y]
    
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
                    length.append(word[i-1]+":"+str(count))
                    count=1
            length.append(word[i-1]+":"+str(count))
        else:
            i=0
            length.append(word[i-1]+":"+str(count))
    
        chars=kryptospy.passwd(password)

        length_en_zip=""
        for i in range(len(length)):
            x,y=length[i].split(':')
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
            for j in range(len(chars)):
                try:
                    f+=str(j)*chars[j].index(text[i])
                except:
                    pass
        text=f

        #3:
        text=[*text]
        binary=""
        for i in range(len(text)):
            if (i % 2) == 0:
                binary+=str("0"*(int(text[i])+1))
            else:
                binary+=str("1"*(int(text[i])+1))
        text=binary

        #2:
        text=frombinary(text)

        #1:
        text=fromb64(text)

        #
        return text

    def passwd(text):
        chars_list=[]
        t=True
        while t==True:
            text=tomd5(text)+tobase64(tomd5(text)).upper()+tobase64(tomd5(text)).lower()+tomd5(text).upper()
            x=[*text]
            for i in range(len(x)):
                if x[i] not in chars_list and x[i]!="=":
                    if len(chars_list)<54:
                        chars_list.append(x[i])
                    else:
                        t=False
        step=6
        return [chars_list[i::step] for i in range(step)]

#}END.