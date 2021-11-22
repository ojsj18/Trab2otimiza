# -*- coding: utf-8 -*-
import sys

def acha_o_maior(mochila,j):
    global ordenado1
    if j>= len(ordenado1):
        return -1

    maior = ordenado1[j][1]
    return maior

def maximador(lista):
    #recebe a lista e calcula a função de maximização, acho que usar a global vai dar boa
    global pesos
    print(lista)
    soma=0
    for i in range (0,len(lista)):
        soma = soma + pesos[i]*lista[i]
    print("maximo ",soma) 
    return soma

def achaproibido(item):
    global duplas
    for i in range(0,len(duplas),2):
        if duplas[i]==item:
                return duplas[i+1]
    return 0

def itensmochila(item,mochila,lista):
    global c
    global listinha
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
        if (listinha[mochila[i]-1][2] == item) or (mochila[i] == listinha[item-1][2]):
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
                print("inviavel")
                return -1
            mochila.append(i+1)
            j = j+ valores_itens[i]
    if j > c:
        print("inviavel")
        return-1
        
    return mochila

def create_results(mochila):
    global n
    result = [0]*n
    for i in range(0,len(mochila)):
        result[mochila[i]-1]=1

    return result

def branch_create(lista,maior):
    mochila = create_mochila(lista)
    if mochila == -1:
        return -1
    i = tamanho_mochila(mochila)
    print(i)
    global valores_itens
    global c,n,max1
    
    j = 0
    item = 0
    branch = False
    result = create_results(mochila)
    
    while True:
        item = acha_o_maior(mochila,j)
        j = j+1

        while(itensmochila(item,mochila,lista) or valores_itens[item-1]>c):
            item = acha_o_maior(mochila,j)
            j=j+1
        if item == -1:
            break
        if i==c:
            break
        if i+valores_itens[item-1]>c:
            print(i+valores_itens[item-1])
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
            
    maximo= maximador(result)
    if(i==c):
        print("integralidade")
        return maximo
    if maximo <=maior  and not branch:
        print("menor")
        return maior
    if(branch):
       print("ramifica")
       a = branch_create(branch_fix1,maximo)
       b = branch_create(branch_fix0,maximo)
       if a>b:
           return a
       else:
            return b
    if(item == -1):
        print("integralidade")
        return maximo


# tratamento de entradas
n,m,c = map(int, sys.stdin.readline().split())
valores_itens = map(int, sys.stdin.readline().split())
pesos = map(int, sys.stdin.readline().split())
duplas = map(int, sys.stdin.read().split())

#ordenando pelo valor relativo

listinha = list()
item = [0]*3
for i in range(0,n):
    item[0]= pesos[i]/float(valores_itens[i])
    item[1]= i+1
    item[2]= achaproibido(i+1)
    listinha.append(item[:])

ordenado1 = sorted(listinha, key= lambda item : item[0],reverse=True)
maximo = branch_create([0]*n,0)
print("resposta",maximo)