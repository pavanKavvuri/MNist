import pandas as pk 
import numpy as np	

df = pk.read_excel("/home/tcs/Desktop/pavan_guest/neway.xlsx", sheetname=0)

h = np.timedelta64(1, 'h')

#Diff = pk.Timedelta(df.CheckoutTime[x] - df.CheckinTime[x]).days * 24
#hourPair= lambda x: (df.CheckinTime[x].hour, df.CheckoutTime[x].hour)
#hourPair = lambda x: (df.CheckinTime[x].hour, round((np.datetime64(df.CheckoutTime[x]) - np.datetime64(df.CheckinTime[x]))/h))
Duration = lambda x: round((np.datetime64(df.CheckoutTime[x]) - np.datetime64(df.CheckinTime[x]))/h)
CheckIn = lambda x: df.CheckinTime[x].hour
Dates = lambda x: (df.CheckinTime[x].date())

#g= np.datetime64(df.CheckoutTime[0]) - np.datetime64(df.CheckinTime[0])
#print (g / np.timedelta64(1, 'h'))

#g = pk.Timedelta(df.CheckoutTime[0] - df.CheckinTime[0]).seconds
#print (df.CheckoutTime[0] , df.CheckinTime[0])
	
#print f(2)   pd.Timedelta(t2 - t1).seconds / 60.0
#seq = [1,2,3,4,35]

Du = map(Duration, range(0, len(df)))
Da = map(Dates, range(0,len(df)))
Cin = map(CheckIn, range(0,len(df)))

#print p

d = {'Duration' : pk.Series(Du), 'Date': pk.Series(Da), 'CheckinTime': pk.Series(Cin)}
   

df_new = pk.DataFrame(d)

#print df_new
'''
writer = pk.ExcelWriter('/home/tcs/Desktop/pavan_guest/MakeNew/NewOne.xlsx', engine='xlsxwriter' )
df_new.to_excel(writer, 'Sheet_1')
writer.save()
'''


#/home/tcs/Desktop/pavan_guest/MakeNew