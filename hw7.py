
from numpy import *
from matplotlib import pyplot
import time
import scipy
from scipy import io

#dataset 1
temp = scipy.io.loadmat('hw7_1_data1.mat')
X = transpose(temp['Yn'])
(N,I)=shape(X)
pyplot.ion()
K = 5
C = X[0:K,:]
E = 1
m = 0
itr_max = 20

min_dis = zeros((itr_max,N))
ind = zeros((itr_max, N))
ss = zeros((itr_max))
CC = zeros((K, I, itr_max))
CC[:,:,0] = C

while (E > 1e-3):
  for n in range(0,N):
    dis = sqrt(sum(array(ones((K,1))*X[n] - C)**2, axis=1))
    min_dis[m,n] = amin(dis)
    ind[m,n] = argmin(dis)
  for k in range(0,K):
    C[k,:] = mean(X[ind[m,:] == k,:], axis=0)
    CC[:,:,m+1] = C
    E = linalg.norm(CC[:,:,m+1] - CC[:,:,m])
    ss[m] = sum(min_dis[m,:]**2)
    pyplot.figure(m+2)
    cr = 'brgyk'
  for k in range(0,K):
    pyplot.plot(X[ind[m,:]==k,0], X[ind[m,:]==k,1], '.', \
    color = cr[k], markersize = 10)
    pyplot.plot(C[k,0], C[k,1], 'o', color = cr[k], markersize = 15)
  m = m+1
  
pyplot.figure(m+2)
pyplot.plot(range(0,m), ss[0:m])
pyplot.show()


# dataset 2
temp = scipy.io.loadmat('hw7_1_data2.mat')
X = transpose(temp['Yn'])
(N,I)=shape(X)
pyplot.ion()

K = 5
C = X[19:19+K,:] # Here use the 20th to 24th data as initial value
E = 1
m = 0
itr_max = 20

min_dis = zeros((itr_max,N))
ind = zeros((itr_max, N))
ss = zeros((itr_max))
CC = zeros((K, I, itr_max))
CC[:,:,0] = C

while (E > 1e-3):
  for n in range(0,N):
    dis = sqrt(sum(array(ones((K,1))*X[n] - C)**2, axis=1))
    min_dis[m,n] = amin(dis)
    ind[m,n] = argmin(dis)
  for k in range(0,K):
    C[k,:] = mean(X[ind[m,:] == k,:], axis=0)
    CC[:,:,m+1] = C
    E = linalg.norm(CC[:,:,m+1] - CC[:,:,m])
    ss[m] = sum(min_dis[m,:]**2)
    pyplot.figure(m+2)
    cr = 'brgyk'
  for k in range(0,K):
    pyplot.plot(X[ind[m,:]==k,0], X[ind[m,:]==k,1], '.', \
    color = cr[k], markersize = 10)
    pyplot.plot(C[k,0], C[k,1], 'o', color = cr[k], markersize = 15)
  m = m+1
   
pyplot.figure(m+2)
pyplot.plot(range(0,m), ss[0:m])
pyplot.show()