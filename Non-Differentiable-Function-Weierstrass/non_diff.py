import numpy as np
import matplotlib.pyplot as plt

# N = number of simulation points
N = 1000

x = np.linspace(-2,2,N)

#T = number of terms
T = 100

def term(x,n):
    return np.cos(np.pi * x * np.power(13,n)) / np.power(2,n)

y = np.zeros(N)
for i in range(T):
    y += term(x,i)

plt.plot(x,y,label=r'$cos(\pi x) + \frac{1}{2} \cos{(13 \pi x)} + \frac{1}{4} \cos{(169 \pi x)} + \ldots$')
plt.legend(fontsize=20)
plt.savefig('non_diff.pdf',format='pdf',dpi=1200)
plt.show()
            
