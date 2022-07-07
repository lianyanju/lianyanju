
# 运行起来没有保证且有打印 就是表示 安装的appium 配置安装配置ok
from appium import webdriver

desired_caps = dict()
# 创建一个空字典


desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'emulator-5554'  # 随便取
desired_caps['appPackage'] = 'com.android.settings'  # 设置应用
desired_caps['appActivity'] = 'com.android.settings.Settings'  # 首页面

# /wd/hub
# wd：可以理解是WebDriver的缩写
# hub：是指主节点、中心节点
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print("启动【设置】应用")
driver.quit()
