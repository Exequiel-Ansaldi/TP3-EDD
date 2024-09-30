class Tramite ():

    def __init__(self, numero: int, apellido: str, nombre:str, requerimiento: str, terminada: int) -> None:
        self.numero = numero
        self.apellido = apellido
        self.nombre =nombre
        self.requerimiento = requerimiento
        self.terminada = terminada

    def __eq__(self, other):
        if isinstance(other, Tramite):
            return self.numero == other.numero
        return False

    def __str__(self):
        estado = "Terminada" if self.terminada else "En proceso"
        return (f"Trámite #{self.numero}\n"
                f"Nombre: {self.nombre}\n"
                f"Apellido: {self.apellido}\n"
                f"Requerimiento: {self.requerimiento}\n"
                f"Estado: {estado}\n")
    