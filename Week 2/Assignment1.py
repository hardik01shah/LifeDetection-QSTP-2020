import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

plt.style.use('seaborn') 
plt.rcParams['figure.figsize'] = (12, 8)

def plot_normal(x_range, mu=0, sigma=1, cdf=False, **kwargs):
    x = x_range
    if cdf:
        y = ss.norm.cdf(x, mu, sigma)
    else:
        y = ss.norm.pdf(x, mu, sigma)
    plt.plot(x, y, **kwargs)

x = np.linspace(-10, 10, 5000)

plot_normal(x, 0, sqrt(5), color='red', lw=2, ls='-', alpha=0.5, label='plot1')
plot_normal(x, 4, sqrt(0.2), color='blue', lw=2, ls='-', alpha=0.5, label='plot2')
plot_normal(x, -3.5, sqrt(0.05), color='green', lw=2, ls='-', alpha=0.5, label='plot3')

plt.title('normal distribution assignment',fontsize=10)

plt.xlabel('x')
plt.ylabel('Normal Distribution')

plt.savefig("normal_distribution.png")
plt.show()