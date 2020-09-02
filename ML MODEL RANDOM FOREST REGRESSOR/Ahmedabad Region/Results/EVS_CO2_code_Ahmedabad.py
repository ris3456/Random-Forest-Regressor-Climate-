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
y1 = d2['co2_conc']
y2 = d3['co2_conc']
y3 = d4['co2_conc']
y4 = d5['co2_conc']
y5 =  d6['co2_conc']
y6 =  d7 ['co2_conc']
y7 =  d8['co2_conc']
y8 = d9['co2_conc']
y9 = d10['co2_conc']
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
plt.ylabel('CO2(ppm)')
plt.legend(['(20,70)','(20,72.5)','(20,75)','(22,70)','(22,72.5)','(22,75)','(24,70)','(24,72.5)','(24,75)'])
plt.title('Data of CO2 in ppm for analysis of OLR in 9 regions with poisitions')
plt.show()


