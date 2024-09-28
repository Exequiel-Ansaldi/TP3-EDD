from linked_list_ext import LinkedListExt

class linked_list_ext_client(LinkedListExt):

    linked_list = LinkedListExt()

    print("Añadiendo elementos al inicio de la lista...")
    linked_list.add_first(10)
    linked_list.add_first(20)
    linked_list.add_first(30)
    print(f"Lista después de agregar elementos: {linked_list}")

    
    print("Eliminando el último elemento...")
    linked_list.pop()
    print(f"Lista después de eliminar el último elemento: {linked_list}")

    print("Añadiendo una lista de elementos con '+='...")
    linked_list += [100, 200, 300]
    print(f"Lista después de agregar con '+=': {linked_list}")

    print("Invirtiendo la lista...")
    linked_list.__reversed__()
    print(f"Lista después de invertir: {linked_list}")