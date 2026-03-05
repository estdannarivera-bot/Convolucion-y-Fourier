import numpy as np
import matplotlib.pyplot as plt
import serial
import time

# CONFIGURACIÓN GENERAL

# MODO puede ser:
# "serial", Captura datos desde microcontrolador
# "archivo", Carga datos desde archivo .txt
MODO = "archivo"

PORT = 'COM4'       # Puerto serial
BAUD = 115200       # Velocidad comunicación
FS = 200            # Frecuencia de muestreo (Hz)
TIEMPO = 10         # Duración de captura (segundos)
N = FS * TIEMPO     # Número total de muestras esperadas

ARCHIVO = "EOG.txt" # Archivo donde se guarda o carga la señal

VREF = 3.3          # Voltaje referencia ADC
ADC_MAX = 4095      # Resolución ADC 12 bits


# ADQUISICIÓN DE LA SEÑAL

if MODO == "serial":
    print("Adquiriendo señal desde microcontrolador...")

    # Abrir puerto serial
    ser = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(2)

    x = []

    # Leer hasta completar N muestras
    while len(x) < N:
        try:
            line = ser.readline().decode('utf-8').strip() # Leer línea y decodificar
            if line.isdigit():                            # Verificar que es un número
                value = int(line)                         # Convertir a entero
                x.append(value)                           # Agregar a la lista
        except:
            pass

    ser.close()    # Cerrar puerto serial

    # Convertir lista a arreglo
    x = np.array(x)

    # Convertir valores ADC a voltios
    senal_v = (x / ADC_MAX) * VREF

    # Guardar señal en archivo
    np.savetxt(ARCHIVO, senal_v)

else:
    print("Cargando señal desde archivo...")
    senal_v = np.loadtxt(ARCHIVO)


# PROCESAMIENTO

N = len(senal_v)                # Número real de muestras
t = np.arange(N) / FS           # Vector de tiempo

# Se resta la media para centrar la señal en 0
senal_centrada = senal_v - np.mean(senal_v)

# Convolución simple que suaviza la señal
h = np.array([0.5, 0.5])
senal_filtrada = np.convolve(senal_centrada, h, mode='same')

# ESTADÍSTICOS EN EL DOMINIO DEL TIEMPO

print("\n***ESTADÍSTICOS EN TIEMPO***")
print("Media:", np.mean(senal_filtrada))
print("Mediana:", np.median(senal_filtrada))
print("Desviación estándar:", np.std(senal_filtrada))
print("Máximo:", np.max(senal_filtrada))
print("Mínimo:", np.min(senal_filtrada))

# Gráfica de la señal filtrada
plt.figure()
plt.plot(t, senal_filtrada)
plt.title("Señal EOG")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (mV)")
plt.grid()
plt.show()

# TRANSFORMADA DE FOURIER

# N para normalizar la FFT
X = np.fft.fft(senal_filtrada) / N

# Obtener vector de frecuencias
frecuencias = np.fft.fftfreq(N, 1/FS)

# Solo frecuencias positivas
pos = frecuencias >= 0
frecuencias = frecuencias[pos]
X = X[pos]

# Magnitud del espectro
magnitud = np.abs(X)

plt.figure()
plt.plot(frecuencias, magnitud)
plt.title("Transformada de Fourier")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()
plt.show()

# DENSIDAD ESPECTRAL DE POTENCIA

PSD = (np.abs(X)**2)

plt.figure()
plt.plot(frecuencias, PSD)
plt.title("Densidad Espectral de Potencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Potencia")
plt.grid()
plt.show()

# ESTADÍSTICOS EN FRECUENCIA

# Frecuencia media ponderada por potencia       
f_media = np.sum(frecuencias * PSD) / np.sum(PSD) 

# Suma acumulada de la potencia
cumsum = np.cumsum(PSD) 

# Frecuencia mediana
f_mediana = frecuencias[np.where(cumsum >= cumsum[-1]/2)[0][0]]  

# Desviación estándar ponderada por potencia
f_std = np.sqrt(np.sum(((frecuencias - f_media)**2) * PSD) / np.sum(PSD))

print("\n***ESTADÍSTICOS EN FRECUENCIA***")
print("Frecuencia media:", f_media)
print("Frecuencia mediana:", f_mediana)
print("Desviación estándar frecuencia:", f_std)