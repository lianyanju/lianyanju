"""
   最常用的一种鉴权方式
   获取之后，在后续的每次请求的头中传递：headers=****，key-value，key是和服务端协商好自定义的

"""
import requests


class TestTokenVerify:
    def setup_class(self):
        self.proxy = {
            "http": "http://127.0.0.1:8889",
            "https": "http://127.0.0.1:8889",
        }

    def test_litemall_token(self):

        login_url = "http://litemall.hogwarts.ceshiren.com/admin/auth/login"
        login_data ={"username":"admin123","password":"admin123","code":""}

        r = requests.post(login_url,json=login_data)
        token = r.json()["data"]["token"]
        print(token)

        nnotice_url ="http://litemall.hogwarts.ceshiren.com/admin/profile/nnotice"
        headers_data ={"X-Litemall-Admin-Token": token}
        r2 = requests.get(nnotice_url, headers=headers_data)
        print(r2.json())