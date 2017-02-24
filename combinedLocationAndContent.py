#!coding:utf-8
import os
from pymongo import MongoClient

namelist = []
uri = "mongodb://10.120.37.128:27017"
client = MongoClient(uri)
db = client.__getitem__("family")
collection = db.__getitem__("travel4")

for item in collection.find():
    namelist.append(item["location"].encode("utf-8"))

path = "E:/project/documents/"
files = os.listdir(path)
dict_total = {}
n = 0
for file in files:
    dict = {}
    with open(path+file,"r") as f:
        content = f.read()
        f.close()

    dict[file.split(".")[0]] = content
    n = int(file.split(".")[0])
    name = namelist.__getitem__(n).decode("utf-8")
    if name=="":
        continue

    if not dict_total.has_key(name):
        dict_total[name] = 1
    else:
        dict_total[name] += 1

    num = str(dict_total[name])
    fileName= unicode(name+"_"+num)
    with open("E:/project/documents1/"+fileName+".txt","w") as f:
        f.write(content)
        f.close()
    n += 1
    print n

print "Finish !!"
