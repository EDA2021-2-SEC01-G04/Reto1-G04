"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from DISClib.DataStructures.arraylist import size
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- ")
    print("5- crear una muestra")

def printTypeList():
    print("cual tipo de representación de la lista desea usar")
    print("1- ARRAY_LIST")
    print("2- LINKED_LIST")
def prinMenuList():
    print("cual de estos sort quiere usar")
    print("1- insertion")
    print("2- merges")
    print("4- quick")
    print("4- selection")


def initCatalog(type_list):
    return controller.initCatalog(type_list)

def loadData(catalog):
    controller.loadData(catalog)

def subList(catalog,muestra):

    controller.sortArworks(catalog,muestra)
def sortArtworksByAcquiringDate(catalog,num):
    controller.sortArtworksByAcquiringDate(catalog,num)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        printTypeList()
        type_list = int(input())
        print("Cargando información de los archivos ....")
        catalog = initCatalog(type_list)
        loadData(catalog)
        print("Numero de artistas: " + str(lt.size(catalog["artists"])))
        print("Numero de obras: "+ str(lt.size(catalog["artworks"])))
        print("Ultimos tres elementos de artistas" + str(controller.Last3Artists) + "y de las obras " + str(controller.Last3Artworks))
        print(str(lt.size(catalog["artworks"])))


    elif int(inputs[0]) == 2:
        printTypeList
        num = int(input())
        time = sortArtworksByAcquiringDate(catalog,num)
        print("El tiempo (mseg) es: " + str(round(time,3)))

    elif int(inputs[0]) == 5:
        muestra = int(input("ingrese el tamañano de la muestra\n"))
        result = subList(catalog,muestra)
        print("el tamaño de la lista ahora es de " + str(muestra) )

        
    
        


    else:
        sys.exit(0)
sys.exit(0)
