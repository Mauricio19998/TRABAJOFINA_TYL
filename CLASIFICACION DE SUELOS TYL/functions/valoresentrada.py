import pandas as pd
import numpy as np

tamiz = pd.Series(['1 1/2"','1"','3/4"','3/8"','No.4','No.10','No.20','No.40','No.60','No.100','No.200'])

abertura = [
    37.5,   # abertura tamiz 1 1/2"
    25.4,   # abertura tamiz 1"
    19,     # abertura tamiz 3/4"
    9.51,   # abertura tamiz 3/8"
    4.76,   # abertura tamiz No.4
    2,      # abertura tamiz No.10
    0.841,  # abertura tamiz No.20
    0.420,  # abertura tamiz No.40
    0.250,  # abertura tamiz No.60
    0.149,  # abertura tamiz No.100
    0.074   # abertura tamiz No.200
]

retenido = [
    100,    # porcentaje de partículas que pasan por el tamiz 1 1/2"
    90,     # porcentaje de partículas que pasan por el tamiz 1"
    80,     # porcentaje de partículas que pasan por el tamiz 3/4"
    76.5,   # porcentaje de partículas que pasan por el tamiz 3/8"
    69,     # porcentaje de partículas que pasan por el tamiz No.4
    60.5,   # porcentaje de partículas que pasan por el tamiz No.10
    52,     # porcentaje de partículas que pasan por el tamiz No.20
    38.4,   # porcentaje de partículas que pasan por el tamiz No.40
    23,     # porcentaje de partículas que pasan por el tamiz No.60
    5,      # porcentaje de partículas que pasan por el tamiz No.100
    78      # porcentaje de partículas que pasan por el tamiz No.200
]

peso_total = sum(retenido)
porcentaje_retenido = [(r / peso_total) * 100 for r in retenido]
acumulado = [porcentaje_retenido[0]]
pasa = [100 - valor for valor in acumulado]
for i in range(1, 11):
    acumulado.append(acumulado[i - 1] + porcentaje_retenido[i])
    pasa.append(100 - acumulado[i])

Estructura = pd.DataFrame({
    'Tamiz': tamiz,
    'Abertura (mm)': abertura,
    'Retenido (g)': retenido,
    '% Retenido': porcentaje_retenido,
    '% Acumulado': acumulado,
    '% Pasa': pasa
})

print(Estructura)
