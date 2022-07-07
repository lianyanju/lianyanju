# 前提是，已经把 模拟器中的 api demo。apk应用启动进入首页
# 再运行下面的代码


"""
   本次优化为：结合测试框架pytest，让测试框架管理用例
"""
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class Testdemo:
    def setup(self):
        caps = dict()
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["ensureWebviewsHavePages"] = True
        caps["noReset"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def teardown(self):
        self.driver.quit()

    def test_input(self):
        el1 = self.driver.find_element_by_accessibility_id("OS")
        el1.click()
        el2 = self.driver.find_element_by_accessibility_id("Morse Code")
        el2.click()
        el3 = self.driver.find_element(By.ID, "io.appium.android.apis:id/text")
        el3.clear()
        el3.send_keys("mugworts")
        sleep(2)
        self.driver.back()
        self.driver.back()
        # 此处加断言

        result = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[@content-desc='Accessibility']").text

        assert result == "Accessibility"
