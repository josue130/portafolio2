def principal(lista1,lista2):
     if isinstance(lista1,list) and isinstance(lista2,list):
          return principal_aux(lista1,lista2,[],[],[])
def principal_aux(lista1,lista2,pares,impares,res):
     if lista1 and lista2==[]:
          return res + [ordenar_lista([pares])] + [ordenar_lista([impares])]
     else:
          if lista1[0]%2==0 and lista2[0]%2==0:
               return principal_aux(lista1[1:],lista2[1:],pares + [lista1[0]]+[lista2[0]],impares,res)
          if lista1[0]%2!=0 and lista2[0]%2!=0:
               return principal_aux(lista1[1:],lista2[1:],pares,impares + [lista1[0]]+[lista2[0]],res)
          if lista1[0]%2!=0 and lista2[0]%2==0:
               return principal_aux(lista1[1:],lista2[1:],pares+ [lista2[0]],impares +[lista1[0]],res)
          else:
               return principal_aux(lista1[1:],lista2[1:],pares+ [lista1[0]],impares +[lista2[0]],res)
