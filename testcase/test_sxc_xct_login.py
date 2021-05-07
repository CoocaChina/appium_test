import os
import time
import unittest  # 单元测试框架
from time import sleep

from comm import sxc_appium_server
from testcase import sxc_xct_login
from BeautifulReport import BeautifulReport as bf  # 导入BeautifulReport模块，这个模块也是生成报告的模块，但是比HTMLTestRunner模板好看
from comm import sxc_test_log
from testMode.exectfuntion import Makeappcase
from comm.log import LOG, logger

class appTest(unittest.TestCase):
    def setUp(self):
        self.log = sxc_test_log.logger()
        # self.log.info('开始测试')
        self.wd = sxc_appium_server.startServer()
        pass

    # def test_a_login(self):
    #     # sxc_xct_login.xct_login(self.wd,"15757185534")
    #     try:
    #         self.wd.find_element_by_xpath("//*[@text='手机号登录']").click()
    #         self.wd.find_element_by_xpath("//*[@text='请输入手机号']").send_keys("15757185534")
    #         # self.wd.find_element_by_xpath("//android.widget.EditText[2]").send_keys("23456")
    #         self.wd.keyevent(9)
    #         self.wd.keyevent(10)
    #         self.wd.keyevent(11)
    #         self.wd.keyevent(12)
    #         self.wd.keyevent(13)
    #         self.wd.keyevent(66)
    #         # self.wd.find_element_by_xpath('//*[contains(@content-desc, "登录")]').click()
    #         self.wd.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()
    #         sleep(5)
    #     except BaseException:
    #         print('登录出错')

    def test_login(self, **kwargs):
        path = os.getcwd()
        path_ = os.path.join(os.path.join(path, 'yaml/'))
        self.path = path_ + 'login.yaml'
        print(self.path)
        self.deriver = self.wd
        self.open = Makeappcase(self.deriver, path=self.path)
        f = self.open.exce_case(**kwargs)
        if f['code'] == 1:
            LOG.info('无法获取断言')
            return
        else:
            beijing = f['data']
            return beijing

    def tearDown(self):
        self.wd.quit()
        sleep(15)
        appiumidcmd = "ps -ef|grep node|grep -v grep|cut -c 8-15|xargs kill -9"
        os.system(appiumidcmd)
        # print(type(appiumid))
        # os.system('kill -9' + str(appiumid))


