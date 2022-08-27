import json
data={"key1":"value1","key2":"value2"}
a=json.dumps(data)
x=type(a)
print(x)