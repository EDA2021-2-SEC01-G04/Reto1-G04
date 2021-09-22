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
    print("Bienvenido, por favor introduzca la opcion que desea: ")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronologicamente los artistas")
    print("3- Listar cronologicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por tecnica")
    print("5- crear una muestra")

def printTypeList():
    print("cual tipo de representación de la lista desea usar")
    print("1- ARRAY_LIST")
    print("2- LINKED_LIST")
def countArtworksbyCountry(catalog):
    return controller.countArtworksbyCountry(catalog)
def top10country(countries):
    bst_cntry= countries[0]
    dct = countries[1]
    j = 0
    while j <= 10:
        j += 1
        for cntry in dct:
            if dct[cntry] ==  lt.getElement(bst_cntry,j) and j <= 10:
                print(cntry,lt.getElement(bst_cntry,j))

def dateArtists(date1,date2,catalog):
    return controller.dateArtists(date1,date2,catalog)

def dateArtworks(date1,date2,catalog):
    return controller.dateArtworks(date1,date2,catalog)

def artistsArtwork(pos,lst,catalog):
    return controller.artistsArtwork(pos,lst,catalog)


def initCatalog(type_list):
    
    return controller.initCatalog(type_list)

def loadData(catalog):
    controller.loadData(catalog)

def subList(catalog,muestra):
    controller.sortArworks(catalog,muestra)

def sortArtworksByAcquiringDate(catalog,num):
    count = controller.sortArtworksByAcquiringDate(catalog,num)
    return count[0]

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
        date_1 = input()
        date_2 = input()
        result = dateArtists(date_1,date_2,catalog)
        size = lt.size(result)
        print("Hay un total de " + str(size) + "entre los años " + date_1 + " y " + date_2)
        print("Los 3 primeros y ultimos artistas son: ")
        print("Nombre: " + lt.getElement(result,1)["DisplayName"],"Fecha de nacimiento: " + lt.getElement(result,1)["BeginDate"],"Fecha de muerte: "+ lt.getElement(result,1)["EndDate"],"Nacionalidad: "+ lt.getElement(result,1)["Nationality"],"Genero: "+ lt.getElement(result,1)["Gender"])            
        print("Nombre: " + lt.getElement(result,2)["DisplayName"],"Fecha de nacimiento: " + lt.getElement(result,2)["BeginDate"],"Fecha de muerte: "+ lt.getElement(result,2)["EndDate"],"Nacionalidad: "+ lt.getElement(result,2)["Nationality"],"Genero: "+ lt.getElement(result,2)["Gender"])
        print("Nombre: " + lt.getElement(result,3)["DisplayName"],"Fecha de nacimiento: " + lt.getElement(result,3)["BeginDate"],"Fecha de muerte: "+ lt.getElement(result,3)["EndDate"],"Nacionalidad: "+ lt.getElement(result,3)["Nationality"],"Genero: "+ lt.getElement(result,3)["Gender"])
        print("Nombre: " + lt.getElement(result,size-2)["DisplayName"],"Fecha de nacimiento: " + lt.getElement(result,size-2)["BeginDate"],"Fecha de muerte: "+ lt.getElement(result,size-2)["EndDate"],"Nacionalidad: "+ lt.getElement(result,size-2)["Nationality"],"Genero: "+ lt.getElement(result,size-2)["Gender"])
        print("Nombre: " + lt.getElement(result,size-1)["DisplayName"],"Fecha de nacimiento: " + lt.getElement(result,size-1)["BeginDate"],"Fecha de muerte: "+ lt.getElement(result,size-1)["EndDate"],"Nacionalidad: "+ lt.getElement(result,size-1)["Nationality"],"Genero: "+ lt.getElement(result,size-1)["Gender"])
        print("Nombre: " + lt.getElement(result,size)["DisplayName"],"Fecha de nacimiento: " + lt.getElement(result,size)["BeginDate"],"Fecha de muerte: "+ lt.getElement(result,size)["EndDate"],"Nacionalidad: "+ lt.getElement(result,size)["Nationality"],"Genero: "+ lt.getElement(result,size)["Gender"])
    elif int(inputs[0]) == 3:
        date_1 = input()
        date_2 = input()
        result = dateArtworks(date_1,date_2,catalog)
        lst = result[0]
        size = lt.size(result[0])
        contador = result[1]
        print("El MoMA adquirio "+ str(size) + " piezas unicas entre " + date_1 + " y " + date_2)
        print("El numero total de obras adquiridas por Purchase es: " + str(contador))
        print("Los primeros y ultimos 3 elmentos en el rango determinado son: ")
        print("Titulo: " + lt.getElement(lst,1)["Title"],"Artistas: " + artistsArtwork(1,lst,catalog),"Fecha: " + lt.getElement(lst,1)["DateAcquired"],"Medio: " + lt.getElement(lst,110)["Medium"],"Dimensiones: " + lt.getElement(lst,1)["Dimensions"])




    elif int(inputs[0]) == 4:
        result = countArtworksbyCountry(catalog)
        top10country(result)



    elif int(inputs[0]) == 5:
        muestra = int(input("ingrese el tamañano de la muestra\n"))
        result = controller.sortArtworksByAcquiringDate(catalog,num)
        print("el tamaño de la lista ahora es de " + str(muestra) )


        
    
        


    else:
        sys.exit(0)
sys.exit(0)
