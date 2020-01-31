#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:01:36 2020

@author: vv
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib
a = np.arange(1,9)
b = np.random.randint(10,20,a.shape)
plt.plot(a,b)
plt.ylabel("Grade")
#plt.savefig('test',dpi=300)
plt.axis([0,9,9,21])    #[xmin,xmax,ymin,ymax]
plt.show()

plt.plot(a,a*1.5,a,a*2.5,a,a*3.5,a,a*4.5)
plt.show()

plt.plot(a,a*1.5,'go-',a,a*2.5,'rx-.',a,a*3.5,'*',a,a*4.5)
plt.show()

a = np.arange(0,5,0.02,dtype=np.float)
zhfont = matplotlib.font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-DemiLight.ttc") 
plt.plot(a,np.cos(2*np.pi*a),'r-.')
plt.xlabel('时间',fontproperties=zhfont,fontsize=20)
plt.ylabel('振幅',fontproperties=zhfont,fontsize=20)
plt.title('余弦波 $y=cos(2\pi x)$',fontproperties=zhfont,fontsize=25)
plt.text(2,1,r'$\mu=100$',fontsize=15)
plt.annotate(r'$\mu=100$',xy=(2.5,-1),xytext=(4,-1.4),arrowprops=dict(facecolor='black',shrink=0.05,width=1))
plt.axis([-0.5,5.5,-1.5,1.5])
plt.grid(True)      
plt.show()


plt.subplot2grid((3,3),(0,0),colspan=3)
plt.plot(a,np.cos(2*np.pi*a),'r-.')
plt.subplot2grid((3,3),(1,0),colspan=2)
plt.plot(a,np.sin(2*np.pi*a),'r-.')
plt.subplot2grid((3,3),(2,0),colspan=2)
plt.plot(a,np.tan(2*np.pi*a),'r-.')
plt.subplot2grid((3,3),(1,2),rowspan=2)
plt.plot(a,a**2-a-4,'r-.')
plt.show()

gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,:-1])
ax3 = plt.subplot(gs[1:,-1])
ax4 = plt.subplot(gs[2,0])
ax5 = plt.subplot(gs[2,1])
ax1.plot(a,np.cos(2*np.pi*a),'r-.')

plt.show()
