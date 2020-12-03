
import time,os
import os.path
import requests, json, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import win32gui
import win32con

times = time.strftime("%Y%m%d", time.localtime())
# times = 20200912
def work(type,xt,times):

    #各个环境对应app的上传账号
    pyger = {'test':{'username':'15989510396','password':'yu19950122','name':'测试'},
             'uat':{'username':'13428985701','password':'wang848586','name':'预发布'},
             'master':{'username':'13434435103','password':'abc1234','name':'正式'}}

    #设置selenium启动项
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1366,768')
    chrome_options.add_argument('--disable-infobars')
    # chrome_options.add_argument('--headless')#隐藏浏览器会导致无法选取windows窗口上传文件

    #开始启动浏览器
    driver = webdriver.Chrome(r'E:\dengTa\chromedriver.exe', chrome_options=chrome_options)
    driver.get('https://www.pgyer.com')
    print('启动浏览器成功......')
    try:
        driver.implicitly_wait(2000)
        # driver.find_element_by_xpath('//*[@id="homepage-new"]/div[2]/div[3]/div/div/div/span[2]').click()
        time.sleep(1)
        driver.find_element_by_link_text('立即发布').click()
        # driver.find_element_by_xpath('//*[@id="banner07f3d0f60a453e6f35c630b6e848ef80"]/div/div/div/a').click()
        time.sleep(1)

        #登录蒲公英
        driver.find_element_by_xpath('//*[@id="loginByEmail"]/section[1]/label/input').send_keys(
        pyger[type]['username'])  # 15989510396
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(pyger[type]['password'])
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="submitButton"]').click()
        print('登录成功......')


        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="appUploadForm"]/div/a').click()
        print('开始上传......')
        time.sleep(1)

        #获取windows文件选择弹窗句柄
        dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, r'Z:\测试部\app\等Ta\{}\{}\{}'.format(type,times,filename))
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

        time.sleep(1)
        while 1:
            if driver.title == '蒲公英 - 即将完成':
            # if driver.title == '蒲公英 - 应用概述':
            #     driver.find_element_by_xpath('//*[@id="name"]').send_keys('-test-{}'.format(times))
                #driver.find_element_by_xpath('//*[@id="version_result"]/tr[1]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="submitButton"]').click()
                break
            else:
                print('等待上传完成......')
                time.sleep(1)
                pass
        time.sleep(1)
        print('上传成功....')
        driver.find_element_by_xpath('//*[@id="version_result"]/tr[1]').click()
        time.sleep(2)
        handles = driver.window_handles
        driver.switch_to_window(handles[1])
        if xt == 'Android' and type == 'test':
            try:
                driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
                time.sleep(2)
                sub = driver.find_element_by_xpath('//*[@id="submitButton"]')
                driver.execute_script("return arguments[0].scrollIntoView();",sub)
                driver.find_element_by_xpath('//*[@id="submitButton"]').click()
            except Exception:
                pass
        time.sleep(1)
        url = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/img').get_attribute('src')
        print(url)
        time.sleep(2)
        try:
            driver.close()
        except Exception as e:
            print(e)
        finally:
            driver.quit()

        #调用钉钉机器人接口发送消息
        headers = {"Content-Type": "application/json"}
        data = {
            'msgtype': 'markdown',
            'markdown': {
                'title': '{}新安装包'.format(times),
                'text': r"#### ...下面是{}-{}环境最新{}安装包二维码... ![screenshot]({})".format(
                    times,pyger[type]['name'],xt,url)
            },
            'at': {
                "atMobiles": ['15989510396', '13434435107'], 'isAtAll': True
            }
        }
        r = requests.post(
            'https://oapi.dingtalk.com/robot/send?access_token=afb093a2e7bc0c64947a2a46d193c21347e1ffc609fac83dcd9d940083a9cd6f',
            data=json.dumps(data), headers=headers)
        print('发送消息成功......')
    except Exception as e:
        print(e)
        driver.close()
        driver.quit()
        raise Exception

list = []
while 1:
    num = 1
    type = ['test','uat','master']
    for i in type:
        filenames = r'Z:\测试部\app\等Ta\{}\{}'.format(i,times)
        xt = ''
        file_exist = os.path.isdir(filenames)
        exist = '是' if file_exist ==True else '否'
        print('文件夹名称：{}'.format(filenames))
        print('检测是否存在今日{}{}新文件夹:'.format(times,i),exist)
        if file_exist:
            for dirpath, dirnames, filenames in os.walk(filenames):
                for filename in filenames:
                    if filename not in list and filename != '.DS_Store':
                        azb = filename[-3:]
                        if azb == 'ipa':
                            xt = 'IOS'
                        else:
                            xt = 'Android'
                        print('检测到有新{}环境{}安装包:'.format(i,xt), filename)
                        # 上传蒲公英
                        try:
                            work(i,xt,times)
                            list.append(filename)
                        except Exception as e:
                            print(e)
                            print('上传失败，即将重试第{}次'.format(num))
                            num += 1
                            continue
                    else:
                        print('所有安装包已上传......')

    time.sleep(10)





