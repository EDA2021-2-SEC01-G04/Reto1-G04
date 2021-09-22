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


from DISClib.DataStructures.arraylist import newList
from typing import Text
import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
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

#def addArtistOfArtwork(catalog,artistname,artwork):
    #artists = catalog["ID"]
    #de = lt.isPresent(artists,artistname)
    #for artist in lt.iterator(artists):
        #if artist["ConstituentID"] == artistname:
            #lt.addLast(artist["artworks"],artwork["ObjectID"])


# Punto 1

def dateArtists(date1,date2,catalog):
    lst = lt.newList("ARRAY_LIST")
    for artists in lt.iterator(catalog["artists"]):
        if artists["BeginDate"] >= date1 and artists["BeginDate"] <= date2 :
            lt.addLast(lst,artists)
    #print (lst)

    lst_sort = sort(lst)
    #print (lst_sort)
    return lst_sort

def cmp1(lst,pos):
    if (lt.getElement(lst, pos))["BeginDate"] < (lt.getElement(lst, pos-1))["BeginDate"]:
        return True
    else:
        return False

def sort(lst):
    size = lt.size(lst)
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 > 1) and cmp1(lst,pos2):
            lt.exchange(lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
    return lst

#Punto 2
def dateArtworks(date1,date2,catalog):
    lst = lt.newList("ARRAY_LIST")
    date1 = date1.split("-")
    date2 = date2.split("-")
    for artists in lt.iterator(catalog["artworks"]):
        fecha = artists["DateAcquired"].split("-")
        if len(fecha) == 2:
            fecha.append("01")
        else:
            fecha.append("01")
            fecha.append("01")

        if date1[0] == fecha[0] or date2[0] == fecha[0] and (date1[1] <= fecha[1] and date1[2] <= fecha[2]) and (date2[1] >= fecha[1] and date2[2] >= fecha[2]):
            lt.addLast(lst,artists)
        elif (date1[0] < fecha[0] and date2[0] > fecha[0]):
            lt.addLast(lst,artists)

        else:
            lt.addLast(lst,artists)
    lst_sort = sort2(lst)
    contador = dateArtworksPurchase(lst_sort)


    return (lst_sort,contador)
    
        
def cmp2(lst,pos):
    elemt1 = (lt.getElement(lst,pos)["DateAcquired"]).split("-")
    elemt2 = (lt.getElement(lst,pos-1)["DateAcquired"]).split("-")
    if elemt1[0] == elemt2[0] and elemt1[1] < elemt2[1] and  elemt1[2] < elemt2[2]:
            return True
    if elemt1[0] < elemt2[0]:
        return True
        
    else:
        return False
             
            

def sort2(lst):
    size = lt.size(lst)
    pos1 = 1
    while pos1 <= size:
        pos2 = pos1
        while (pos2 > 1) and cmp2(lst,pos2):
            lt.exchange(lst, pos2, pos2-1)
            pos2 -= 1
        pos1 += 1
    return lst

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
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1


def compareratings(book1, book2):
    return (float(book1['average_rating']) > float(book2['average_rating']))

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

    pass
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

    
