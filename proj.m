function result = proj(X,U,d) 
  temp = zeros(size(U(:,1))); 
for i = 1 : d 
    temp = temp + X * U(:, i) * U(:, i);
end
result = temp;