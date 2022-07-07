import pytest

""" 至于编码问题可以看conftest文件"""


# @pytest.mark.parametrize("goods_name", ["黄金瓜", "大西瓜"])
@pytest.mark.parametrize("goods_name", ["黄金瓜"])
def test_goods(goods_name):
    print(f"商品的名字为:{goods_name}")
    assert type(goods_name) == str
