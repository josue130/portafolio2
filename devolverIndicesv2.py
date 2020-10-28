#E:Recibe dos parametros de entrada
#R:Los parametros tiene que ser listas
#S:Si las listas tienen similitudes se retornan los indices donde estan estas
def devolverIndices2(lista1,encontrar):
     if isinstance(lista1,list) and isinstance(encontrar,list):
          return DI_aux2(lista1,0,encontar,[])
def DI_aux2(lista1,pos,encontrar,res):
     if encotrar==[]:
          return res
     else:
          if lista[pos:]==[]:
               return DI_aux2(lista,0,encontrar[1:],res)
          else:
               if lista[pos]==encontrar[0]:
                    return DI_aux2(lista,pos+1,encontrar,res + [pos])
               else:
                    return DI_aux2(lista,pos+1,encontrar,res)
