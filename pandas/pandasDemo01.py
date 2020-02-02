#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:52:33 2020

@author: vv
"""

import numpy as np
import pandas as pd

print(pd.Series)
d = pd.Series(np.arange(10))
print(d.cumsum())

d = pd.Series([0,7,5,4],index=['a','b','c','d'])
print(d)
d = pd.Series({'a':9,'b':7,'c':'c','d':3})
print(d)
print("========")
d = pd.Series({'a':9,'b':7,'c':6,'d':3},index=['c','a','b','d','e'])
print(d)
m = pd.Series(np.arange(4),index=np.arange(9,5,-1))
print("========")
print(m.index,m.values)

print(d[[0,1,2]])
print(d[['c','a','b']])
print("========")
print(d[2])
print(d[:3])
print("========")
print(d[d>d.median()])  # vaules > vaules' median
print(np.exp2(d))

b = pd.Series([9,8,7,6],['a','b','c','d'])
print(b.get('e',10))

print('DataFrame')

df = pd.DataFrame(np.arange(10).reshape(2,5))
print(df)


dl = {'c':['Beijing','shanghai','guangzhou','shenzhen','shengyang'],
      'h':[101.5,101.2,101.3,102.0,100.1],
      't':[120.7,127.3,119.4,140.9,101.4],
      'd':[121.4,127.8,120.0,145.5,101.6]      
      }

c = pd.DataFrame(dl,index=['c1','c2','c3','c4','c5'])
print(c)
'''
            c      h      t      d
c1    Beijing  101.5  120.7  121.4
c2   shanghai  101.2  127.3  127.8
c3  guangzhou  101.3  119.4  120.0
c4   shenzhen  102.0  140.9  145.5
c5  shengyang  100.1  101.4  101.6
'''
c = c.reindex(index=['c5','c3','c1','c2','c4'],columns=['c','d','t','h'])
print(c)
new_c = c.columns.insert(4,'n')
newd = c.reindex(columns=new_c,fill_value=200)
print(newd)

nc = c.columns.delete(2)
print(nc)
'''
            c      d      t      h    n
c5  shengyang  101.6  101.4  100.1  200
c3  guangzhou  120.0  119.4  101.3  200
c1    Beijing  121.4  120.7  101.5  200
c2   shanghai  127.8  127.3  101.2  200
c4   shenzhen  145.5  140.9  102.0  200
'''
ni = c.index.insert(5,'c0')
print('.ffill()')
nd = c.reindex(index=ni,columns=nc).ffill()     # .ffill()
print(nd)
'''
            c      d      h
c5  shengyang  101.6  100.1
c3  guangzhou  120.0  101.3
c1    Beijing  121.4  101.5
c2   shanghai  127.8  101.2
c4   shenzhen  145.5  102.0
c0   shenzhen  145.5  102.0
'''

b = pd.DataFrame(np.arange(20).reshape(4,5))
d = pd.Series(np.arange(4))
print(d-10)
print(b-d)
'''
      0     1     2     3   4
0   0.0   0.0   0.0   0.0 NaN
1   5.0   5.0   5.0   5.0 NaN
2  10.0  10.0  10.0  10.0 NaN
3  15.0  15.0  15.0  15.0 NaN
不同维度间为广播运算，一维Series默认在轴1参与运算（b的每一行减去d的元素）
若要使轴0参与运算，需要指定axis
'''
print(b.sub(d,axis=0))
'''
    0   1   2   3   4
0   0   1   2   3   4
1   4   5   6   7   8
2   8   9  10  11  12
3  12  13  14  15  16
'''