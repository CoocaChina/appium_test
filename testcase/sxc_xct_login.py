
from time import sleep

def xct_login(wd,mobile,pwd):

    wd.find_element_by_xpath("//*[@text='手机号登录']").click()
    # self.wd.find_element_by_xpath("//*[@text='测试用户列表']").click()
    wd.find_element_by_xpath("//*[@text='请输入手机号']").send_keys(mobile)
    wd.find_element_by_xpath("//android.widget.EditText[2]").send_keys(pwd)
    # wd.keyevent(9)
    # wd.keyevent(10)
    # wd.keyevent(11)
    # wd.keyevent(12)
    # wd.keyevent(13)
    # wd.keyevent(66)
    sleep(5)
    # self.wd.find_element_by_xpath('//android.widget.TextView[@text="登录"]').click()
    # self.wd.find_element_by_xpath('//*[@text="登录" and @index="0"]').click()
    # self.wd.find_element_by_xpath('//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup').click()
    # self.wd.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView")')[4].click()
    # self.wd.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("登录")').click()
    # self.wd.find_element_by_xpath('//*[contains(@content-desc, "登录")]').click()
    wd.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()
    # print(2)
    # self.wd.keyevent(66)
    # print(3)
    # self.touch_tap(100,100)
    # self.wd.tap([(64,724),(656,762)],1000)
    # self.wd.swipe(100,740,500,740,500)
    sleep(5)


def xct_logout(wd):
    wd.find_element_by_xpath("//*[@text='我的']").click()
    wd.find_element_by_xpath("//*[@text='退出登录']").click()