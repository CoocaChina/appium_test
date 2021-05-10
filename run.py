import os
import time
import unittest  # 单元测试框架
from time import sleep

from comm import sxc_appium_server
from testcase import sxc_xct_login
from BeautifulReport import BeautifulReport as bf  # 导入BeautifulReport模块，这个模块也是生成报告的模块，但是比HTMLTestRunner模板好看
from comm import sxc_test_log
from config.globalparameter import test_case_path,report_path,report_name


# class appTest(unittest.TestCase):
#     def setUp(self):
#         self.log = sxc_test_log.logger()
#         # self.log.info('开始测试')
#         self.wd = sxc_appium_server.startServer()
#         pass
#
#     @unittest.skip
#     def test_a_login(self):
#         # sxc_xct_login.xct_login(self.wd,"15757185534")
#         try:
#             self.wd.find_element_by_xpath("//*[@text='手机号登录']").click()
#             self.wd.find_element_by_xpath("//*[@text='请输入手机号']").send_keys("15757185534")
#             # self.wd.find_element_by_xpath("//android.widget.EditText[2]").send_keys("23456")
#             self.wd.keyevent(9)
#             self.wd.keyevent(10)
#             self.wd.keyevent(11)
#             self.wd.keyevent(12)
#             self.wd.keyevent(13)
#             self.wd.keyevent(66)
#             # self.wd.find_element_by_xpath('//*[contains(@content-desc, "登录")]').click()
#             self.wd.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()
#             sleep(5)
#         except BaseException:
#             print('登录出错')
#
#     @unittest.skip
#     def test_b_cutout(self):
#         self.wd.find_element_by_xpath("//*[@text='生产管理']").click()
#         sleep(2)
#         # cmyfty = self.wd.find_element_by_android_uiautomator('new UiSelector().text("兰陵001")').text
#         # self.log.info(self.wd.find_element_by_android_uiautomator('new UiSelector().text("兰陵001")').text)
#
#         self.wd.find_element_by_xpath("//*[@text='切底拉走']").click()
#         self.wd.find_element_by_xpath("//*[@text='切底地点']").click()
#         self.wd.find_element_by_xpath("//*[@text='sjf04']").click()
#         self.wd.find_element_by_xpath("//*[@text='确定']").click()
#         self.wd.find_element_by_xpath("//*[@text='添加切底原料']").click()
#         self.wd.find_element_by_xpath("//*[@text='熊鑫测试 [16475]']").click()
#         self.wd.find_element_by_xpath("//*[@text='确定']").click()
#         self.wd.find_element_by_xpath("//*[@text='提交']").click()
#         # duanyan = self.wd.find_element_by_android_uiautomator('new UiSelector().text("操作成功")').text
#         # self.log.info(self.wd.find_element_by_android_uiautomator('new UiSelector().text("操作成功")').text)
#         # self.assertEqual('操作成功', duanyan)
#         self.log.info(self.wd.page_source)
#
#     def test_c_createbill(self):
#         self.wd.find_element_by_xpath("//*[@text='原料采购']").click()
#         self.wd.find_element_by_xpath("//*[@text='创建需求单']").click()
#         self.wd.find_element_by_xpath("//*[@text='供应商']").click()
#         self.wd.find_element_by_xpath("//*[@text='王飞飞']").click()
#         self.wd.find_element_by_xpath("//*[@text='收货地址']").click()
#         self.wd.find_element_by_xpath("//*[@text='兰陵001']").click()
#         self.wd.find_element_by_xpath("//*[@text='发货时间']").click()
#         sleep(5)
#         self.wd.find_element_by_xpath("//*[@text='确定']").click()
#         self.wd.find_element_by_xpath("//*[@text='添加商品']").click()
#         self.wd.find_element_by_xpath("//*[@text='16475 熊鑫测试']").click()
#         self.wd.find_element_by_xpath("//*[@text='确定']").click()
#         self.wd.find_element_by_xpath("//android.widget.EditText[1]").click()
#         self.wd.keyevent(10)
#         self.wd.find_element_by_xpath("//android.widget.EditText[2]").click()
#         self.wd.keyevent(10)
#         try:
#             self.wd.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[7]/android.widget.EditText[1]").click()
#         except:
#             print(1)
#         self.wd.keyevent(10)
#         try:
#             self.wd.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[7]/android.widget.EditText[2]").click()
#         except:
#             print(1)
#         self.wd.keyevent(10)
#         self.wd.find_element_by_xpath("//*[@text='确定']").click()
#
#     @unittest.skip
#     def test_z_logout(self):
#         sxc_xct_login.xct_logout(self.wd)
#
#     def tearDown(self):,
#         self.wd.quit()
#         sleep(15)
#         appiumidcmd = "ps -ef|grep node|grep -v grep|cut -c 8-15|xargs kill -9"
#         os.system(appiumidcmd)
#         # print(type(appiumid))
#         # os.system('kill -9' + str(appiumid))





# 构造测试套件

suite = unittest.TestLoader().discover(start_dir=test_case_path,pattern='test*.py')
# 执行测试
runner = bf(suite)  # 实例化BeautifulReport模块
runner.report(filename=report_name, description='这个描述参数是必填的',report_dir='')
