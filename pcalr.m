function SSE = pcalr(X,y,d) 
C = cov(X);
[U, ~, ~] = svd(C);
U1 = U(:,1:d);
X1 = X * U1;
b1hat = multilinreg(X1,y);
SSE = norm(y - X1 * b1hat)^2;