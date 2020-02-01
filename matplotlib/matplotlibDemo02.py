#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:01:36 2020

@author: vv
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

labels = 'Frogs','Hogs','Dogs','Logs'
sizes = [150,300,405,100]
explode = [0,0.1,0,0]
plt.pie(sizes,explode=explode,labels=labels,autopct='%.1f%%',startangle=90,radius=1,shadow=True)
plt.title(".pie()")
plt.show()


np.random.seed(5)
mu,sigma = 100,10
a = np.random.normal(mu,sigma,size=100)
plt.hist(a,20,range=(80,120),histtype="bar",color='#FF00FF',alpha=1)
plt.title(".hist()")
plt.show()


N=10
theta=np.linspace(0.0,2*np.pi,N,endpoint=False)
r = np.arange(1,11)/10
#r = np.random.rand(N)
plt.plot(theta,r)
plt.show()
plt.polar(theta,r)
plt.title(".polar()")
plt.show()

#width = 2*np.pi*r/np.sum(r)
width = np.full_like(r,np.pi/5)     #same width
ax = plt.subplot(111,projection='polar')
bars = ax.bar(theta,r,width=width,bottom=0.0)
# set_facecolor()
for i in range(N):
    bars[i].set_facecolor(plt.cm.viridis(r[i]))
    bars[i].set_alpha(0.5)
plt.show()


fig,ax = plt.subplots()
ax.plot(10*np.random.randn(100),10*np.random.randn(100),'x')
ax.plot(np.random.normal(0,sigma,size=100),np.random.normal(0,sigma,size=100),'o')
ax.set_title("Simple Scatter")
plt.show()
plt.scatter(np.random.normal(0,sigma,size=100),np.random.normal(0,sigma,size=100))
plt.title(".scatter()")
plt.show()