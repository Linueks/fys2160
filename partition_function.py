import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

states1 = np.array([-0.1, -0.05, 0, 0.05, 0.1])
states2 = np.array([0, 0.05, 0.1, 0.15, 0.2])
temp = 300
k = 8.6173e-5

boltzmann_factors1 = np.exp(-states1 / (temp * k))
boltzmann_factors2 = np.exp(-states2 / (temp * k))

print(boltzmann_factors1)
print(boltzmann_factors2)

Z1 = np.sum(boltzmann_factors1)
Z2 = np.sum(boltzmann_factors2)
P1 = 1 / Z1 * np.exp(-states1 / (temp * k))
P2 = 1 / Z2 * np.exp(-states2 / (temp * k))

plt.subplot(211)
plt.title('Probability $P(\\epsilon)$')
plt.xlabel('State Energy $\\epsilon$ [eV]')
plt.ylabel('P($\\epsilon$)')
plt.scatter(states1, P1)
plt.plot(states1, P1)
plt.legend(['$Z_1 = {:.2f}$'.format(Z1)])

plt.subplot(212)
plt.xlabel('State Energy $\\epsilon$ [eV]')
plt.ylabel('P($\\epsilon$)')
plt.scatter(states2, P2)
plt.plot(states2, P2)
plt.legend(['$Z_2 = {:.2f}$'.format(Z2)])
plt.tight_layout()

plt.show()
