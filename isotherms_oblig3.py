import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.signal as sign
plt.style.use('ggplot')


critical_pressure = 33.6 #[atm]
critical_volume = 0.089 #[l / mole]
critical_temperature = 126 #[K]
temperatures = np.array([60, 77, 100, 110, 115, 120, 125, 150])
volumes = np.linspace(0.4, 10, 1000)


def pressure(volume, temp):
    return (8 * temp) / (3 * volume - 1) - 3 / (volume)**2


def plot_liquid_gas_volume():
    v_l = np.array([0.51, 0.58, 0.62, 0.69, 0.85])
    v_g = np.array([4.37, 2.91, 2.23, 1.70, 1.22])
    T = np.array([100, 110, 115, 120, 125])


    diff = v_l - v_g
    a, b = stats.linregress(T, diff)[0:2]


    plt.title("Regression Plot of $V_{l - g}(T)$")
    plt.scatter(T, diff, c='k')
    plt.plot(T, a*T + b)
    plt.xlabel(r"$T [K]$")
    plt.ylabel(r"$V_l - V_g $")
    plt.legend([r"$a = {0:.2f}, b = {1:.2f}, T_c = {2:.2f}$".format(a, b, -b/a)])
    plt.show()


plot_liquid_gas_volume()


for temp in temperatures:
    plt.plot(volumes, pressure(volumes, temp / critical_temperature), label = r"$T$=%g[K]" % (temp))


plt.title("Dimensionless Pressure of van der Waals Gas")
plt.ylabel(r"$\hat{P}$")
plt.xlabel(r"$\hat{V}$")
plt.xlim(0, 7)
plt.ylim(-0.1, 1.3)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()
