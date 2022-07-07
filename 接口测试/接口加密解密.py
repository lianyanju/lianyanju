import base64
import json


def decode():
    entext = "eyJ0b3BpY3MiOgp7CiJvcmFuZ2UiOiJtb3ZpZSIsCiJzaG9vbCI6InRlc3Rpbmctc3R1ZGlvIiwKInByZXNpZGVudCI6InNldmVuaXJ1YnkiCn0KfQo="
    r = base64.b64decode(entext)
    print(r)
    print(json.loads(r))#json字符串 转换成 json对象


if __name__ == '__main__':
    decode()

"""
b'{"topics":\n{\n"orange":"movie",\n"shool":"testing-studio",\n"president":"seveniruby"\n}\n}\n'
{'topics': {'orange': 'movie', 'shool': 'testing-studio', 'president': 'seveniruby'}}

"""