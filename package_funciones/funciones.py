from gtts import gTTS
from playsound import playsound
from colorama import Fore,Style
import json
import os

def eliminar_usuario_json():
    usuario = str(input(Fore.LIGHTCYAN_EX + "[~] Ingrese el usuario original: "))
    while(not usuario.replace("_","").isalnum()):
        print(Fore.RED + "[!] Error: Ingrese un nombre valido" + Style.RESET_ALL)
        usuario = str(input(Fore.LIGHTCYAN_EX + "[~] Ingrese el usuario original: "))
    
    with open("jsons/users_rename.json", "r", encoding="utf-8") as archivo:
        contenido = json.load(archivo)
    
    if(contenido.get(usuario)):
        contenido.pop(usuario)
        print(Fore.LIGHTGREEN_EX + f"[+] {usuario} eliminado con exito de la lista json")
        with open("jsons/users_rename.json", "w", encoding="utf-8") as archivo:
            json.dump(contenido,archivo, indent=4)
    else:
        print(Fore.LIGHTRED_EX + f"[!] {usuario} no existe en la lista json")

def agregar_usuario_json():
    usuario = str(input(Fore.LIGHTCYAN_EX + "[~] Ingrese el usuario original: "))
    while(not usuario.replace("_","").isalnum()):
        print(Fore.RED + "[!] Error: Ingrese un nombre valido" + Style.RESET_ALL)
        usuario = str(input(Fore.LIGHTCYAN_EX + "[~] Ingrese el usuario original: "))

    rename = str(input(Fore.LIGHTMAGENTA_EX + "[~] Ingrese el rename: "))
    while(not rename.replace("_","").isalnum()):
        print(Fore.RED + "[!] Error: Ingrese un nombre valido" + Style.RESET_ALL)
        rename = str(input(Fore.LIGHTMAGENTA_EX + "[~] Ingrese el rename: "))
    
    with open("jsons/users_rename.json", "r",encoding="utf-8") as archivo:
        contenido_json = json.load(archivo)
    
    contenido_json[usuario] = rename

    with open("jsons/users_rename.json", "w", encoding="utf-8") as archivo:
        json.dump(contenido_json, archivo, indent=4)

def obtener_usuarios_json()->str:
    with open("jsons/users_rename.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    return datos

def validar_usuario(nickname: str,lista_usuarios:dict)->bool | str:
    return nickname in lista_usuarios

def obtener_nombre()->str:
    dibujar_terminal("titulo_menu")
    print(Fore.LIGHTCYAN_EX + "\n[!] Ingrese su nombre de tiktok sin '@'")
    nombre_tiktok = str(input(Fore.WHITE + "[~] @: "))

    while(not nombre_tiktok.replace("_", "").isalnum()):
        print(Fore.RED + "[!] ERROR: Ingrese un nombre valido" + Style.RESET_ALL)
        nombre_tiktok = str(input(Fore.WHITE + "[~] @: "))

    limpiar_terminal()
    return nombre_tiktok

def dibujar_terminal(clave: str):
    if(clave == "titulo_menu"):
        print(Fore.LIGHTBLUE_EX + r'''
___        ___  __                    ___ 
 |  | |__/  |  /  \ |__/ |    | \  / |__  
 |  | |  \  |  \__/ |  \ |___ |  \/  |___ 
                                          
      __   __     __  ___           ___   
 /\  /__` /__` | /__`  |   /\  |\ |  |    
/~~\ .__/ .__/ | .__/  |  /~~\ | \|  |    ''' + Style.RESET_ALL)
    elif(clave == "opciones_menu_principal"):
        print("\n" + Fore.LIGHTCYAN_EX + "- [1] " + Fore.WHITE + "Renombrar usuarios-live" + Style.RESET_ALL + "\n" +
              Fore.LIGHTCYAN_EX + "- [2] " + Fore.WHITE + "Eliminar usuarios-live" + Style.RESET_ALL + "\n" +
              Fore.LIGHTCYAN_EX + "- [3] " + Fore.WHITE + "Cambiar sonidos de alertas" + Style.RESET_ALL + "\n" +
              Fore.LIGHTYELLOW_EX + "- [4] " + Fore.WHITE + "Empezar directo" + Style.RESET_ALL + "\n" +
              Fore.LIGHTCYAN_EX + "- [5] " + Fore.WHITE + "Salir" + Style.RESET_ALL)

def limpiar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

async def mensaje_spam_validacion(mensaje: str)-> bool:
    retorno = False
    emojis = 0
    if(not mensaje.replace(" ","").isalpha()):
        for letra in mensaje:
            if(ord(letra) > 255):
                emojis += 1
        
        retorno = True if emojis >= 5 else False
    
    if(emojis <= 5):
        contador = 0
        auxiliar = ""
        for i in range(len(mensaje)):
            if(i == 0):
                auxiliar = mensaje[i]
            elif(mensaje[i] == auxiliar):
                contador += 1
            auxiliar = mensaje[i]
        
        retorno = True if contador >= 5 else False
    
    return retorno

async def hablar(texto: str)->None:
    mensaje = gTTS(texto.lower(), lang="es")
    mensaje.save("sounds\mensaje.mp3")
    playsound("sounds\mensaje.mp3")