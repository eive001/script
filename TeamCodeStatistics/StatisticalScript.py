#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
url = str(sys.argv[1]) 
os.system("git clone "+ url)
basename = os.path.basename(url)
basedir = os.popen("pwd").read()[:-1]
os.chdir(basedir+"/"+basename)
users = [
    ["Shirong Hao","shirong@linux.alibaba.com","shirong.hsr@alibaba-inc.com"],
    ["Xynnn_","ding.ma@linux.alibaba.com","mading.ma@alibaba-inc.com"],
    ["Jiale Zhang","zhangjiale@linux.alibaba.com","xinjian.zjl@alibaba-inc.com"]
]
##git log --author='Jiale Zhang' --since=2022-04-01 --until=2022-09-30 --pretty=tformat: --numstat | awk '{ adds += $1; subs += $2; sum += $1 - $2 } END { printf "%s insertions(+), %s deletions(-), %s delta\n", adds, subs, sum }'
for user in users:
    re = os.popen("git log --author="+ user[1] +" --oneline --since=2022-04-01 --until=2022-09-30 | wc -l").read()
    commit,nu = re.split("\n")
    re = os.popen("git log --author="+ user[2] +" --oneline --since=2022-04-01 --until=2022-09-30 | wc -l").read()
    _commit,nu = re.split("\n")
    user.append(int(commit)+int(_commit))
    re = os.popen("git log --author="+ user[1] +" --since=2022-04-01 --until=2022-09-30 --pretty=tformat: --numstat | awk '{ adds += $1; subs += $2; sum += $1 - $2 } END { printf \"%s,%s,%s\", adds, subs, sum }'").read()
    add1,de1,delta1  = re.split(",")
    re = os.popen("git log --author="+ user[2] +" --since=2022-04-01 --until=2022-09-30 --pretty=tformat: --numstat | awk '{ adds += $1; subs += $2; sum += $1 - $2 } END { printf \"%s,%s,%s\", adds, subs, sum }'").read()
    add2,de2,delta2  = re.split(",")
    add = 0
    de = 0
    delta = 0
    if(add1!=''):
         add += int(add1)
    if(add2!=''):
         add += int(add2)
    if(de1!=''):
         de+= int(de1)
    if(de2!=''):
         de += int(de2)
    if(delta1!=''):
         delta += int(delta1)
    if(delta2!=''):
         delta += int(delta2)

    user.append(add)
    user.append(de)
    user.append(delta)
    


target_file = "../"+basename+".md"
os.system("rm -rf "+target_file)
os.system("touch " + target_file )
os.system("echo \| 姓名 \| 邮箱 \| Commits数 \| 代码增加行数 \| 代码删除行数 \| 代码净增量 \| >> "+ target_file)
os.system("echo \| :-: \| :-: \| :-: \| :-: \| :-: \| :-: \|  >> "+ target_file)

for user in users:
    if user[3] == 0:
        continue
    else :
        os.system("echo \|" +user[0] + " \| "+user[1] +" \| "+str(user[3]) +" \| "+ str(user[4])+ " \| "+str(user[5])+" \| "+str(user[6]) +" \|  >> "+ target_file)

