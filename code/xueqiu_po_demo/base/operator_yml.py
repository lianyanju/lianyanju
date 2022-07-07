import logging

import yaml

"""让yaml文件中的数据和测试用例之间建立关联
   据说把yaml文件中的数据读取出来
"""


def get_data(filename):
    logging.info(f"读取yaml文件数据{filename}")
    logging.info("==================")
    with open(filename) as f:
        datas = yaml.safe_load(f)

        logging.info(f"yaml文件数据是：{datas}")

        return datas
