import json
a={"key1":"value1","key2":"value2"}
a["key3"]="value3"
# b=open("myfile.json","w")
c=json.dumps(a,indent=2,separators=(",","="))
# separators=(",","=")
print(c)
