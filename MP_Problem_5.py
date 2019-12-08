#MP5-Python
import matplotlib.pyplot as plt
import numpy as np
n = np.linspace(0,199,num=200)
x = eval(input('Equation: '))
for n in range(0,199,1):
    m = n
    if m == 0:
        ay = -1.5 * x
        n = n + 1
        by = 2 * x
        n = n + 2
        cy = 0.5 * x
        y = ay + by - cy
    elif (m > 0)|(m < 199):
        n = n + 1
        ay = 0.5 * x
        n = n - 1
        by = 0.5 * x
        y = ay - by
    elif m == 199:
        ay = 1.5 * x
        n = n - 1
        by = 2 * x
        n = n - 2
        cy = 0.5 * x
        y = ay - by + cy
plt.plot(x,'k-',label = 'x(n)')
plt.plot(y,'r-',label = 'y(n)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc = 'upper right')
plt.grid()
plt.show()