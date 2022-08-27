import json
c={}
filename="txt.file"
with open(filename) as f:
    for i in f:
        key,value=i.strip().split(None,1)
        c[key]=value
print(json.dumps(c,indent=2))
file=open("txt.json","w")
json.dump(c,file,indent=2)
file.close()
f.close()
