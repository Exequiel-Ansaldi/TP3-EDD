from linked_stack_ext import LinkedStackExt

class Linked_Stack_Ext_Client(LinkedStackExt):
    pila_nueva = LinkedStackExt()
    pila_nueva.push(1)
    pila_nueva.push(2)
    pila_nueva.push(2)
    pila_nueva.push(2)
    pila_nueva.push(5)
    pila_nueva.push(6)

    print("Elementos eliminados de la pila ", pila_nueva.multi_pop(3))
    pila_nueva.replace_all(2,6)
    print("Pila luego de 3 pops y cambiando 2 por 6:\n",pila_nueva,"\n")
    pila_nueva.__imul__(2)
    print("Pila nueva: " , pila_nueva)
    
    