#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"
import time
from selenium import webdriver

"""
此配置文件用来统一配置自动化测试用例的路径，
环境变量等
"""

#all dir config
#testcase dir
testCase_dir = "D:\\Workstation\\Code\\Python\\Pytho3.5\\Python_study\\Workstation\\Workspace\\tools\\autoTest\\run\\core"
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_FilePath = "D:\\Workstation\\Code\\Python\\Pytho3.5\\Python_study\\Workstation\\Workspace\\tools\\autoTest\\run\\report\\"
report_FileName = "D:\\Workstation\\Code\\Python\\Pytho3.5\\Python_study\\Workstation\\Workspace\\tools\\autoTest\\run\\report\\" + now + 'result.html'


#para
base_url = "http://192.168.56.101:8080/#!/login"

#浏览器类型
browser_type = "chrome"
def browser_select():
    if browser_type == "Firefox" or browser_type == "firefox":
        return  webdriver.Firefox()
    elif browser_type == "Chrome" or browser_type == "chrome":
        return webdriver.Chrome()