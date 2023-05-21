from valoresentrada import *
from cartaplasticidad import *
from granulometria import *

def clasificacion():
  if T200>50: #se usa la funcion if para conocer si el porcentaje es mayor o menor  al 50%
      print("Es un suelo de tipo Grueso") #se clasifica el suelo como suelo Grueso
      #se ingresa el porcentaje que pasa por el tamiz #4     
      if T4>50: # Se clasifican como Grava
        if T200<5: # porcentaje menor al 5%, se clasifica como Gravas limpias
          if Cu>=4 and (Cc<3 or Cc>1):#se clasifica usando valores de cc y cu
            print("GW (Grava bien graduada)")#se imprime  el tipo de suelo
          elif Cu<4 and (Cc>3 or Cc<1):#se clasifica usando valores de cc y cu
            print("GP (Grava mal graduada)")#se imprime  el tipo de suelo
          else:
            print("No aplica a la clasificacion")#se imprime que no entra en la clasificacion         
        elif T200>12: #porcenetaje mayor al 12%, se clasifican como Gravas con finos
          if  IP>7:#se clasifica usando el IP
            print("GC (Grava Arcillosa)")#se imprime  el tipo de suelo
          elif IP<4:#se clasifica usando el IP
            print("GM (Grava limosa)")#se imprime  el tipo de suelo
          else:
            print("No aplica a la clasificacion")#se imprime que no entra en la clasificacion 
        else: # porcentaje de finos entre 5% y 12, se clasifica como gravas limpias y con finos 
          if Cu>=4 and (Cc>=1 and Cc<=3):
            if IP<4:#se clasifica usando el IP
              print("GW-GM (Grava bien graduada con limo)")#se imprime  el tipo de suelo
          elif Cu>=4 and (Cc>=1 and Cc<=3):
            if IP>7:#se clasifica usando el IP
              print("GW-GC (Grava bien graduada con arcilla)")#se imprime  el tipo de suelo
          else:
            print("No aplica a la clasificacion")#se imprime que no entra en la clasificacion
          if Cu<4 and (Cc<1 and Cc>3):
            if IP<4:#se clasifica usando el IP
              print("GP-GM (Grava mal graduada con limo)")#se imprime  el tipo de suelo
            else:
              if IP>7:#se clasifica usando el IP
                print("GP-GC (Grava mal graduada con arcilla)")#se imprime  el tipo de suelo                                 
      else: #se calsifican como arenas
        if T200<5:
          if Cu>=6 and 1<=Cc <=3:
            print("SW (Arena bien graduada)")#se imprime  el tipo de suelo
          elif Cu<6 and (1>Cc or Cc>3):
            print("SP (Arena mal graduada)")#se imprime  el tipo de suelo
          else:
            print("No aplica a la calsificacion")#se imprime que no entra en la clasificacion
        elif T200>12:
          if IP<4:#se clasifica usando el IP
            print("SM (Arena limosa)")#se imprime  el tipo de suelo
          elif IP>7:#se clasifica usando el IP
            print("SC (Arena arcillosa)")#se imprime  el tipo de suelo
          else:
            print("No aplica a ninguna clasificacion") #se imprime que no entra en la clasificacion
        else:
          if (Cu>=6 and 1<=Cc <=3):
            if IP<4:#se clasifica usando el IP
              print("SW_SM (Arena bien graduada con limo)")#se imprime  el tipo de suelo
            elif IP>7:#se clasifica usando el IP
              print("SW_SC (Arena bien graduada con arcilla)")#se imprime  el tipo de suelo
            else:
              print("No aplica a la clasificacion")#se imprime que no entra en la clasificacion
          elif Cu<6 and (1>Cc or Cc>3):
            if IP<4:#se clasifica usando el IP
              print("SP_SM (Arena mal graduada con limo)")#se imprime  el tipo de suelo
            elif IP>7:#se clasifica usando el IP
              print("SP_SC (Arena mal graduada con arcilla)") #se imprime  el tipo de suelo
            else:
              print("No aplica a la clasfificacion")#se imprime que no entra en la clasificacion
          else:
            print("No aplica a la clasificacion")#se imprime que no entra en la clasificacion                
  else:  
    print("Se clasifican como finos")#se clasifica el suelo como finos
    cartaplasticidad()
    