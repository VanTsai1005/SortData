#!coding:utf-8
import os
import unicodedata

path = "E:/project/documents1/"
path1 = "E:/project/wordcount/"
path2 = "E:/tags.txt"

f2 = open(path2,"r")
aList = f2.readlines()
f2.close()

def chkWords(word):
    for item in aList:
        tag = item.decode("utf-8").strip()
        if word==tag or word.__contains__(tag) or tag.__contains__(word):
            chk=True
            break
        else:
            chk=False
    return chk

files = [unicodedata.normalize('NFC', f) for f in os.listdir(u"E:/project/documents1/")]
tmpName = ""
for i in range(0,len(files)):
    print i+1
    # if i<1216:
    #     continue

    totalList = []
    totalSet = set()

    f1 = files.__getitem__(i)
    fileName1 = f1.split("_")[0]
    if fileName1 == tmpName:
        continue

    file1 = open(path+f1,"r")
    for item1 in file1.readlines():
        totalList.append(item1.decode("utf-8").strip().split(" ")[0])
        totalSet.add(item1.decode("utf-8").strip().split(" ")[0])

    for j in range(i+1,len(files)):
        f2 = files.__getitem__(j)
        fileName2 = f2.split("_")[0]
        file2 = open(path + f2, "r")
        if fileName1 == fileName2:
            tmpName = fileName1
            for item2 in file2.readlines():
                totalList.append(item2.decode("utf-8").strip().split(" ")[0])
                totalSet.add(item2.decode("utf-8").strip().split(" ")[0])
        else:
            tmpName = fileName1
            break
        file2.close()
    dict = {}
    for item in totalSet:
        if chkWords(item):
            dict[item] = 0

    for item in totalList:
        if dict.has_key(item):
            dict[item] += 1

    if len(dict) < 10:
        for item in totalSet:
            dict[item] = 0
        for item in totalList:
            if dict.has_key(item):
                dict[item] += 1

    sortDict = sorted(dict.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
    file1.close()

    with open("E:/project/wordcount3/tfidf_"+fileName1+".txt", "w") as f:
        for item in sortDict:
            s = item[0].encode("utf-8") + " " + str(item[1])
            f.write(s+"\n")
        f.close()








