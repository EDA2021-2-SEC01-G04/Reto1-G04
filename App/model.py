"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from os import terminal_size
from DISClib.DataStructures.arraylist import newList
from typing import Text
import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
import math as math
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(type_list):
    if type_list == 1:
            type_list = "ARRAY_LIST"
    else:
        type_list = "LINKED_LIST"

    catalog = {"artworks": None,
               "artists": None}
               #"ID":None}
    catalog["artworks"] = lt.newList(type_list)
    catalog["artists"] = lt.newList(type_list)
    catalog["ID"] = lt.newList(type_list)
    return catalog


# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    artist["artworks"] = lt.newList("ARRAY_LIST")
    lt.addLast(catalog["artists"],artist)
    lt.addLast(catalog["ID"],artist["ConstituentID"])

def addArtwork(catalog,artwork):
    lt.addLast(catalog["artworks"],artwork)
    #artists = artwork["ConstituentID"].replace("[", "").replace("]", "").split(",")
    #for artist in artists:
        #addArtistOfArtwork(catalog,artist,artwork)

#def addArtistOfArtwork(catalog):
    #for artist in lt.iterator(catalog["artists"]):
    
#def artworArstis(id,catalog):
    #ConstituentID
    #for artwork in lt.iterator(catalog["artworks"]):
        #if artwork["ConstituentID"]

# Punto 1

def dateArtists(date1,date2,catalog):
    lst = lt.newList("ARRAY_LIST")
    for artists in lt.iterator(catalog["artists"]):
        if artists["BeginDate"] >= date1 and artists["BeginDate"] <= date2 :
            lt.addLast(lst,artists)
    #print (lst)

    lst_sort = merge.sort(lst,compareratings2)
    #print (lst_sort)
    return lst_sort


#Punto 2
def dateArtworks(date1,date2,catalog):
    lst = lt.newList("ARRAY_LIST")
    date1 = date1.split("-")
    date2 = date2.split("-")
    for artists in lt.iterator(catalog["artworks"]):
        fecha = artists["DateAcquired"].split("-")
        #if len(fecha) == 2:
            #fecha.append("01")
        #else:
            #fecha.append("01")
            #fecha.append("01")

        if (len(fecha) == 3) and (date1[0] == fecha[0] and date1[1] <= fecha[1] ) or (date2[0] == fecha[0] and date2[1] >= fecha[1]):
            lt.addLast(lst,artists)
        elif (len(fecha) == 3) and (date1[0] < fecha[0] and date2[0] > fecha[0]):
            lt.addLast(lst,artists)



    lst_sort = merge.sort(lst,compareratings)
    contador = dateArtworksPurchase(lst_sort)


    return (lst_sort,contador)
    

def dateArtworksPurchase(lst):
    contadr = 0
    for artwork in lt.iterator(lst):
        if artwork["CreditLine"] == "purchase" or artwork["CreditLine"] == "Purchase":
            contadr += 1
    return contadr

def artistsArtwork(pos,lst,catalog):
    texto = ""
    artwork = lt.getElement(lst,pos)
    constId = artwork["ConstituentID"].replace("[", "").replace("]", "").split(",")
    for Id in constId:
        nombre_a = nameArtistsId(catalog,Id)
    
        if type(nombre_a) != "str":
            nombre_a = ""
        texto += (nombre_a + ",") 
    return texto 

    

def nameArtistsId(catalog,id):
    for artists in lt.iterator(catalog["artists"]):
        if id == artists["ConstituentID"]:
            return artists["DisplayName"]



#Punto 4
def countArtworksbyCountry(catalog):
    cntry_artwrks = {}
    lst = lt.newList("ARRAY_LIST")
    for country in lt.iterator(catalog["artists"]):
        if len(country["Nationality"]) > 0 and country["Nationality"]:
            if country["Nationality"] not in cntry_artwrks:
                cntry_artwrks[country["Nationality"]] = lt.size(country["artworks"])
            else:
                cntry_artwrks[country["Nationality"]] += lt.size(country['artworks'])
    for cntry in cntry_artwrks:
        number = cntry_artwrks[cntry]
        lt.addLast(lst,number)
    lst_sort = (merge.sort(lst,compareID))


    return (lst_sort,cntry_artwrks)


#Punto 5
def artworksDepartment(catalog,depart):
    department = lt.newList("ARRAY_LIST")
    peso = 0
    costo_total = 0
    for artwork in lt.iterator(catalog["artworks"]):
        if artwork["Weight (kg)"] != "":
            peso += float(artwork["Weight (kg)"])
    
        if artwork["Department"] == depart:
            lt.addLast(department,artwork)
            artwork["costo"] = costoArtwork(artwork)
            if  artwork["costo"] != "":
                costo_total += artwork["costo"]
        
        
    lst_sort_costo = orderCost(department,catalog)
    lst_sort_date = orderDate(department,catalog)
    return (lst_sort_costo,lst_sort_date,peso,costo_total)

def orderCost(lst,catalog):
    lst_sort = merge.sort(lst,compareratings4)
    uno =("Titulo: " + lt.getElement(lst_sort,1)["Title"]," Artistas: " + artistsArtwork(1,lst_sort,catalog)+ " Clasificacion: " + lt.getElement(lst_sort,1)["Classification"]," Fecha: "+lt.getElement(lst_sort,1)["Date"],"Medio: "+ lt.getElement(lst_sort,1)["Medium"],"Dimensiones: "+lt.getElement(lst_sort,1)["Dimensions"],"Costo trasnporte: "+str(lt.getElement(lst_sort,1)["costo"]))                                                             
    dos =("Titulo: " + lt.getElement(lst_sort,2)["Title"]," Artistas: " + artistsArtwork(2,lst_sort,catalog)+ " Clasificacion: " + lt.getElement(lst_sort,2)["Classification"]," Fecha: "+lt.getElement(lst_sort,2)["Date"],"Medio: "+ lt.getElement(lst_sort,2)["Medium"],"Dimensiones: "+lt.getElement(lst_sort,2)["Dimensions"],"Costo trasnporte: "+str(lt.getElement(lst_sort,2)["costo"]))                                                             
    tres =("Titulo: " + lt.getElement(lst_sort,3)["Title"]," Artistas: " + artistsArtwork(3,lst_sort,catalog)+ " Clasificacion: " + lt.getElement(lst_sort,3)["Classification"]," Fecha: "+lt.getElement(lst_sort,3)["Date"],"Medio: "+ lt.getElement(lst_sort,3)["Medium"],"Dimensiones: "+lt.getElement(lst_sort,3)["Dimensions"],"Costo trasnporte: "+str(lt.getElement(lst_sort,3)["costo"]))                                                             
    cuatro =("Titulo: " + lt.getElement(lst_sort,4)["Title"]," Artistas: " + artistsArtwork(4,lst_sort,catalog)+ " Clasificacion: " + lt.getElement(lst_sort,4)["Classification"]," Fecha: "+lt.getElement(lst_sort,4)["Date"],"Medio: "+ lt.getElement(lst_sort,4)["Medium"],"Dimensiones: "+lt.getElement(lst_sort,4)["Dimensions"],"Costo trasnporte: "+str(lt.getElement(lst_sort,4)["costo"]))                                                             
    cinco =("Titulo: " + lt.getElement(lst_sort,5)["Title"]," Artistas: " + artistsArtwork(5,lst_sort,catalog)+ " Clasificacion: " + lt.getElement(lst_sort,5)["Classification"]," Fecha: "+lt.getElement(lst_sort,5)["Date"],"Medio: "+ lt.getElement(lst_sort,5)["Medium"],"Dimensiones: "+lt.getElement(lst_sort,5)["Dimensions"],"Costo trasnporte: "+str(lt.getElement(lst_sort,5)["costo"]))                                                             


    return (lst_sort,(uno,dos,tres,cuatro,cinco))

def orderDate(lst,catalog):
    lst_sort = merge.sort(lst,compareratings3)
    uno =("Titulo: " + lt.getElement(lst_sort,1)["Title"]," Artistas: " + artistsArtwork(1,lst_sort,catalog)+ " Clasificacion: " + lt.getElement(lst_sort,1)["Classification"]," Fecha: "+lt.getElement(lst_sort,1)["Date"],"Medio: "+ lt.getElement(lst_sort,1)["Medium"],"Dimensiones: "+lt.getElement(lst_sort,1)["Dimensions"],"Costo trasnporte: "+str(lt.getElement(lst_sort,1)["costo"]))                                                             
    dos =("Titulo: " + lt.getElement(lst_sort,2)["Title"]," Artistas: " + artistsArtwork(2,lst_sort,catalog)+ " Clasificacion: " + lt.getElement(lst_sort,2)["Classification"]," Fecha: "+lt.getElement(lst_sort,2)["Date"],"Medio: "+ lt.getElement(lst_sort,2)["Medium"],"Dimensiones: "+lt.getElement(lst_sort,2)["Dimensions"],"Costo trasnporte: "+str(lt.getElement(lst_sort,2)["costo"]))                                                             
    tres =("Titulo: " + lt.getElement(lst_sort,3)["Title"]," Artistas: " + artistsArtwork(3,lst_sort,catalog)+ " Clasificacion: " + lt.getElement(lst_sort,3)["Classification"]," Fecha: "+lt.getElement(lst_sort,3)["Date"],"Medio: "+ lt.getElement(lst_sort,3)["Medium"],"Dimensiones: "+lt.getElement(lst_sort,3)["Dimensions"],"Costo trasnporte: "+str(lt.getElement(lst_sort,3)["costo"]))                                                             
    cuatro =("Titulo: " + lt.getElement(lst_sort,4)["Title"]," Artistas: " + artistsArtwork(4,lst_sort,catalog)+ " Clasificacion: " + lt.getElement(lst_sort,4)["Classification"]," Fecha: "+lt.getElement(lst_sort,4)["Date"],"Medio: "+ lt.getElement(lst_sort,4)["Medium"],"Dimensiones: "+lt.getElement(lst_sort,4)["Dimensions"],"Costo trasnporte: "+str(lt.getElement(lst_sort,4)["costo"]))                                                             
    cinco =("Titulo: " + lt.getElement(lst_sort,5)["Title"]," Artistas: " + artistsArtwork(5,lst_sort,catalog)+ " Clasificacion: " + lt.getElement(lst_sort,5)["Classification"]," Fecha: "+lt.getElement(lst_sort,5)["Date"],"Medio: "+ lt.getElement(lst_sort,5)["Medium"],"Dimensiones: "+lt.getElement(lst_sort,5)["Dimensions"],"Costo trasnporte: "+str(lt.getElement(lst_sort,5)["costo"]))                                                             

    return (lst_sort,(uno,dos,tres,cuatro,cinco))

def costoArtwork(artwork):
    precio_1 = 0
    precio_2 = 0
    precio_3 = 0
    precio_4 = 0
    precio_5 = 0
    precio = 0

    if artwork["Dimensions"] != "":
        if artwork["Circumference (cm)"] != "" and artwork["Diameter (cm)"] == "":
            r = (float(artwork["Circumference (cm)"]))/(math.pi*2)
            if  artwork["Depth (cm)"] != "":
                depht = (float(artwork["Depth (cm)"]))/100
                precio_1 = ((math.pi * r**2)* depht)/72
                
            else:
                precio_1 =  (math.pi * r**2)/72
                
        elif artwork["Diameter (cm)"] != "":
            r = (float(artwork["Diameter (cm)"]))/2
            if  artwork["Depth (cm)"] != "":
                depht = (float(artwork["Depth (cm)"]))/100
                precio_2= ((math.pi * r**2)* depht)/72
                
            else:
                precio_2 = (math.pi * r**2)/72
                
        if artwork["Weight (kg)"] != "":
            precio_3 = (float(artwork["Weight (kg)"]))/72

        if  artwork["Length (cm)"] != "" and artwork["Height (cm)"] != "":
            if artwork["Width (cm)"] != "":
                precio_4 = (float(artwork["Length (cm)"]))*(float(artwork["Height (cm)"]))*(float(artwork["Width (cm)"]))
            else:
                precio_4 = (float(artwork["Length (cm)"]))*(float(artwork["Height (cm)"]))
        
        if  artwork["Length (cm)"] == "" and artwork["Height (cm)"] != "":
            if artwork["Width (cm)"] != "":
                precio_4 = (float(artwork["Height (cm)"]))*(float(artwork["Width (cm)"]))/72
        
        
        
        if  artwork["Length (cm)"] != "" and artwork["Height (cm)"] == "":
            if artwork["Width (cm)"] != "":
                precio_4 = (float(artwork["Length (cm)"]))*(float(artwork["Width (cm)"]))/72
        

    else:
        precio_5 = 42
        
    precio = max(precio_1,precio_2,precio_4,precio_3,precio_5)
    if precio == 0:
        precio = 42
    return precio








def subList(muestra,catalog):
    subList = lt.subList(catalog,0,muestra) 
    return None

# Funciones para creacion de datos
def newArtist(name):
    artist = {"name":"","artworks":None}
    artist["name"] = name
    artist["artworks"] = lt.newList("ARRAY_LIST")
    return artist

# Funciones de consulta
def getLast3Artworks(catalog):
    pos1 = int(lt.size(catalog["artworks"]))-4
    pos2 = int(lt.size(catalog["artworks"]))-5
    pos3 = int(lt.size(catalog["artworsk"]))-6

    artwork1 = lt.getElement(catalog["artworks"],1)
    artwork2 = lt.getElement(catalog["artworks"],2)
    artwork3 = lt.getElement(catalog["artworks"],3)
    text = "{0}, {1}, {2}".format(artwork1,artwork2,artwork3)
    text = catalog["artwork"].keys()
    return text

def getLast3Artists(catalog):
    pos1 = int(lt.size(catalog["artists"]))-4
    pos2 = int(lt.size(catalog["artists"]))-5
    pos3 = int(lt.size(catalog["artists"]))-6

    artist1 = lt.getElement(catalog["artists"][1],1)
    artist2 = lt.getElement(catalog["artists"][1],2)
    artist3 = lt.getElement(catalog["artists"][1],3)
    text = "{0}, {1}, {2}".format(artist1,artist2,artist3)
    return text



# Funciones utilizadas para comparar elementos dentro de una lista
def compareauthors(authorname1, author):
    if (authorname1["DateAcquired"].lower() in author['DateAcquired'].lower()):
        return 0
    return -1


def compareratings(book1, book2):
    date1 = book1["DateAcquired"]
    date2 = book2["DateAcquired"]
    if((date1) < (date2)):
        return 1
    #elif (date1) > (date2):
        #return -1
    else:
        return 0
def compareratings2(book1, book2):
    date1 = book1["BeginDate"]
    date2 = book2["BeginDate"]
    if((date1) < (date2)):
        return 1
    else:
        return 0

def compareratings3(book1, book2):
    date1 = book1["Date"]
    date2 = book2["Date"]
    if((date1) < (date2)):
        return 1
    else:
        return 0
def compareratings4(book1, book2):
    date1 = book1["costo"]
    date2 = book2["costo"]
    if((date1) < (date2)):
        return 0
    else:
        return 1


def mayYmenor(lista):
    size = lt.size(lista)


def compareID(ID, ID2):
    if (ID > ID2):
        return 1
    elif (ID < ID2):
        return 0
    

def cmpArtworkByDateAcquired(artwork1,artwork2):
    date_1 = artwork1["DateAcquired"]
    date_2 = artwork2["DateAcquired"]
    if date_1 < date_2:
        return True
    else:
        return False
    
# Funciones de ordenamiento
def sortArtworks(catalog, size):
    sub_list = lt.subList(catalog['artworks'], 1, size)
    sub_list = sub_list.copy()
    return sub_list

def sortArtworksByDate(num,catalog):
    if num == 1:
        start_time = time.process_time()
        sorted_list=insertion.sort(catalog["artworks"],cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg,sorted_list
    elif num == 2:
        start_time = time.process_time()
        sorted_list=sa.sort(catalog["artworks"],cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg,sorted_list
    elif num == 3:
        start_time = time.process_time()
        sorted_list=merge.sort(catalog["artworks"],cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg,sorted_list
    elif num == 4:
        start_time = time.process_time()
        sorted_list = quick.sort(catalog["artworks"],cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg,sorted_list

    
