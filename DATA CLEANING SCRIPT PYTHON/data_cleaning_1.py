# -*- coding: utf-8 -*-
"""DATA_CLEANING_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1elbknIY0dnmX5P7nRRzGMqVhnpQq1lzF
"""

import pandas as pd
import numpy as np
dat=pd.read_csv("/content/CO2_DATASET_NEW - rlutcs_all_2010_2017_rcp8570.0_74.0_20.0_24.0.csv")
df=pd.DataFrame(dat)
df

dfs=[]
a=0
b=3
for ix in df['lat']:
  if ix==20:
    dfm=df[['lat','lon',
              '2010/01/16','2010/02/15','2010/03/16','2010/04/16','2010/05/16','2010/06/16','2010/07/16','2010/08/16','2010/09/16','2010/10/16','2010/11/16','2010/12/16',
              '2011/01/16','2011/02/15','2011/03/16','2011/04/16','2011/05/16','2011/06/16','2011/07/16','2011/08/16','2011/09/16','2011/10/16','2011/11/16','2011/12/16',
              '2012/01/16','2012/02/15','2012/03/16','2012/04/16','2012/05/16','2012/06/16','2012/07/16','2012/08/16','2012/09/16','2012/10/16','2012/11/16','2012/12/16',
              '2013/01/16','2013/02/15','2013/03/16','2013/04/16','2013/05/16','2013/06/16','2013/07/16','2013/08/16','2013/09/16','2013/10/16','2013/11/16','2013/12/16',
              '2014/01/16','2014/02/15','2014/03/16','2014/04/16','2014/05/16','2014/06/16','2014/07/16','2014/08/16','2014/09/16','2014/10/16','2014/11/16','2014/12/16',
              '2015/01/16','2015/02/15','2015/03/16','2015/04/16','2015/05/16','2015/06/16','2015/07/16','2015/08/16','2015/09/16','2015/10/16','2015/11/16','2015/12/16',
              '2016/01/16','2016/02/15','2016/03/16','2016/04/16','2016/05/16'
              ]].iloc[[a,b]].mean(axis=0)
    dfs.append(dfm)
    a=a+1
    b=b+1
mean_matrix=pd.concat(dfs,axis=1)
ler=pd.DataFrame(mean_matrix.transpose())
ler
c=['lat','lon',
              '2010/01/16','2010/02/15','2010/03/16','2010/04/16','2010/05/16','2010/06/16','2010/07/16','2010/08/16','2010/09/16','2010/10/16','2010/11/16','2010/12/16',
              '2011/01/16','2011/02/15','2011/03/16','2011/04/16','2011/05/16','2011/06/16','2011/07/16','2011/08/16','2011/09/16','2011/10/16','2011/11/16','2011/12/16',
              '2012/01/16','2012/02/15','2012/03/16','2012/04/16','2012/05/16','2012/06/16','2012/07/16','2012/08/16','2012/09/16','2012/10/16','2012/11/16','2012/12/16',
              '2013/01/16','2013/02/15','2013/03/16','2013/04/16','2013/05/16','2013/06/16','2013/07/16','2013/08/16','2013/09/16','2013/10/16','2013/11/16','2013/12/16',
              '2014/01/16','2014/02/15','2014/03/16','2014/04/16','2014/05/16','2014/06/16','2014/07/16','2014/08/16','2014/09/16','2014/10/16','2014/11/16','2014/12/16',
              '2015/01/16','2015/02/15','2015/03/16','2015/04/16','2015/05/16','2015/06/16','2015/07/16','2015/08/16','2015/09/16','2015/10/16','2015/11/16','2015/12/16',
              '2016/01/16','2016/02/15','2016/03/16','2016/04/16','2016/05/16']
ler.to_excel("co2_A.xls", header=c,index=False)

dfs=[]
a=3
b=6
for ix in df['lat']:
  if ix==22:
    dfm=df[['lat','lon',
              '2010/01/16','2010/02/15','2010/03/16','2010/04/16','2010/05/16','2010/06/16','2010/07/16','2010/08/16','2010/09/16','2010/10/16','2010/11/16','2010/12/16',
              '2011/01/16','2011/02/15','2011/03/16','2011/04/16','2011/05/16','2011/06/16','2011/07/16','2011/08/16','2011/09/16','2011/10/16','2011/11/16','2011/12/16',
              '2012/01/16','2012/02/15','2012/03/16','2012/04/16','2012/05/16','2012/06/16','2012/07/16','2012/08/16','2012/09/16','2012/10/16','2012/11/16','2012/12/16',
              '2013/01/16','2013/02/15','2013/03/16','2013/04/16','2013/05/16','2013/06/16','2013/07/16','2013/08/16','2013/09/16','2013/10/16','2013/11/16','2013/12/16',
              '2014/01/16','2014/02/15','2014/03/16','2014/04/16','2014/05/16','2014/06/16','2014/07/16','2014/08/16','2014/09/16','2014/10/16','2014/11/16','2014/12/16',
              '2015/01/16','2015/02/15','2015/03/16','2015/04/16','2015/05/16','2015/06/16','2015/07/16','2015/08/16','2015/09/16','2015/10/16','2015/11/16','2015/12/16',
              '2016/01/16','2016/02/15','2016/03/16','2016/04/16','2016/05/16'
              ]].iloc[[a,b]].mean(axis=0)
    dfs.append(dfm)
    a=a+1
    b=b+1
mean_matrix=pd.concat(dfs,axis=1)
ler=pd.DataFrame(mean_matrix.transpose())
ler
c=['lat','lon',
              '2010/01/16','2010/02/15','2010/03/16','2010/04/16','2010/05/16','2010/06/16','2010/07/16','2010/08/16','2010/09/16','2010/10/16','2010/11/16','2010/12/16',
              '2011/01/16','2011/02/15','2011/03/16','2011/04/16','2011/05/16','2011/06/16','2011/07/16','2011/08/16','2011/09/16','2011/10/16','2011/11/16','2011/12/16',
              '2012/01/16','2012/02/15','2012/03/16','2012/04/16','2012/05/16','2012/06/16','2012/07/16','2012/08/16','2012/09/16','2012/10/16','2012/11/16','2012/12/16',
              '2013/01/16','2013/02/15','2013/03/16','2013/04/16','2013/05/16','2013/06/16','2013/07/16','2013/08/16','2013/09/16','2013/10/16','2013/11/16','2013/12/16',
              '2014/01/16','2014/02/15','2014/03/16','2014/04/16','2014/05/16','2014/06/16','2014/07/16','2014/08/16','2014/09/16','2014/10/16','2014/11/16','2014/12/16',
              '2015/01/16','2015/02/15','2015/03/16','2015/04/16','2015/05/16','2015/06/16','2015/07/16','2015/08/16','2015/09/16','2015/10/16','2015/11/16','2015/12/16',
              '2016/01/16','2016/02/15','2016/03/16','2016/04/16','2016/05/16']
ler.to_excel("co2_B.xls", header=c,index=False)

dfs=[]
a=0
b=3
for ix in df['lon']:
  if ix==20:
    dfm=df[['lat','lon',
              '2010/01/16','2010/02/15','2010/03/16','2010/04/16','2010/05/16','2010/06/16','2010/07/16','2010/08/16','2010/09/16','2010/10/16','2010/11/16','2010/12/16',
              '2011/01/16','2011/02/15','2011/03/16','2011/04/16','2011/05/16','2011/06/16','2011/07/16','2011/08/16','2011/09/16','2011/10/16','2011/11/16','2011/12/16',
              '2012/01/16','2012/02/15','2012/03/16','2012/04/16','2012/05/16','2012/06/16','2012/07/16','2012/08/16','2012/09/16','2012/10/16','2012/11/16','2012/12/16',
              '2013/01/16','2013/02/15','2013/03/16','2013/04/16','2013/05/16','2013/06/16','2013/07/16','2013/08/16','2013/09/16','2013/10/16','2013/11/16','2013/12/16',
              '2014/01/16','2014/02/15','2014/03/16','2014/04/16','2014/05/16','2014/06/16','2014/07/16','2014/08/16','2014/09/16','2014/10/16','2014/11/16','2014/12/16',
              '2015/01/16','2015/02/15','2015/03/16','2015/04/16','2015/05/16','2015/06/16','2015/07/16','2015/08/16','2015/09/16','2015/10/16','2015/11/16','2015/12/16',
              '2016/01/16','2016/02/15','2016/03/16','2016/04/16','2016/05/16'
              ]].iloc[[a,b]].mean(axis=0)
    dfs.append(dfm)
    a=a+1
    b=b+1
mean_matrix=pd.concat(dfs,axis=1)
ler=pd.DataFrame(mean_matrix.transpose())
ler
c=['lat','lon',
              '2010/01/16','2010/02/15','2010/03/16','2010/04/16','2010/05/16','2010/06/16','2010/07/16','2010/08/16','2010/09/16','2010/10/16','2010/11/16','2010/12/16',
              '2011/01/16','2011/02/15','2011/03/16','2011/04/16','2011/05/16','2011/06/16','2011/07/16','2011/08/16','2011/09/16','2011/10/16','2011/11/16','2011/12/16',
              '2012/01/16','2012/02/15','2012/03/16','2012/04/16','2012/05/16','2012/06/16','2012/07/16','2012/08/16','2012/09/16','2012/10/16','2012/11/16','2012/12/16',
              '2013/01/16','2013/02/15','2013/03/16','2013/04/16','2013/05/16','2013/06/16','2013/07/16','2013/08/16','2013/09/16','2013/10/16','2013/11/16','2013/12/16',
              '2014/01/16','2014/02/15','2014/03/16','2014/04/16','2014/05/16','2014/06/16','2014/07/16','2014/08/16','2014/09/16','2014/10/16','2014/11/16','2014/12/16',
              '2015/01/16','2015/02/15','2015/03/16','2015/04/16','2015/05/16','2015/06/16','2015/07/16','2015/08/16','2015/09/16','2015/10/16','2015/11/16','2015/12/16',
              '2016/01/16','2016/02/15','2016/03/16','2016/04/16','2016/05/16']
ler.to_excel("co2_A.xls", header=c,index=False)