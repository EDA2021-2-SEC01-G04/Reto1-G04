﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog(type_list):
    catalog = model.newCatalog(type_list)
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    loadArtists(catalog)
    loadArtwork(catalog)

def loadArtists(catalog):
    artistfile = cf.data_dir + "MoMA/Artists-utf8-small.csv"
    input_file = csv.DictReader(open(artistfile,encoding="utf-8"))
    for artist in input_file:
        model.addArtist(catalog, artist)

def loadArtwork(catalog):
    artworkfile = cf.data_dir + "MoMA/Artworks-utf8-small.csv"
    input_file = csv.DictReader(open(artworkfile,encoding="utf-8"))
    for artwork in input_file:
        model.addArtwork(catalog,artwork)

# Funciones de ordenamiento
def sortArworks(catalog, muestra):

    return model.sortArtworks(catalog, muestra)

# Funciones de consulta sobre el catálogo
def Last3Artists(catalog):
    artists = model.getLast3Artists(catalog)
    return artists
def Last3Artworks(catalog):
    artworks = model.getLast3Artworks(catalog)
    return artworks
