import unicodedata
import os
path = u"E:/project/alsRawData/"
locationSet = set()
files = [unicodedata.normalize('NFC', f) for f in os.listdir(path)]
for file in files:
    with open(path+file, "r") as f:
        for line in f.readlines():
            no = line.split(",")[0].split("(")[1]
            name = line.split(",")[1]
            s = no+","+name
            locationSet.add(s)
        f.close()

# from pymongo import MongoClient
# uri = "mongodb://13.113.88.246:27017"
# client = MongoClient(uri)
# db = client.__getitem__("g3site")
# collection = db.__getitem__("g3site_travel")

f1 = open("E:/project/namegid.txt", "r")
sList = f1.readlines()
f1.close()

dict = {}
for line in locationSet:
    no = line.split(",")[0].strip()
    name = line.split(",")[1].strip()
    dict[no] = name

n = 0
aList = []
for idx, item in enumerate(dict.items()):
    print idx
    no = item[0]
    name = item[1]
    s = ""
    for line in sList:
        name1 = line.split(" &")[0].split(":")[1]
        gid = int(line.split(" &gid:")[1].strip())
        if name == name1:
            s = str(no)+","+name+","+str(gid)
            n += 1
            aList.append(s)

print n
with open("E:/reviseData.txt", "w") as f:
    for line in aList:
        f.writelines(line+"\n")
    f.close()

