m = 1;
g = 1;
l = 1;
mu = 0.1;
alpha = 2;
x1 = linspace(pi/2, 3*pi/2,10);
x2 = linspace(-2, 2,10);
[X1,X2]=meshgrid(x1,x2);
V = -m*g*l*(1+cos(X1)) + alpha*m*g*l*(1-cos(X1).^2) + 0.5*m*(l^2)*(X2.^2);
meshc(X1,X2,V);

Xu = cos(X1) < -1/(2*alpha) & V >= 0 & -mu*X2^2 <= 0;
meshc(X1,X2,Xu);

c = @(t,X) [X(2); -g*sin(X(1))/l - mu*X(2)/(m*l^2) - 2*alpha*g*sin(X(1))*cos(X(1))/l];
u = zeros(size(X1));
v = zeros(size(X1));
t=0;
for i = 1:numel(X1)
    Cprime = c(t,[X1(i); X2(i)]);
    u(i) = Cprime(1);
    v(i) = Cprime(2);
end
quiver(X1,X2,u,v)

c_vals = 0.05:0.1:1.25;
contour(X1,X2,V, c_vals)
