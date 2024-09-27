from linked_stack_ext import LinkedStackExt

class Linked_Stack_Ext_Client(LinkedStackExt):
    pila_nueva = LinkedStackExt()
    pila_nueva.push(1)
    pila_nueva.push(2)
    pila_nueva.push(2)
    pila_nueva.push(2)
    pila_nueva.push(5)
    pila_nueva.push(6)

    print(pila_nueva.multi_pop(3))
    
    