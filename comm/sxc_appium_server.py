import os
from time import sleep
from appium import webdriver # appium库


def startServer():
    # cmd = 'appium --address 127.0.0.1' + ' --port' + str(port) + ' --bootstrap-port ' + str(port - 2000) + ' -U ' +serial + ' -session-override --no-rest'
    cmd = 'appium -a 127.0.0.1 -p 4723 --session-override &'
    os.system(cmd)
    sleep(10)
    # cmd = 'appium -a 127.0.0.1 -p 4723 --session-override &'
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '10.0'
    # desired_caps['deviceName'] = 'CLBGL18A23000056'
    desired_caps['platformVersion'] = '6.0'
    desired_caps['deviceName'] = '85ZTTCWS99999999'
    desired_caps['app'] = '/Users/shijifeng/PycharmProjects/appium_test/testApp/bossbb-android-release-1619593549681.apk'
    desired_caps['appPackage'] = 'com.sxc.bossbb'
    desired_caps['Activity'] = 'com.bossbb.MainActivity'
    # desired_caps['udid'] = serial
    # desired_caps['systemPort'] = systemPort
    desired_caps['noReset'] = True
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeyboard"] = True

    wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    wd.implicitly_wait(60)
    return wd