import sqlite3
from typing import List, Optional
from linked_queue import LinkedQueue
from tramite_db import Tramite
from linked_queue_ext_db import LinkedQueueExt

class TramitesAdmin:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.tramites_queue = LinkedQueueExt()  # Cola para manejar trámites en memoria
        self.create_table()  # Crea la tabla si no existe

    def cargar_tramites_desde_bd(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT numero, apellido, nombre, requerimiento, terminada FROM Tramite')
            tramites = cursor.fetchall()
            for numero, apellido, nombre, requerimiento, terminada in tramites:
                tramite = Tramite(numero, apellido, nombre, requerimiento, bool(terminada))
                self.tramites_queue.enqueue(tramite)
                # CREATE TABLE IF NOT EXISTS tramites (
                #                 numero INTEGER PRIMARY KEY,
                #                 apellido TEXT,
                #                 nombre TEXT,
                #                 requerimiento TEXT,
                #                 terminada INTEGER

    def create_table(self):
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
        self.tramites_queue.enqueue(tramite)
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO Tramite (numero, apellido, nombre, requerimiento, terminada) 
                              VALUES (?, ?, ?, ?, ?)''',
                           (tramite.numero, tramite.apellido, tramite.nombre, tramite.requerimiento, int(tramite.terminada)))
            conn.commit()

    def remove_tramite(self) -> Optional[Tramite]:
        if not self.tramites_queue.is_empty():
            tramite = self.tramites_queue.dequeue()
            if isinstance(tramite, Tramite):
                with sqlite3.connect(self.db_name) as conn:
                    cursor = conn.cursor()
                    cursor.execute('DELETE FROM Tramite WHERE numero = ?', (tramite.numero,))
                    conn.commit()
                return tramite
            else:
                print("El objeto eliminado no es una instancia de Tramite.")
        
        # Si la cola está vacía, devuelve None
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

    def load_tramites_from_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT numero, apellido, nombre, requerimiento, terminada FROM Tramite')
            tramites_data = cursor.fetchall()
            self.tramites_queue = LinkedQueue()
            for tramite_data in tramites_data:
                tramite = Tramite(
                    numero=tramite_data[0],
                    apellido=tramite_data[1],
                    nombre=tramite_data[2],
                    requerimiento=tramite_data[3],
                    terminada=bool(tramite_data[4])  # Convertir el INT de SQLite a bool
                )
                self.tramites_queue.enqueue(tramite)
