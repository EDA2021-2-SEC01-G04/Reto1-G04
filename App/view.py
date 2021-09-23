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
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Obras por departamento")

def printTypeList():
    print("cual tipo de representación de la lista desea usar")
    print("1- ARRAY_LIST")
    print("2- LINKED_LIST")
def countArtworksbyCountry(catalog):
    return controller.countArtworksbyCountry(catalog)
    
def top10country(countries):
    bst_cntry= countries[2]
    num = countries[1]
    j = 1
    while j <= 10:
        print(lt.getElement(bst_cntry,j) +":  "+ str(lt.getElement(num,j)))
        j += 1

def dateArtists(date1,date2,catalog):
    return controller.dateArtists(date1,date2,catalog)

def dateArtworks(date1,date2,catalog):
    return controller.dateArtworks(date1,date2,catalog)

def artistsArtwork(pos,lst,catalog):
    return controller.artistsArtwork(pos,lst,catalog)

def artworksDepartment(catalog,depart):
    return controller.artworksDepartment(catalog,depart)

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
        print(str(lt.size(catalog["artworks"])))
        

    
    elif int(inputs[0]) == 2:
        date_1 = input("Introduzca el año desde del que quiere hacer el filtro: ")
        date_2 = input("Introduzca el año hasta donde quiere hacer el filtro: ")
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
        date_1 = input("Introduzca la fecha desde del que quiere hacer el filtro: ")
        date_2 = input("Introduzca la fecha hasta donde quiere hacer el filtro: ")
        result = dateArtworks(date_1,date_2,catalog)
        lst = result[0]
        size = lt.size(lst)
        contador = result[1]
        print("El MoMA adquirio "+ str(size) + " piezas unicas entre " + date_1 + " y " + date_2)
        print("El numero total de obras adquiridas por Purchase es: " + str(contador))
        print("Los primeros y ultimos 3 elmentos en el rango determinado son: ")
        print("Titulo: " + lt.getElement(lst,1)["Title"],"Artistas: " + artistsArtwork(1,lst,catalog),"Fecha: " + lt.getElement(lst,1)["DateAcquired"],"Medio: " + lt.getElement(lst,1)["Medium"],"Dimensiones: " + lt.getElement(lst,1)["Dimensions"])
        print("Titulo: " + lt.getElement(lst,2)["Title"],"Artistas: " + artistsArtwork(2,lst,catalog),"Fecha: " + lt.getElement(lst,2)["DateAcquired"],"Medio: " + lt.getElement(lst,2)["Medium"],"Dimensiones: " + lt.getElement(lst,2)["Dimensions"])
        print("Titulo: " + lt.getElement(lst,3)["Title"],"Artistas: " + artistsArtwork(3,lst,catalog),"Fecha: " + lt.getElement(lst,3)["DateAcquired"],"Medio: " + lt.getElement(lst,3)["Medium"],"Dimensiones: " + lt.getElement(lst,3)["Dimensions"])
        print("Titulo: " + lt.getElement(lst,size-2)["Title"],"Artistas: " + artistsArtwork(size-2,lst,catalog),"Fecha: " + lt.getElement(lst,size-2)["DateAcquired"],"Medio: " + lt.getElement(lst,size-2)["Medium"],"Dimensiones: " + lt.getElement(lst,size-2)["Dimensions"])
        print("Titulo: " + lt.getElement(lst,size-1)["Title"],"Artistas: " + artistsArtwork(size-1,lst,catalog),"Fecha: " + lt.getElement(lst,size-1)["DateAcquired"],"Medio: " + lt.getElement(lst,size-1)["Medium"],"Dimensiones: " + lt.getElement(lst,size-1)["Dimensions"])
        print("Titulo: " + lt.getElement(lst,size)["Title"],"Artistas: " + artistsArtwork(size,lst,catalog),"Fecha: " + lt.getElement(lst,size)["DateAcquired"],"Medio: " + lt.getElement(lst,size)["Medium"],"Dimensiones: " + lt.getElement(lst,size)["Dimensions"])





    elif int(inputs[0]) == 4:
        name_artist = str(input("Introduzca el nombre del artista del que desea hacer la busqueda: "))
        result = controller.artworksOfArtistByMedium(name_artist,catalog)
        total_obras = result[0]
        cantidad_tecnicas = result[1]
        tecnica = result[2]
        lista = result[3]
        tecnicas = result[4]
        print("El numero total de obras encontradas es de: "+ str(total_obras))
        print("La cantidad de tecnicas utilizadas es de: " + str(cantidad_tecnicas))
        print("La siguiente lista es el total de tecnicas utilizadas: " + str(tecnicas))
        print("La tecnica mas utilizada es: " + str(tecnica))
        print("A continuacion se muestra el listado de obras de la tecnica mas utilizada: ")
        print("Titulo: " + lt.getElement(lista,1)["Title"] + " Fecha de la obra: " + lt.getElement(lista,1)["Date"] + " Medio: "+ lt.getElement(lista,1)["Medium"] + " Dimensiones: "+ lt.getElement(lista,1)["Dimensions"])
        print("Titulo: " + lt.getElement(lista,2)["Title"] + " Fecha de la obra: " + lt.getElement(lista,2)["Date"] + " Medio: "+ lt.getElement(lista,2)["Medium"] + " Dimensiones: "+ lt.getElement(lista,2)["Dimensions"])
        print("Titulo: " + lt.getElement(lista,3)["Title"] + " Fecha de la obra: " + lt.getElement(lista,3)["Date"] + " Medio: "+ lt.getElement(lista,3)["Medium"] + " Dimensiones: "+ lt.getElement(lista,3)["Dimensions"])
        
        



    elif int(inputs[0]) == 5:
        result = countArtworksbyCountry(catalog)
        lst_c = result[0]
        size = lt.size(lst_c)
        lst_1 = lt.getElement(lst_c,1)
        lst_2 = lt.getElement(lst_c,2)
        lst_3 = lt.getElement(lst_c,3)
        lst_4 = lt.getElement(lst_c,size-3)
        lst_5 = lt.getElement(lst_c,size-2)
        lst_6 = lt.getElement(lst_c,size-1)
        top10country(result)
        print("Los primeros y ultimos 3 artistas por pais con mas obras: ")
        print("ID del objeto: " + lt.getElement(lst_1,1)["ObjectID"], " Titulo: " + lt.getElement(lst_1,1)["Title"]," Nombre del artista: " + artistsArtwork(1,lst_1,catalog)," Medio: " + lt.getElement(lst_1,1)["Medium"]," Año: " + lt.getElement(lst_1,1)["Date"]," Dimensiones: " + lt.getElement(lst_1,1)["Dimensions"]," Departamento: " + lt.getElement(lst_1,1)["Department"])          
        print("ID del objeto: " + lt.getElement(lst_2,1)["ObjectID"], " Titulo: " + lt.getElement(lst_2,1)["Title"]," Nombre del artista: " + artistsArtwork(1,lst_2,catalog)," Medio: " + lt.getElement(lst_2,1)["Medium"]," Año: " + lt.getElement(lst_2,1)["Date"]," Dimensiones: " + lt.getElement(lst_2,1)["Dimensions"]," Departamento: " + lt.getElement(lst_2,1)["Department"])          
        print("ID del objeto: " + lt.getElement(lst_3,1)["ObjectID"], " Titulo: " + lt.getElement(lst_3,1)["Title"]," Nombre del artista: " + artistsArtwork(1,lst_3,catalog)," Medio: " + lt.getElement(lst_3,1)["Medium"]," Año: " + lt.getElement(lst_3,1)["Date"]," Dimensiones: " + lt.getElement(lst_3,1)["Dimensions"]," Departamento: " + lt.getElement(lst_3,1)["Department"])          
        print("ID del objeto: " + lt.getElement(lst_4,1)["ObjectID"], " Titulo: " + lt.getElement(lst_4,1)["Title"]," Nombre del artista: " + artistsArtwork(1,lst_4,catalog)," Medio: " + lt.getElement(lst_4,1)["Medium"]," Año: " + lt.getElement(lst_4,1)["Date"]," Dimensiones: " + lt.getElement(lst_4,1)["Dimensions"]," Departamento: " + lt.getElement(lst_4,1)["Department"])          
        print("ID del objeto: " + lt.getElement(lst_5,1)["ObjectID"], " Titulo: " + lt.getElement(lst_5,1)["Title"]," Nombre del artista: " + artistsArtwork(1,lst_5,catalog)," Medio: " + lt.getElement(lst_5,1)["Medium"]," Año: " + lt.getElement(lst_5,1)["Date"]," Dimensiones: " + lt.getElement(lst_5,1)["Dimensions"]," Departamento: " + lt.getElement(lst_5,1)["Department"])          
        print("ID del objeto: " + lt.getElement(lst_6,1)["ObjectID"], " Titulo: " + lt.getElement(lst_6,1)["Title"]," Nombre del artista: " + artistsArtwork(1,lst_6,catalog)," Medio: " + lt.getElement(lst_6,1)["Medium"]," Año: " + lt.getElement(lst_6,1)["Date"]," Dimensiones: " + lt.getElement(lst_6,1)["Dimensions"]," Departamento: " + lt.getElement(lst_6,1)["Department"])          

    elif int(inputs[0]) == 6:
        department = input("ingrese el nombre del departamento: " )
        result = artworksDepartment(catalog,department)
        lst_dt = result[1][1]
        lst_cst = result[0][1]
        total = result[0][0]
        size = lt.size(total)
        precio = result[3]
        peso = result[2]
        print("El total de obras transportadas son: "+ str(size) )
        print("El peso estiamdo de todas las obras fue de: " + str(peso))
        print("El precio estimado del envio fue de: "+str(precio))
        print("el top 5 obras mas costosas es: ")
        print(lst_cst[0])
        print(lst_cst[1])
        print(lst_cst[2])
        print(lst_cst[3])
        print(lst_cst[4])
        print("el top 5 obras mas antiguas es: ")
        print(lst_dt[0])
        print(lst_dt[1])
        print(lst_dt[2])
        print(lst_dt[3])
        print(lst_dt[4])

    else:
        sys.exit(0)
sys.exit(0)
