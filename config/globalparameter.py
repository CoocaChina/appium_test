# coding:utf-8
__author__ = "helen"

'''
description:配置全局参数
'''
import time,os
# 获取当前项目的存放路径
project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
# 测试用例代码存放路径（拥有构建suite）
test_case_path = project_path+"/testcase"
# 测试报告的存放路径，并以当前时间作为报告的前缀
report_path = "report/"
report_name = report_path+time.strftime('%Y-%m-%d_%H_%M_%S_',time.localtime())
# img存放路径
img_path = project_path+"/testcase/case_img/"
img_name = img_path+time.strftime('%Y-%m-%d_%H_%M_%S_',time.localtime())+".png"
# 日志存放
log_path = project_path+"/testlog/"
#yaml 路径
yaml_path = project_path+"/testcase/yaml/"
platformName = 'ANDROID'
platformVersion = '6.0'
# deviceName = '85ZTTCWS99999999'
deviceName = 'emulator-5554'
app = project_path+'/testApp/bossbb-android-release-1620963514573.apk'
appPackage = 'com.sxc.bossbb'
Activity = 'com.bossbb.MainActivity'
noReset = True
unicodeKeyboard = True
resetKeyboard = True