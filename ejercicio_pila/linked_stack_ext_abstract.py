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

    