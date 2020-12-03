# -*- coding : utf-8 -*-
# @Auther    : Careslten
# @time      : 2020/12/1 12:13
# @File      : test.py
# @SoftWare  : dengTa
#获取指定时间段内代码提交记录

import gitlab
url = 'http://121.201.57.217/'
private_token = 'DUgdN1MbC2E1squpi2TL'
gl = gitlab.Gitlab(url, private_token)
start_time = '2020-10-22T00:00:00Z'
end_time = '2020-12-01T00:00:00Z'
projects = gl.projects.list(all=True)#先把所有项目查出来
coms = []
for i in projects:
    branches = i.branches.list()
    if i.description == 'IOS等他项目':#指定项目
        for s in branches:
            if s.name == 'v1.2_appstore':#指定分支/不指定分支会遍历所有分支，导致不同分支的同一次提交记录重复多次
                commits = i.commits.list(all=True,query_parameters={'since': start_time,'until':end_time, 'ref_name': s.name})
                for commit in commits:
                    com_dict = {}
                    com = i.commits.get(commit.id)
                    com_dict['author_name'] = com.author_name
                    com_dict['additions'] = com.stats['additions']
                    com_dict['deletions'] = com.stats['deletions']
                    com_dict['total'] = com.stats['total']
                    print(com_dict)
                    coms.append(com_dict)
import xlwt
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('My Worksheet')
for index,val in enumerate(coms):
    worksheet.write(index,1,val['author_name'])
    worksheet.write(index, 2, val['additions'])
    worksheet.write(index, 3, val['deletions'])
    worksheet.write(index, 4, val['total'])
workbook.save('gitlabss.xls')