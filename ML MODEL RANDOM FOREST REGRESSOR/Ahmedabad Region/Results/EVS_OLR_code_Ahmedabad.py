import pandas as pd
from matplotlib import pyplot as plt

d1 = pd.read_csv('FINAL.csv')
d2 = d1[(d1['lat']==20) & (d1['lon']==70)]
d3 = d1[(d1['lat']==20) & (d1['lon']==72.5)]
d4 = d1[(d1['lat']==20) & (d1['lon']==75)]
d5 = d1[(d1['lat']==22) & (d1['lon']==70)]
d6 = d1[(d1['lat']==22) & (d1['lon']==72.5)]
d7 = d1[(d1['lat']==22) & (d1['lon']==75)]
d8 = d1[(d1['lat']==24) & (d1['lon']==70)]
d9 = d1[(d1['lat']==24) & (d1['lon']==72.5)]
d10 = d1[(d1['lat']==24) & (d1['lon']==75)]
#print(d2)
x = range(77)
y1 = d2['OLR_w/m2']
y2 = d3['OLR_w/m2']
y3 = d4['OLR_w/m2']
y4 = d5['OLR_w/m2']
y5 =  d6['OLR_w/m2']
y6 =  d7 ['OLR_w/m2']
y7 =  d8['OLR_w/m2']
y8 = d9['OLR_w/m2']
y9 = d10['OLR_w/m2']
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.plot(x,y5)
plt.plot(x,y6)
plt.plot(x,y7)
plt.plot(x,y8)
plt.plot(x,y9)
plt.xlabel('2010 January to 2016 May in Monthwise')
plt.ylabel('OLR(W/m^2)')
plt.legend(['(20,70)','(20,72.5)','(20,75)','(22,70)','(22,72.5)','(22,75)','(24,70)','(24,72.5)','(24,75)'])
plt.title('Data analysis for OLR in 9 regions with poisitions')
plt.show()


