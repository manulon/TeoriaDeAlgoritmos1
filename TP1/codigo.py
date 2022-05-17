import sys



def buscarAntenaQueCubraEspacioDisponible(setDeDatos, conjuntoFinal, kmCubiertos):
    candidatoFinal = []
    seEncontroCandidato = False
    nuevosKmCubiertos = 0

    for i in range(0, len(setDeDatos)):
        comienzoCoberturaCandidato  = int(setDeDatos[i][1]) - int(setDeDatos[i][2])
        finalCoberturaCandidato     = int(setDeDatos[i][1]) + int(setDeDatos[i][2])
        
        if ((comienzoCoberturaCandidato <= kmCubiertos and finalCoberturaCandidato > kmCubiertos)):
            if (len(candidatoFinal) != 0):
                finalCoberturaCandidatoFinal = int(candidatoFinal[1]) + int(candidatoFinal[2])
                if (finalCoberturaCandidato >= finalCoberturaCandidatoFinal):
                    candidatoFinal = setDeDatos[i]
                    seEncontroCandidato = True
            else:
                candidatoFinal = setDeDatos[i]
                seEncontroCandidato = True
    
    if seEncontroCandidato:
        conjuntoFinal.append(candidatoFinal)
        nuevosKmCubiertos = int(candidatoFinal[1]) + int(candidatoFinal[2])

    return conjuntoFinal, seEncontroCandidato, nuevosKmCubiertos
        
        
def cobertura(file, k):    
    setDeDatos = []
    conjuntoFinal = []
    kmCubiertos = 0

    with open(file) as archivo:
        for linea in archivo:
            setDeDatos.append(linea.split()[0].split(','))            
        
    while (kmCubiertos < int(k)) :
        conjuntoFinal, seEncontroCandidato, nuevosKmCubiertos = buscarAntenaQueCubraEspacioDisponible \
                                                                (setDeDatos, conjuntoFinal, kmCubiertos)
        if seEncontroCandidato:
            kmCubiertos = nuevosKmCubiertos 
        else:
            print('No es posible cubrir toda la ruta, solamente se pudieron cubrir', kmCubiertos, \
                  'kilometros.')       
            return -1

    print('Se puede cubrir la ruta completa. Las propuestas seleccionadas son:', end=" ")
    for i in range(0,len(conjuntoFinal)):
        print(conjuntoFinal[i][0], end=" ")
    print('\nSe cubriran', k, 'kilometros.')
    
    return 0
       
cobertura("contratos.txt", sys.argv[1])