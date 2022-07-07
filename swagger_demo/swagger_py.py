import json

import swagger2


url = 'https://petstore.swagger.io/v2/swagger.json'

swagger = swagger2.parse(url)

print('转换接口：{}个'.format(len(swagger.apis)))

api_path = 'api.json'
with open(api_path,mode='w',encoding='utf8') as f:
    f.write(json.dumps(swagger.apis,ensure_ascii=False))

'''api.json内容

[
    {
        "id": "de0993295bf94750980b3bf62e08a02b",
        "name": "uploadFile",
        "method": "post",
        "path": "/v2/pet/{petId}/uploadImage",
        "url": "https://petstore.swagger.io/v2/pet/{petId}/uploadImage",
        "headers": {
            "Content-Type": "multipart/form-data"
        },
        "paths": {
            "petId": 0
        },
        "query": {},
        "json": {},
        "form": {},
        "formData": {
            "additionalMetadata": "string",
            "file": "file.txt"
        }
    },
    {
        "id": "8b5d1baa6cc44e418861bc97c1a04855",
        "name": "addPet",
        "method": "post",
        "path": "/v2/pet",
        "url": "https://petstore.swagger.io/v2/pet",
        "headers": {
            "Content-Type": "application/json"
        },
        "paths": {},
        "query": {},
        "json": {
            "id": 0,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "doggie",
            "photoUrls": [],
            "tags": [],
            "status": "string"
        },
        "form": {},
        "formData": {}
    },
    ...
    ...
]
'''