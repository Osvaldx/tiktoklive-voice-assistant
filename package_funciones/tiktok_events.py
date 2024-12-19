from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent,CommentEvent,FollowEvent,GiftEvent
from package_funciones.funciones import *

comentarios_ya_leidos = set()
followers_ya_leidos = set()

cliente = TikTokLiveClient(unique_id="@elfokinronz")

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
            if(event.user.nickname == "bauta_gallardo_madrid_912"):
                await hablar(f"bautii dijo {event.comment}")
            else:
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
        playsound("sounds\oye-gela.mp3")

@cliente.on(GiftEvent)
async def donacion_monedas(event: GiftEvent):
    nombre_usuario = event.user.nickname if event.user.nickname else event.user.unique_id
    nombre_regalo = event.gift.name if event.gift.name else "un regalo"

    if(event.gift.streakable and not event.streaking):
        cantidad = event.repeat_count if event.repeat_count else 1
        print(Fore.LIGHTMAGENTA_EX + f"[$] {nombre_usuario} ha donado {cantidad} {nombre_regalo}")
        await hablar(f"{nombre_usuario} ha donado {cantidad} {nombre_regalo}")
        playsound("sounds\goku-eta-vaina-e-seria.mp3")

    elif(not event.gift.streakable):
        print(Fore.LIGHTMAGENTA_EX + f"[$] {nombre_usuario} ha donado {nombre_regalo}")
        await hablar(f"{nombre_usuario} ha donado un {nombre_regalo}")
        playsound("sounds\goku-eta-vaina-e-seria.mp3")