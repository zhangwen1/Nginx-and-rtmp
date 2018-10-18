#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
try:
    fh = open("testfile","w")
    fh.write("用于异常测试/n+qwer")
except IOError:
    print("Error: 没有找到文件或文件读取失败")
else:
    print("内容写入成功")
    fh.close()

print("测试try") 
print("继续执行")  

