INFINITO = float('inf')
import sys

def obtener_aristas(fileName):
    f = open(fileName, 'r')
    tramos = f.readlines()
    f.close()
    grafo = {}
    nodos = []
    for t in tramos:
        data = t.split()[0].split(',')
        if data[0] not in nodos:
            nodos.append(data[0])
        if len(data) == 1:
            grafo['origen'] = data[0]
        elif len(data) == 3:
            grafo[data[0] + data[1]] = int(data[2])
            if data[1] not in nodos:
                nodos.append(data[1])
    return grafo, nodos

def string_ciclo(ciclo):
    c = ""
    for i in ciclo:
        c += i
    cadena_invertida = ""
    for letra in c:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

def encontrar_ciclo_negativo(padre, costos, v, w):
    ciclo = [v]
    costo = 0
    while padre[v] != w:
        ciclo.append(padre[v])
        v = padre[v]
    ciclo.append(w)
    ciclo.append(ciclo[0])
    for i in range(len(ciclo)):
        if (i+1) > len(ciclo) - 1:
            ciclo.pop()
            return ciclo, costo
        tramo = ciclo[i] + ciclo[i+1]
        try: 
            costo += costos[tramo]
        except KeyError:
            tramo = ciclo[i+1] + ciclo[i]
            costo += costos[tramo]
    ciclo.pop()
    return ciclo, costo

def camino_minimo(aristas, nodos):
    dist = {}
    padre = {}
    for v in nodos:
        dist[v] = INFINITO
    origen = aristas.get('origen')
    dist[origen] = 0
    padre[origen] = None 
    for i in range(len(nodos)):
        for tramo, peso in aristas.items():
            if tramo != 'origen': 
                v = tramo[0]
                w = tramo[1]
                if dist[v] + peso < dist[w]:
                    padre[w] = v
                    dist[w] = dist[v] + peso 
    for tramo, peso in aristas.items():
        if tramo != 'origen': 
            v = tramo[0]
            w = tramo[1]
            if dist[v] + peso < dist[w]:
                ciclo, costo = encontrar_ciclo_negativo(padre, aristas, v, w)
                print("Existe al menos un ciclo negativo en el grafo. {} -> costo: {} ".format(string_ciclo(ciclo), costo))
                return None 
    print("No existen ciclos negativos en el grafo")
    return padre, dist

def main():
    grafo, nodos = obtener_aristas(sys.argv[1])
    camino_minimo(grafo, nodos)
    return 0

main()
