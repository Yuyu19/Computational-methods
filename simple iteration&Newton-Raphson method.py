# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:21:11 2019

@author: 18800
"""
from numpy import *
from matplotlib import pyplot

# problem 1
# simple iteration
f= lambda x:0.9*sin(x)-x

x0=pi/4
x=zeros(1000)
x[0] = x0
gx=f(x[0])+x[0]
i=0

while abs(x[i] -gx)> 1e-6:
    gx = x[i]
    x[i+1] = f(x[i])+x[i]
    i=i+1
    
pyplot.figure(1)
pyplot.plot(range(0,i+1),x[0:i+1],'b-')

#Newton-Raphson method
df = lambda x: 0.9*cos(x)-1

x=zeros(1000)
x[0]=x0
gx= x[0] - f(x[0])/df(x[0])
i=0
while abs(x[i] - gx)>1e-6:
    gx=x[i]
    x[i+1]=x[i]-f(x[i])/df(x[i])
    i =i +1

pyplot.figure(1)
pyplot.plot(range(0,i+1),x[0:i+1],'r-')
pyplot.show()

# problem 2
f = lambda x: x**5 - 4.5*x**4 + 4.55*x**3 + 2.675*x**2 - 3.3*x - 1.4375
df = lambda x: 5*x**4 - 18*x**3 + 13.65*x**2 + 5.35*x - 3.3

x0 = -0.6;
x = zeros(1000)
x[0] = x0
gx = x[0]-f(x[0])/df(x[0])
i = 0
while (abs(x[i] - gx) > 1e-6):
   gx = x[i]
   x[i+1] = x[i] - f(x[i])/df(x[i])
   i = i+1
   
x = x[0:i+1]
E = diff(x)
K = E[2:-1] / E[1:-2]
print("K[-1] = ", K[-1])
