import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as const
from scipy import integrate
plt.style.use('ggplot')

k = const.Boltzmann #[m^2kgs^-2K^-1]
velocities = np.linspace(2400, 80000, 1000000) #[m/s]
mass_n2 = 4.7e-26 #[kg]
mass_h2 = 3.3e-27 #[kg]
mass_he = 6.6e-27 #[kg]
t1 = 1000 #[K]
t2 = 600 #[K]

boltzmann_distribution_n1 = (mass_n2 / (2 * np.pi * k * t1))**(3/2) * 4 * np.pi * velocities**2 * np.exp(-mass_n2 * velocities**2 / (2 * k * t1))
boltzmann_distribution_n2 = (mass_n2 / (2 * np.pi * k * t2))**(3/2) * 4 * np.pi * velocities**2 * np.exp(-mass_n2 * velocities**2 / (2 * k * t2))
boltzmann_distribution_h1 = (mass_h2 / (2 * np.pi * k * t1))**(3/2) * 4 * np.pi * velocities**2 * np.exp(-mass_h2 * velocities**2 / (2 * k * t1))
boltzmann_distribution_h2 = (mass_h2 / (2 * np.pi * k * t2))**(3/2) * 4 * np.pi * velocities**2 * np.exp(-mass_h2 * velocities**2 / (2 * k * t2))
boltzmann_distribution_he1 = (mass_he / (2 * np.pi * k * t1))**(3/2) * 4 * np.pi * velocities**2 * np.exp(-mass_he * velocities**2 / (2 * k * t1))
boltzmann_distribution_he2 = (mass_he / (2 * np.pi * k * t2))**(3/2) * 4 * np.pi * velocities**2 * np.exp(-mass_he * velocities**2 / (2 * k * t2))

print(np.sum(boltzmann_distribution_n1) * (velocities[1] - velocities[0]))

#v_rms
n1_rms = np.sqrt(3 * k * t1 / mass_n2)
n2_rms = np.sqrt(3 * k * t2 / mass_n2)
h1_rms = np.sqrt(3 * k * t1 / mass_h2)
h2_rms = np.sqrt(3 * k * t2 / mass_h2)
he1_rms = np.sqrt(3 * k * t1 / mass_he)
he2_rms = np.sqrt(3 * k * t2 / mass_he)

#v most prob
n1_mp = np.sqrt(2 * k * t1 / mass_n2)
n2_mp = np.sqrt(2 * k * t2 / mass_n2)
h1_mp = np.sqrt(2 * k * t1 / mass_h2)
h2_mp = np.sqrt(2 * k * t2 / mass_h2)
he1_mp = np.sqrt(2 * k * t1 / mass_he)
he2_mp = np.sqrt(2 * k * t2 / mass_he)

#v avg
n1_avg = np.sqrt(8 * k * t1 / (np.pi * mass_n2))
n2_avg = np.sqrt(8 * k * t2 / (np.pi * mass_n2))
h1_avg = np.sqrt(8 * k * t1 / (np.pi * mass_h2))
h2_avg = np.sqrt(8 * k * t2 / (np.pi * mass_h2))
he1_avg = np.sqrt(8 * k * t1 / (np.pi * mass_he))
he2_avg = np.sqrt(8 * k * t2 / (np.pi * mass_he))

"""
print(n1_rms, n2_rms, h1_rms, h2_rms, he1_rms, he2_rms)
print(n1_mp, n2_mp, h1_mp, h2_mp, he1_mp, he2_mp)
print(n1_avg, n2_avg, h1_avg, h2_avg, he1_avg, he2_avg)
"""

"""
plt.figure()
plt.title('Boltzmann-distributions for $N_2$, $H_2$ and $He$')
plt.plot(velocities, boltzmann_distribution_n1, label='$N_2$, T = 300K')
plt.plot(velocities, boltzmann_distribution_n2, label='$N_2$, T = 600K')

plt.plot(velocities, boltzmann_distribution_h1, label='$H_2$, T = 300K')
plt.plot(velocities, boltzmann_distribution_h2, label='$H_2$, T = 600K')

plt.plot(velocities, boltzmann_distribution_he1, label='$He$, T = 300K')
plt.plot(velocities, boltzmann_distribution_he2, label='$He$, T = 600K')
plt.xlabel('v [m/s]')
plt.ylabel('D(v)')
plt.legend()

plt.show()
"""
