from Persona import Persona 

class Estudiante(Persona):
    def __init__(self, nombre, edad, direccion, curso):
       
        super().__init__(nombre, edad, direccion)
        self._curso = curso

    def get_curso(self):
        return self._curso

    def set_curso(self, curso):
        self._curso = curso

    def __str__(self):
        
        return f"Datos estudiante: ({super().__str__()}, estan en el curso: {self._curso})"
