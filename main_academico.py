"""Vistas del negocio académico.

Estudiantes, Docentes y Materias usan el MenuCRUD de la parte 3 TAL CUAL (polimorfismo:
un solo menú, tres controladores). Solo Matrículas necesita una subclase, igual que
MenuVentas.
"""

from main import MenuCRUD                      # el menú genérico de la parte 3
from models_academico import Nota, Matricula
from shared.herramientas import (
    imprimir_titulo, imprimir_exito, imprimir_error, imprimir_info
)
from views_academico import (
    EstudianteController, DocenteController, MateriaController, MatriculaController
)


# =====================================================================
# HERENCIA + SOBRESCRITURA: MenuMatriculas es un MenuCRUD con extras
# =====================================================================
class MenuMatriculas(MenuCRUD):

    def __init__(self, controlador):
        super().__init__(controlador, "MATRÍCULAS")
        self._opciones["1"] = ("Matricular estudiante", self.crear)    # reemplaza la opción 1
        volver = self._opciones.pop("0")                               # para que "0" quede al final
        self._opciones["7"] = ("Agregar nota", self.agregar_nota)
        self._opciones["8"] = ("Ver boletín", self.ver_boletin)
        self._opciones["0"] = volver

    @staticmethod
    def mostrar_lista(titulo, objetos):
        imprimir_info(titulo)
        if not objetos:
            print("  (no hay registros)")
        for objeto in objetos:
            print(f"  {objeto}")           # POLIMORFISMO: __str__ -> etiqueta() de cada modelo

    def crear(self):
        """Sobrescribe: una matrícula necesita elegir un estudiante y una materia existentes."""
        imprimir_titulo("MATRICULAR ESTUDIANTE")
        self.mostrar_lista("Estudiantes:", self._controlador.estudiantes.listar())
        estudiante_id = self.pedir_entero("\nId del estudiante: ")
        if estudiante_id is None:
            imprimir_error("El id debe ser un número")
            return self.pausa()

        print()
        self.mostrar_lista("Materias:", self._controlador.materias.listar())
        materia_id = self.pedir_entero("\nId de la materia: ")
        if materia_id is None:
            imprimir_error("El id debe ser un número")
            return self.pausa()

        periodo = input(f"Periodo [{Matricula.PERIODO_DEFECTO}]: ")
        self.mostrar_resultado(*self._controlador.crear({
            "estudiante_id": estudiante_id,
            "materia_id": materia_id,
            "periodo": periodo,
        }))
        self.pausa()

    def agregar_nota(self):
        imprimir_titulo("AGREGAR NOTA")
        matricula_id = self.pedir_entero("Id de la matrícula: ")
        matricula = self._controlador.obtener(matricula_id) if matricula_id else None
        if matricula is None:
            imprimir_error("No existe esa matrícula")
            return self.pausa()

        imprimir_info(f"Matrícula: {matricula.etiqueta()}")
        print(f"Tipos permitidos: {', '.join(Nota.TIPOS)}")
        tipo = input("Tipo: ")
        valor = input(f"Nota ({Nota.MINIMA} a {Nota.MAXIMA}): ")
        peso = input("Peso [1]: ").strip() or 1
        self.mostrar_resultado(*self._controlador.agregar_nota(matricula_id, tipo, valor, peso))
        self.pausa()

    def ver_boletin(self):
        imprimir_titulo("BOLETÍN")
        self.mostrar_lista("Estudiantes:", self._controlador.estudiantes.listar())
        estudiante_id = self.pedir_entero("\nId del estudiante: ")
        texto = self._controlador.boletin(estudiante_id) if estudiante_id else None
        if texto is None:
            imprimir_error("No existe ese estudiante")
        else:
            print()
            print(texto)
        self.pausa()


# =====================================================================
# REPORTES POLIMÓRFICOS
# =====================================================================
def mostrar_objetos(objetos, sangria="  "):
    """POLIMORFISMO: no pregunta de qué clase es cada objeto; todos saben mostrarse
    con __str__ (que llama a etiqueta()). Sirve igual para docentes, materias, etc."""
    for objeto in objetos:
        print(f"{sangria}{objeto}")


def reporte_materias_por_docente(docentes, materias):
    imprimir_titulo("MATERIAS POR DOCENTE")
    lista_docentes = docentes.listar()
    if not lista_docentes:
        imprimir_info("No hay docentes registrados.")
    for docente in lista_docentes:
        asignadas = materias.materias_de_docente(docente.id)
        print(f"\n  {docente}  ->  {len(asignadas)} materia(s)")
        mostrar_objetos(asignadas, sangria="      ")

    sin_docente = [m for m in materias.listar() if m.docente_id is None]
    if sin_docente:
        print(f"\n  Sin docente asignado  ->  {len(sin_docente)} materia(s)")
        mostrar_objetos(sin_docente, sangria="      ")


def reporte_reprobados(matriculas):
    imprimir_titulo("ESTUDIANTES REPROBADOS")
    reprobadas = matriculas.reprobadas()
    if not reprobadas:
        imprimir_info("No hay matrículas reprobadas.")
        return
    for matricula in reprobadas:
        estudiante = matriculas.estudiantes.obtener(matricula.estudiante_id)
        materia = matriculas.materias.obtener(matricula.materia_id)
        quien = estudiante.nombre_completo if estudiante else f"estudiante {matricula.estudiante_id}"
        que = materia.nombre if materia else f"materia {matricula.materia_id}"
        print(f"  {quien} · {que} · {matricula.periodo} · promedio {matricula.promedio:.2f}"
              f" (mínimo {Matricula.NOTA_APROBACION})")
    imprimir_info(f"Total: {len(reprobadas)}")


class MenuReportes:
    def __init__(self, docentes, materias, matriculas):
        self._docentes = docentes
        self._materias = materias
        self._matriculas = matriculas
        self._activo = True

    def ejecutar(self):
        self._activo = True
        while self._activo:
            imprimir_titulo("REPORTES")
            print("  1. Materias por docente")
            print("  2. Estudiantes reprobados")
            print("  0. Volver\n")
            tecla = input("Opción: ").strip()
            if tecla == "1":
                reporte_materias_por_docente(self._docentes, self._materias)
                MenuCRUD.pausa()
            elif tecla == "2":
                reporte_reprobados(self._matriculas)
                MenuCRUD.pausa()
            elif tecla == "0":
                self._activo = False
            else:
                imprimir_error("Opción no válida")
                MenuCRUD.pausa()


# =====================================================================
class MenuPrincipal:

    def __init__(self):
        estudiantes = EstudianteController()
        docentes = DocenteController()
        materias = MateriaController(docentes)
        matriculas = MatriculaController(estudiantes, materias)

        self._activo = True
        # DICCIONARIO de menús: el MISMO MenuCRUD con tres controladores distintos
        self._menus = {
            "1": MenuCRUD(estudiantes, "ESTUDIANTES"),
            "2": MenuCRUD(docentes, "DOCENTES"),
            "3": MenuCRUD(materias, "MATERIAS"),
            "4": MenuMatriculas(matriculas),
            "5": MenuReportes(docentes, materias, matriculas),
        }

    def ejecutar(self):
        while self._activo:
            imprimir_titulo("SISTEMA ACADÉMICO")
            print("  1. Estudiantes")
            print("  2. Docentes")
            print("  3. Materias")
            print("  4. Matrículas y notas")
            print("  5. Reportes")
            print("  0. Salir\n")
            tecla = input("Opción: ").strip()

            if tecla == "0":
                imprimir_info("¡Hasta luego! 👋")
                self._activo = False
            elif tecla in self._menus:
                self._menus[tecla].ejecutar()
            else:
                imprimir_error("Opción no válida")
                MenuCRUD.pausa()


if __name__ == "__main__":
    try:
        MenuPrincipal().ejecutar()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
