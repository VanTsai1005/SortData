# !coding:utf-8
from pymongo import MongoClient
from threading import Thread
from Queue import Queue
import jieba
import re

NUM_THREADS = 8
jieba.load_userdict("E:/userWords.txt")
jieba.load_userdict("E:/ab104g3_userdict.txt")
stopWords = []
with open("E:/stopWords.txt","r") as f:
    for item in f.readlines():
        stopWords.append(item.decode("utf-8").strip())
    f.close()

uri = "mongodb://10.120.37.128:27017"
client = MongoClient(uri)
db = client.__getitem__("family")
collection = db.__getitem__("travel")
#collection1 = db.__getitem__("travel2")

article_list = []
sList = []
aList = []
# for item in collection.find():
#     title = item["title"]
#     if title.__contains__(u"大樹先生"):
#         sList.append(item["content"])
for item in collection.find():
    sList.append(item)

queue = Queue()
for i in range(0,collection.count()):
    if  i == 100:
        break
    queue.put(i)

def segmentation(item, idx):
    wordlist = []
    seglist=jieba.cut(item["title"], cut_all=False)
    for seg in seglist:
        m = re.search("\d*",seg)
        m1 = re.search("[a-zA-Z]*",seg)
        if (seg not in stopWords) and (m.group(0)=="") and (m1.group(0)==""):
            wordlist.append(seg)

    article = (" ".join((wordlist)))
   # item["title2"] = article
   # collection1.insert_one(item)
    aList.append(article)
    # with open("E:/project/segmentation1/article_"+str(idx+1)+".txt","w") as f:
    #     f.write(article.encode("utf-8"))
    #     f.close()
    print idx

def worker():
    while not queue.empty():
        idx=queue.get()
        segmentation(sList.__getitem__(idx), idx)


# 設定THREAD數量及執行的FUNCTION
threads = map(lambda i: Thread(target=worker), xrange(NUM_THREADS))
# 啟動THREAD
map(lambda th: th.start(), threads)
map(lambda th: th.join(), threads)

with open("E:/project/title.txt","w") as f:
    for item in aList:
        f.write(item.encode("utf-8")+"\n")
    f.close()
print "All Finish !!"


