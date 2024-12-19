from package_funciones.tiktok_events import *

if __name__ == "__main__":
    try:
        on_directo = False
        bandera = True

        while(bandera):
            dibujar_terminal("titulo_menu")
            dibujar_terminal("opciones_menu_principal")
            respuesta_terminal = str(input(Fore.LIGHTYELLOW_EX + "assistant:-~ "))
            match respuesta_terminal:
                case("1"):
                    limpiar_terminal()
                case("2"):
                    pass
                    limpiar_terminal()
                case("3"):
                    pass
                    limpiar_terminal()
                case("4"):
                    on_directo = True
                    bandera = False
                    limpiar_terminal()
                case("5"):
                    bandera = False
                    limpiar_terminal()
                case _:
                    limpiar_terminal()
                    print(Fore.RED + "[!] Ingrese una opcion valida!")
            
        if(on_directo):
            cliente.run()
        
    except Exception as e:
        hablar("Se perdio la conexion en LIVE")
        print(Fore.RED + f"[!] Error al conectar: {e}" + Style.RESET_ALL)