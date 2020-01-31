#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:47:54 2020

@author: vv
"""

import numpy as np
from PIL import Image

img = Image.open("/media/vv/_dde_data/code/pythonCode/mid.jpg").convert("L")
#img.show()
print(np.array(img))
a = np.array(img).astype("float")
print(a)
grad = np.gradient(a)
depth = 10.
grad_x,grad_y = grad

grad_x = grad_x*depth/100
grad_y = grad_y*depth/100

A = np.sqrt(grad_x**2+grad_y**2+1)

uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A

vec_el = np.pi/2.2                   # 光源的俯视角度，弧度值
vec_az = np.pi/4.                    # 光源的方位角度，弧度值
dx = np.cos(vec_el)*np.cos(vec_az)   #光源对x 轴的影响
dy = np.cos(vec_el)*np.sin(vec_az)   #光源对y 轴的影响
dz = np.sin(vec_el)              #光源对z 轴的影响

b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)     #光源归一化

b = b.clip(0,255)
print(b)
img = Image.fromarray(b.astype("uint8"))
img.show()
img.save('/media/vv/_dde_data/code/pythonCode/midHD.jpg')
