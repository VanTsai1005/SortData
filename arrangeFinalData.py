# !coding:utf-8
from pymongo import MongoClient

with open("E:/project/ArrangeData/Location_final.txt", "r") as f:
    locationNames = f.readlines()
    f.close()

uri = "mongodb://13.113.88.246:27017"
uri1 = "mongodb://10.120.37.128:27017"
client = MongoClient(uri)
client1 = MongoClient(uri1)
db = client.__getitem__("g3site")
db1 = client1.__getitem__("g3site")
collection = db.__getitem__("g3site_Address")
collection1 = db.__getitem__("travel")
collection2 = db1.__getitem__("g3site_Address")
print collection.count()
print collection2.count()
locationList = []
collectSet = set()
num = 0
for idx, item in enumerate(collection2.find()):
    print idx
    name = item["name"]
    chk = False
    tmpName = ""
    dict = {}
    for i in range(len(locationNames)-1,-1,-1):
        locationName = locationNames[i]
        words = locationName.split(";")[2].split(",")
        for word in words:
            word = word.strip().decode("utf-8")
            if word == u"":
                continue
            if name.__contains__(word):
                chk = True
                tmpName = locationName.split(";")[1]
                locationNames.__delitem__(i)
                break
        if chk:
            break

    if chk:
        collectSet.add(tmpName)
        num += 1

        dict["gid"] = num
        dict["name"] = tmpName
        dict["category_ming"] = ""
        dict["type"] = ""
        dict["picUrl"] = []
        dict["words"] = []

        try:
            dict["new_img"] = item["new_img"]
        except:
            dict["new_img"] = ""
        try:
            dict["about"] = item["about"]
        except:
            dict["about"] = ""
        try:
            dict["website"]  = item["website"]
        except:
            dict["website"] = ""
        try:
            dict["category_fb"] = item["category"]
        except:
            dict["category_fb"] = ""
        try:
            dict["phone"] = item["phone"]
        except:
            dict["phone"] = ""
        try:
            dict["rating"] = item["overall_star_rating"]
        except:
            dict["rating"] = ""
        try :
            dict["address"] = item["address"]
        except:
            dict["address"] = ""
        try:
            dict["area"] = item["area"]
        except:
            dict["area"] = ""
        try:
            dict["onTime"] = item["ontime"]
        except:
            dict["onTime"] = ""
        try:
            dict["longt"] = item["longt"]
            dict["lat"] = item["lat"]
        except:
            dict["longt"] = ""
            dict["lat"] = ""
        locationList.append(dict)

for locationName in locationNames:
    name = locationName.split(";")[1]
    num += 1
    dict= {}
    dict["about"] = ""
    dict["gid"] = num
    dict["new_img"] = ""
    dict["website"] = ""
    dict["name"] = name
    dict["category_ming"] = ""
    dict["type"] = ""
    dict["picUrl"] = []
    dict["words"] = []
    dict["category_fb"] = ""
    dict["phone"] = ""
    dict["rating"] = 0
    dict["address"] = ""
    dict["area"] = ""
    dict["onTime"] = ""
    dict["longt"] = ""
    dict["lat"] = ""
    locationList.append(dict)

print len(locationList)

with open("E:/project/ArrangeData/class_doc.txt") as f:
    for line in f.readlines():
        name = line.split("\t")[0]
        cate = line.split("\t")[1]
        pics = line.split("\t")[3].strip().split(",")
        for idx, item in enumerate(locationList):
            name1 = item["name"]
            if name == name1:
                item["category_ming"] = cate
                item["picUrl"] = pics
                locationList.__setitem__(idx,item)
    f.close()

with open("E:/project/ArrangeData/Location_outinside.txt", "r") as f:
    for line in f.readlines():
        name = line.split("\t")[1]
        t = line.split("\t")[2]
        for idx, item in enumerate(locationList):
            name1 = item["name"]
            if name == name1:
                item["type"] = t
                locationList.__setitem__(idx, item)
    f.close()

import os
import unicodedata
files = [unicodedata.normalize('NFC', f) for f in os.listdir(u"E:/project/wordcount5/")]
for file in files:
    file1 = file.encode("utf-8").split("_")[1].split(".")[0]
    sList = []
    with open(u"E:/project/wordcount5/"+file,"r") as f:
        for line in f.readlines():
            sList.append(line.split(" ")[0].strip())
        f.close()

    for idx, item in enumerate(locationList):
        name1 = item["name"]
        if file1 == name1:
            item["words"] = sList
            locationList.__setitem__(idx, item)

for item in locationList:
    collection1.insert_one(item)

print "Finish !!!"



