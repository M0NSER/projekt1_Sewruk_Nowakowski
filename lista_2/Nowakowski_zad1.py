def fun(lista1, lista2):
    lista3=[]
    if len(lista1)> len(lista2):
        for i in range(0,len(lista2),2):
            lista3.append(lista1[i+1])
            lista3.append(lista2[i])
        for a in range(len(lista2)+1,len(lista1),2):
            lista3.append(lista1[i])
    elif len(lista1)< len(lista2):
        for i in range(0, len(lista1), 2):
            lista3.append(lista1[i])
            lista3.append(lista2[i+1])
        for a in range(len(lista1) + 1, len(lista2), 2):
            lista3.append(lista2[i])
    else:
        for i in range(1, len(lista1), 2):
            lista3.append(lista1[i-1])
            lista3.append(lista2[i])
        lista3.append(lista1[len(lista3)])

    return lista3

lista1=[1,2,3,4,5]
lista2=[6,7,8,9,10]
lista3=fun(lista1,lista2)
print(lista3)