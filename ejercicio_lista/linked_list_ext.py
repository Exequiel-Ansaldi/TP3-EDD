from linked_list import LinkedList
from linked_list_ext_abstract import LinkedListExtAbstract
from linked_stack import LinkedStack
from list_node import ListNode
from typing import Any, List

class LinkedListExt(LinkedList, LinkedListExtAbstract):
     
    def __reversed__(self) -> None:
        stack = LinkedStack()  
        actual = self._header.next
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
       if other is not None:  
            new_node = ListNode(other)  
            new_node.next = self._header.next  
            self._header.next = new_node  
            self._size += 1 

    def __iadd__(self, other: List[Any]) -> None:
        for elementos in reversed(other): 
            self.add_first(elementos)
        return self