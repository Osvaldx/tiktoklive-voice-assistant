from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent,CommentEvent,FollowEvent
import pyttsx3
from colorama import Fore,Style

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

comentarios_ya_leidos = set()
followers_ya_leidos = set()

cliente = TikTokLiveClient(unique_id="@elfokinronz")

print(Fore.LIGHTBLUE_EX + r'''
___        ___  __                    ___ 
 |  | |__/  |  /  \ |__/ |    | \  / |__  
 |  | |  \  |  \__/ |  \ |___ |  \/  |___ 
                                          
      __   __     __  ___           ___   
 /\  /__` /__` | /__`  |   /\  |\ |  |    
/~~\ .__/ .__/ | .__/  |  /~~\ | \|  |    
                                        
''' + Style.RESET_ALL)

async def mensaje_spam_validacion(mensaje: str)-> bool:
    retorno = False
    if(mensaje.isalpha() or (len(mensaje) <= 2)):
        contador = 0
        auxiliar = ""
        for i in range(len(mensaje)):
            if(i == 0):
                auxiliar = mensaje[i]
            
            if(mensaje[i] == auxiliar):
                contador += 1
            
            auxiliar = mensaje[i]
        if(contador >= 4):
            retorno = True
    else:
        retorno = True
    
    return retorno

async def hablar(texto: str)->None:
    engine.say(texto)
    engine.runAndWait()

@cliente.on(ConnectEvent)
async def conectar_live(event: ConnectEvent)-> None:
    print(Fore.LIGHTGREEN_EX + f"[+] Se conecto al Live de: {event.unique_id} correctamente!" + Style.RESET_ALL)

@cliente.on(CommentEvent)
async def leer_comentarios(event: CommentEvent)-> None:
    if(await mensaje_spam_validacion(event.comment) == False):
        clave_comentario = f"{event.user.nickname}: {event.comment}"
        if clave_comentario not in comentarios_ya_leidos:
            comentarios_ya_leidos.add(clave_comentario)
            print(Fore.LIGHTYELLOW_EX + f"[MESSAGE] {event.user.nickname}: {event.comment}" + Style.RESET_ALL)
            await hablar(f"{event.user.nickname} dijo {event.comment}")
    else:
        print(Fore.LIGHTRED_EX + f"[SPAM] {event.user.nickname}: {event.comment}" + Style.RESET_ALL)
        await hablar(f"{event.user.nickname} intento mandar un mensaje spam")

@cliente.on(FollowEvent)
async def me_siguieron(event: FollowEvent):
    clave_seguidores = f"{event.user.unique_id}"
    if clave_seguidores not in followers_ya_leidos:
        followers_ya_leidos.add(clave_seguidores)
        engine.setProperty("rate", 125)
        print(Fore.LIGHTCYAN_EX + f"[FOLLOW] {event.user.unique_id} te empezo a seguir!" + Style.RESET_ALL)
        await hablar(f"{event.user.nickname} nos acaba de seguir!")

if __name__ == "__main__":
    try:
        cliente.run()
    except Exception as e:
        print(Fore.RED + f"[!] Error al conectar: {e}" + Style.RESET_ALL)