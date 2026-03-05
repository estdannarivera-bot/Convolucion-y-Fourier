# Laboratorio 2  
## Convolución, correlación y transformada de Fourier

**Programa:** Ingeniería Biomédica  
**Asignatura:** Procesamiento Digital de Señales  
**Universidad:** Universidad Militar Nueva Granada  
**Estudiantes:** Danna Rivera, Duvan Paez

---
# Introducción
En el procesamiento digital de señales, herramientas matemáticas como la convolución, la correlación y la Transformada de Fourier permiten analizar, caracterizar y comparar señales discretas.

-La convolución describe la respuesta de un sistema ante una señal de entrada.

-La correlación cruzada mide el grado de similitud entre dos señales.

-La Transformada de Fourier permite analizar una señal en el dominio de la frecuencia, identificando sus componentes espectrales.

Estas técnicas son ampliamente utilizadas en el análisis de señales biomédicas, procesamiento de audio, imágenes y sistemas de comunicación.
## Parte A
**Definición de señales**
Se definieron dos secuencias discretas basadas en datos personales:

Sistema:
`h[n] = {5,6,0,0,9,3,8}`

Señal de entrada:
`x[n]={1,0,2,8,4,8,4,0,3,4}`

La convolución entre ambas señales se define como:
`y[n]=x[n]∗h[n]`

**Implementación en Python:**

Se utilizó la función `numpy.convolve()` para calcular la convolución de manera automática.

El código realiza:

1. Definición de las secuencias discretas.

2. Cálculo de la convolución.

3. Visualización gráfica del resultado.

```python
y = np.convolve(x, h)
```
**Resultado:**
El resultado de la convolución corresponde a una nueva secuencia cuya longitud es:

`Ny​ = Nx​+Nh​−1`

Esta señal representa la respuesta del sistema `h[n]` cuando se aplica la señal `x[n]` como entrada.
La gráfica generada mediante `matplotlib` permite visualizar la amplitud de cada muestra de la señal resultante.


