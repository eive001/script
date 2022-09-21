#-*- encoding:utf-8 -*-
### Python 2.7.17
### 将项目链接逐行添加至当前目录下 urls.txt文件
import os
for line in open("urls.txt"):
    line = line[:-1]
    os.system("python StatisticalScript.py " + line)