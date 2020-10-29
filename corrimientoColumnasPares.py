def corrimiento_Columnas_pares(matriz):
     if isinstance(matriz,list):
          return CCP_aux(matriz,0,0,1)
     else:
          return "Parametros de entrada incorrectos"
def CCP_aux(matriz,fila,columna,fila1):
     #print("Esta es la matriz",matriz)
     #print("Quiero probar esto~~>",matriz[fila][columna],"Estoy igualando a esto~~~>",matriz[fila1][columna])
     if fila1==len(matriz):
          return matriz
     if columna==len(matriz[0])-1:
          return CCP_aux(matriz,fila+1,0,fila1+1)
     if columna%2==0:
          print("Quiero probar esto~~>",matriz[fila1][columna],"Estoy igualando a esto~~~>",matriz[fila][columna])
          
          matriz[fila1][columna]=matriz[fila+1][columna]
          return CCP_aux(matriz,fila,columna + 1 ,fila1)
     else:
          return CCP_aux(matriz,fila ,columna + 1,fila1)
