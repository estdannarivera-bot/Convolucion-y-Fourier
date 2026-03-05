# Laboratorio 2  
## Convolución, correlación y transformada de Fourier

**Programa:** Ingeniería Biomédica  
**Asignatura:** Procesamiento Digital de Señales  
**Universidad:** Universidad Militar Nueva Granada  
**Estudiantes:** Danna Rivera, Duvan Paez

---
![ALGORITMO](ALGORITMO.png)

# Introducción
En el procesamiento digital de señales, herramientas matemáticas como la convolución, la correlación y la Transformada de Fourier permiten analizar, caracterizar y comparar señales discretas.

-La convolución describe la respuesta de un sistema ante una señal de entrada.

-La correlación cruzada mide el grado de similitud entre dos señales.

-La Transformada de Fourier permite analizar una señal en el dominio de la frecuencia, identificando sus componentes espectrales.

Estas técnicas son ampliamente utilizadas en el análisis de señales biomédicas, procesamiento de audio, imágenes y sistemas de comunicación.

## Parte A – Convolución de Señales Discretas
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
Las gráficas generada mediante `matplotlib` permite visualizar la amplitud de cada muestra de la señal resultante.


*Estudinate 1:*

![CONVOLUCIÓN](Convolucion.png)

*Estudiante 2:*


---
## Parte B – Correlación Cruzada
**Definición de señales**

Se definieron dos señales sinusoidales discretas:

`x₁[nTₛ] = cos(2π · 100 · nTₛ)`

`x₂[nTₛ] = sin(2π · 100 · nTₛ)`

donde: 
`Tₛ=1.25ms`
y:
`0≤n<9`


**Implementación en Python**

La correlación cruzada se calculó utilizando:

```python
r = np.correlate(x1, x2, mode='full')
```

El parámetro `mode='full'` permite obtener todos los retardos posibles entre ambas señales.
También se calculó el vector de retardos:

```python
lags = np.arange(-len(x1)+1, len(x1))
```
**Interpretación**

La correlación cruzada permite medir el grado de similitud entre dos señales dependiendo de su desfase temporal. En este caso, las señales seno y coseno tienen un desfase de 90°, por lo tanto, la correlación presenta valores característicos que reflejan ese desplazamiento entre ambas señales.

Esta técnica se utiliza en:

detección de patrones, sincronización de señales, análisis de señales biomédicas, procesamiento de imágenes

**Resultados**

![CORRELACION CRUZADA](CorrelacionCruzada.png)

**¿En qué situaciones resulta útil aplicar la correlación cruzada en el procesamiento digital de señales?**


En el procesamiento digital de señales, la correlación cruzada resulta útil cuando se desea medir el grado de similitud entre dos señales y determinar el desfase temporal entre ellas. Esta herramienta permite identificar si dos señales tienen patrones similares y en qué momento una señal coincide con la otra.

En aplicaciones prácticas, la correlación cruzada se utiliza en detección de patrones, sincronización de señales, localización de eventos en señales biomédicas, y procesamiento de audio o comunicaciones. Por ejemplo, en señales biomédicas como EEG o EOG, permite comparar señales registradas en distintos momentos o sensores para identificar actividad similar o retrasos entre ellas. También es útil para detectar la presencia de una señal conocida dentro de otra señal con ruido, facilitando el análisis y la interpretación de datos.

---
## Parte C – Análisis de Señal Biológica


