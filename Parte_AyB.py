import numpy as np                      # cálculos numéricos
import matplotlib.pyplot as plt         # gráficos

print("***PARTE A***")

# PARTE A - CONVOLUCIÓN

# Datos personales
h = np.array([5,6,0,0,9,3,8])            # Código 5600938
x = np.array([1,0,2,8,4,8,4,0,3,4])      # Cédula 1028484034

# Convolución
y = np.convolve(x, h)

print("h[n] =", h)
print("x[n] =", x)
print("y[n] (convolución) =", y)

# Gráfica convolución
plt.figure()
plt.stem(y)
plt.title("Convolución y[n]")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.grid()
plt.show()


print("\n***PARTE B***")

# PARTE B - CORRELACIÓN CRUZADA

Ts = 0.00125     # 1.25 ms
n = np.arange(0,9)

# Señales
x1 = np.cos(2*np.pi*100*n*Ts)
x2 = np.sin(2*np.pi*100*n*Ts)

print("x1[n] (coseno) =", x1)
print("x2[n] (seno)   =", x2)

# Correlación cruzada
r = np.correlate(x1, x2, mode='full')

print("Correlación cruzada =", r)

# Eje de retardos
lags = np.arange(-len(x1)+1, len(x1))

# Gráfica correlación
plt.figure()
plt.stem(lags, r)
plt.title("Correlación Cruzada")
plt.xlabel("Retardo")
plt.ylabel("Amplitud")
plt.grid()
plt.show()