import os
import time
import unittest  # 单元测试框架
from time import sleep

from comm import sxc_appium_server
from testcase import sxc_xct_login
from BeautifulReport import BeautifulReport as bf  # 导入BeautifulReport模块，这个模块也是生成报告的模块，但是比HTMLTestRunner模板好看
from comm import sxc_test_log
from comm.log import LOG, logger
from comm import adbCommon
from config.globalparameter import img_path
from comm.save_img import save_img

class appTest(unittest.TestCase):

    def setUp(self):
        self.log = sxc_test_log.logger()
        # self.log.info('开始测试')
        self.wd = sxc_appium_server.startServer()
        pass

    @bf.add_test_img('test_case_1')
    def test_a_createbill(self):
        """创建需求单用例"""
        try:
            shouye = self.wd.find_element_by_xpath("//*[@text='宋小菜工作台']").text
        except:
            shouye = ''
        if shouye != '宋小菜工作台':
            sxc_xct_login.xct_login(self.wd,'13988885326','12345')
        self.wd.find_element_by_xpath("//*[@text='档口宝']").click()
        self.wd.find_element_by_xpath("//*[@text='长山档口']").click()
        self.wd.find_element_by_xpath("//*[@text='南庄兜档口-测试']").click()
        self.wd.find_element_by_xpath("//*[@text='需求单']").click()
        self.wd.find_element_by_xpath("//*[@text='新增需求单']").click()
        sleep(5)
        self.wd.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.TextView[1]").click()
        sleep(2)
        self.wd.find_element_by_xpath("//*[@text='选好了']").click()
        sleep(1)
        self.wd.find_element_by_xpath("//*[@text='提交']").click()
        LOG.info(self.wd.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[2]").text)
        #打开云掌柜
        self.wd.start_activity('com.sxc.yunzhanggui.alfred', 'com.alfred.MainActivity')
        try:
            shouye2 = self.wd.find_element_by_xpath("//*[@text='云掌柜']").text
        except:
            shouye2 = ''
        if shouye2 != '云掌柜':
            sxc_xct_login.xct_login(self.wd,'13758106666','12345')


        self.wd.find_element_by_xpath("//*[@text='内采需求单']").click()
        self.wd.find_element_by_xpath("//*[@text='杭州市']").click()
        self.wd.find_element_by_xpath("//*[@text='选择站点']").click()
        self.wd.find_element_by_xpath("//*[@text='南庄兜档口']").click()
        self.wd.find_element_by_xpath("//*[@text='提交']").click()
        self.wd.find_element_by_xpath("//*[@text='9361 云采姜三级34斤']").click()
        self.wd.find_element_by_xpath("//*[@text='提交']").click()
        self.wd.find_element_by_xpath("//*[@text='供应商']").click()
        self.wd.find_element_by_xpath("//*[@text='王飞飞']").click()
        self.wd.find_element_by_xpath("//*[@text='交货地址']").click()
        self.wd.find_element_by_xpath("//*[@text='杭州天冉中心仓']").click()
        self.wd.find_element_by_xpath("//*[@text='价格待补充']").click()
        self.wd.find_element_by_xpath("//*[@text='提交']").click()
        sleep(3)
        self.wd.find_element_by_xpath("//*[@text='确认']").click()
        sleep(1)
        self.wd.find_element_by_xpath("//*[@text='提交']").click()
        self.wd.find_element_by_xpath("//*[@text='完成']").click()

        #打开宋小菜供应商APP

        self.wd.start_activity('com.sxc.warehouse','com.warehouse.MainActivity')
        try:
            shouye1 = self.wd.find_element_by_xpath("//*[@text='接货管理 - 测试']").text
        except:
            shouye1 = ''
        if shouye1 != '接货管理 - 测试':
            sxc_xct_login.xct_login(self.wd,'18857169672','12345')
        self.wd.find_element_by_xpath("//*[@text='承运单']").click()
        sleep(3)
        self.wd.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView[1]").click()
        self.wd.find_element_by_xpath("//*[@text='请选择配送站点']").click()
        self.wd.find_element_by_xpath("//*[@text='添加配送点']").click()
        self.wd.find_element_by_xpath("//*[@text='[档口]南庄兜档口-测试20004']").click()
        sleep(3)
        self.wd.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup[1]").click()
        self.wd.find_element_by_xpath("//*[@text='提交']").click()
        self.wd.find_element_by_xpath("//*[@text='可见内容']").click()
        self.wd.find_element_by_xpath("//*[@text='只显示有应配量的 SKU']").click()
        self.wd.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView[1]").click()
        self.wd.find_element_by_xpath("//*[@text='下一步']").click()
        self.wd.find_element_by_xpath("//*[@text='输入司机姓名/手机号']").send_keys('1575718553')
        self.wd.find_element_by_xpath("//*[@text='是简单']").click()
        self.wd.find_element_by_xpath("//android.widget.EditText[@text='请输入']").send_keys('222')
        self.wd.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[5]/android.view.ViewGroup[1]/android.widget.TextView[3]").click()
        sleep(3)
        self.wd.find_element_by_xpath("//*[@text='确认']").click()
        self.wd.find_element_by_xpath("//*[@text='提交']").click()
        self.wd.find_element_by_xpath("//*[@text='完成']").click()
        self.wd.find_element_by_xpath("//*[@text='我的']").click()
        self.wd.find_element_by_xpath("//*[@text='退出登录']").click()

        sxc_xct_login.xct_login(self.wd, '18158171590', '12345')
        self.wd.find_element_by_xpath("//*[@text='承运单']").click()
        self.wd.find_element_by_xpath("//*[@text='司机：是简单 15757185534']").click()
        self.wd.find_element_by_xpath("//*[@text='操作']").click()
        self.wd.find_element_by_xpath("//*[@text='快捷发货']").click()
        self.wd.find_element_by_xpath("//*[@text='确定']").click()

        self.wd.start_activity('com.sxc.bossbb', 'com.bossbb.MainActivity')
        self.wd.find_element_by_xpath("//*[@text='档口宝']").click()
        self.wd.find_element_by_xpath("//*[@text='长山档口']").click()
        self.wd.find_element_by_xpath("//*[@text='南庄兜档口-测试']").click()
        self.wd.find_element_by_xpath("//*[@text='签收管理']").click()
        self.wd.find_element_by_xpath("//*[@text='去签收']").click()
        self.wd.find_element_by_xpath("//*[@text='输入']").send_keys('2')
        self.wd.find_element_by_xpath("//*[@text='确认签收']").click()

    def tearDown(self):
        self.wd.quit()
        sleep(15)
        appiumidcmd = "ps -ef|grep node|grep -v grep|cut -c 8-15|xargs kill -9"
        os.system(appiumidcmd)
        # print(type(appiumid))
        # os.system('kill -9' + str(appiumid))


