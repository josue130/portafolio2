def partirLista2(lista):
     if isinstance(lista,list):
          return PL_aux2(lista,[],[],[])
def PL_aux2(lista,sublista,resultado,negativos):
     if lista==[]:
          return resultado + [sublista] + [negativos]
     elif lista[0]>=0:
          return PL_aux2(lista[1:],sublista+[lista[0]],resultado,negativos)
     else:
          return PL_aux2(lista[1:],[],resultado+[sublista],negativos + [lista[0]])
          
