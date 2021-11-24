import os
import sys
import re

with open(r"C:\Users\rs21255\Desktop\abc.txt",'r') as f:
       ips=f.readlines()
       ptrn=re.compile(r'[0-9].*')
       list=[]
       for line in ips:
              list.append(re.search(ptrn,line)[0])
       print(list)
for n in list:
       res=os.system("ping -c 4 "+n)
       print(res)
       if res==0:
           print("up")
       
       else:
           print("down")   
