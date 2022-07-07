import logging
import traceback

import allure
from appium.webdriver.common.mobileby import MobileBy

BLACK_LISTS = [(MobileBy.ID, "com.xueqiu.android:id/iv_action_back")]

"""
黑名单处理 【在定位元素时 会可能出现突然的弹框，这样就会异常找不到元素】
1:  app 弹框异常处理
2:  这里的fun 就是 修饰的函数 find
"""


def black_wrapper(fun):
    def run(*args, **kwargs):
        from code.xueqiu_po_demo.base.basepage import BasePage
        basepage: BasePage = args[0]

        try:
            return fun(*args, **kwargs)

        except Exception as e:

            screenshot_name = basepage.get_png_name("black_wrapper")
            screenshot_path = "./../image/" + screenshot_name
            basepage.screenshot(screenshot_path)
            logging.info(f"完成截图：{screenshot_path}")

            # 执行黑名单
            logging.info("执行黑名单")
            for black in BLACK_LISTS:
                logging.info(f"执行黑名单,当前的弹框是：{black}")
                eles = basepage.driver.find_elements(*black)

                if len(eles) > 0:
                    eles[0].click()

                    # 进行执行当前的元素查找---递归
                    logging.info("进行执行当前的元素查找")
                    return fun(*args, **kwargs)

            logging.error(f"元素查找失败：{e}")

            # 截图放到 报告中

            allure.attach.file(screenshot_path, "截图1111", allure.attachment_type.PNG)

            # 控制台格式的日志
            logging.error(f"traceback.format_exc：{traceback.format_exc()}")
            raise e

    return run
