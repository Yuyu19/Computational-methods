function b = backsub(X,y)
l=size(X);
n=l(2);
b(n,1)=y(n,1)/X(n,n);
for j= n-1:-1:1
    b(j,1)=(y(j,1)-X(j,j+1:n)*b(j+1:n,1))/X(j,j)
end

X=[6 3 9 2;0 4 6 1; 0 0 8 8; 0 0 0 5]
y=[1; 4; 6; 1]
backsub(X,y)
%% 

function v = house(x)
m = length(x)
mu= norm(x,2)
v = x
if mu~=0
c= x(1) + sign(x(1))*mu
v(2 : m, 1) = v(2 : m, 1)/c
end
v(1) = 1
 x=[1.4 5.8 2.3 8.1 9.0]' 
 house(x)
 
 %% 
 function X = householder(X)
[m, n] = size(X)
v = zeros(m, 1)
for j = 1 : n
  v(j : m, 1) = house(X(j : m, j));
  X(j : m, j : n) = rowhouse(X(j : m, j : n), v(j : m, 1));
end
X=[ 1.4 4.5 6.5; 5.8 3.2 7.3; 2.3 -2.6 8.2; 8.1 -5.8 -8.0; 9.0 0.3 1.5]
householder(X)

%% 
x=[1.4 5.8 2.3 8.1 9.0]'