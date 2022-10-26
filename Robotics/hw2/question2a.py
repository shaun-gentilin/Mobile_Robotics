from matplotlib import pyplot as plt
from scipy.integrate import odeint
import numpy

kt = 5.276 * 10 ** -1
m = 65
Kp = 5

def f(h,t):
    return (h[1],(4*kt*Kp/m)*(1-h[0]))
y0 = [0,0]
xs = numpy.linspace(0,10)
hs = odeint(f,y0,xs)
ys = hs[:,0]
plt.plot(xs,ys,'-')
plt.show()
