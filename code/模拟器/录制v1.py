# 前提是，已经把 模拟器中的 api demo。apk应用启动进入首页
# 再运行下面的代码
from appium import webdriver

caps = dict()
caps["platformName"] = "android"
caps["deviceName"] = "emulator-5554"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_accessibility_id("OS")
el1.click()
el2 = driver.find_element_by_accessibility_id("Morse Code")
el2.click()
el3 = driver.find_element_by_id("io.appium.android.apis:id/text")
el3.clear()
el3.send_keys("hogworts")
print("222222222222")

driver.back()
driver.back()

driver.quit()