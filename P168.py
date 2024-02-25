# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 17:15:22 2024

@author: Aidan
"""

class Libro:
    def __init__(self, nombre_del_libro, nombre_del_autor, año_de_publicacion, precio_del_libro, ilustracion, ):
        self.libro = nombre_del_libro
        self.autor = nombre_del_autor
        self.año = año_de_publicacion
        self.precio = precio_del_libro
        self. ilustra = ilustracion 
        
    def datos_del_Libro(self):
        print("Nombre del libro: " + str(self.libro))
        print("Nombre del autor: " + str(self.autor))
        print("Año de publicación: " + str(self.año))
        print("Precio: " + str(self.precio_del_libro))
        print("Contiene ilustraciones?: " + str(self.ilustracion))
        
objeto_libro1 = Libro("The hunger games", "Suzanne Collins", 2009, 264, "No")
objeto_libro1.añadiendo_datos()

objeto_libro2 = Libro("Bobicraft y el tesoro perdido", "Bobicraft", 2022, 250, "si")
objeto_libro2.añadiendo_datos()