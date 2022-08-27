import json
dic={
    "name":"sam",
    "rool no":56,
    "cgpa":8.6,
    "no":96
}
with open("a.json","w") as outfile:
    json.dump(dic,outfile)
