def listacapicua(lista):
     if isinstance(lista,list):
          return lista_c(lista,0,-1,0)
     else:
          print("Tiene que ser una lista")
def lista_c(lista,cont1,cont2,n):
     if largo(lista)< cont1 and cont2:
          return "Ya no hay mas elementos por comparar"
     else:
          #cont1 izq
          #cont2 der
          if lista[cont1]==lista[cont2]:
               return lista[cont1]*10**n + lista_c(lista,cont1+1,cont2-1,n+1)
          else:
               return False
