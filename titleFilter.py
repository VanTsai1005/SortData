#coding:utf-8

from threading import Thread
from Queue import Queue
from pymongo import MongoClient

# uri = "mongodb://10.120.37.128:27017"
# client = MongoClient(uri)
# db = client.__getitem__("family")
# collection = db.__getitem__("travel3")
# aList = []
# for item in collection.find():
#     if item["finded"] == 0:
#         aList.append(item)
#
# with open("E:/location.txt","w") as f:
#     for item in aList:
#         f.write(item["title"].encode("utf-8")+"\n")
#     f.close()

wordList = []
hadlist = []
nolist = []
with open("E:/AttractionsName.txt","r") as f:
    for item in f.readlines():
        wordList.append(item)

uri = "mongodb://10.120.37.128:27017"
client = MongoClient(uri)
db = client.__getitem__("family")
collection = db.__getitem__("travel2")
collection1 = db.__getitem__("travel4")

for item in collection.find():
    content = item["content2"]
    sList = []
    chk = False
    sName = ""
    for word in wordList:
        sList = word.strip().split(",")
        for ss in sList:
            if ss == "":
                continue
            s = ss.decode("utf-8").strip()
            if content.__contains__(s):
                chk=True
                sName = sList[0]
                break
        if chk:
            break

    item["location"] = sName
    if chk:
        item["finded"] = 1
    else:
        item["finded"] = 0
    collection1.insert_one(item)
    print collection1.count()

print "All  Finish !!"

