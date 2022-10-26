syms h(t)
Dh = diff(h);
m = 65;
kt = 5.276 * 10^-4;
Kp = 5;
ode = diff(h,t,2) == 4*kt*Kp/m - 4*kt*Kp*h/m;
cond1 = h(0) == 0;
cond2 = Dh(0) == 0;
conds = [cond1, cond2];
hSol(t) = dsolve(ode,conds);
hSol = simplify(ySol);
disp(hSol)