import sys
from tramite_db import Tramite
from tramites_admin import TramitesAdmin

def main():
    db_name = "tramites.db" 
    tramites_admin = TramitesAdmin(db_name)  
    tramites_admin.cargar_tramites_desde_bd()

    while True:
        print("\nMenu:")
        print("1. Agregar trámite")
        print("2. Quitar trámite")
        print("3. Listar trámites")
        print("4. Marcar trámite como terminado")
        print("5. Salir")
        
        eleccion = input("Seleccione una opción: ")

        if eleccion == '1':
            numero = int(input("Ingrese número del trámite: "))
            apellido = input("Ingrese apellido: ")
            nombre = input("Ingrese nombre: ")
            requerimiento = input("Ingrese requerimiento: ")
            terminada = False
            
            tramite = Tramite(numero, apellido, nombre, requerimiento, terminada)
            tramites_admin.add_tramite(tramite)
            print("Trámite agregado exitosamente.")

        elif eleccion == '2':
            tramite = tramites_admin.remove_tramite()
            if tramite:
                print(f"Trámite {tramite.numero} eliminado.")
            else:
                print("No hay trámites para quitar.")

        elif eleccion == '3':
            tramites = tramites_admin.list_tramites()
            if tramites:
                print("Trámites en la base de datos:")
                for t in tramites:
                    print(t)
            else:
                print("No hay trámites en la base de datos.")

        elif eleccion == '4':
            numero = int(input("Ingrese número del trámite a marcar como terminado: "))
            tramites_admin.mark_tramite_as_terminada(numero)
            print(f"Trámite {numero} marcado como terminado.")

        elif eleccion == '5':
            print("Saliendo del programa.")
            sys.exit(0)

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
