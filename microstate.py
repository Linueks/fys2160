from __future__ import division, print_function
from scipy.constants import Boltzmann
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
style.use('ggplot')
np.random.seed(1)


def multiplicity(N, S, omega_max):


    return omega_max * np.exp(-S**2 / (2 * N))


k = Boltzmann
N = 60
M = 10 ** 7


microstates = np.random.randint(2, size=(M, N))
ones = np.sum((microstates == 1), axis=1)
zeroes = np.sum((microstates == 0), axis=1)


net_spin = ones - zeroes
print(net_spin)
ns =  np.arange(-N, N)
spins = np.linspace(-N, N, 1000)
temp = Counter(net_spin)
omega_max = temp.most_common(1)[0][1]


plt.xlabel("Net spin S")
plt.ylabel("Microstates")
plt.hist(net_spin, ns)
plt.plot(spins, multiplicity(N, spins, omega_max))


#plt.xlabel("Net spin $S$")
#plt.ylabel("Entropy $S_B$")
#plt.plot(spins, k * np.log(multiplicity(N, spins, omega_max)))


plt.show()
