#se importan las librerias
import pandas as pd
import numpy as np
import math 
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from valoresentrada import *
T200 = retenido[10]
T4 = retenido[4]
print("Porcentaje que pasa del tamiz 200:", T200)
print("Porcentaje que pasa del número 4:", T4)
# Calcula el Cu y Cc
d60 = retenido[6]  # Tamaño de partícula correspondiente al tamiz No. 40
d10 = retenido[9]  # Tamaño de partícula correspondiente al tamiz No. 200
d30 = retenido[8]  # Tamaño de partícula correspondiente al tamiz No. 60

Cu = d60 / d10
Cc = (d30 ** 2) / (d60 * d10)
#Se calculao los valores de LL(limite liquido) y de IP(indice de plasticidad) a partir del Cu y del Cc
LL= (Cu-17)/(0.5-0.1*Cc)
IP= LL-20

#se tabulan los límites superior e inferior máximo permitidos por el INVIAS
#limite superior
limite_superior_ejey = pd.Series([100,100,100,100,100,100,100,85,60,30,10])
limite_superior_ejex = pd.Series([25,19,12.5,9.5,6.6,4.75,2.36,1.18,0.6,0.3,0.15]) 

#limite inferior
limite_inferior_ejey = pd.Series([100,100,100,100,100,95,80,50,25,10,2])
limite_inferior_ejex = pd.Series([25,19,12.5,9.5,6.6,4.75,2.36,1.18,0.6,0.3,0.15])

#se crea la grafica granulometrica
plt.figure(figsize=(10, 3))  # Ajusta el tamaño de la figura

plt.scatter(limite_superior_ejex, limite_superior_ejey)
plt.plot(limite_superior_ejex, limite_superior_ejey, label="Límite superior")
plt.scatter(limite_inferior_ejex, limite_inferior_ejey, label="Límite inferior")
plt.plot(limite_inferior_ejex, limite_inferior_ejey, label="Límite inferior")
plt.scatter(abertura, retenido, label="granulometria")
plt.plot(abertura, retenido, label="granulometria")
plt.grid(color='grey', lw=0.5)
plt.xscale('log', base=10)
plt.gca().invert_xaxis()
plt.title("DISTRIBUCION GRANULOMETRICA", fontsize=15, color="black")  # se agrega el título a la gráfica granulométrica
plt.xlabel("Tamaño de partícula (mm)", fontsize=12)  # se agregan los títulos a los ejes
plt.ylabel("Porcentaje que pasa (%)", fontsize=12)  # se agregan los títulos a los ejes
plt.ylim(0, 110)  # Se establece el límite máximo del eje y
plt.annotate("Limite superior", (0.5, 65))  # se agregan los títulos
plt.annotate("Limite inferior", (4, 30))  # se agregan los títulos
rect = patches.Rectangle((0.05, 75), 0.06, 30, linewidth=1, edgecolor='black', facecolor='none')
plt.gca().add_patch(rect)
# Agrega los valores de Cu y Cc en la gráfica
plt.text(0.1, 80, f"Cu: {Cu:.2f}", fontsize=12, ha='left')
plt.text(0.1, 90, f"Cc: {Cc:.2f}", fontsize=12, ha='left')
plt.tight_layout()  # Ajusta el espaciado de la figura
plt.show()
# Imprime el Cu y Cc
print("Coeficiente de Uniformidad (Cu):", round(Cu, 2))
print("Coeficiente de Curvatura (Cc):", round(Cc, 2))