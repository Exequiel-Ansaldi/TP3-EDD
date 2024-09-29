from typing import Any
from abc import ABC, abstractmethod


class DequeAbstract(ABC):
    """Representa una estructura de datos lineal de acceso restringido
    que soporta inserción y eliminación por ambos extremos."""

    @abstractmethod
    def __len__(self) -> int:
        """Devuelve la cantidad actual de elementos en la estructura.

        Returns:
                                        int: Devuelve la cantidad de elementos, cero la si estructura está vacía.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Concatena en un único string todos los elementos almacenados
        en los nodos de la estructura.

        Returns:
                                        str: convierte en str todos los elementos y los concatena en un string.
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Indica si la estructura está vacía.

        Returns:
                                        bool: True si la estructura está vacía, False en caso contrario.
        """
        pass

    @abstractmethod
    def first(self) -> Any:
        """Devuelve el elemento ubicado en el frente de la estructura.

        Raises:
                                        Exception: Arroja excepción si la estructura está vacía.

        Returns:
                                        Any: Devuelve el elemento dato correspondiente al frente de la
                                        estructura.
        """
        pass

    @abstractmethod
    def last(self) -> Any:
        """Devuelve el elemento correspondiente al nodo ubicado al final de
        la estructura.

        Raises:
                                        Exception: Arroja excepción si la estructura está vacía.

        Returns:
                                        Any: Devuelve el elemento dato correspondiente al final de la estructura.
        """
        pass

    @abstractmethod
    def add_first(self, element: Any) -> None:
        """_summary_

        Args:
                                        element (Any): elemento que va a ser agregado al principio de la
                                        estructura.
        """
        pass

    @abstractmethod
    def add_last(self, element: Any) -> None:
        """Agrega un elemento al final de la estructura.

        Args:
                                        element (Any): elemento que va a ser agregado al final de la estructura.
        """
        pass

    @abstractmethod
    def delete_first(self) -> None:
        """Quita el elemento ubicado en el frente de la estructura.

        Raises:
                                        Exception: Arroja excepción si la estructura está vacía.
        """
        pass

    @abstractmethod
    def delete_last(self) -> None:
        """Quita el elemento ubicado al final de la estructura.

        Raises:
                                        Exception: Arroja excepción si la estructura está vacía.
        """
        pass
