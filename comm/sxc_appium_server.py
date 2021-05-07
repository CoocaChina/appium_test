import os
from time import sleep
from appium import webdriver # appium库
from config.globalparameter import platformName,platformVersion,deviceName,app,appPackage,Activity,noReset,unicodeKeyboard,resetKeyboard


def startServer():
    # cmd = 'appium --address 127.0.0.1' + ' --port' + str(port) + ' --bootstrap-port ' + str(port - 2000) + ' -U ' +serial + ' -session-override --no-rest'
    cmd = 'appium -a 127.0.0.1 -p 4723 --session-override &'
    os.system(cmd)
    sleep(10)
    # cmd = 'appium -a 127.0.0.1 -p 4723 --session-override &'
    desired_caps = {}
    desired_caps['platformName'] = platformName
    # desired_caps['platformVersion'] = '10.0'
    # desired_caps['deviceName'] = 'CLBGL18A23000056'
    desired_caps['platformVersion'] = platformVersion
    desired_caps['deviceName'] = deviceName
    desired_caps['app'] = app
    desired_caps['appPackage'] = appPackage
    desired_caps['Activity'] = Activity
    # desired_caps['udid'] = serial
    # desired_caps['systemPort'] = systemPort
    desired_caps['noReset'] = noReset
    desired_caps["unicodeKeyboard"] = unicodeKeyboard
    desired_caps["resetKeyboard"] = resetKeyboard

    wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    wd.implicitly_wait(60)
    return wd