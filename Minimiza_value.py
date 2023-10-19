cantidad_N,cantidad_G = list(map(int,input().split()))

def lista_numeros(item):
    resultados=[]
    valor_E = int(item/9)
    valor_D = int((((item/9)-valor_E)*10))
    for i in range (0,valor_E):
        resultados.append(1)
        resultados.append(2)
        resultados.append(3)
        resultados.append(4)
        resultados.append(5)
        resultados.append(6)
        resultados.append(7)
        resultados.append(8)
        resultados.append(9)
    

    for i in range (1,valor_D+1):
        resultados.append(i)
    return resultados

lista_N=lista_numeros(cantidad_N)

def buscar_Mayor_Caso(lista,cantidad,numeros):
    lista.sort()
    Union=[]
    x = 0
    S=True
    for i in range(0,numeros):
        Union.append( [lista[i]])
    for i in range(0,numeros):
        lista.pop(0)
    x+=1
    while(x<round(cantidad/numeros)):
        if(x+1 == round(cantidad/numeros)):
            lista.sort(reverse=True)
        for i in range(0,numeros):
            Union[i].append( lista[i])
        for i in range(0,numeros):
            lista.pop(0)
        x+=1
        lista.sort(reverse=False)
    
    respuesta =['']
    Union.sort(reverse=True)
    for i in range(numeros):
        for j in Union[i]:
            respuesta[0]= str(respuesta[0])+ str(j)
        break
        
        
            

    print(respuesta[0])



buscar_Mayor_Caso(lista_N,cantidad_N,cantidad_G)      
