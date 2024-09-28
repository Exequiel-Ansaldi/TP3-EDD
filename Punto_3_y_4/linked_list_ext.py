from linked_list import LinkedList
from linked_list_ext_abstract import LinkedListExtAbstract
from Punto_1_y_2.linked_stack import LinkedStack
from list_node import ListNode
from typing import Any, List

class LinkedListExt(LinkedList, LinkedListExtAbstract):
     
    def __reversed__(self) -> None:
        stack = LinkedStack()  
        actual = self._header
        while actual is not None:
            stack.push(actual)
            actual = actual.next
        self[:] = [] 
        while not stack.is_empty():
            self.append(stack.pop())

    def pop(self) -> None:
        if self._header is None:  
            raise IndexError("Lista vacia")
        if self._header.next is None:
            self.header = None
            return
        current = self._header
        while current.next.next is not None:
            current = current.next
        current.next = None

    def add_first(self, other: Any) -> None:
        new_node = ListNode(other)  
        new_node.next = self.head
        self.head = new_node

    def __iadd__(self, other: List[Any]) -> None:
        for elementos in reversed(other): 
            self.add_first(elementos)
        return self