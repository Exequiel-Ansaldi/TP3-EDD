from deque_abstract import DequeAbstract
from list_node import ListNode
from typing import Any, Union

class Deque (DequeAbstract, ListNode):

    def __init__(self) -> None:
        self._head : Union[ListNode, None] = None
        self._size : int = 0
        self._tail : Union[ListNode, None] = None

    def __len__(self) -> int:
        return self._size
    
    def __str__(self) -> str:
        resultado = " "
        actual = self._head
        while actual:
            resultado += str(actual.element) + "  "
            actual = actual.next
        return resultado[:-2] 
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def first(self) -> Any:
        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")
        
        return self._head.element
    
    def last(self) -> Any:
        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")
        return self._tail.element
    
    def add_first(self, elem : Any) -> None: 

        nuevo_nodo = ListNode(elem, self._head)
        if self.is_empty():
            self._head = nuevo_nodo
            self._tail = nuevo_nodo
        else:
            self._head = nuevo_nodo
        self._size += 1

    def add_last(self, element : Any) -> None:
        nuevo_nodo = ListNode(element, None)
        
        if self.is_empty():
            self._head = nuevo_nodo
            self._tail = nuevo_nodo
        else:
            self._tail.next = nuevo_nodo
            self._tail = self._tail.next
        self._size += 1

    def delete_first(self) -> None:
        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")
        self._head = self._head.next
        self._size -= 1

    def delete_last(self) -> None:
        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")
        nuevo_tail=self._head

        while nuevo_tail.next.next:
            nuevo_tail=nuevo_tail.next
        
        self._tail=nuevo_tail
        self._tail.next=None
        self._size-=1
    
