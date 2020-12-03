import requests
import time
import json
from random import randint

# phone = range(15900000100,15900001000)
# num = 0
# for i in phone:
#     num += 1
#     try:
#         host = 'http://test-api.51dengta.net'
#         r = requests.post(host+'/user/auth/smsLogin',data={
#             'phone':i,
#             'code':'80008'
#         })
#         token = r.json()['info']['access_token']
#         user_id = r.json()['info']['user_id']
#         print(user_id)
#
#         rs = requests.post(host+'/user/user/destroy',data={
#             'access_token':token,
#             'code':80008
#         })
#         print(rs.json())
#
#
#         # r_ws = requests.post(host + '/user/user/completeProfile', data={
#         #     'access_token': token,
#         #     'name': 'test' + str(num),
#         #     'birth_year': '1972',
#         #     'sex': '2',
#         #     'avatar': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1595912962287&di=60dd63552bcdb244cb8769890e6e75e5&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201608%2F23%2F20160823222246_Jhi4U.thumb.700_0.jpeg',
#         #     'province': '北京',
#         #     'city': '北京',
#         #     'city_code': '110100'
#         # })
#         # print(r_ws.text)
#         #
#         #
#         #
#         # r_gz = requests.post(host+'/user/user/follow',data={
#         #     'access_token':token,
#         #     'user_id':8361361716,
#         #     'status':1
#         # })
#         #
#         # print(r_gz.json())
#         #
#         # time.sleep(1)
#         # rs_gz = requests.post(host+'/user/user/follow', data={
#         #     'access_token':'eyJhbGciOiJITUFDU0hBMjU2IiwiaXNzIjoiRWFzeVN3b29sZSIsImV4cCI6MTYyNzQzOTI2NCwic3ViIjpudWxsLCJuYmYiOjE1OTU5MDMyNjQsImF1ZCI6bnVsbCwiaWF0IjoxNTk1OTAzMjY0LCJqdGkiOiJtaWx2eGRFdEZCIiwic2lnbmF0dXJlIjoiNmIyZGYzOTY5OWZhMzAwMWQyNDE0NWRkNzg1N2RkNTA2NjliMjIzMTMzOGU1MzM4MjcxOTg3YWNmMTc5NjgwNyIsInN0YXR1cyI6MSwiZGF0YSI6IjgzNjEzNjE3MTYifQ%3D%3D',
#         #     'user_id': user_id,
#         #     'status': 1
#         # })
#         # print(rs_gz.json())
#         #
#         #
#         #
#         # rs = requests.post('https://test-manager.51dengta.net/admin.php/app/match_maker/add.html',data={'phone':i},headers={
#         #     'method': 'POST',
#         #     'path': '/admin.php/app/match_maker/add.html',
#         #     'scheme': 'https',
#         #     'accept': '*/*',
#         #     'accept-encoding': 'gzip, deflate, br',
#         #     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
#         #     'content-length': '17',
#         #     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         #     'cookie': 'liaoadmin_language=zh-cn; PHPSESSID=n1nidlsv110lc60hu9ktu4ufcc; liaohisi_iframe=1; liaohisi_admin_theme=default',
#         #     'origin': 'https://test-manager.51dengta.net',
#         #     'referer': 'https://test-manager.51dengta.net/admin.php/app/match_maker/add.html?hisi_iframe=yes',
#         #     'sec-fetch-mode': 'cors',
#         #     'sec-fetch-site': 'same-origin',
#         #     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.56 Safari/537.36',
#         #     'x-requested-with': 'XMLHttpRequest'
#         # })
#         # print('ok',i)
#     except Exception as e:
#         print(e)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests,json
from random import randint

headers = {
# 'authority':'test-manager.51dengta.net',
# 'method':'GET',
# 'path':'/admin.php/system/publics/index.html',
# 'scheme':'https',
# 'accept':'*/*',
# 'accept-encoding':'gzip,deflate,br',
# 'accept-language':'zh-CN,zh;q=0.9',
# 'content-length':'108',
# 'content-type':'application/x-www-form-urlencoded;charset=UTF-8',
'cookie':'liaoadmin_language=zh-cn; PHPSESSID=2ngn9aik5d0on2lkgld1h73neb; liaohisi_iframe=1; liaohisi_admin_theme=default',
'Host':'uat-manager.51dengta.net',
# 'origin':'https://test-manager.51dengta.net',
# 'referer':'https://test-manager.51dengta.net/admin.php/system/publics/index.html',
# 'sec-fetch-dest':'empty',
# 'sec-fetch-mode':'cors',
# 'sec-fetch-site':'same-origin',
# # 'user-agent':'Mozilla/5.0 (Windows NT 6.1;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
'x-requested-with':'XMLHttpRequest',
}
r = requests.get('http://uat-manager.51dengta.net/admin.php/app/content_audit/video.html?page=1&limit=10000&name=1&sex=&role=&top=0&status=1&name_value=&label=',headers=headers)
data = r.json()['data']
for i in data:
    # if i['title'] == '':
    try:
        rs = requests.post('http://uat-manager.51dengta.net/admin.php/app/content_audit/toaudit.html?id={}'.format(i['id']),data={'label':randint(1,4)},headers=headers)
        if rs.status_code == 200 and rs.json()['msg'] == '操作成功':
            time.sleep(1)
            print(i['id'],rs.json()['msg'])
        else:
            print(rs.text)
    except Exception as e:
        print(e)