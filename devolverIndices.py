#E:Recibe dos parametros de entrada
#R:Los parametros tiene que ser listas
#S:Si las listas tienen similitudes se retornan los indices donde estan estas
def devolverIndices(lista1,encontrar):
     if isinstance(lista1,list) and isinstance(encontrar,list):
          return DI_aux(lista1,encontrar,[],0)
def DI_aux(lista1,encontrar,resultado,cont):
     if lista1==[] and encontrar==[]:
          return resultado
     if lista1[0]==encontrar[0]:
          return DI_aux(lista1[1:],encontrar[1:],resultado+[cont],cont+1)
     else:
          return DI_aux(lista1[1:],encontrar,resultado,cont+1)
