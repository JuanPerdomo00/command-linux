#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# proyecto preguntar comando de linux y mostrar su utilidad
# este proyecto se me ocurrio gracias a un video de Pelado Nerd
# este sofware trabaja bajo la GNU GENERAL PUBLIC LICENSE version 3
#
# Creador: Jakepy Perdomo <j4kyjak3@protonmail.com>
# Título: Linux Command
# FechaCreación: mayo-14-2021
#
# Copyright (c) 2022 Jakepy Perdomo <j4kyjak3@protonmail.com>.
# 
# Comentarios bienvenidos.
# Permiso otorgado para uso y distribución no comercial siempre que
# este aviso de derechos de autor permanece intacto.
#
# Hay ejemplos de cómo usar este código en el README.md.
#
# Cual quier duda escribeme, o talvez este dormido jsjs.

# modulos
import time as tm 
import os
import platform
import comandos
import comandos.comando as cm
from colorama import Fore
from pyfiglet import Figlet

# version
__version__ = 1.1


class Color:
    # los que aparecen dentro de string es porque el modulo de colorama no los tiene disponibles(el color naranja y la negrita)
    naranja = '\033[93m'
    negrita = '\033[1m'
    rojo = Fore.RED
    amarillo = Fore.YELLOW
    azul = Fore.BLUE
    verde = Fore.GREEN
    reset =  Fore.RESET
    cyan = Fore.CYAN
    magenta = Fore.MAGENTA
    blanco = Fore.WHITE


# detecta que sistema operativo ejecuta el programa
# y limpia la pantalla
def clearPant():
    sys = platform.system()
    if sys == "Windows":
        os.system("cls")
    elif sys == "Linux":
        os.system("clear")
    else:
        pass


# fuente de letra para letreros
f = Figlet(font="3-d")


# muestra letrero al usuario
def figlet():
        clearPant()
        print(f"{Color.verde}{Color.negrita}",  f.renderText("Linux Command"),"\t\t")
        print(f"\t\t\t\t\t{Color.cyan} {Color.negrita}-+- By: JuanPerdomo00 <jakepy> -+- {Color.reset}")


# mostrara por pantalla el saludo y la version
def saludar_usuario():
        figlet()
        print(f""" {Color.magenta}
        +-------------------------------+
        |   Bienvenido a LINUX COMMAND  |
        |      20 comandos de linux     |
        +-------------------------------+
        """)

        print(f"""{Color.rojo}
        +----------------------------------------------+     
            [!] Version del proyecto: {__version__}     
        +----------------------------------------------+
        """)




# Simula una carga
def load():
    print(f"\n{Color.rojo}[+] {Color.verde}Buscando...\n{Color.reset}")
    print(f"[{Color.azul}###                  {Color.reset}] {Color.naranja}5%{Color.reset}")
    tm.sleep(1)
    print(f"[{Color.amarillo}#########            {Color.reset}] {Color.naranja}25%{Color.reset}")
    tm.sleep(1)
    print(f"[{Color.cyan}#############        {Color.reset}] {Color.naranja}50%{Color.reset}")
    tm.sleep(1)
    print(f"[{Color.magenta}#################    {Color.reset}] {Color.naranja}75%{Color.reset}")
    tm.sleep(1)
    print(f"[{Color.rojo}#####################{Color.reset}]{Color.naranja}100%{Color.reset}")
    tm.sleep(1)


# Pintamos por consola las opciones de los comandos
def pedir_comandos():
    print(f""" {Color.amarillo}
    +------------------------------------------------------+
    |  1.ls          6.pwd       11.locate   16.chmod      |
    |  2.cd          7.cat       12.find     17.ping       |
    |  3.mkdir       8.mv        13.grep     18.wget       |
    |  4.cp          9.rmdir     14.sudo     19.uname      |
    |  5.touch       10.rm       15.tar      20.top        |
    +------------------------------------------------------+                                                            
    {Color.reset}""")

    try:
    ###############################################################
        opcion = str(input(f"{Color.magenta}[{Color.amarillo}?{Color.magenta}] {Color.verde}Que comando desea buscar: {Color.reset}"))
        clearPant()
        figlet()
        load()
        clearPant()
        figlet()
        comandos(opcion)
    ###############################################################
    except KeyboardInterrupt:
        clearPant()
        figlet()
        print(f"\n{Color.rojo}Salio de manera forzosa...\n{Color.reset}")
        exit(1)


def error():
    clearPant()
    figlet()
    print(f"\n{Color.rojo} [!] la opcion que usted escogio no es valida")
    print(f"{Color.rojo} [!] ERROR...")
    print(f"{Color.rojo} [!] Ingrese otra opcion o salga del programa :){Color.reset}\n")



# Si el usuario quere buscar otro comando el prgrama volvera a ejecutarse
# En caso de que diga que no se agradesera al ususario y se cerrara
# Y si no menciona ninguna de las anteriores pues es error
def otroCommad():
    try:
        print(f"\n{Color.naranja}{Color.negrita}[?] Quiere buscar otro comando?\n")
        o = str(input(f"[!] {Color.negrita}si[s] o {Color.negrita}no[n]: {Color.reset}"))
        if o == "s" or o == "si" and o != "":
            clearPant()
            figlet()
            pedir_comandos()
        elif o == "n" or o == "no" and o != "":
            clearPant()
            figlet()
            print(f"\n{Color.blanco}{Color.amarillo}[*] {Color.verde}Gracias por usar Linux Command {Color.cyan}:)\n{Color.reset}")
            exit(0)
        else:
            error()
            otroCommad()
    except KeyboardInterrupt:
        clearPant()
        figlet()
        print(f"{Color.rojo}[!!] Salio forzado...{Color.reset}\n")
        exit(1)


def comandos(opcion):
        if opcion == "1" or opcion == "ls":
            print("\n", cm.ls)
            otroCommad()

        elif opcion == "2" or opcion == "cd":
            print("\n", cm.cd)
            otroCommad()

        elif opcion == "3" or opcion == "mkdir":
            print("\n", cm.mkdir)
            otroCommad()

        elif opcion == "4" or opcion == "cp":
            print("\n", cm.cp)
            otroCommad()

        elif opcion == "5" or opcion == "touch":
            print("\n", cm.touch)
            otroCommad()

        elif opcion == "6" or opcion == "pwd":
            print("\n", cm.pwd)
            otroCommad()

        elif opcion == "7" or opcion == "cat":
            print("\n", cm.cat)
            otroCommad()

        elif opcion == "8" or opcion == "mv":
            print("\n", cm.mv)
            otroCommad()

        elif opcion == "9" or opcion == "rmdir":
            print("\n", cm.rmdir)
            otroCommad()

        elif opcion == "10" or opcion == "rm":
            print("\n", cm.rm)
            otroCommad()
        
        elif opcion == "11" or opcion == "locate":
            print("\n", cm.locate)
            otroCommad()

        elif opcion == "12" or opcion == "find":
            print("\n", cm.find)
            otroCommad()

        elif opcion == "13" or opcion == "grep":
            print("\n", cm.grep) 
            otroCommad()   

        elif opcion == "14" or opcion == "sudo":
            print("\n", cm.sudo)
            otroCommad()

        elif opcion == "15" or opcion == "tar":
            print("\n", cm.tar)
            otroCommad()
        
        elif opcion == "16" or opcion == "chmod":
            print("\n", cm.chmod)
            otroCommad()

        elif opcion == "17" or opcion == "ping":
            print("\n", cm.ping)
            otroCommad()
        
        elif opcion == "18" or opcion == "wget":
            print("\n", cm.wget)
            otroCommad()
        
        elif opcion == "19" or opcion == "uname":
            print("\n", cm.uname)
            otroCommad()
        
        elif opcion == "20" or opcion == "top":
            print("\n", cm.top)
            otroCommad()
        
        else:
            error()
            otroCommad()


# Funcion principal
def main():
    saludar_usuario()
    pedir_comandos()


if __name__ == "__main__":
    main()
