

def touch_tap(wd, x, y, duration=1000):  # 点击坐标  ,x1,x2,y1,y2,duration
    '''
    method explain:点击坐标
    parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
    Usage:
        device.touch_coordinate(277,431)      #277.431为点击某个元素的x与y值
    '''
    screen_width = wd.get_window_size()['width']  # 获取当前屏幕的宽
    screen_height = wd.get_window_size()['height']  # 获取当前屏幕的高

    # a = (float(x) / screen_width) * screen_width
    a = 0.5 * screen_width
    x1 = int(a)
    # b = (float(y) / screen_height) * screen_height
    b = 0.427 * screen_height
    y1 = int(b)
    print(screen_height, screen_width)
    print(wd.find_element_by_android_uiautomator('new UiSelector().text("登录")').get_attribute('bounds'))
    try:
        print(wd.find_element_by_android_uiautomator('new UiSelector().text("登录")').get_attribute('index'))
    except BaseException:
        print(222222)

    # print(self.wd.find_element_by_xpath("//*[@text='登录']").get_attribute('text'))
    print(x1, y1)
    wd.tap([(x1, y1), (x1, y1)], duration)