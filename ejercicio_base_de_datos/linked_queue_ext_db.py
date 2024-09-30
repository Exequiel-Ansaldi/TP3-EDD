from linked_queue import LinkedQueue

class LinkedQueueExt(LinkedQueue):

    def __iter__(self):
        nodos = []
        actual = self._front  
        for _ in range(len(self)):  
            nodos.append(actual)  
            actual = actual.next
        for nodo in nodos:
            yield nodo.element