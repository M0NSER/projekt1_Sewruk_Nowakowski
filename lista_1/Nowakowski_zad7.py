lista=[]
for i in range(1,11):
    lista.append(i)
lista2=lista[5:]
lista=lista[:5]

lista+=lista2
lista.insert(0,0)
lista.sort(reverse=True)
