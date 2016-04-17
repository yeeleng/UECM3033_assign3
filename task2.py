import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
   
def ode(y, t, a, b):
    y0, y1 = y
    dydt = [a*(y0-y0*y1), b*(-y1+y0*y1)]
    return dydt

a = 1
b = 0.2
y0_0 = 0.1
y1_0 = 1.0
y_0 = [y0_0, y1_0]

t= np.linspace(0, 5, 100)

sol = odeint(ode, y_0, t, args=(a,b))

fig = plt.figure(1)
plt.plot(t, sol[:, 0], 'b', label='y0(t)', color='blue')
plt.plot(t, sol[:, 1], 'g', label='y1(t)', color='green')
plt.title('Graph of y against t')
plt.legend(loc='best')
plt.xlabel('t (years)')
plt.ylabel('y')
plt.show()

fig=plt.figure(2)
plt.plot(sol[:,0], sol[:,1], 'r', label='y1(y0)', color='red')
plt.title('Graph of y1 against y0')
plt.legend(loc='best')
plt.xlabel('y0')
plt.ylabel('y1')
plt.show()

###

y0_new = 0.11
y1_new = 1.0
y_new = [y0_new, y1_new]

sol_new = odeint(ode, y_new, t, args=(a,b))

fig = plt.figure(1)
plt.plot(t, sol_new[:, 0], 'c', label='y0(t)_new', color='cyan')
plt.plot(t, sol_new[:, 1], 'm', label='y1(t)_new', color='magenta')
plt.title('Graph of y against t')
plt.legend(loc='best')
plt.xlabel('t (years)')
plt.ylabel('y')
plt.show()
plt.savefig('Graph of y against t.jpg')

fig=plt.figure(2)
plt.plot(sol_new[:,0], sol[:,1], 'k', label='y1(y0)_new', color='black')
plt.title('Graph of y1 against y0')
plt.legend(loc='best')
plt.xlabel('y0')
plt.ylabel('y1')
plt.show()
plt.savefig('Graph of y1 against y0.jpg')
