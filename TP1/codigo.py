import sys

def criterioOrdenamiento(setDeDatos):
    return (int(setDeDatos[2]) - int(setDeDatos[1]))

def quitarSolapadas(setDeDatos):
    inicioPrimeroLista = int(setDeDatos[0][1]) - int(setDeDatos[0][2])
    if inicioPrimeroLista < 0:
        inicioPrimeroLista = 0
    finalPrimeroLista  = int(setDeDatos[0][1]) + int(setDeDatos[0][2])
    numerosAEliminar = []
    for i in range(1,len(setDeDatos)):
        inicioEvaluadoActual = int(setDeDatos[i][1]) - int(setDeDatos[i][2])
        if inicioEvaluadoActual < 0:
            inicioEvaluadoActual = 0
        finalEvaluadoActual  = int(setDeDatos[i][1]) + int(setDeDatos[i][2]) 
        if ((inicioPrimeroLista <= inicioEvaluadoActual) & (finalPrimeroLista >= finalEvaluadoActual)):
          numerosAEliminar.append(i)

    numerosAEliminar.sort(reverse=True)
    
    for i in range(0,len(numerosAEliminar)):
        setDeDatos.pop(numerosAEliminar[i])
    
    return setDeDatos
    
def intervalSchedulingAdaptado(file, k):    
    setDeDatos = []
    conjuntoFinal = []
    kmCubiertos = 0

    with open(file) as archivo:
        for linea in archivo:
            setDeDatos.append(linea.split()[0].split(','))            
   
    setDeDatos.sort(reverse=True, key=criterioOrdenamiento)
        
    while ( (len(setDeDatos) != 0) and (kmCubiertos != int(k)) ) :
        conjuntoFinal.append(setDeDatos[0])
        setDeDatos = quitarSolapadas(setDeDatos)
        setDeDatos.pop(0)

        inicioUltimoLista = int(conjuntoFinal[-1][1]) - int(conjuntoFinal[-1][2])
        finalUltimoLista  = int(conjuntoFinal[-1][1]) + int(conjuntoFinal[-1][2])
        if finalUltimoLista > int(k):
            finalUltimoLista = int(k)
        if inicioUltimoLista > kmCubiertos:
            print('No es posible cubrir toda la ruta con las propuestas existentes ')
            return -1
        kmCubiertos += (finalUltimoLista - kmCubiertos)

    if kmCubiertos < int(k):
        print('No es posible cubrir toda la ruta con las propuestas existentes, solamente se pudieron cubrir ', kmCubiertos,' kilometros.')
        return -1
    else:
        print('Se puede cubrir la ruta completa. Las propuestas seleccionadas son:', end=" ")
        for i in range(0,len(conjuntoFinal)):
            print(conjuntoFinal[i][0], end=" ")
        print('\nSe cubriran ', kmCubiertos, ' kilometros.')
        return 0
       
intervalSchedulingAdaptado("contratos.txt", sys.argv[1])

