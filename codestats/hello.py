#-*- encoding:utf-8 -*-
import os
urls = []
for line in open("urls.txt"):
    line = line[:-1]
    urls.append(line)
un_counted = "../uncounted"

#print(urls)
basedir = os.popen("pwd").read()[:-1]
for url in urls:
    #下载并进入项目目录
    basename = os.path.basename(url)
    os.system("git clone " + url)
    os.chdir(basedir+"/"+basename)
    os.system("echo ------"+ basename+">> "+ un_counted)
    print("----------------+++-----------------")
    re = os.popen("git shortlog -s -n -e --since=2022-04-01 --until=2022-09-30").read()
    contributors = re.split("\n")
    contributors_temp = []
    for contributor in contributors:
        index_tab = contributor.find("\t")
        index_email = contributor.find("<")
        contributor = [contributor[0:index_tab].strip(),contributor[index_tab:index_email].strip(), contributor[index_email+1:-1].strip()]
        contributors_temp.append(contributor)
    #print(contributors_temp)
    #这里不太清楚为什么会有一个空的值 可能是初始化时引入的 需要去除掉 不然会有错误
    contributors_temp = [i for i in contributors_temp if i[0] != '']
    results={}
    for count,name,email in contributors_temp:
        company = email[email.find("@")+1:]
        if company in results:
            result = results[company]
        else:
            result = [0,0,0,0]
        ## 分别代表 提交数 代码增加量 代码减少量 静增加量
        commits_num,add_num,del_num,delta_num = result
        commits_num += int(count)
        ##这里有些人查出来是未知的 
        ##git log --author='Jiale Zhang' --since=2022-04-01 --until=2022-09-30 --pretty=tformat: --numstat | awk '{ adds += $1; subs += $2; sum += $1 - $2 } END { printf "%s insertions(+), %s deletions(-), %s delta\n", adds, subs, sum }'
        re = os.popen("git log --author="+ email +" --since=2022-04-01 --until=2022-09-30 --pretty=tformat: --numstat | awk '{ adds += $1; subs += $2; sum += $1 - $2 } END { printf \"%s,%s,%s\", adds, subs, sum }'").read()
       
        a,b,c  = re.split(",")
        #同样这里也有个空值， 不知道原因
        if (a=='') | (b == '') | (c==''):
            results[company] = result
        else:
            result = commits_num,add_num+int(a),del_num+int(b),delta_num+int(c)
            results[company] = result

    #print[results]
    
## 合并 换名处理 // 不在本地的名字都不会被加入到输出结果

    company_name={"intel.com":"Intel","linux.alibaba.com":"Ali","fossa.io":"other","alibaba-inc.com":"Ali","uk.ibm.com":"IBM","ibm.com":"IBM","cn.ibm.com":"IBM","redhat.com":"Redhat","arm.com":"Arm"
                ,"il.ibm.com":"IBM","us.ibm.com":"IBM" ,"hygon.cn":"海光","fidencio.org":"other","hashbangbash.com":"other"
                ,"rivosinc.com":"rivos","protonmail.com":"other","protonmail.com":"other","fidencio.org":"other","gmail.com":"other",
                "users.noreply.github.com":"other","qq.com":"other","foxmail.com":"other"}
    output={}

    for result in results:
        if result in company_name:
            if company_name[result] in output:
                output[company_name[result]] =  output[company_name[result]][0] + results[result][0], output[company_name[result]][1] + results[result][1],output[company_name[result]][2] + results[result][2],output[company_name[result]][3] + results[result][3]
            else:
                output[company_name[result]] = results[result][0],results[result][1],results[result][2],results[result][3]
        else:
            print("*** "+ result)
            os.system("echo "+ result+ ">> "+ un_counted)
    print(output)
    commits_total = 0
    commits_ali = 0
    add_total =0
    del_total =0
    delta_total =0
    delta_ali =0
    target_file = "../"+basename+".md"
    os.system("rm -rf "+target_file)
    os.system("touch " + target_file )
    os.system("echo \| 贡献公司 \| Commits数 \| 代码增加行数 \| 代码删除行数 \| 代码净增量 \| >> "+ target_file)
    #os.system("echo ---- >> "+ target_file)
    os.system("echo \| :-: \| :-: \| :-: \| :-: \| :-: \|  >> "+ target_file)
    for out in output:
        os.system("echo \| "+ out +" \| " + str(output[out][0])+" \| "+str(output[out][1])+" \| " + str(output[out][2])+" \| "+str(output[out][3]) +" \| >> "+ target_file)
        commits_total +=output[out][0]
        add_total += output[out][1]
        del_total += output[out][2]
        delta_total +=  output[out][3]
        if out == "Ali":
            commits_ali = output[out][0]
            delta_ali = output[out][3]


    os.system("echo \| " + "总计 \| "+ str(commits_total)+" \| "+ str(add_total)+" \| " +str(del_total)+"\|"+str(delta_total)+"\| >> "+target_file )
    os.system("echo \| " + "阿里占比 \| "+str(float(commits_ali)/commits_total)+" \| "+ "--"+" \| " +"--"+"\|"+str(float(delta_ali)/delta_total)+"\| >> "+target_file )
    print("----------------+++-----------------")
    ### 返回工作目录
    os.chdir(basedir)