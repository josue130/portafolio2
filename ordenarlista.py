def ordenar_lista(lista):
     if isinstance(lista,list):
          return aux_ordenar(lista,len(lista)-1,0,False)
def aux_ordenar(lista,largo,cont,ordenado):
     if ordenado and cont==largo:
          return lista
     else:
          if cont==largo:
               return aux_ordenar(lista,largo,0,True)
          else:
               if (lista[cont])<=(lista[cont+1]):
                    return aux_ordenar(lista,largo,cont+1,ordenado)
               else:
                    tempo=lista[cont]
                    lista[cont]=lista[cont+1]
                    lista[cont+1]=tempo
                    ordenado=False
                    return aux_ordenar(lista,largo,cont+1,ordenado)
