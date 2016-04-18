import numpy as np
import sympy as sy
#Your optional code here


#You can import some modules or create additional functions
from numpy.linalg import eigh
# DO NOT CHANGE THE NAME OF gausslegendre() function
def gausslegendre(f, a, b, n=20):
#    ans = 0
    # Edit here to implement your code
    b=np.zeros(n-1);
    for i in range (np.size(b)):
        b[i]=(i+1)/np.sqrt(4*(i+1)*(i+1)-1)
    j=np.diag(b,-1)+np.diag(b,1)
    x,ev=eigh(j);
    w=2*ev[0]*ev[0]
    return(x,w)
#    return ans
    

if __name__ == "__main__":
    def f(x):
        return (x**2 +7*x)/(1 +np.sqrt(x))**4
    
    def my_integral():
        x = sy.Symbol('x')
        ans = sy.integrate((x**2 +7*x)/(1 +sy.sqrt(x))**4, (x,0, 1))
        return ans
    
    print('Answer:                    I = ', my_integral())
    print('Your implementation gives: I = ', gausslegendre(f, 0,1))
