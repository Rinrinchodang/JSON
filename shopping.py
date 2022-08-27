import json
a={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
item=input("enter the item:")
quantity=int(input("enter how much you want to buy:"))
b=a["shopping_list"][item]
r=int(b)-quantity
a["shopping_list"][item]=r
f=open("meraki9.json","w")
y=json.dump(a,f,indent=2)
f.close()