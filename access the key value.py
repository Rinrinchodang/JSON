import json
a="""{"key1":"value1","key2":"value2"}"""
b=json.loads(a)
print(b["key2"])