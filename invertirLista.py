def invertirlista(lista):
     if isinstance(lista,list):
          return invertir_aux(lista,[])
     else:
          print("Error en el parametro de entrada")
def invertir_aux(lista,nueva):
     if lista==[]:
          return (nueva)
     else:
          if lista[-1]!=[]:
               return [lista[-1]] + nueva  + invertir_aux(lista[:-1],nueva)
