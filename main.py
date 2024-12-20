from package_funciones.tiktok_events import *

if __name__ == "__main__":
    try:
        bandera = True
        nombre_ingresado = False

        while(bandera):
            dibujar_terminal("titulo_menu")
            dibujar_terminal("opciones_menu_principal")
            respuesta_terminal = str(input(Fore.LIGHTYELLOW_EX + "assistant:-~ "))
            match respuesta_terminal:
                case("1"):
                    agregar_usuario_json()
                    limpiar_terminal()
                case("2"):
                    pass
                    limpiar_terminal()
                case("3"):
                    limpiar_terminal()
                    cliente.run()
                case("4"):
                    bandera = False
                    limpiar_terminal()
                case _:
                    limpiar_terminal()
                    print(Fore.RED + "[!] Ingrese una opcion valida!")
    except Exception as e:
        print(Fore.RED + f"[!] Error al conectar: {e}" + Style.RESET_ALL)