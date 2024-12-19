from package_funciones.tiktok_events import *

if __name__ == "__main__":
    try:
        on_directo = False
        bandera = True
        dibujar_terminal("titulo_menu")
        dibujar_terminal("opciones_menu_principal")

        while(bandera):
            respuesta_terminal = str(input("assistant:-~ "))
            match respuesta_terminal:
                case("1"):
                    pass
                case("2"):
                    pass
                case("3"):
                    pass
                case("4"):
                    on_directo = True
                    bandera = False
                case("5"):
                    bandera = False
                case _:
                    print(Fore.RED + "[!] Ingrese una opcion valida!")
            
        if(on_directo):
            cliente.run()
        
    except Exception as e:
        hablar("Se perdio la conexion en LIVE")
        print(Fore.RED + f"[!] Error al conectar: {e}" + Style.RESET_ALL)