#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright (c) 2022 Jakepy Perdomo <j4kyjak3@protonmail.com>.
 
import platform
import os
import time

def clear():
    if platform.system() == "nt":
        os.system("cls")
    else:
        os.system("clear")


def banner():
    clear()
    print("="*50)
    print("[*] Istalador de Dependiencias by: jakepy")
    print("="*50)


def install_dependencias():
    banner()
    try:
        import colorama
        import pyfiglet
        print("\n[+] Dependiencias instaladas\n")
        exit(0)

    except ImportError:
        print("[!] Dependencias no instaladas")
        time.sleep(1.9)
        print("[!] Iniciando descarga de Dependencias...")
        time.sleep(1.9)
        os.system("pip3 install -r requirements.txt")
        time.sleep(1)
        print("[+] Dependencias Instaladas")
    
    except KeyboardInterrupt:
        print("[!] Instalacion cancelada...")
        exit(1)

if __name__=="__main__":
    install_dependencias()
