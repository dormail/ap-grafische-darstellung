### main.py ###
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('daten.csv')
m = df['m']
x = df['x']

a, b, r, p, std_err  = stats.linregress(m,x)
# a = g/k <=> k = g/a
g = 9.81
k = g/a
# bringen k auf si
k = 0.1*k

m_plt = np.linspace(0,6.5,100)
plt.plot(m_plt, a*m_plt + b, label=rf'Ausgleichsgerade zu $k = {{{k:.4}}} kg/s^2$');
plt.scatter(m,x, marker="+", color='k', label="Daten")
plt.legend()
plt.xlabel(r'$m/$g')
plt.ylabel(r'$x/$cm')

plt.savefig('aufgabe1-plot.pdf')
