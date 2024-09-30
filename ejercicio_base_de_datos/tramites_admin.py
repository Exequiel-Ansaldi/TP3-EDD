import sqlite3
from typing import List, Optional
from tramite_db import Tramite
from linked_queue_ext_db import LinkedQueueExt

class TramitesAdmin:
    def __init__(self, db_name: str):
        """Inicializa el administrador de trámites y la conexión a la base de datos."""
        self.db_name = db_name
        self.tramites_queue = LinkedQueueExt()  # Cola para manejar trámites en memoria
        self.create_table()  # Crea la tabla si no existe

    def create_table(self):
        """Crea la tabla Tramite en la base de datos si no existe."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Tramite (
                                numero INTEGER PRIMARY KEY,
                                apellido TEXT NOT NULL,
                                nombre TEXT NOT NULL,
                                requerimiento TEXT NOT NULL,
                                terminada INTEGER NOT NULL)''')
            conn.commit()

    def add_tramite(self, tramite: Tramite) -> None:
        """Agrega un trámite a la cola y lo persiste en la base de datos."""
        self.tramites_queue.enqueue(tramite)
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO Tramite (numero, apellido, nombre, requerimiento, terminada) 
                              VALUES (?, ?, ?, ?, ?)''',
                           (tramite.numero, tramite.apellido, tramite.nombre, tramite.requerimiento, int(tramite.terminada)))
            conn.commit()

    def remove_tramite(self) -> Optional[Tramite]:
        """Quita el trámite del frente de la cola y lo elimina de la base de datos."""
        if not self.tramites_queue.is_empty():
            tramite = self.tramites_queue.dequeue()
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM Tramite WHERE numero = ?', (tramite.numero,))
                conn.commit()
            return tramite
        return None

    def list_tramites(self) -> List[Tramite]:
        """Devuelve una lista de todos los trámites desde la base de datos."""
        tramites = []
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Tramite')
            for row in cursor.fetchall():
                numero, apellido, nombre, requerimiento, terminada = row
                tramites.append(Tramite(numero, apellido, nombre, requerimiento, bool(terminada)))
        return tramites

    def mark_tramite_as_terminada(self, numero: int) -> None:
        """Marca un trámite como terminado en la base de datos."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE Tramite SET terminada = 1 WHERE numero = ?', (numero,))
            conn.commit()

    def load_tramites_from_db(self) -> None:
        """Carga todos los trámites de la base de datos a la cola."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Tramite')
            for row in cursor.fetchall():
                numero, apellido, nombre, requerimiento, terminada = row
                tramite = Tramite(numero, apellido, nombre, requerimiento, bool(terminada))
                self.tramites_queue.enqueue(tramite)
