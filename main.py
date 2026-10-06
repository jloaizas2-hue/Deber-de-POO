# Clase base Cliente
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

# Clase Estudiante que hereda o implementa la lógica utilizada en la imagen
class Estudiante:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.materias = []
        self.notas = {}

    def inscribir_materia(self, materia):
        if materia not in self.materias:
            self.materias.append(materia)

    def agregar_nota(self, materia, nota):
        self.inscribir_materia(materia)
        self.notas[materia] = nota

    def obtener_promedio(self):
        if not self.notas:
            return 0.0
        return sum(self.notas.values()) / len(self.notas)

    def materias_en_comun(self, otro_estudiante):
        return list(set(self.materias).intersection(set(otro_estudiante.materias)))

    def a_diccionario(self):
        return {
            "nombre": self.nombre,
            "cedula": self.cedula,
            "materias": self.materias,
            "notas": self.notas
        }

    @classmethod
    def desde_diccionario(cls, datos):
        est = cls(datos["nombre"], datos["cedula"])
        est.materias = datos.get("materias", [])
        est.notas = datos.get("notas", {})
        return est

    def __str__(self):
        return f"Estudiante({self.nombre}, Cedula: {self.cedula}, Materias: {len(self.materias)})"


# --- PRUEBAS DEL SCRIPT (main.py) ---
if __name__ == "__main__":
    est1 = Estudiante("CAMPOS CLIENTE", "1234567890")
    est2 = Estudiante("Cliente 2", "0987654321")

    print("\n--- inscribir_materia (Física repetida no debe duplicarse) ---")
    est1.inscribir_materia("Física")
    est1.inscribir_materia("Física")
    print(est1.materias)

    print("\n--- agregar_nota (también inscribe la materia) ---")
    est1.agregar_nota("Matemática", 18)
    est1.agregar_nota("Matemática", 19)  # Actualiza la nota
    est1.agregar_nota("Inglés", 17)
    est2.agregar_nota("Matemática", 15)
    est2.agregar_nota("Programación", 20)

    print("est1 notas:", est1.notas, "| materias:", est1.materias)
    print("est2 notas:", est2.notas, "| materias:", est2.materias)

    print("\n--- obtener_promedio ---")
    print("est1:", est1.obtener_promedio())
    print("est2:", est2.obtener_promedio())

    print("\n--- materias_en_comun ---")
    print(est1.materias_en_comun(est2))

    print("\n--- a_diccionario ---")
    datos = est1.a_diccionario()
    print(datos)

    print("\n--- desde_diccionario ---")
    copia = Estudiante.desde_diccionario(datos)
    print(copia)
    print("¿Mismas notas?", copia.notas == est1.notas)
    print("¿Mismas materias?", copia.materias == est1.materias)

    print("\n--- __str__ ---")
    print(est1)
    print(est2)
