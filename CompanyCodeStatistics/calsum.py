#-*- encoding:utf-8 -*-
import os

re = os.popen("find .  -maxdepth 1 -name  \"*.md\"").read()
file_path = re.split("\n")
#file = []
results={}
commits_total = 0
commits_ali = 0
add_total =0
del_total =0
delta_total =0
delta_ali =0
for f in file_path:
    #file.append(f[2:])
    file = f[2:]
    if (file==''):
        continue
    
    for line in open(file):
        _m,a,b,c,d,e,_n = line.split("|")
        if(a.strip() == "贡献公司".strip())|(a.strip() == "总计".strip())|(a.strip() == ":-:".strip())|(a.strip() == "阿里占比".strip()):
            continue
        else:
            if a in results:
                commits_num,add_num,del_num,delta_num = results[a]
            else:
                results[a] = [0,0,0,0]
                commits_num,add_num,del_num,delta_num = results[a]
            
            commits_num+=int(b)
            add_num+=int(c)
            del_num+=int(d)
            delta_num+=int(e)
            results[a] =  commits_num,add_num,del_num,delta_num


target_file = "result.md"
os.system("touch " + target_file )
os.system("echo \| 贡献公司 \| Commits数 \| 代码增加行数 \| 代码删除行数 \| 代码净增量 \| >> "+ target_file)
os.system("echo \| :-: \| :-: \| :-: \| :-: \| :-: \|  >> "+ target_file)
for result in results:
    os.system("echo \| "+ result +" \| " + str(results[result][0])+" \| "+str(results[result][1])+" \| " + str(results[result][2])+" \| "+str(results[result][3]) +" \| >> "+ target_file)
    commits_total += results[result][0]
    add_total += results[result][1]
    del_total += results[result][2]
    delta_total += results[result][3]
    if(result.strip() == "Ali"):
        commits_ali += results[result][0]
        delta_ali += results[result][3]

os.system("echo \| " + "总计 \| "+ str(commits_total)+" \| "+ str(add_total)+" \| " +str(del_total)+"\|"+str(delta_total)+"\| >> "+target_file )
os.system("echo \| " + "阿里占比 \| "+str(float(commits_ali)/commits_total)+" \| "+ "--"+" \| " +"--"+"\|"+str(float(delta_ali)/delta_total)+"\| >> "+target_file )






