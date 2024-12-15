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

@cliente.on(ConnectEvent)
async def conectar_live(event: ConnectEvent)-> None:
    print(f"[+] Se conecto al Live de: {event.unique_id} correctamente!")

@cliente.on(CommentEvent)
async def leer_comentarios(event: CommentEvent)-> None:
    clave_comentario = f"{event.user.nickname}: {event.comment}"
    if clave_comentario not in comentarios_ya_leidos:
        comentarios_ya_leidos.add(clave_comentario)
        print(f"{event.user.nickname}: {event.comment}")
        engine.say(f"{event.user.nickname} dijo {event.comment}")
        engine.runAndWait()

@cliente.on(FollowEvent)
async def me_siguieron(event: FollowEvent):
    clave_seguidores = f"{event.user.unique_id}"
    if clave_seguidores not in followers_ya_leidos:
        followers_ya_leidos.add(clave_seguidores)
        print(f"{event.user.unique_id} Acabar de seguirte!")
        engine.say(f"{event.user.nickname} nos acaba de seguir!")
        engine.runAndWait()

if __name__ == "__main__":
    cliente.run()