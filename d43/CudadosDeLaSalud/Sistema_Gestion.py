#!/usr/bin/python
#-*- coding: utf-8 -*-

class Sistema_Gestion:


    def mostrar_menu(opciones):
        """
        Muestra las opciones del menu

        Args: 
            opciones (int) : opcion seleccionada para efectuar el uso del menu 
        Returns: 

        """
        print('Seleccione una opción:')
        for clave in sorted(opciones):
            print(f' {clave}) {opciones[clave][0]}')
    def leer_opcion(opciones):
        """
        Lee las opciones del menu

        Args: 
            opciones (int) : opcion seleccionada para efectuar el uso del menu 
        Returns: 

        """
        while (a := input('Opción: ')) not in opciones:
            print('Opción incorrecta, vuelva a intentarlo.')
        return a
    def ejecutar_opcion(opcion, opciones):
        """
        Ejecuta la opcion del menu elegida
        Args: 
            opcion (int) : opcion seleccionada para efectuar el uso 
            opciones (int) : extraido desde el menu principal
        Returns: 

        """
        opciones[opcion][1]()
    def generar_menu(opciones, opcion_salida):
        """
        Genera las opciones del menu
        Args: 
            opcion (int) : opcion seleccionada para efectuar el uso del menu 
            opcion_salida (int) : ayuda a comparar la opcion del usuario 
        Returns: 

        """
        opcion = None
        while opcion != opcion_salida:
            mostrar_menu(opciones)
            opcion = leer_opcion(opciones)
            ejecutar_opcion(opcion, opciones)
            print() # se imprime una línea en blanco para clarificar la salida por pantalla
    
    
    
    def menu_principal():
        """
        Muestra las opciones del menu desde la ejecucion principal
        Args: 
        
        Returns: 

        """
        opciones = {
            '1': ('mostrar funciones ', mostrar),
            '2': ('agregar funciones ', agregar),
            '3': ('actualizar funciones', actualizar),
        }

        generar_menu(opciones, '3')
    def mostrar():
        """
        Muestra las opciones del funcionamento cuidando la salud
        Args: 
            
        Returns: 

        """
        print('Haz elegido opcion agregar')
    def agregar():
        """
        Agrega una nueva funcionalidad del sistema
        Args: 
            
        Returns: 

        """
        print('Haz elegido opcion agregar')



    def actualizar():
        """
        Actualiza los nuevos cambios 
        Args: 
            
        Returns: 

        """
        print('Haz elegido opcion actualizar')
     
    

    if __name__ == '__main__':
        menu_principal()
 

    

