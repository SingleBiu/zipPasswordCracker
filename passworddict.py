'''
Author: SingleBiu
Date: 2024-10-27 15:48:06
LastEditors: SingleBiu
LastEditTime: 2024-10-27 16:39:20
Description: A password dict gernerator
'''
import itertools

print("Gernerate password start")
key ="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/*-+~!@#$%^&*()_+[];',./{}|\\"
password = itertools.product(key,repeat=16)
f = open("pwd_dict.txt","a")
for i in password:
    f.write("".join(i))
    f.write("\n")
f.close()
print("Gernerate password finished")
