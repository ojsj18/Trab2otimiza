# -*- coding: utf-8 -*-
#!/usr/bin/python2
import sys

def acha_o_maior(mochila,j):
    global ordenado1
    if j>= len(ordenado1):
        return -1

    maior = ordenado1[j][1]
    return maior

def maximizador(lista):
    #recebe a lista e calcula a função de maximização, acho que usar a global vai dar boa
    global pesos
    soma=0
    for i in range (0,len(lista)):
        soma = soma + pesos[i]*lista[i]
    return soma

def achaproibido(item):
    global duplas
    for i in range(0,len(duplas),2):
        if duplas[i]==item:
                return duplas[i+1]
    return 0

def itensmochila(item,mochila,lista):
    global c
    global lista_escolhidos
    global valores_itens
    n = 0
    if item == -1:
        return False
    for i in range(0,len(mochila)):
        if item == mochila[i]:
            return True
        if lista[item-1] == 3:
            return True
        if valores_itens[item-1]>c:
            return True 
        if (lista_escolhidos[mochila[i]-1][2] == item) or (mochila[i] == lista_escolhidos[item-1][2]):
            return True
    return False

def tamanho_mochila(mochila):
    global valores_itens
    n = 0
    for i in range(0,len(mochila)):
        n = n+valores_itens[mochila[i]-1]
    return n

def create_mochila(lista):
    mochila = list()
    global valores_itens
    global c
    j=0
    for i in range(0,len(lista)):
        if lista[i] == 2:
            if(itensmochila(i+1,mochila,lista)):
                return -1
            mochila.append(i+1)
            j = j+ valores_itens[i]
    if j > c:
        return-1
        
    return mochila

def create_results(mochila):
    global n
    result = [0]*n
    for i in range(0,len(mochila)):
        result[mochila[i]-1]=1

    return result

def branch_create(lista,maior,z):
    z=z+1

    mochila = create_mochila(lista)
    if mochila == -1:
        return -1
    i = tamanho_mochila(mochila)
    result = create_results(mochila)
    
    global valores_itens,limitador
    global c,n
    
    j = 0
    item = 0
    branch = False
    maximo = list()
    
    while True:
        item = acha_o_maior(mochila,j)
        j = j+1
        while(itensmochila(item,mochila,lista) or valores_itens[item-1]>c and item!= -1):
            item = acha_o_maior(mochila,j)
            j=j+1
        if item == -1:
                break
        if i==c:
            break
        if i+valores_itens[item-1]>c:
            branch = True
            branch_fix1 = list(lista)
            branch_fix1[item-1]= 2
            branch_fix0 = list(lista)
            branch_fix0[item-1]= 3
            result[item-1] = (c-i)/float(valores_itens[item-1])
            mochila.append(item)
            break
        if i+valores_itens[item-1]<=c :
            mochila.append(item)
            i = i+valores_itens[item-1]
            result[item-1]=1
            
    maximo.append(maximizador(result))
    maximo.append(mochila)

    if(i==c):
        if limitador[0] < maximo[0]:
           limitador = list(maximo)
        return limitador
    if maximo[0] <= limitador[0] and not branch:
        return limitador
    if(item == -1):
        if limitador[0] < maximo[0]:
           limitador = list(maximo)
        return maximo
    if(branch):
       if limitador[0]>= maximo[0]:
           return limitador
       a = branch_create(branch_fix1,maximo,z)
       b = branch_create(branch_fix0,maximo,z)
       if a>b:
           return a
       else:
           return b

# tratamento de entradas
n,m,c = map(int, sys.stdin.readline().split())
valores_itens = map(int, sys.stdin.readline().split())
pesos = map(int, sys.stdin.readline().split())
duplas = map(int, sys.stdin.read().split())
lista_escolhidos = list()
limitador = [0]
item = [0]*3

for i in range(0,n):
    item[0]= pesos[i]/float(valores_itens[i])
    item[1]= i+1
    item[2]= achaproibido(i+1)
    lista_escolhidos.append(item[:])

ordenado1 = sorted(lista_escolhidos, key= lambda item : item[0],reverse=True)
bolsa_final = branch_create([0]*n,0,0)
print(bolsa_final[0])
if bolsa_final[0]>0:
    bolsa_final[1] = sorted(bolsa_final[1])

saida= str()
for itens in bolsa_final[1]:
    saida = saida+str(itens)+" "
print(saida)