import pandas as pd 
import numpy as np 
import time as t

z= np.zeros(48)	
sumArray = np.zeros([48, ])
#print z

#df_new = pd.read_excel("/home/tcs/Desktop/pavan_guest/MakeNew/NewOne_2.xlsx", sheetname=0)
df_new = pd.read_excel("/home/tcs/Desktop/pavan_guest/MakeNew/NewOne.xlsx", sheetname=0)

#print df_new.Duration
Q= []
new_d = df_new['Date'].unique()
#print  df_new[df_new.Duration>=48]
#print new_d

#df = df_new.groupby(["Date"], as_index=False).count()

#print map(lambda x: df_new[df_new.Date == new_d[x]], range(0, len(new_d)-1))



#r = map(lambda q : map(lambda e : map(lambda u : df[df_new == q] ), range(len(df_4)) ), new_d)


#list(map(lambda x:n.extend(map(x,[100,200,300])),map(lambda x:lambda y:x+y,[0,1,2])))

#[100,200,300,101,201,301,102,202,302]

'''
x_, y_ = df_new.CheckinTime[0], df_new.Duration[0]

#print x_, y_


z[x_:y_] = map(lambda x: z[x]+1, range(x_, y_))

z[x_:y_] = map(lambda x: z[x]+1, range(x_, y_))


z[x_:y_] = map(lambda x: z[x]+1, range(x_, y_))	
#print z

'''

def wrr(j):
    print j
    #sumArray = np.zeros([48, ])
    #z = np.zeros(48)
    x_, y_ = df_new.CheckinTime[j], df_new.Duration[j]
    #print (x_, y_)
    z[x_:x_ + y_] = map(lambda x: z[x] + 1, range(x_, x_ + y_))
    #print 'hello'
    return z
    #t.sleep(5)
    #sumArray = np.add(sumArray, z)
    #print sumArray
    #Q.append(z)
    


def frr(i):
    #print i
    z = np.zeros(48)
    q = df_new[df_new.Date == new_d[i]] 
    #print new_d[i]
    #print q.Index
    print len(q)
    #print q[0]
    s = map(wrr, q.Index)
    print 'pavan'
    print s
    Q.append(s[1])
    

    
    #print s[0]
    

    #print type(s[0])
    
    #return q



'''


for i in range(len(new_d)):
    z = np.zeros(48)
    q = df_new[df_new.Date == new_d[i]]
    for j in range(len(q)):
        x_, y_ = df_new.CheckinTime[j], df_new.Duration[j]
        z[x_:x_+y_] = map(lambda x: z[x] + 1, range(x_, x_+y_))
    print z
'''

#r = map(lambda q : map(lambda e : map(lambda u : df[df_new == q] ), range(len(df_4)) ), new_d)

r = map(frr, range(1,2))
print 'kumar'
print Q
#jj = map(wrr, range(0, map()))









