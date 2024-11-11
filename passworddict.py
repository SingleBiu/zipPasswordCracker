'''
Author: SingleBiu
Date: 2024-10-27 15:48:06
LastEditors: SingleBiu
LastEditTime: 2024-11-12 07:45:05
Description: A password dict gernerator.
'''
import itertools

print("Gernerate password start")
#密码字典包含的内容
# key ="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/*-+~!@#$%^&*()_+[];',./{}|\\"
key ="0123456789a"
#知道密码长度就只需要修改repreat就行了 比如说长度8位就令repeat等于8
password = itertools.product(key,repeat=4)
#每次生成密码字典重新创建文件写入
f = open("pwd_dict.txt","w+")
for i in password:
    f.write("".join(i))
    f.write("\n")
f.close()
print("Gernerate password finished")
