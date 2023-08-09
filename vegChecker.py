import json
with open("./items.json") as json_file:
    data=json.load(json_file)
print("To exit type exit it promt")
for item in data.keys():
    
    if data[item]["isVeg"]=="":
        flag=input(f"Is the {item} veg (Y/n)")
        flag=flag.lower()
        if flag=="": flag="y"
        if flag=="y":            
            data[item]["isVeg"]=True;
        else:
            data[item]["isVeg"]=False;

with open("./items.json","w") as json_file:
    json.dump(data,json_file)
    
