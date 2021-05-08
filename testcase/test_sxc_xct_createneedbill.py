import os
import time
import unittest  # 单元测试框架
from time import sleep

from comm import sxc_appium_server
from testcase import sxc_xct_login
from BeautifulReport import BeautifulReport as bf  # 导入BeautifulReport模块，这个模块也是生成报告的模块，但是比HTMLTestRunner模板好看
from comm import sxc_test_log
from comm.log import LOG, logger
from config.globalparameter import img_path
from comm import save_img

class appTest(unittest.TestCase):

    def setUp(self):
        self.log = sxc_test_log.logger()
        # self.log.info('开始测试')
        self.wd = sxc_appium_server.startServer()
        pass

    @bf.add_test_img('test_case_1')
    def test_c_createbill(self):
        shouye = self.wd.find_element_by_xpath("//*[@text='宋小菜工作台']").text
        if shouye != '宋小菜工作台':
            sxc_xct_login.xct_login(self.wd,'15757185534','23456')
        self.wd.find_element_by_xpath("//*[@text='原料采购']").click()
        self.wd.find_element_by_xpath("//*[@text='创建需求单']").click()
        self.wd.find_element_by_xpath("//*[@text='供应商']").click()
        self.wd.find_element_by_xpath("//*[@text='王飞飞']").click()
        self.wd.find_element_by_xpath("//*[@text='收货地址']").click()
        self.wd.find_element_by_xpath("//*[@text='兰陵001']").click()
        self.wd.find_element_by_xpath("//*[@text='发货时间']").click()
        sleep(5)
        self.wd.find_element_by_xpath("//*[@text='确定']").click()
        self.wd.find_element_by_xpath("//*[@text='添加商品']").click()
        self.wd.find_element_by_xpath("//*[@text='16475 熊鑫测试']").click()
        self.wd.find_element_by_xpath("//*[@text='确定']").click()
        self.wd.find_element_by_xpath("//android.widget.EditText[1]").click()
        self.wd.keyevent(10)
        self.wd.find_element_by_xpath("//android.widget.EditText[2]").click()
        self.wd.keyevent(10)
        try:
            self.wd.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[7]/android.widget.EditText[1]").click()
        except:
            print(1)
        self.wd.keyevent(10)
        try:
            self.wd.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[7]/android.widget.EditText[2]").click()
        except:
            print(1)
        self.wd.keyevent(10)
        self.wd.find_element_by_xpath("//*[@text='确定']").click()
        duanyan = self.wd.find_element_by_xpath("//*[@text='需求单']").text
        LOG.info(duanyan)
        self.assertEqual(duanyan,'需求单',"创建成功")

    def tearDown(self):
        self.wd.quit()
        sleep(15)
        appiumidcmd = "ps -ef|grep node|grep -v grep|cut -c 8-15|xargs kill -9"
        os.system(appiumidcmd)
        # print(type(appiumid))
        # os.system('kill -9' + str(appiumid))


