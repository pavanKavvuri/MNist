import numpy as np
import datetime as dt
from dateutil.parser import parse

x_in =  [1,2,3,4,5,1]
x_out = [2,3,7,5,6,3]

p_in = [9,10,5,6,3,4]
p_out = [19,16,9,8,4,7]

q = 0
hrs = []
for i in range(0, 24):
    q = 0
    for j in range(0, 6):
        if (i >= p_in[j]) & (i < p_out[j]):
            q += 1
            #print (i, j, q)

    if q > 0:

        hrs.append(q)

    else:
        hrs.append(0)

a = dt.datetime(1995,01,21,00,01,00)
b = dt.datetime(2017,03,26,00,01,00)
string = "12/08/2016 01:01:00"


(b-a).total_seconds()
print (b-a)
l = string.split()
print (l)

print l[0].replace("/", ",")
s = l[1].replace(":", ",")

dt1 = dt.datetime.strptime(l[0].replace("/", ","), '%m,%d,%Y')
n = (('{0},{1},{2:}'.format(dt1.year, dt1.month, dt1.day % 100)))









