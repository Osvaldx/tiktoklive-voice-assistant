from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent,CommentEvent,FollowEvent
from gtts import gTTS
from playsound import playsound
from colorama import Fore,Style

comentarios_ya_leidos = set()
followers_ya_leidos = set()

cliente = TikTokLiveClient(unique_id="@tizitizi52")

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
    if(not mensaje.replace(" ","").isalpha()):
        emojis = 0
        for letra in mensaje:
            if(ord(letra) > 255):
                emojis += 1
        
        if(emojis >= 5):
            retorno = True
    
    contador = 0
    auxiliar = ""
    for i in range(len(mensaje)):
        if(i == 0):
            auxiliar = mensaje[i]
        elif(mensaje[i] == auxiliar):
            contador += 1
        auxiliar = mensaje[i]
    
    if(contador >= 5):
        retorno = True
    
    return retorno

async def hablar(texto: str)->None:
    mensaje = gTTS(texto, lang="es")
    mensaje.save("mensaje.mp3")
    playsound("mensaje.mp3")

@cliente.on(ConnectEvent)
async def conectar_live(event: ConnectEvent)-> None:
    print(Fore.LIGHTGREEN_EX + f"[+] Se conecto al Live de: {event.unique_id} correctamente!" + Style.RESET_ALL)

@cliente.on(CommentEvent)
async def leer_comentarios(event: CommentEvent)-> None:
    if(not await mensaje_spam_validacion(event.comment)):
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
        print(Fore.LIGHTCYAN_EX + f"[FOLLOW] {event.user.unique_id} te empezo a seguir!" + Style.RESET_ALL)
        await hablar(f"{event.user.nickname} nos acaba de seguir!")

if __name__ == "__main__":
    try:
        cliente.run()
    except Exception as e:
        print(Fore.RED + f"[!] Error al conectar: {e}" + Style.RESET_ALL)