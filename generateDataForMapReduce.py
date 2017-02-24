import random
import datetime

num = 20000
addAry = [10,20,30]
aList = []
bList = []
for i in range(0,20000):
    n = random.randint(1,500)
    user = "A{}".format(n)
    hour = random.randint(0,23)
    min = random.randint(0,59)
    sec = random.randint(0,59)
    asc = random.randint(5,60)
    n = random.randint(1,3)

    t1 = datetime.timedelta(hours=hour,minutes=min,seconds=sec)
    t2 = t1 + datetime.timedelta(minutes=asc)
    s1 = user + "," + str(t1) + "," + "in"
    s2 = user + "," + str(t2) + "," + "out"
    aList.append(s1)
    aList.append(s2)
    t3 = t1
    for j in range(0,n):
        add = addAry[random.randint(0, 2)]
        t3 = t3 + datetime.timedelta(minutes=add)
        if t3 > t2:
            break
        else:
            money = random.randint(10, 1000)
            s3 = user + "," + str(t3) + "," + str(money)
            bList.append(s3)

with open("E:/A.txt","w") as fa:
    for item in aList:
        fa.write(item+"\n")
    fa.close()

with open("E:/B.txt","w") as fb:
    for item in bList:
        fb.write(item+"\n")
    fb.close()
print "Finish !!"