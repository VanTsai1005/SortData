# !coding:utf-8
from pymongo import MongoClient
import json

wordLimit = 50
article2File = 2000
web = "xuite"
linkUrl = "E:/"+web+"_{}.json"
uri = "mongodb://10.120.37.128:27017"
client = MongoClient(uri)
db = client.__getitem__("test")
collection = db.__getitem__("testXuite")
print collection.count()

filterTexts = []
filterTexts = [u"請推薦",u"嗎",u"呢",u"？",u"幫",u"幫忙",u"排行程",u"排一下",u"去哪",u"求助",u"?",u"建議",u"可以推薦",\
              u"請問",u"求救",u"在哪",u"誰知道",u"有那裡",u"介紹",u"幾人房",u"麻煩",u"有去過",u"請進",u"有沒有",u"問題",\
              u"有去",u"好不好",u"關於",u"分享經驗",u"請水水推薦",u"請大家推薦",u"何處去",u"請教",u"尋找",u"在那",u"怎麼玩",\
              u"如何",u"分享一下",u"想去",u"那間",u"可否",u"是否",u"能否",u"關於",u"問",u"傷腦筋",u"請媽咪推薦",u"請推見",\
              u"提議",u"哪",u"規劃",u"有誰",u"去過",u"北海道",u"大陸",u"東京",u"適合去",u"協助",u"說說看",u"日本",u"韓國"]

compareTexts = []
compareTexts = [u"相關文章",u"延伸閱讀",u"更多分享",u"下一篇",u"繼續閱讀",u"好吃分享",u"好玩分享",u"文章出處",u"臉書粉絲",\
                u"延伸文章",u"相關閱讀",u"相關資訊",u"下篇分享",u"延伸資訊",u"好物推薦",u"吃喝玩樂記錄",u"以下文章"\
                u"廣告連結"]
# u"粉絲專頁",u"粉絲團",u"粉絲頁"
areaList = [u"基隆",u"新北",u"臺北",u"台北",u"桃園",u"新竹",u"苗栗",u"台中",u"彰化",u"南投",u"嘉義",u"台南",u"雲林",u"高雄",u"屏東",u"台東",u"花蓮",u"宜蘭",u"澎湖"]
num = 0
n = 0
totalnum = 0

aList = []
for idx, item in enumerate(collection.find()):
    dict = {
        "title":"",
        "content":"",
        "area":"",
        "auth":"",
        "resp":"",
        "date":"",
        "tags":""
    }
    # content = item["content"].replace('$("#ifAd").attr("src", "https://mamibuy.com.tw/ad/content.aspx?app=" + util.queryString("app"));', "")
    try:
        content = item["content"]
    except:
        content = ""
    for contentText in compareTexts:
        if content.__contains__(contentText):
            pos = content.index(contentText)
            content = content[0:pos]

    if len(content) < wordLimit:
        continue

    chk = False
    try:
        title = item["name"]
    except:
        title = item["title"]

    for aText in filterTexts:
        if title.__contains__(aText):
            chk = True
            break;
    if chk:
        continue

    chk = False
    for i in range(0, len(areaList)):
        area = areaList[i]
        if title.__contains__(area):
            dict["area"] = area
            chk = True

    if chk==False:
        for i in range(0, len(areaList)):
            area = areaList[i]
            if content.__contains__(area):
                dict["area"] = area
                chk = True

    if chk==False:
        dict["area"] = u"未知"

    dict["title"] = title
    dict["content"] = content
    try:
        dict["auth"] = item["auth"]
    except:
        dict["auth"] = ""
    try:
        dict["resp"] = item["resp"]
    except:
        dict["resp"] = ""
    try:
        dict["date"] = item["date"]
    except:
        dict["date"] = ""
    dict["web"] = web
    try:
        dict["tags"] = item["tags"]
    except:
        dict["tags"] = ""

    aList.append(dict)
    totalnum += 1
    n += 1
    if n == article2File:
        n = 0
        num += 1
        encodedjson = json.dumps(aList, ensure_ascii=False)
        with open(linkUrl.format(num*article2File), "w") as f:
            f.write(encodedjson.encode("utf-8"))
            f.close()

        aList = []
        print "Finish !!"

num += 1
encodedjson = json.dumps(aList, ensure_ascii=False)
with open(linkUrl.format((num-1)*article2File+n), "w") as f:
    f.write(encodedjson.encode("utf-8"))
    f.close()
print "Finish !! total = "+ str(totalnum)




