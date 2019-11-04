# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:26:06 2019

@author: 18800
"""

from numpy import *
from matplotlib import pyplot

n = 100
x = [6, 52, 28, 14]
theta = zeros(100)
theta[0] = 0.4
nth = (theta[0]/(2+theta[0])*x[1]+x[0]+x[3])/(2*(theta[0]/(2+theta[0])*x[1]+x[0]+x[2]+x[3]))
i = 0;


while (abs(theta[i]-nth)>1e-6):
      nth = theta[i]
      theta[i+1] = (theta[i]/(2+theta[i])*x[1]+x[0]+x[3])/ \
                   (2*(theta[i]/(2+theta[i])*x[1]+x[0]+x[2]+x[3]))
      i = i+1

pyplot.subplot(211)
pyplot.plot(range(0,i+1), theta[0:i+1], 'b-*')

ll = zeros(i+1)
for k in range(0,i+1):
    ll[k] = (x[0]+x[3])*log(theta[k]) + x[1]*log(2+theta[k]) + x[2]*log(1-2*theta[k]);

pyplot.subplot(212);
pyplot.plot(range(0, i+1), ll[:], 'ro-')
pyplot.show()
print("the estimated theta is", theta[i])