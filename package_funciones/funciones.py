from gtts import gTTS
from playsound import playsound
from colorama import Fore,Style
import os

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
        print("\n" + Fore.LIGHTGREEN_EX + "- [1] " + Fore.WHITE + "Ingresar nombre TikTok-Live" + Style.RESET_ALL + "\n" +
              Fore.LIGHTGREEN_EX + "- [2] " + Fore.WHITE + "Renombrar usuarios-live" + Style.RESET_ALL + "\n" +
              Fore.LIGHTGREEN_EX + "- [3] " + Fore.WHITE + "Cambiar sonidos de alertas" + Style.RESET_ALL + "\n" +
              Fore.LIGHTYELLOW_EX + "- [4] " + Fore.LIGHTMAGENTA_EX + "Empezar directo" + Style.RESET_ALL + "\n" +
              Fore.LIGHTGREEN_EX + "- [5] " + Fore.WHITE + "Salir" + Style.RESET_ALL)

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