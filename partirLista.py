def partirLista(lista):
     if isinstance(lista,list):
          return PL_aux(lista,[],[])
def PL_aux(lista,sublista,resultado):
     if lista==[]:
          return resultado + [sublista]
     elif lista[0]>=0:
          return PL_aux(lista[1:],sublista+[lista[0]],resultado)
     else:
          return PL_aux(lista[1:],[],resultado+[sublista])
