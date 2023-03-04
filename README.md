# 🌊 Hydraulic 🌊
Program to calculate channel hydraulic parameters 

___________________________________________
## ☀ ¿QUÉ HAY AQUÍ?

Programa para calcular los parámetros hidráulicos principales:

➥ Y normal
➥ Y crítico
➥ N equivalente
➥ Área mojada
➥ Espejo de agua
➥ Perímetro mojado
➥ Radio y diámetro hidráulico.

● Se realiza el cálculo para mediante las dimensiones de un canal circular.

▰ Se realiza el cálculo mediante las dimensiones de un canal trapezoidal. El canal trapezoidal se encuentra diseñado por el método tradicional, estandart, paso directo, runge kutta 4 y muskingum.

∘ Comportamiento de la onda cinemática para determinar la distribución del flujo como una función de la distancia x, y del tiempo t


___________________________________________

## ☂¿QUÉ SE DEBE INTALAR?  ⇣⇣
➥ Se recomienda utilizar la distribución de python de **Anaconda** 

	Desde la terminal
	➥ En caso de requerirlo crear un ambiente de conda 
		》conda activate  ➥se activa (base)
		》conda create name_ambiente
		》conda env list  ➥se muestran todos tus ambientes
		》conda activate name_ambiente

LIBRERÍAS QUE SE NECESITAN 

	tkinter: #Libreria para interfaz grafica.
		》conda install -c anaconda tk
		
	numpy:# se importa la libreria numpy o matematica.
		》conda install -c anaconda numpy
	
	math: #Libreria para calculo de los angulos 
		》conda install -c conda-forge python-markdown-math
	
	matplotlib: # libreria para graficar
		》conda install -c conda-forge matplotlib

	pandas: # para crear el data frame
		》conda install -c anaconda pandas

	turtle: #Para dibujar el canal
		》conda install -c r r-turtlegraphics

	io: # viene por defecto : sirve para herramientas para trabajar con E/S (entrada/salida) en Python. 
	Esta librería incluye clases para manejar archivos de texto y binarios, así como para trabajar 
	con flujos de datos de memoria, entre otros.
	Ejemplo : io.StringIO: Para trabajar con cadenas de caracteres como si fueran archivos de texto.
