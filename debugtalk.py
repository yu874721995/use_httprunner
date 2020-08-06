# import hashlib
# import hmac
# import random
# import string
# import requests
#
# SECRET_KEY = "DebugTalk"
#
#
# def get_cookies():
#     cookie = requests.sessions.RequestsCookieJar()
#     r = requests.post("http://dev.manager.51dengta.net/admin.php/system/publics/index.html",data={
#         "username":"admin",
#         'password':'e10adc3949ba59abbe56e057f20f883e',
#         '__token__':'42b32e03ac033c348e5ca781a048e45c',
#         'captcha':''
#     })
#     cookiess = {c.name:c.value for c in r.cookies}
#     return cookiess
#     # cookie.update(r.cookies)
#     # return cookie
#
# def get_data():
#     data = {
#         'phone':'15900000006'
#     }
#     return data
import requests,json,time

headers = {"Content-Type": "application/json"}
data = {
                      'msgtype':'markdown',
                      'markdown':{
                          'title':'{}新安装包'.format('20200714'),
                          'text':r"#### .........   下面是{}安装包二维码 ![screenshot]({})\n>".format('https://www.pgyer.com/app/qrcode/9oTx?sign=&auSign=&code=')
                      },
    'at':{
"atMobiles":['15989510396','13434435107'],'isAtAll':False
    }
                  }
r = requests.post('https://oapi.dingtalk.com/robot/send?access_token=afb093a2e7bc0c64947a2a46d193c21347e1ffc609fac83dcd9d940083a9cd6f',
                  data=json.dumps(data),headers=headers)
print(r.text)

