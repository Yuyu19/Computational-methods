function [alphaest, muest, sigmaest, loglikelihood] = emnormal(Y, alpha, mu, sigma)
n = length(Y);
i = 1;
stop = 1;
loglike(i) = sum(log(alpha(i, 1)*normpdf(Y, mu(i, 1), sigma(i, 1))+...
alpha(i, 2)*normpdf(Y, mu(i, 2), sigma(i, 2))));
while (stop>1e-6)
P(1, :) = alpha(i, 1) * normpdf(Y, mu(i, 1), sigma(i, 1))./...
(alpha(i, 1) * normpdf(Y, mu(i, 1), sigma(i, 1)) + alpha(i, 2)...
* normpdf(Y, mu(i, 2), sigma(i, 2)));
P(2, :) = alpha(i, 2) * normpdf(Y, mu(i, 2), sigma(i, 2))./...
(alpha(i, 1) * normpdf(Y, mu(i, 1), sigma(i, 1)) + alpha(i, 2)...
* normpdf(Y, mu(i, 2), sigma(i, 2)));
alpha(i+1, 1) = 1/n * sum(P(1, :));
alpha(i+1, 2) = 1/n * sum(P(2, :));
mu(i+1, 1) = sum(Y .* P(1, :)) / sum(P(1, :));
mu(i+1, 2) = sum(Y .* P(2, :)) / sum(P(2, :));
sigma(i+1, 1) = sqrt(sum((Y - mu(i+1,1)).^2 .* P(1, :))/sum(P(1, :)));
sigma(i+1, 2) = sqrt(sum((Y - mu(i+1,2)).^2 .* P(2, :))/sum(P(2, :)));
loglike(i+1) = sum(log(alpha(i+1, 1)*normpdf(Y, mu(i+1, 1), sigma(i+1, 1))+...
alpha(i+1, 2)*normpdf(Y, mu(i+1, 2), sigma(i+1, 2))));
stop = min(abs([alpha(i+1, 1)-alpha(i, 1),alpha(i+1, 2)-alpha(i, 2),...
mu(i+1, 1)-mu(i, 1),mu(i+1, 2)-mu(i, 2), sigma(i+1, 1)...
-sigma(i, 1), sigma(i+1, 2)-sigma(i, 2)]));
i = i+1;
end
alphaest = alpha(end,:);
muest = mu(end,:);
sigmaest = sigma(end,:);
loglikelihood = loglike;