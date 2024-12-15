from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent,CommentEvent,FollowEvent
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

comentarios_ya_leidos = set()
followers_ya_leidos = set()

cliente = TikTokLiveClient(unique_id="@elfokinronz")

async def mensaje_spam_validacion(mensaje: str)-> bool:
    retorno = False
    for letra in mensaje:
        if mensaje.count(letra) >= 10:
            retorno = True
            break
    
    return retorno

async def hablar(texto: str)->None:
    engine.say(texto)
    engine.runAndWait()

@cliente.on(ConnectEvent)
async def conectar_live(event: ConnectEvent)-> None:
    print(f"[+] Se conecto al Live de: {event.unique_id} correctamente!")

@cliente.on(CommentEvent)
async def leer_comentarios(event: CommentEvent)-> None:
    if(await mensaje_spam_validacion(event.comment) == False):
        clave_comentario = f"{event.user.nickname}: {event.comment}"
        if clave_comentario not in comentarios_ya_leidos:
            comentarios_ya_leidos.add(clave_comentario)
            print(f"{event.user.nickname}: {event.comment}")
            await hablar(f"{event.user.nickname} dijo {event.comment}")
    else:
        await hablar(f"{event.user.nickname} intento mandar un mensaje spam")

@cliente.on(FollowEvent)
async def me_siguieron(event: FollowEvent):
    clave_seguidores = f"{event.user.unique_id}"
    if clave_seguidores not in followers_ya_leidos:
        followers_ya_leidos.add(clave_seguidores)
        engine.setProperty("rate", 125)
        print(f"{event.user.unique_id} Acabar de seguirte!")
        await hablar(f"{event.user.nickname} nos acaba de seguir!")

if __name__ == "__main__":
    cliente.run()