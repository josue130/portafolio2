def intercambio_columnas_impares(m):
     if largo(m)==largo(m[0]):
          mitad=largo(m[0])
          return aux(m,0,0,mitad)

def aux(m,fila,columna,mitad):
     if fila==mitad:
          return m
     elif columna==largo(m[0]):
          return aux(m,fila+1,0,mitad)
     elif columna%2!=0:
          tempo=m[fila+mitad][columna]
          m[fila+mitad][columna]=m[fila][columna]
          m[fila][columna]=tempo
          return aux(m,fila,columna+1,mitad)
     else:
          return aux(m,fila,columna+1,mitad)
