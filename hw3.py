# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:45:15 2019

@author: 18800
"""
## probelm 1
# Write multilinreg program in Matlab to solve the following regression problem:
# find least-square estimate
from numpy import *
##backsub
def backsub(X, y):
    l = shape(X)  
    n = l[1]
    b = zeros((n,1))
    b[n-1, 0] = y[n-1, 0]/X[n-1, n-1]
    for j in range(n-1,0,-1):
        b[j-1,0] = (y[j-1,0] - dot(X[j-1, range(j,n)], b[range(j,n),0]))/X[j-1, j-
1]
    return b


##house
def house(x):
    m = size(x)
    mu = linalg.norm(x)
    v = x.copy()
    if mu != 0:
        c = x[0] + sign(x[0])*mu
        v[1:m+1] = v[1:m+1]/c
    v[0] = 1
    return v

###rowouse
def rowhouse(X,v):
    X = mat(X)
    v = mat(v)
    X = X - 2*v*v.T/(v.T*v)*X
    return X


def multilinreg(X0,y0):
    X= X0.copy()
    y= y0.copy()
    m,n= shape(X0)
    for j in range(1,n+1):
        v = house(X[j-1:m,j-1])
        X[j-1:m,j-1:n]=rowhouse(X[j-1:m,j-1:n], v)
        beta = -2.*(v.T*y[j-1:m])/(v.T*v)
        y[j-1:m]=y[j-1:m]+v*beta
    b=backsub(X,y)
    return b
  
X1= mat("5. 0. 9. 3.; 3. 6. 8. 9.; 4. 4. 9. 6. ; 0. 3. 1. 8. ; 2. 8. 2. 3.")
y1= mat("20.; 17.; 32.; 10.; 12.")
multilinreg(X1,y1)


## probelm 2
## find and display the principal direction of a 2D dataset
x = mat("15 16 12 14 13 15 16 21 12 11 19 14 13 14 16 17 12 16; 13 11 13 12 9 14 12 16 9 8 15 13 15 13 12 16 11 9")

## load pyplot package
from numpy import *
from matplotlib import pyplot
import scipy
import scipy.linalg

### Plot this data on a 2D scatter plot
pyplot.figure(1)
pyplot.plot(x[0,:],x[1,:],'*')
pyplot.axis([60,80,60,80])
pyplot.axis('equal')
pyplot.xlabel('First Trial')
pyplot.ylabel('Second Trial')

## Perform PCA on this data
x=x.T
m,n=shape(x)
C=cov(x.T)
U,S,Vh = linalg.svd(C)
V=Vh.T
U1=U[:,0:2]
Z= x*U1

##Draw the first principal direction on this plot
pyplot.figure(1)
m_x =x.mean(axis=0)
TP1=array(2*sqrt(S[0])*mat([-U[0,0],U[0,0]])+m_x[0,0])
TP2=array(2*sqrt(S[0])*mat([-U[1,0],U[1,0]])+m_x[0,1])
pyplot.plot(TP1[0],TP2[0],'g-')
pyplot.show()


##the ratio of this variance over the total variance in the original data
Cov_x =cov(x.T)
Cov_Z =cov(Z.T)
Total_var_x=trace(Cov_x)
Ratio =Cov_Z[0,0] / Total_var_x

Cov_Z[0,0] 
Ratio    


###Probelm 3
# PCA and Linear Regression
from numpy import *
from mlr import *
import matplotlib.pyplot as plt


##find sample covarianc matrix
##compute SVD, b1hat, SSE
def pcalr(X,y,d):
    C=cov(X.T)
    U,s,V=linalg.svd(C)
    U=mat(U)
    U1=U[:,range(0,d)]
    X1= X*U1
    b1hat=multilinreg(X1,y)
    SSE=linalg.norm(y-X1*b1hat)**2
    return SSE

##load data
import scipy.io
mat_contents=scipy.io.loadmat('hw3_3_data.mat')
X=mat(mat_contents['X'])
y=mat(mat_contents['y'])

###plot SSE values
SSE=zeros((10,1))
i=0
for d in range(10,110,10):
    SSE[i] =pcalr(X,y,d)
    print("d= ",d)
    print("SSE= ",SSE[i])
    i=i+1

plt.plot(range(10,110,10), SSE)

