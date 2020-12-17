### main.py ###
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('daten.csv')
g = df['g']
b = df['b']
G = 1/g
B = 1/b

# Aufgabe a)
# Berechnung der Werte fuer f
f = 1 / (G + B)
mean = np.mean(f)
s = np.std(f)
u = 1/np.sqrt(6) * s
print(f)
print(f'Mittelwert: {mean}')
print(f'Standartabweichung: {s}')
print(f'Unsicherheit: {u}')

# Aufgabe b)
# berehchne gerade mit 1/f = m*x+b

m, y0, r, p, std_err  = stats.linregress(G,B)
x = np.linspace(0,0.02,1000)
print('Geradengleichung: y=m*x + y0')
print(f'm = {m}\t y0={y0}')
plt.plot(x, m*x + y0, label="Ausgleichsgerade");

plt.scatter(G,B, marker="+", color='k', label="Daten")
plt.legend()

plt.xlabel(r'$G = 1/g$')
plt.ylabel(r'$B = 1/b$')

# F = 1/f = G + B = m*x + y0
# in der lin regress ist G = m*x, also fuer x = 0
# gilt F = y0 <=> 1/f=y0 <=> f = 1/y0
print('Laut linregress:')
print(f'f = {1 / y0}')

plt.savefig('aufgabe2-plot.pdf')
