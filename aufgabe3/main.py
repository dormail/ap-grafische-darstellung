### main.py ###
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit

df = pd.read_csv('daten.csv')
# N ist in 1/60s, wird angepasst um in SI zu sein
df['N'] = df['N']/60
d = df['d']
N = df['N']

# messunsicherheit
dN = np.sqrt(N)
df['dN'] = dN
print(df)

# curve fit
def n(d, N0, mu):
    return N0 * np.exp(-1 * mu * d)

popt, pcov = curve_fit(n, d, N)
N0 = popt[0]
mu = popt[1]

# plot
x = np.linspace(0,5.1,1000)
# lin-log
fig = plt.figure()
ax = fig.add_subplot(2,1,1)

plt.errorbar(d, N,yerr=dN, fmt=',', label='Messdaten') ## messdaten
plt.plot(x, n(x, N0, mu), linewidth=0.5, color='r', 
        label=rf'Curve-Fit für $\mu={{{mu:.4f}}}cm$')

plt.xlabel('$d/$cm')
plt.ylabel('$N \cdot 1$s')
plt.legend()
plt.title('Absorbtion, halblogarithmischer Plot')

ax.set_yscale('log')

# lin-lin
ax = fig.add_subplot(2,1,2)

plt.errorbar(d, N,yerr=dN, fmt=',', label='Messdaten')
plt.plot(x, n(x, N0, mu), linewidth=0.5, color='r', 
        label=rf'Curve-Fit für $\mu={{{mu:.4f}}}cm$')

plt.xlabel('$d/$cm')
plt.ylabel('$N \cdot 1$s')
plt.legend()
plt.title('Absorbtion, linearer Plot')

# damit die plots nicht ineinander haengen
fig.tight_layout(h_pad=2)
plt.savefig('aufgabe3-plot.pdf')

# ausgabe von mu
print(f'mu = {mu}')
#plt.show()
