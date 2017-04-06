import pandas as pd
import numpy as np
import datetime as dt
from operator import add
import matplotlib.pyplot as plt
start = dt.datetime.now()
z = np.zeros(48)
sumArray = np.zeros([48, ])
# print z

# df_new = pd.read_excel("/home/tcs/Desktop/pavan_guest/MakeNew/NewOne_2.xlsx", sheetname=0)
df_new = pd.read_excel("/home/pavan/PAVANKUMAR/MachineLearning/CaseStudy/ML_DATA/v4/k4/NewOne_2.xlsx", sheetname=0)


dayList = []
one_day_b4_List = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
two_day_b4_List = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


# print df_new.Duration
Q = []

L =[]
new_d = df_new['Date'].unique()
print  len(new_d)

'''
def wrr(j):
    print j
    # sumArray = np.zeros([48, ])
    # z = np.zeros(48)
    x_, y_ = df_new.CheckinTime[j], df_new.Duration[j]
    # print (x_, y_)
    z[x_:x_ + y_] = map(lambda x: z[x] + 1, range(x_, x_ + y_))
    # print 'hello'
    return z
    # t.sleep(5)
    # sumArray = np.add(sumArray, z)
    # print sumArray
    # Q.append(z)


def frr(i):
    # print i
    z = np.zeros(48)
    q = df_new[df_new.Date == new_d[i]]
    # print new_d[i]
    # print q.Index
    print len(q)
    # print q[0]
    s = map(wrr, q.Index)
    print 'pavan'
    print s
    Q.append(s[1])



    # print s[0]


    # print type(s[0])

    # return q



r = map(frr, range(1, 2))
print 'kumar'
print Q
# jj = map(wrr, range(0, map()))


'''

q = df_new[df_new.Date == new_d[1]].index.tolist()
#print q


for i in range(0,28):
    z = np.zeros(100)
    q = df_new[df_new.Date == new_d[i]].index.tolist()

    for j in range(q[0], q[-1]+1):
        x_, y_ = df_new.CheckinTime[j], df_new.Duration[j]
        z[x_:x_+y_] = map(lambda x: z[x] + 1, range(x_, x_+y_))
    L.append(z)


    dayList.append(map(add, map(add, L[i][0:24], one_day_b4_List), two_day_b4_List))
    one_day_b4_List = L[i][24:48]
    two_day_b4_List = L[i][48:72]
    #print (dayList)
    #print (one_day_b4_List)
    #print (two_day_b4_List)
    #break



dayList = reduce(add, dayList)

print len(L)
print len(new_d)

print dt.datetime.now() - start

plt.plot(dayList)
plt.show()

# r = map(lambda q : map(lambda e : map(lambda u : df[df_new == q] ), range(len(df_4)) ), new_d)









