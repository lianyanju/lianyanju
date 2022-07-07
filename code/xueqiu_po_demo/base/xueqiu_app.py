"""
app 相关的操作： start、  stop 、重启、切后台


"""
import logging

from appium import webdriver

from code.xueqiu_po_demo.base.basepage import BasePage



class XueQiuApp(BasePage):

    # 启动app
    def start(self):
        if self.driver is None:

            logging.info("driver初始化启动")
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = 'com.xueqiu.android'
            desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
            desired_caps['skipDeviceInitialization'] = 'true'  # 跳过安装、权限设置操作
            desired_caps['autoAcceptAlerts'] = 'true'  # 默认选择接受弹窗的条款，有些app启动的时候，会有一些权限的弹窗
            desired_caps['noReset'] = "true"
            desired_caps['unicodeKeyBoard'] = 'true'
            desired_caps['resetKeyBoard'] = 'true'

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(40)
        else:
            logging.info("driver复用")
            self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        pass

    # 没有实际意义 只是 切换到主页面
    def go_main(self):
        from code.xueqiu_po_demo.page.main_page import MainPage
        return MainPage(self.driver)
