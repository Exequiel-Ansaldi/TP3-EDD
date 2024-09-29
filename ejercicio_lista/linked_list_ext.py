from linked_list import LinkedList
from linked_list_ext_abstract import LinkedListExtAbstract
from linked_stack import LinkedStack
from list_node import ListNode
from typing import Any, List

class LinkedListExt(LinkedList, LinkedListExtAbstract):
     
    def __reversed__(self) -> None:
        stack = LinkedStack()  
        actual = self._header
        while actual is not None:
            stack.push(actual.element)
            actual = actual.next
        actual = self._header
        while not stack.is_empty():
            actual.element = stack.pop()  
            actual = actual.next

    def pop(self) -> None:
        if self._header is None:  
            raise IndexError("Lista vacia")
        if self._header.next is None:
            self.header = None
        else:
            actual = self._header
        while actual.next and actual.next.next:
            actual = actual.next
        actual.next = None
        self._size -= 1 

    def add_first(self, other: Any) -> None:
        if other is not None:  # Ensure the element is not None
            nuevo_nodo = ListNode(other)  
            # If it's the first element, skip the dummy header
        if self._header.element is None and self._header.next is None:
            self._header = nuevo_nodo  # Replace the dummy header with the new node
        else:
            nuevo_nodo.next = self._header  # Point new node to the current first node
            self._header = nuevo_nodo  # Set the new node as the header
        self._size += 1

    def __iadd__(self, other: List[Any]) -> None:
        for elementos in reversed(other): 
            self.add_first(elementos)
        return self