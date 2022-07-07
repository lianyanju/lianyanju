import requests
from requests_mock import Mocker

with Mocker() as mock:
    # 注意，mock的地址但一定要和请求的地址一致
    mock.get("http://www.google.com", status_code=200, json={"a": 1})

    rep = requests.get("http://www.google.com")#这个请求就不再发出去了
    assert rep.status_code == 200
    assert rep.json() == {"a": 1}

if __name__ == '__main__':
    pass
