from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.sin(x/5)*np.exp(x/10)+5*np.exp(-x/2)


x0 = 30
# bounds=((1, 30),) # Границы поиска для функции minimize

res = minimize(f, x0, method='BFGS')
print('Result:', res)

# Построим график функции f(x)
x_plt = np.arange(1, 30, 0.1)
y_plt = f(x_plt)
plt.figure()
plt.plot(x_plt, y_plt)
plt.show()
