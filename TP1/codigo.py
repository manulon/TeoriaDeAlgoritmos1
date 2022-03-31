'''
    Sea P un set de datos
	Sea A el conjunto final
	
	Ordenar P por lugar de inicio de cobertura

	Mientras P no este vacío
		Sea i el pedido en P con menor lugar de inicio de cobertura
		Agrego i a la lista A
		Quito de P todas las antenas solapadas con i
		Si el primer elemento de P tiene un lugar de inicio mayor al ultimo punto cubierto 	por el ultimo 
        elemento de la lista A
			retornar que no se puede cubrir toda la ruta
	retornar que se puede conectar toda la ruta y las antenas que deben conectarse
'''
import sys

def criterioOrdenamiento(setDeDatos):
  return (int(setDeDatos[2]) - int(setDeDatos[1]))

def quitarSolapadas(setDeDatos):
  for i in range(0,len(setDeDatos)-1):
      print(i)

def intervalSchedulingAdaptado(file):
    setDeDatos = []
    conjuntoFinal = []

    with open(file) as archivo:
        for linea in archivo:
            setDeDatos.append(linea.split()[0].split(','))            

    setDeDatos.sort(reverse=True, key=criterioOrdenamiento)

    while len(setDeDatos) != 0:
        conjuntoFinal.append(setDeDatos[0])
        setDeDatos = quitarSolapadas(setDeDatos)
    

intervalSchedulingAdaptado("contratos.txt")

