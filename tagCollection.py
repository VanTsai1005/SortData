from pymongo import MongoClient

uri = "mongodb://10.120.37.128:27017"
client = MongoClient(uri)
db = client.__getitem__("family")
collection = db.__getitem__("travel4")

tagSet = set()
for item in collection.find():
    try:
        line = item["tags"]
        tags = line.split(",")
        for tag in tags:
            tagSet.add(tag.strip())
    except:
        pass

aList = []
for tag in tagSet:
    aList.append(tag)
aList.sort()

with open("E:/tags.txt","w") as f:
    for item in aList:
        f.write(item.encode("utf-8")+"\n")
    f.close()
