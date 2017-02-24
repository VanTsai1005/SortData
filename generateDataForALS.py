
with open("E:/Data/result.txt","r") as f:
    totalSet = set()
    list1 = f.readlines()
    for item in list1:
        uid = item.split(",")[0]
        lid = item.split(",")[3]
        s = uid.strip() + " " + lid.strip()
        totalSet.add(s)

    totalList = []
    for item in totalSet:
        uid = item.split(" ")[0]
        lid = item.split(" ")[1]
        for item1 in list1:
            uid1 = item1.split(",")[0]
            lid1 = item1.split(",")[3]
            rank1 = item1.split(",")[4]
            date1 = item1.split(",")[2]
            if uid==uid1 and lid==lid1:
                s = uid1.strip() + " " + lid1.strip() + " " + rank1.strip() + " " + date1.strip()
                totalList.append(s)
                break
    totalList.sort()

    with open("E:/result1.txt", "w") as f:
        for item in totalList:
            f.write(item + "\n")
        f.close()
    #     print i
    #     uid1 = list1[i].split(",")[0]
    #     lid1 = list1[i].split(",")[3]
    #     rank1 = list1[i].split(",")[4]
    #     date1 = list1[i].split(",")[2]
    #     chk = False
    #     for j in range(i+1,len(list1)):
    #         uid2 = list1[j].split(",")[0]
    #         lid2 = list1[j].split(",")[3]
    #         rank2 = list1[j].split(",")[4]
    #         date2 = list1[j].split(",")[2]
    #         if uid1==uid2 and lid1==lid2:
    #             chk=True
    #             break
    #     if not chk:
    #         s = uid1+" "+lid1+" "+rank1+" "+date1
    #         totallist.append(s)
    f.close()



# from pymongo import MongoClient
#
# uri = "mongodb://10.120.37.128:27017"
# client = MongoClient(uri)
# db = client.__getitem__("test")
# collection = db.__getitem__("testXuite")
#
# authSet = set()
# contentList = []
# for item in collection.find():
#     authSet.add(item["auth"])
#     contentList.append(item["content"])
# print len(authSet)
# print "Finish !!"


