import json
sj={"id":1,"name":"value2","age":29}
a=open("myfile.json","w")
c=json.dump(sj,a,indent=2,sort_keys=True)
a.close()