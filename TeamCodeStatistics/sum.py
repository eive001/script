#-*- encoding:utf-8 -*-
### Python 2.7.17
### 仅统计当前目录 重复运行时记得手动删除上次运行生成的旧的 !!!result.md

import os

re = os.popen("find .  -maxdepth 1 -name  \"*.md\"").read()
file_path = re.split("\n")
#file = []
users = [
    ["Shirong Hao","shirong@linux.alibaba.com",0,0,0,0],
    ["Xynnn_","ding.ma@linux.alibaba.com",0,0,0,0],
    ["Jiale Zhang","zhangjiale@linux.alibaba.com",0,0,0,0]
]
print file_path
for f in file_path:
    #file.append(f[2:])
    file = f[2:]
    if (file==''):
        continue
    
    for line in open(file):
        _m,name,email,commit,add,de,delta,_n = line.split("|")
        if(name.strip() == "姓名".strip())|(name.strip() == ":-:".strip()):
            continue
        else:
            for user in users:
                print email,user," ---  ",_m,name,email,commit,add,de,delta,_n
                if(user[1].strip() == email.strip() ):
                    user[2] = int(commit) + user[2]
                    user[3]+=int(add)
                    user[4]+=int(de)
                    user[5]+=int(delta)
target_file = "sum.md"
os.system("rm -rf "+target_file)
os.system("touch " + target_file )
os.system("echo \| 姓名 \| 邮箱 \| Commits数 \| 代码增加行数 \| 代码删除行数 \| 代码净增量 \| >> "+ target_file)
os.system("echo \| :-: \| :-: \| :-: \| :-: \| :-: \| :-: \|  >> "+ target_file)

for user in users:
    os.system("echo \|" +str(user[0]) + " \| "+str(user[1]) +" \| "+str(user[2])+" \| "+ str(user[3])+ " \| "+str(user[4])+" \| "+str(user[5]) +" \|  >> "+ target_file)


            
#             commits_num+=int(b)
#             add_num+=int(c)
#             del_num+=int(d)
#             delta_num+=int(e)
#             results[a] =  commits_num,add_num,del_num,delta_num