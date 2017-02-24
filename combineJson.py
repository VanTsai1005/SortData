from pymongo import MongoClient
import json

uri = "mongodb://10.120.37.128:27017"
client = MongoClient(uri)
db = client.__getitem__("family")
collection = db.__getitem__("travel")
print collection.count()

aList = []
for idx, item in enumerate(collection.find()):
    dict={}
    try:
        dict["title"] = item["title"]
    except:
        dict["title"] = ""
    dict["content"] = item["content"]
    try:
        dict["auth"] = item["auth"]
    except:
        dict["auth"] = ""
    dict["area"] = item["area"]
    dict["resp"] = item["resp"]
    dict["date"] = item["date"]
    try:
        dict["tags"] = item["tags"]
    except:
        dict["tags"] = ""

    aList.append(dict)

encodedjson = json.dumps(aList, ensure_ascii=False)
with open("E:/testArticles.json", "w") as f:
    f.write(encodedjson.encode("utf-8"))
    f.close()
print "FInish !!"