# -*- coding: utf-8 -*-
#!/usr/bin/python2
import sys
import time
import timeit

def acha_o_maior(j):
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

def par_proibido(item,mochila):
    achou = False
    global duplas
    for i in range(0,len(duplas)):
        if duplas[i] ==item:
            if(i%2==0):
                for j in range(0,len(mochila)):
                    if mochila[j]== duplas[i+1]:
                        achou =True
            else:
                for j in range(0,len(mochila)):
                    if mochila[j]== duplas[i-1]:
                        achou =True
    return achou

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
        if (par_proibido(item,mochila)):
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

def branch_create(lista):
    global nos,integros,limitados,inviaveis
    nos=nos+1
    mochila=list()
    mochila = create_mochila(lista)
    if mochila == -1:
        inviaveis=inviaveis+1
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
        item = acha_o_maior(j)
        j = j+1
        while(itensmochila(item,mochila,lista) or valores_itens[item-1]>c and item!= -1):
            item = acha_o_maior(j)
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
        integros=integros+1
        return limitador
    if maximo[0] < limitador[0] and not branch:
        limitados=limitados+1
        return limitador
    if(item == -1):
        if limitador[0] < maximo[0]:
           limitador = list(maximo)
        integros=integros+1
        return maximo
    if(branch):
       if limitador[0]>= maximo[0]:
           limitados=limitados+1
           return limitador
       a = branch_create(branch_fix1)
       b = branch_create(branch_fix0)
       if a>b:
           integros= integros+1
           return a
       else:
           integros= integros+1
           return b

# tratamento de entradas
n,m,c = map(int, sys.stdin.readline().split())
valores_itens = map(int, sys.stdin.readline().split())
pesos = map(int, sys.stdin.readline().split())
duplas = map(int, sys.stdin.read().split())
lista_escolhidos = list()
limitador = [0]
item = [0]*2
nos = 0
integros = 0
inviaveis = 0
limitados = 0 

for i in range(0,n):
    item[0]= pesos[i]/float(valores_itens[i])
    item[1]= i+1
    lista_escolhidos.append(item[:])

ordenado1 = sorted(lista_escolhidos, key= lambda item : item[0],reverse=True)
ini = timeit.default_timer()
bolsa_final = branch_create([0]*n)
fim = timeit.default_timer()

print(bolsa_final[0])
tempo_total = fim-ini
#tratamento da saida
if bolsa_final[0]>0:
    bolsa_final[1] = sorted(bolsa_final[1])

saida= str()
if len(bolsa_final)>1:
    for itens in bolsa_final[1]:
        saida = saida+str(itens)+" "
print(saida)
#erro com numero de nos e o tempo de execuvao
erro=str()
erro="numero de nos :"+ str(nos)+"\n"+"tempo total de execução: "+str(tempo_total)
sys.stderr.write(erro)
print >> sys.stderr, "Error Detected!"