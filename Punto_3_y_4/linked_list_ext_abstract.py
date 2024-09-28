from abc import ABC, abstractmethod
from typing import Any, List

class LinkedListExtAbstract(ABC):
    
    @abstractmethod
    def __reversed__(self) -> None: 
        """Invierte el orden de los elementos en la lista utilizando un LinkedStack."""
        pass

    @abstractmethod
    def pop(self) -> None: 
        """Quita el último elemento de la estructura."""
        pass

    @abstractmethod
    def add_first(self, other: Any) -> None: 
        """Agrega el elemento al principio de la estructura.

        Args:
            other (Any): elemento a agregar en la lista.
        """
        pass

    @abstractmethod
    def __iadd__(self, other: List[Any]) -> None:
        """Agrega todos los elementos de other en la estructura actual.

        Args:
            other (List[Any]): se trata de una lista nativa python cuyos elementos se agregarán al principio de la actual.
        """
        pass