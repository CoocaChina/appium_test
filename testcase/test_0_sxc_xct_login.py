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
from config.globalparameter import yaml_path
from comm.save_img import save_img

class appTest(unittest.TestCase):
    def setUp(self):
        self.log = sxc_test_log.logger()
        # self.log.info('开始测试')
        self.wd = sxc_appium_server.startServer()
        pass


    @bf.add_test_img('test_errors_save_imgs')
    def test_a_login(self):
        """测试登录"""
        # time.sleep(10)
        # shouye = self.wd.find_element_by_xpath("//*[@text='宋小菜工作台']").text
        # if shouye == '宋小菜工作台':
        #     sxc_xct_login.xct_logout(self.wd)
        # sxc_xct_login.xct_login(self.wd,"15757185534")
        try:
            self.wd.find_element_by_xpath("//*[@text='手机号登录']").click()
            self.wd.find_element_by_xpath("//*[@text='请输入手机号']").send_keys("15757185534")
            # self.wd.find_element_by_xpath("//android.widget.EditText[2]").send_keys("23456")
            self.wd.keyevent(9)
            self.wd.keyevent(10)
            self.wd.keyevent(11)
            self.wd.keyevent(12)
            self.wd.keyevent(13)
            self.wd.keyevent(66)
            # self.wd.find_element_by_xpath('//*[contains(@content-desc, "登录")]').click()
            self.wd.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()
            save_img(self.wd,'test_errors_save_imgs')
            sleep(5)
        except BaseException:
            print('登录出错')
    # @bf.add_test_img('test_case_1')
    # def test_login(self):
    #     self.path = yaml_path + 'login.yaml'
    #     print(self.path)
    #     self.deriver = self.wd
    #     self.open = Makeappcase(self.deriver, path=self.path)
    #     f = self.open.exce_case()
    #     save_img(self.wd,'test_case_1')
    #     if f['code'] == 1:
    #         LOG.info('无法获取断言')
    #         return
    #     else:
    #         beijing = f['data']
    #         return beijing

    def tearDown(self):
        self.wd.quit()
        sleep(15)
        appiumidcmd = "lsof -n -i:4723 | grep LISTEN | awk '{print $2}' | xargs kill"
        os.system(appiumidcmd)


