from linked_stack import LinkedStack
from linked_stack_ext_abstract import LinkedStackExtAbstract
from typing import Any, List

class LinkedStackExt(LinkedStackExtAbstract, LinkedStack):

    def multi_pop(self, num: int) -> List[Any]:
        if self.is_empty():
            raise Exception("La pila está vacía")
        if num > self._size:
            raise Exception(f"No se pueden hacer {num} pops porque la pila tiene {self._size} elementos")
        
        elementos_pops = []
        for _ in range(num):
            elementos_pops.append(self.pop()) 
        
        return elementos_pops

    
    def replace_all(self, param1: Any, param2: Any) -> None:
        pila_temp = []
        while not self.is_empty(): 
            elemento = self.pop()  
            if elemento == param1:
                pila_temp.append(param2) 
            else:
                pila_temp.append(elemento)  
        
        while pila_temp:
            self.push(pila_temp.pop())

    def __imul__(self, other: int) -> None:
        if other < 0:
            raise ("No es posible hacer esa cantidad de repeticiones")
        elementos_repetidos = []
        actual = self._head
        while actual is not None:
            elementos_repetidos.append(actual)
            actual = actual.next
        for _ in range(other -1):
            for elementos in elementos_repetidos:
                self.push(elementos)