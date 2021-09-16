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


from typing import Text
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
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
               "artists": None,
               "ID":None}
    catalog["artworks"] = lt.newList(type_list)
    catalog["artists"] = lt.newList(type_list)
    catalog["ID"] = lt.newList(type_list)
    return catalog


# Funciones para agregar informacion al catalogo
def addArtwork(catalog,artwork):
    lt.addLast(catalog["artworks"],artwork)
    
    #for artist in artists:
        #addArtistOfArtwork(catalog,artist.strip(),artwork)
       

"""def addArtistOfArtwork(catalog,artistname,artwork):
    artists = catalog["artists"]
    
    posartist = compareauthors(artists,artistname
    if posartist > 0:
        artist = lt.getElement(artists,posartist)
    else:
        artist = newArtist(artistname)
        lt.addLast(artists,artist)
    lt.addLast(artist["artworks"],artwork)"""

def addArtist(catalog, artist):
    lt.addLast(catalog["artists"],artist)
    lt.addLast(catalog["ID"],artist["ConstituentID"])
    
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
    if (authorname1.lower() in author['ConstituentID'].lower()):
        return 0
    return -1


def compareratings(book1, book2):
    return (float(book1['average_rating']) > float(book2['average_rating']))


def compareID(ID, ID2):
    if (id > ID2):
        return 1
    elif (id < ID2):
        return -1
    return 0
# Funciones de ordenamiento
def sortArtworks(catalog, size):
    sub_list = lt.subList(catalog['artworks'], 1, size)
    sub_list = sub_list.copy()
    return sub_list