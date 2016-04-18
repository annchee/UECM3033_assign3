import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#To solve this equation with `odeint`, we must first convert
# it to a system of first order equations.
# Let `y` be the vector [`M`, `N`].  We implement this system
# in model function :
def model(y, t, b, c):
    M, N = y
    
    return np.array([a*(M-M*N),b*(-N+M*N)])

a = 1.0
b = 0.2

y0 = [ 0.1, 1.0]
# We generate a solution 101 evenly spaced samples in the interval
# 0 <= `t` <= 5.  So our array of times is:
t = np.linspace(0, 5,101)

y1=[0.1,1.0]

#Graph of y0 and y1 against t
sol = odeint(model, y0, t, args=(a, b))
plt.ylim([0,1.0])
plt.plot(t, sol[:, 0], 'b', label='M(t)')
plt.plot(t, sol[:, 1], 'g', label='N(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

#Graph of y0 against y1
sol2 = odeint(model, y0, y1, args=(a, b))
plt.ylim([0,1.0])
plt.plot(y0,y1)
plt.legend(loc='best')
plt.ylabel('y1')
plt.xlabel('y0')
plt.grid()
plt.show()

