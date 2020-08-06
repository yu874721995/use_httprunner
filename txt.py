
import time,os
import os.path
import requests, json, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import win32gui
import win32con

times = time.strftime("%Y%m%d", time.localtime())
def work(xt,times):

    chrome_options = Options()
    chrome_options.add_argument('--window-size=1366,768')
    chrome_options.add_argument('--disable-infobars')
    # chrome_options.add_argument('--headless')#隐藏浏览器会导致无法选取windows窗口上传文件
    driver = webdriver.Chrome(r'E:\dengTa\chromedriver.exe', chrome_options=chrome_options)
    driver.get('https://www.pgyer.com')
    print('启动浏览器......')
    try:
        driver.implicitly_wait(2000)
        driver.find_element_by_xpath('//*[@id="homepage-new"]/div[2]/div[1]/div/div/div/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="loginByEmail"]/section[1]/label/input').send_keys(
            '15989510396')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('5454yu')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="submitButton"]').click()
        print('登录成功......')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="appUploadForm"]/div/a').click()
        print('开始上传......')
        time.sleep(1)
        dialog = win32gui.FindWindow('#32770', '打开')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, r'Z:\测试部\app\等Ta\test\{}\{}'.format(times,filename))
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        time.sleep(1)
        while 1:
            if driver.title == '蒲公英 - 即将完成':
                driver.find_element_by_xpath('//*[@id="name"]').send_keys('-test-{}'.format(times))
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="submitButton"]').click()
                break
            else:
                print('等待上传完成......')
                time.sleep(1)
                pass
        time.sleep(1)
        print('上传成功....')
        driver.find_element_by_xpath('//*[@id="wxmp"]/div/div/div/section[1]/button').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div/a').click()
        time.sleep(2)
        handles = driver.window_handles
        time.sleep(2)
        driver.switch_to_window(handles[1])
        time.sleep(2)
        if xt == 'Android':
            driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="submitButton"]').click()
        time.sleep(1)
        url = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/img').get_attribute('src')
        time.sleep(2)
        try:
            driver.close()
        except Exception as e:
            print(e)
        finally:
            driver.quit()
        headers = {"Content-Type": "application/json"}
        data = {
            'msgtype': 'markdown',
            'markdown': {
                'title': '{}新安装包'.format(times),
                'text': r"#### ...下面是{}最新{}安装包二维码... ![screenshot]({})".format(
                    times,xt,url)
            },
            'at': {
                "atMobiles": ['15989510396', '13434435107'], 'isAtAll': True
            }
        }
        r = requests.post(
            'https://oapi.dingtalk.com/robot/send?access_token=afb093a2e7bc0c64947a2a46d193c21347e1ffc609fac83dcd9d940083a9cd6f',
            data=json.dumps(data), headers=headers)
        print('发送消息成功......')
    except:
        driver.close()
        driver.quit()
        raise Exception




list = []
while 1:
    num = 1
    filenames = r'Z:\测试部\app\等Ta\test\{}'.format(times)
    xt = ''
    file_exist = os.path.isdir(filenames)
    print('文件夹名称：{}'.format(filenames))
    print('检测是否存在今日{}新文件夹:'.format(times),file_exist)
    if file_exist:
        for dirpath, dirnames, filenames in os.walk(filenames):
            for filename in filenames:
                if filename not in list and filename != '.DS_Store':
                    azb = filename[-3:]
                    if azb == 'ipa':
                        xt = 'IOS'
                    else:
                        xt = 'Android'
                    print('检测到有新{}安装包:'.format(xt), filename)
                    # 上传蒲公英
                    try:
                        work(xt,times)
                        list.append(filename)
                    except Exception as e:
                        print(e)
                        print('上传失败，即将重试第{}次'.format(num))
                        num += 1
                else:
                    print('所有安装包已上传......')

    time.sleep(60)





