import json
# a=["neelam","programer","24","2400"]
# ["komal","trainer","24","20000"],
# ["anuradha","HR","25","40000"],
# ["Abhishek","manager","29","63000"],
# b=["name","designation","age","salary"]
# **
a=["neelam","programer","24","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
e=["name","designation","age","salary"]
# c={}
# i=0
# while i<len(a):
#     d={}
#     j=0
#     while j<len(a[i]):
#         c[b[j]]=a[i][j]
#         j+=1
#     i+=1
#     m="emp"+str(i)
#     d[m]=c
#     print(d)

dic1={}
dic2={}
dic3={}
dic4={}
dic={}
i=0
while i<len(a):
    dic1[e[i]]=a[i]
    dic2[e[i]]=b[i]
    dic3[e[i]]=c[i]
    dic4[e[i]]=d[i]
    i=i+1
dic["emp"]=dic1
dic["emp"]=dic2
dic["emp"]=dic3
dic["emp"]=dic4
print(dic)
f=open("meraki8.json","w")
j=json.dump(dic,f,indent=2)
f.close()

# d={}
# i=0
# while i<len(a):
#     s={}
#     m="emp"+str(i+1)
#     j=0
#     while j<len(a[i]):
#         s[b[j]]=a[i][j]
#         j+=1
#     i+=1
#     d[m]=s
# with open("meraki 8.json","w") as f:
#     y=json.dump(d,f,indent=2)
