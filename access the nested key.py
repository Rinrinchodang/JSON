import json
a="""{
    "company":{
        "employee":{
            "name":"emma",
            "payable":{
                "salary":7000,
                "bonus":800}
        }
    }
}"""
b=json.loads(a)
print(b["company"]["employee"]["payable"]["salary"])