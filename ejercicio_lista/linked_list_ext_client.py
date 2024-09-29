from linked_list_ext import LinkedListExt

class LinkedExtClient(LinkedListExt):
    def __init__(self):
            self.linked_list = LinkedListExt() 

            self.linked_list.append(15)
            self.linked_list.append(23)
            self.linked_list.append(3)

            print("Añadiendo elementos al inicio de la lista...")
            self.linked_list.add_first(10)
            print(f"Lista después de agregar elementos: {self.linked_list}")
            
            self.linked_list.pop()  
            print(f"Lista después de eliminar el último elemento: {self.linked_list}")

            print("Añadiendo una lista de elementos ")
            self.linked_list += [100, 200, 300] 
            print(f"Lista después de agregar con '+=': {self.linked_list}")
            print("Invirtiendo la lista...")
            self.linked_list.__reversed__() 
            print(f"Lista después de invertir: {self.linked_list}")

if __name__ == "__main__":
    cliente = LinkedExtClient()