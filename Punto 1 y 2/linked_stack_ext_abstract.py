from abc import ABC, abstractmethod
from typing import Any, List

class LinkedStackExtAbstract(ABC):
    """Representa un conjunto de métodos para extender la implementación original
        de LinkedStack.
    """
    @abstractmethod
    def multi_pop(self, num: int) -> List[Any]:
        """Realiza la cantidad de operaciones pop() indicada por num.

        Args:
            num (int): número de veces que se va a ejecutar pop().

        Raises:
            Exception: Arroja excepción si se invoca a pop() por cuando la estructura
            está vacía.

        Returns:
            List[Any]: lista formada por todos los topes que se quitaron de la pila.
        """
        pass

    @abstractmethod
    def replace_all(self, param1: Any, param2: Any) -> None:
        """Reemplaza todas las ocurrencias de param1 en la pila por param2.

        Args:
            param1 (Any): Valor a buscar/reemplazar.
            param2 (Any): Nuevo valor.
        """
        pass

    @abstractmethod
    def __imul__(self, other: int) -> None:
        """Repite tantas veces como lo indique other los elmentos actuales de la pila y los inserta al final de la misma.

        Args:
            other (int): cantidad de veces que se deben repetir los elementos de la pila.
        """
        pass

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
        other (List[Any]): se trata de una lista nativa python cuyos elementos se
        agregarán al principio de la actual.
        """
        pass
