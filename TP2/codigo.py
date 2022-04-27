INFINITO = float('inf')
import sys

def main():
    resultado = encontrar_ciclo_negativo(sys.argv[1], int(sys.argv[2]))
    print(resultado)

def parsearGrafo(tramos):
    grafo = {}
    nodos = []
    recorridos = {}
    for t in tramos:
        data = t.split()[0].split(',')
        if data[0] not in nodos:
            nodos.append(data[0])
            recorridos[data[0]] = ''
        if len(data) == 1:
            grafo['s'] = data[0]
        elif len(data) == 3:
            grafo[data[0]+data[1]] = int(data[2])
            if data[1] not in nodos:
                nodos.append(data[1])
                recorridos[data[1]] = ''
    return grafo, nodos, recorridos

def encontrar_ciclo_negativo(fileName, n):
    l, v = (n, n)
    OPT = [[0 for i in range(l)] for j in range(v + 1)] 
    for l in range(n + 1):
        for v in range(1, n):
            OPT[l][v] = INFINITO 

    f = open(fileName, 'r')
    lines = f.readlines()
    grafo, nodos, recorridos = parsearGrafo(lines)
    f.close()

    for l in range(0, n + 1):
        for v in range(1, n):
            OPT[l][v] = OPT[l-1][v]
            for p in range(len(nodos)):
                if OPT[l][v] > OPT[l-1][p] + w(p,v, grafo, nodos):
                    OPT[l][v] = OPT[l-1][p] + w(p,v, grafo, nodos)
                    recorridos[nodos[p]] =  nodos[v]
                    if l == n:
                        return imprimir_ciclo_negativo(recorridos, nodos[p], grafo)
                        
    return "No existen ciclos negativos en el grafo"

def imprimir_ciclo_negativo(recorridos, nodo_i, grafo):
    nodo_f = ''
    ciclo = ''
    nodo_anterior = nodo_i
    costo = 0
    while(nodo_f != nodo_i):
        ciclo += recorridos[nodo_anterior]
        costo += grafo[nodo_anterior + recorridos[nodo_anterior]]
        nodo_anterior = recorridos[nodo_anterior]
        nodo_f = nodo_anterior
    return "Existe al menos un ciclo negativo en el grafo. {} -> costo: {} ".format(ciclo, costo)

def w(p,v, grafo, nodos):
    tramo = nodos[p] + nodos[v]
    try:
        return grafo[tramo]
    except KeyError:
        return INFINITO

main()
