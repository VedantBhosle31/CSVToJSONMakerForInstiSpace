import os
import json
#import chardet
# prices=[]
allItems={}

files = os.listdir("./csv")
print(files)

for csv in files:
#    with open("./csv/"+csv, 'rb') as file:
 #       print(chardet.detect(file.read()))
    suppliers=csv[:-4]
    print("opened " + csv)
    itemNamesAndPrices=[]
    with open("./csv/"+csv) as file:
        for line in file:
            a=line.strip().split(',')
#            print(a)
            try:
                itemNamesAndPrices.append(a)
                prices.append(float(a[1]))
            except:
                continue;
    
    for item in itemNamesAndPrices:
        try:
#            print(item)
            allItems[item[0]]={}
            allItems[item[0]]["supplier"]=suppliers
            allItems[item[0]]["price"]=item[1]
            try:
                allItems[item[0]]["isVeg"]=item[2]
            except:
                allItems[item[0]]["isVeg"]=True
                #This is the default case
        except:
            continue

            
with open("./items.json","w") as output:
    json.dump(allItems,output)

