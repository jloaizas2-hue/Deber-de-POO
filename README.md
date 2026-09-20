"""}}}
Soluciones — 20 Ejercicios: Clases y Colecciones con Métodos Reutilizables
Python · Unidad 1-2 (sin herencia)

Cada clase tiene:
  - __init__ que prepara las colecciones vacías
  - un método base que resuelve una tarea concreta
  - métodos que REUTILIZAN el método base (a veces con *args)

Al final hay un programa principal que prueba cada ejercicio con assert.
Ejecuta:  python soluciones_20_ejercicios.py
"""

import math


# ---------------------------------------------------------------------------
# Ej. 1 — Validador de notas con promedio
# ---------------------------------------------------------------------------
class Calificador:
    def __init__(self):
        self.notas = []                      # lista de notas válidas

    def validar_nota(self, nota):
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):      # reutiliza el validador
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)


# ---------------------------------------------------------------------------
# Ej. 2 — Contador de palabras únicas
# ---------------------------------------------------------------------------
class AnalizadorTexto:
    def __init__(self):
        self.unicas = set()                  # evita duplicados
        self.orden = []                      # conserva el orden de aparición

    def agregar_palabra(self, palabra):
        if palabra not in self.unicas:
            self.unicas.add(palabra)
            self.orden.append(palabra)

    def contar_palabras(self):
        return len(self.unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)    # reutiliza agregar_palabra
        return self.contar_palabras()


# ---------------------------------------------------------------------------
# Ej. 3 — Gestor de compras con totales
# ---------------------------------------------------------------------------
class CarroCompras:
    def __init__(self):
        self.articulos = {}                  # {nombre: precio}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []
        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)
        return resultado


# ---------------------------------------------------------------------------
# Ej. 4 — Inversor de secuencias
# (Corrección: las listas no pueden ser claves de un diccionario porque no son
#  hashables, así que la clave es la lista convertida a TUPLA.)
# ---------------------------------------------------------------------------
class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):   # de atrás hacia adelante
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            resultado[tuple(lista)] = self.invertir_lista(lista)
        return resultado


# ---------------------------------------------------------------------------
# Ej. 5 — Detector de pares e impares
# ---------------------------------------------------------------------------
class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        actual = {"pares": [], "impares": []}
        for n in numeros:
            if self.es_par(n):
                actual["pares"].append(n)
                self.pares.append(n)
            else:
                actual["impares"].append(n)
                self.impares.append(n)
        return actual

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))


# ---------------------------------------------------------------------------
# Ej. 6 — Estadísticas de temperatura
# ---------------------------------------------------------------------------
class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):
        for t in temps:
            self.registrar_temperatura(t)    # reutiliza el registro

    def minima(self):
        return min(self.temperaturas) if self.temperaturas else None

    def maxima(self):
        return max(self.temperaturas) if self.temperaturas else None

    def promedio(self):
        if not self.temperaturas:
            return None
        return sum(self.temperaturas) / len(self.temperaturas)


# ---------------------------------------------------------------------------
# Ej. 7 — Mapeador de edades
# ---------------------------------------------------------------------------
class GestorPersonas:
    def __init__(self):
        self.personas = {}                   # {nombre: edad}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        resultado = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)
        return resultado

    def edad_promedio(self):
        if not self.personas:
            return None
        return sum(self.personas.values()) / len(self.personas)


# ---------------------------------------------------------------------------
# Ej. 8 — Asignador de equipos
# ---------------------------------------------------------------------------
class Equipos:
    def __init__(self):
        self.equipos = {}                    # {equipo: [jugadores]}

    def crear_equipo(self, nombre_equipo):
        if nombre_equipo not in self.equipos:
            self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        if equipo not in self.equipos:
            self.crear_equipo(equipo)        # reutiliza crear_equipo
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mejor = None
        maximo = -1
        for nombre, jugadores in self.equipos.items():
            if len(jugadores) > maximo:
                maximo = len(jugadores)
                mejor = nombre
        return mejor                         # None si no hay equipos


# ---------------------------------------------------------------------------
# Ej. 9 — Validador de caracteres
# ---------------------------------------------------------------------------
class AnalizadorString:
    VOCALES = "aeiouáéíóúü"

    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return len(letra) == 1 and letra.lower() in self.VOCALES

    def es_consonante(self, letra):
        return letra.isalpha() and not self.solo_vocales(letra)

    def contar_por_tipo(self, texto):
        conteo = {"vocales": 0, "consonantes": 0, "digitos": 0}
        for c in texto:
            if self.solo_vocales(c):
                conteo["vocales"] += 1
            elif self.es_consonante(c):
                conteo["consonantes"] += 1
            elif c.isdigit():
                conteo["digitos"] += 1
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto
        return conteo


# ---------------------------------------------------------------------------
# Ej. 10 — Gestor de tareas con prioridad
# ---------------------------------------------------------------------------
class Tareas:
    def __init__(self):
        self.tareas = []                     # lista de tuplas (descripcion, prioridad)

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        resultado = []
        for tarea in self.tareas:
            if tarea[1] == "alta":
                resultado.append(tarea)
        return resultado

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                return True
        return False


# ---------------------------------------------------------------------------
# Ej. 11 — Contador de frecuencia
# ---------------------------------------------------------------------------
class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}                # {elemento: veces}

    def agregar_elemento(self, elemento):
        self.frecuencias[elemento] = self.frecuencias.get(elemento, 0) + 1

    def agregar_multiples(self, *elementos):
        for e in elementos:
            self.agregar_elemento(e)

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)

    def elemento_mas_frecuente(self):
        mejor = None
        maximo = 0
        for elemento, veces in self.frecuencias.items():
            if veces > maximo:
                maximo = veces
                mejor = elemento
        return mejor


# ---------------------------------------------------------------------------
# Ej. 12 — Selector de rango con tuplas
# ---------------------------------------------------------------------------
class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))          # fin incluido

    def elementos_en_multiples_rangos(self, *rangos):
        unicos = set()
        for inicio, fin in rangos:
            for n in self.crear_rango(inicio, fin):   # reutiliza crear_rango
                unicos.add(n)
        return sorted(unicos)


# ---------------------------------------------------------------------------
# Ej. 13 — Combinador de listas
# ---------------------------------------------------------------------------
class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        largo = max(len(lista1), len(lista2))
        for i in range(largo):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        # Aplica intercalar de a pares: ((l1 con l2) con l3) ...
        if len(listas) == 0:
            return []
        resultado = list(listas[0])
        for otra in listas[1:]:
            resultado = self.intercalar(resultado, otra)
        return resultado


# ---------------------------------------------------------------------------
# Ej. 14 — Mapeo de estudiantes a notas
# ---------------------------------------------------------------------------
class RegistroNotas:
    def __init__(self):
        self.notas = {}                      # {estudiante: nota}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        resultado = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                resultado.append(estudiante)
        return resultado

    def mejor_estudiante(self):
        mejor = None
        for estudiante, nota in self.notas.items():
            if mejor is None or nota > mejor[1]:
                mejor = (estudiante, nota)
        return mejor                         # tupla (nombre, nota) o None


# ---------------------------------------------------------------------------
# Ej. 15 — Divisores de un número
# ---------------------------------------------------------------------------
class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []
        for d in range(1, numero + 1):
            if numero % d == 0:
                divisores.append(d)
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)   # reutiliza
        return sum(divisores) - numero == numero        # sin contar el propio número

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for n in numeros:
            resultado[n] = self.encontrar_divisores(n)
        return resultado


# ---------------------------------------------------------------------------
# Ej. 16 — Codificador César
# ---------------------------------------------------------------------------
class CodificadorCesar:
    def __init__(self):
        self.historial = {}                  # {(palabra, desplazamiento): resultado}

    def codificar_letra(self, letra, desplazamiento):
        if "a" <= letra <= "z":
            base = ord("a")
        elif "A" <= letra <= "Z":
            base = ord("A")
        else:
            return letra                     # espacios, números, símbolos: igual
        return chr((ord(letra) - base + desplazamiento) % 26 + base)

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)
        self.historial[(palabra, desplazamiento)] = resultado
        return resultado

    def decodificar_palabra(self, palabra, desplazamiento):
        return self.codificar_palabra(palabra, -desplazamiento)


# ---------------------------------------------------------------------------
# Ej. 17 — Grupo de edades
# ---------------------------------------------------------------------------
class AgrupadorEdades:
    def __init__(self):
        self.grupos = {}                     # {categoria: [edades]}

    def clasificar_edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        if edad <= 11:
            return "niño"
        elif edad <= 17:
            return "adolescente"
        elif edad <= 59:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        actual = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)        # reutiliza
            actual.setdefault(categoria, []).append(edad)
            self.grupos.setdefault(categoria, []).append(edad)
        return actual

    def edad_promedio_categoria(self, categoria):
        edades = self.grupos.get(categoria, [])
        if not edades:
            return None
        return sum(edades) / len(edades)


# ---------------------------------------------------------------------------
# Ej. 18 — Matriz de distancias
# ---------------------------------------------------------------------------
class CalculadorDistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        d = math.sqrt(dx ** 2 + dy ** 2)
        self.distancias.append(d)
        return d

    def punto_mas_cercano(self, referencia, *puntos):
        cercano = None
        menor = None
        for punto in puntos:
            d = self.distancia_euclidiana(referencia, punto)   # reutiliza
            if menor is None or d < menor:
                menor = d
                cercano = punto
        return cercano


# ---------------------------------------------------------------------------
# Ej. 19 — Inventario de productos
# ---------------------------------------------------------------------------
class Inventario:
    def __init__(self):
        self.stock = {}                      # {producto: cantidad}

    def agregar_stock(self, producto, cantidad):
        self.stock[producto] = self.stock.get(producto, 0) + cantidad

    def restar_stock(self, producto, cantidad):
        if self.stock.get(producto, 0) >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        resultado = []
        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(producto)
        return resultado


# ---------------------------------------------------------------------------
# Ej. 20 — Analizador de patrones en textos
# ---------------------------------------------------------------------------
class AnalizadorPatrones:
    def __init__(self):
        self.palabras_vistas = set()

    def _separar(self, texto):
        """Divide el texto en palabras, quitando signos de puntuación."""
        palabras = []
        for p in texto.split():
            limpia = p.strip(".,;:!?¡¿\"'()")
            if limpia != "":
                palabras.append(limpia)
        return palabras

    def encontrar_palabras(self, texto, patron):
        resultado = []
        for p in self._separar(texto):
            self.palabras_vistas.add(p.lower())
            if p.lower().startswith(patron.lower()):
                resultado.append(p)
        return resultado

    def agrupar_por_longitud(self, texto):
        grupos = {}
        for p in self._separar(texto):
            self.palabras_vistas.add(p.lower())
            grupos.setdefault(len(p), []).append(p)
        return grupos

    def palabras_unicas(self):
        return self.palabras_vistas


# ===========================================================================
# PROGRAMA PRINCIPAL — prueba cada ejercicio
# ===========================================================================
def mostrar(n, titulo, *resultados):
    print(f"Ej. {n:>2} · {titulo}")
    for r in resultados:
        print("        ", r)


if __name__ == "__main__":
    # 1
    c = Calificador()
    validas = c.cargar_notas(85, 92, 110, 78, -5, 88)
    assert validas == [85, 92, 78, 88] and c.promedio() == 85.75
    mostrar(1, "Calificador", validas, c.promedio())

    # 2
    at = AnalizadorTexto()
    total = at.agregar_multiples("hola", "mundo", "hola")
    assert total == 2 and at.orden == ["hola", "mundo"]
    mostrar(2, "AnalizadorTexto", total, at.orden)

    # 3
    cc = CarroCompras()
    cc.agregar_articulo("pan", 2.50)
    cc.agregar_articulo("leche", 3.00)
    cc.agregar_articulo("queso", 8.00)
    assert cc.total_carrito() == 13.5
    assert cc.articulos_por_rango(2, 3) == ["pan", "leche"]
    mostrar(3, "CarroCompras", cc.total_carrito(), cc.articulos_por_rango(2, 3))

    # 4
    inv = InversorSecuencia()
    assert inv.invertir_lista([1, 2, 3]) == [3, 2, 1]
    multi = inv.invertir_multiples([1, 2, 3], ["a", "b"])
    assert multi == {(1, 2, 3): [3, 2, 1], ("a", "b"): ["b", "a"]}
    mostrar(4, "InversorSecuencia", inv.invertir_lista([1, 2, 3]), multi)

    # 5
    an = AnalizadorNumeros()
    sep = an.separar(1, 2, 3, 4, 5)
    assert sep == {"pares": [2, 4], "impares": [1, 3, 5]}
    assert an.cantidad_pares_impares() == (2, 3)
    mostrar(5, "AnalizadorNumeros", sep, an.cantidad_pares_impares())

    # 6
    gt = GestorTemperatura()
    gt.registrar_multiples(20, 25, 18, 30)
    assert (gt.minima(), gt.maxima(), gt.promedio()) == (18, 30, 23.25)
    mostrar(6, "GestorTemperatura", gt.minima(), gt.maxima(), gt.promedio())

    # 7
    gp = GestorPersonas()
    gp.agregar_persona("Ana", 28)
    gp.agregar_persona("Bob", 17)
    assert gp.personas_mayores(18) == ["Ana"] and gp.edad_promedio() == 22.5
    mostrar(7, "GestorPersonas", gp.personas_mayores(18), gp.edad_promedio())

    # 8
    eq = Equipos()
    eq.crear_equipo("A")
    eq.agregar_jugador("A", "Juan")
    eq.agregar_jugador("A", "Pedro")
    eq.crear_equipo("B")
    eq.agregar_jugador("B", "Luis")
    assert eq.equipo_mayor_integrantes() == "A"
    mostrar(8, "Equipos", eq.equipos, eq.equipo_mayor_integrantes())

    # 9
    astr = AnalizadorString()
    r9 = astr.contar_por_tipo("Hola123")
    assert r9 == {"vocales": 2, "consonantes": 2, "digitos": 3}
    astr.contar_por_tipo("Python")
    assert astr.texto_mas_largo == "Hola123"
    mostrar(9, "AnalizadorString", r9, astr.texto_mas_largo)

    # 10
    t = Tareas()
    t.agregar_tarea("Estudiar", "alta")
    t.agregar_tarea("Leer", "baja")
    assert t.tareas_prioritarias() == [("Estudiar", "alta")]
    assert t.eliminar_completada("Estudiar") is True
    assert t.tareas == [("Leer", "baja")]
    mostrar(10, "Tareas", t.tareas_prioritarias(), t.tareas)

    # 11
    cf = ContadorFrecuencia()
    cf.agregar_multiples("a", "b", "a")
    assert cf.elemento_mas_frecuente() == "a" and cf.frecuencia_elemento("a") == 2
    mostrar(11, "ContadorFrecuencia", cf.elemento_mas_frecuente(), cf.frecuencias)

    # 12
    sr = SelectorRango()
    r12 = sr.elementos_en_multiples_rangos((1, 3), (2, 4))
    assert r12 == [1, 2, 3, 4] and sr.crear_rango(1, 3) == (1, 2, 3)
    mostrar(12, "SelectorRango", r12)

    # 13
    cl = CombinadorListas()
    assert cl.intercalar([1, 2], [3, 4]) == [1, 3, 2, 4]
    assert cl.intercalar([1, 2, 3], ["a"]) == [1, "a", 2, 3]
    mostrar(13, "CombinadorListas", cl.intercalar([1, 2], [3, 4]),
            cl.intercalar_multiples([1, 2], [3, 4], [5, 6]))

    # 14
    rn = RegistroNotas()
    rn.registrar("Ana", 95)
    rn.registrar("Bob", 70)
    assert rn.mejor_estudiante() == ("Ana", 95)
    assert rn.estudiantes_aprobados(71) == ["Ana"]
    mostrar(14, "RegistroNotas", rn.mejor_estudiante(), rn.estudiantes_aprobados(71))

    # 15
    df = DivisorFinder()
    assert df.encontrar_divisores(12) == (1, 2, 3, 4, 6, 12)
    assert df.es_perfecto(6) and not df.es_perfecto(12)
    r15 = df.encontrar_multiples_divisores(6, 7)
    assert r15 == {6: (1, 2, 3, 6), 7: (1, 7)}
    mostrar(15, "DivisorFinder", df.encontrar_divisores(12), df.es_perfecto(6), r15)

    # 16
    ces = CodificadorCesar()
    cod = ces.codificar_palabra("hola", 3)
    assert cod == "krod"
    assert ces.decodificar_palabra("krod", 3) == "hola"
    assert ces.codificar_palabra("xyz", 3) == "abc"
    mostrar(16, "CodificadorCesar", cod, ces.historial)

    # 17
    ae = AgrupadorEdades()
    r17 = ae.agrupar_por_categoria(5, 15, 30, 70)
    assert r17 == {"niño": [5], "adolescente": [15], "adulto": [30], "mayor": [70]}
    ae.agrupar_por_categoria(40)
    assert ae.edad_promedio_categoria("adulto") == 35
    mostrar(17, "AgrupadorEdades", r17, ae.edad_promedio_categoria("adulto"))

    # 18
    cd = CalculadorDistancia()
    assert cd.distancia_euclidiana((0, 0), (3, 4)) == 5.0
    cercano = cd.punto_mas_cercano((0, 0), (5, 5), (1, 1), (3, 4))
    assert cercano == (1, 1)
    mostrar(18, "CalculadorDistancia", 5.0, cercano, cd.distancias)

    # 19
    iv = Inventario()
    iv.agregar_stock("pan", 50)
    assert iv.restar_stock("pan", 30) is True
    assert iv.restar_stock("pan", 100) is False
    # Corrección: quedan 20 y 20 no es menor que 15, así que con 15 da [].
    assert iv.productos_bajo_stock(15) == []
    assert iv.productos_bajo_stock(25) == ["pan"]
    mostrar(19, "Inventario", iv.stock, iv.productos_bajo_stock(15),
            iv.productos_bajo_stock(25))

    # 20
    ap = AnalizadorPatrones()
    r20 = ap.agrupar_por_longitud("el gato está aquí")
    # Corrección: gato, está y aquí tienen 4 letras.
    assert r20 == {2: ["el"], 4: ["gato", "está", "aquí"]}
    assert ap.encontrar_palabras("el gato y la gata", "ga") == ["gato", "gata"]
    assert "gato" in ap.palabras_unicas()
    mostrar(20, "AnalizadorPatrones", r20, sorted(ap.palabras_unicas()))

    
    # ===========================================================================
    # Ej. 21 — Biblioteca de libros
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Crea una clase Biblioteca con un diccionario {titulo: autor}.
    #   - agregar_libro(titulo, autor)
    #   - libros_de_autor(autor): lista de títulos de ese autor
    #   - autores_unicos(): conjunto con los autores sin repetir
    #   - agregar_multiples(*libros): cada libro es una tupla (titulo, autor);
    #     reutiliza agregar_libro y devuelve la cantidad total de libros
    # EJEMPLO: agregar ("Rayuela","Cortázar"), ("Bestiario","Cortázar"), ("Ficciones","Borges")
    #   libros_de_autor("Cortázar") → ["Rayuela", "Bestiario"]
    #   autores_unicos()            → {"Cortázar", "Borges"}
    # ===========================================================================


    class Biblioteca:
        def __init__(self):
            self.libros = {}  # {titulo: autor}

        def agregar_libro(self, titulo, autor):
            self.libros[titulo] = autor

        def libros_de_autor(self, autor):
            resultado = []
            for titulo, a in self.libros.items():
                if a == autor:
                    resultado.append(titulo)
            return resultado

        def autores_unicos(self):
            return set(self.libros.values())

        def agregar_multiples(self, *libros):
            for titulo, autor in libros:
                self.agregar_libro(titulo, autor)  # reutiliza agregar_libro
            return len(self.libros)


    # ===========================================================================
    # Ej. 22 — Lista de asistencia
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase ListaAsistencia con un conjunto de presentes.
    #   - registrar(nombre)
    #   - registrar_multiples(*nombres): reutiliza registrar
    #   - faltantes(curso): lista ORDENADA de los del curso que no vinieron
    #   - porcentaje_asistencia(curso): % de alumnos del curso que vinieron
    # EJEMPLO: curso = ["Ana","Bob","Eva","Leo"]; registrar_multiples("Ana","Eva")
    #   faltantes(curso) → ["Bob","Leo"]     porcentaje_asistencia(curso) → 50.0
    # ===========================================================================
    class ListaAsistencia:
        def __init__(self):
            self.presentes = set()

        def registrar(self, nombre):
            self.presentes.add(nombre)

        def registrar_multiples(self, *nombres):
            for nombre in nombres:
                self.registrar(nombre)

        def faltantes(self, curso):
            return sorted(set(curso) - self.presentes)

        def porcentaje_asistencia(self, curso):
            if len(curso) == 0:
                return 0
            vinieron = len(curso) - len(self.faltantes(curso))  # reutiliza faltantes
            return vinieron * 100 / len(curso)


    # ===========================================================================
    # Ej. 23 — Conversor de temperaturas
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase ConversorTemperatura con un historial (lista de tuplas).
    #   - celsius_a_fahrenheit(c): F = C * 9/5 + 32; guarda (c, f) en el historial
    #   - fahrenheit_a_celsius(f): C = (F - 32) * 5/9
    #   - convertir_multiples(*celsius): lista con las conversiones (reutiliza)
    # EJEMPLO: celsius_a_fahrenheit(100) → 212.0
    #   convertir_multiples(0, 100, -40) → [32.0, 212.0, -40.0]
    # ===========================================================================
    class ConversorTemperatura:
        def __init__(self):
            self.historial = []  # [(celsius, fahrenheit)]

        def celsius_a_fahrenheit(self, c):
            f = c * 9 / 5 + 32
            self.historial.append((c, f))
            return f

        def fahrenheit_a_celsius(self, f):
            return (f - 32) * 5 / 9

        def convertir_multiples(self, *celsius):
            resultado = []
            for c in celsius:
                resultado.append(self.celsius_a_fahrenheit(c))  # reutiliza
            return resultado


    # ===========================================================================
    # Ej. 24 — Analizador de palabras de un texto
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase AnalizadorPalabras con una lista de palabras.
    #   - cargar_texto(texto): agrega las palabras (sin signos . , ; : ! ?) y
    #     devuelve cuántas palabras hay en total
    #   - palabra_mas_larga(): la primera más larga (None si no hay)
    #   - palabras_mayores_a(n): lista de palabras con más de n letras
    #   - longitud_promedio(): promedio de letras por palabra
    # EJEMPLO: cargar_texto("Python es muy divertido.")
    #   palabra_mas_larga() → "divertido"    palabras_mayores_a(4) → ["Python","divertido"]
    # ===========================================================================
    class AnalizadorPalabras:
        def __init__(self):
            self.palabras = []

        def cargar_texto(self, texto):
            for p in texto.split():
                limpia = p.strip(".,;:!?¡¿")
                if limpia != "":
                    self.palabras.append(limpia)
            return len(self.palabras)

        def palabra_mas_larga(self):
            mejor = None
            for p in self.palabras:
                if mejor is None or len(p) > len(mejor):
                    mejor = p
            return mejor

        def palabras_mayores_a(self, n):
            resultado = []
            for p in self.palabras:
                if len(p) > n:
                    resultado.append(p)
            return resultado

        def longitud_promedio(self):
            if not self.palabras:
                return None
            total = 0
            for p in self.palabras:
                total += len(p)
            return total / len(self.palabras)


    # ===========================================================================
    # Ej. 25 — Pila (stack)
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase Pila con una lista (el último en entrar es el primero en salir).
    #   - apilar(elemento) y apilar_multiples(*elementos)
    #   - desapilar(): quita y devuelve el tope (None si está vacía)
    #   - ver_tope(): devuelve el tope sin quitarlo
    #   - esta_vacia()
    #   - invertir_texto(texto): usa la pila para devolver el texto al revés
    # EJEMPLO: apilar_multiples(1, 2, 3) → desapilar() → 3, ver_tope() → 2
    #   invertir_texto("hola") → "aloh"
    # ===========================================================================
    class Pila:
        def __init__(self):
            self.elementos = []

        def apilar(self, elemento):
            self.elementos.append(elemento)

        def apilar_multiples(self, *elementos):
            for e in elementos:
                self.apilar(e)  # reutiliza apilar

        def desapilar(self):
            if self.esta_vacia():
                return None
            return self.elementos.pop()

        def ver_tope(self):
            if self.esta_vacia():
                return None
            return self.elementos[-1]

        def esta_vacia(self):
            return len(self.elementos) == 0

        def invertir_texto(self, texto):
            for letra in texto:
                self.apilar(letra)
            invertido = ""
            for _ in range(len(texto)):
                invertido += self.desapilar()
            return invertido


    # ===========================================================================
    # Ej. 26 — Cola de turnos
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase ColaTurnos (el primero en llegar es el primero en salir).
    #   - encolar(cliente) y encolar_multiples(*clientes)
    #   - atender(): saca al primero de la fila, lo guarda en "atendidos" y lo
    #     devuelve (None si no hay nadie)
    #   - siguiente(): quién sigue, sin sacarlo
    #   - cantidad_en_espera()
    # EJEMPLO: encolar_multiples("Ana","Bob","Eva"); atender() → "Ana"
    #   siguiente() → "Bob"; cantidad_en_espera() → 2
    # ===========================================================================
    class ColaTurnos:
        def __init__(self):
            self.fila = []
            self.atendidos = []

        def encolar(self, cliente):
            self.fila.append(cliente)

        def encolar_multiples(self, *clientes):
            for c in clientes:
                self.encolar(c)  # reutiliza encolar

        def atender(self):
            if len(self.fila) == 0:
                return None
            cliente = self.fila.pop(0)
            self.atendidos.append(cliente)
            return cliente

        def siguiente(self):
            return self.fila[0] if self.fila else None

        def cantidad_en_espera(self):
            return len(self.fila)


    # ===========================================================================
    # Ej. 27 — Agenda de contactos
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase Agenda con un diccionario {nombre: telefono}.
    #   - agregar_contacto(nombre, telefono)
    #   - telefono_de(nombre): el teléfono o None si no existe
    #   - buscar_por_prefijo(prefijo): nombres ORDENADOS que empiezan con ese
    #     prefijo (sin importar mayúsculas)
    #   - eliminar_contacto(nombre): True si lo eliminó, False si no existía
    # EJEMPLO: agregar Ana, Andrés, Bruno → buscar_por_prefijo("an") → ["Ana","Andrés"]
    # ===========================================================================
    class Agenda:
        def __init__(self):
            self.contactos = {}

        def agregar_contacto(self, nombre, telefono):
            self.contactos[nombre] = telefono

        def telefono_de(self, nombre):
            return self.contactos.get(nombre)

        def buscar_por_prefijo(self, prefijo):
            resultado = []
            for nombre in self.contactos:
                if nombre.lower().startswith(prefijo.lower()):
                    resultado.append(nombre)
            return sorted(resultado)

        def eliminar_contacto(self, nombre):
            if nombre in self.contactos:
                del self.contactos[nombre]
                return True
            return False


    # ===========================================================================
    # Ej. 28 — Detector de palíndromos
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase DetectorPalindromos con una lista "encontrados".
    #   - normalizar(texto): minúsculas y solo letras/números (sin espacios)
    #   - es_palindromo(texto): True si se lee igual al derecho y al revés
    #     (un texto vacío NO es palíndromo)
    #   - filtrar_palindromos(*textos): devuelve los que sí lo son y los guarda
    #     en "encontrados"
    # EJEMPLO: es_palindromo("Anita lava la tina") → True
    #   filtrar_palindromos("ana", "hola", "oso") → ["ana", "oso"]
    # ===========================================================================
    class DetectorPalindromos:
        def __init__(self):
            self.encontrados = []

        def normalizar(self, texto):
            limpio = ""
            for c in texto.lower():
                if c.isalnum():
                    limpio += c
            return limpio

        def es_palindromo(self, texto):
            limpio = self.normalizar(texto)
            if limpio == "":
                return False
            izq, der = 0, len(limpio) - 1
            while izq < der:
                if limpio[izq] != limpio[der]:
                    return False
                izq += 1
                der -= 1
            return True

        def filtrar_palindromos(self, *textos):
            resultado = []
            for t in textos:
                if self.es_palindromo(t):  # reutiliza es_palindromo
                    resultado.append(t)
                    self.encontrados.append(t)
            return resultado


    # ===========================================================================
    # Ej. 29 — Estadísticas descriptivas
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase Estadisticas con una lista de datos.
    #   - cargar(*numeros)
    #   - media(), mediana(), moda(), rango() (máximo - mínimo)
    #   - moda: el valor más repetido (si hay empate, el menor)
    #   - si no hay datos, todos devuelven None
    # EJEMPLO: cargar(4, 1, 2, 2, 3) → media 2.4, mediana 2, moda 2, rango 3
    #   con (1, 2, 3, 4) la mediana es 2.5
    # ===========================================================================
    class Estadisticas:
        def __init__(self):
            self.datos = []

        def cargar(self, *numeros):
            for n in numeros:
                self.datos.append(n)

        def media(self):
            if not self.datos:
                return None
            return sum(self.datos) / len(self.datos)

        def mediana(self):
            if not self.datos:
                return None
            ordenados = sorted(self.datos)
            n = len(ordenados)
            medio = n // 2
            if n % 2 == 1:
                return ordenados[medio]
            return (ordenados[medio - 1] + ordenados[medio]) / 2

        def moda(self):
            if not self.datos:
                return None
            frecuencias = {}
            for d in self.datos:
                frecuencias[d] = frecuencias.get(d, 0) + 1
            mejor = None
            for valor in sorted(frecuencias):  # ordenado → gana el menor en empate
                if mejor is None or frecuencias[valor] > frecuencias[mejor]:
                    mejor = valor
            return mejor

        def rango(self):
            if not self.datos:
                return None
            return max(self.datos) - min(self.datos)


    # ===========================================================================
    # Ej. 30 — Eliminador de duplicados
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase LimpiadorListas.
    #   - eliminar_duplicados(lista): nueva lista sin repetidos, conservando el
    #     orden de aparición
    #   - duplicados_encontrados(lista): conjunto con los elementos repetidos
    #   - limpiar_multiples(*listas): lista con cada lista ya limpia (reutiliza)
    # EJEMPLO: eliminar_duplicados([1,2,2,3,1]) → [1,2,3]
    #   duplicados_encontrados([1,2,2,3,1]) → {1, 2}
    # ===========================================================================
    class LimpiadorListas:
        def eliminar_duplicados(self, lista):
            vistos = set()
            resultado = []
            for e in lista:
                if e not in vistos:
                    vistos.add(e)
                    resultado.append(e)
            return resultado

        def duplicados_encontrados(self, lista):
            conteo = {}
            for e in lista:
                conteo[e] = conteo.get(e, 0) + 1
            repetidos = set()
            for e, veces in conteo.items():
                if veces > 1:
                    repetidos.add(e)
            return repetidos

        def limpiar_multiples(self, *listas):
            resultado = []
            for lista in listas:
                resultado.append(self.eliminar_duplicados(lista))  # reutiliza
            return resultado


    # ===========================================================================
    # Ej. 31 — Matriz con listas anidadas
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase Matriz con una lista de listas.
    #   - crear(filas, columnas, valor=0): llena la matriz con ese valor
    #   - asignar(i, j, valor)
    #   - suma_fila(i) y suma_columna(j)
    #   - suma_total(): reutiliza suma_fila
    #   - transpuesta(): devuelve una nueva matriz con filas y columnas cambiadas
    # EJEMPLO: crear(2, 3, 1); asignar(0, 1, 5) → [[1,5,1],[1,1,1]]
    #   suma_fila(0) → 7; suma_columna(1) → 6; suma_total() → 10
    #   transpuesta() → [[1,1],[5,1],[1,1]]
    # ===========================================================================
    class Matriz:
        def __init__(self):
            self.matriz = []

        def crear(self, filas, columnas, valor=0):
            self.matriz = []
            for _ in range(filas):
                fila = []
                for _ in range(columnas):
                    fila.append(valor)
                self.matriz.append(fila)

        def asignar(self, i, j, valor):
            self.matriz[i][j] = valor

        def suma_fila(self, i):
            return sum(self.matriz[i])

        def suma_columna(self, j):
            total = 0
            for fila in self.matriz:
                total += fila[j]
            return total

        def suma_total(self):
            total = 0
            for i in range(len(self.matriz)):
                total += self.suma_fila(i)  # reutiliza suma_fila
            return total

        def transpuesta(self):
            if not self.matriz:
                return []
            resultado = []
            for j in range(len(self.matriz[0])):
                nueva_fila = []
                for i in range(len(self.matriz)):
                    nueva_fila.append(self.matriz[i][j])
                resultado.append(nueva_fila)
            return resultado


    # ===========================================================================
    # Ej. 32 — Estacionamiento
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase Estacionamiento(capacidad) con un conjunto de placas.
    #   - ingresar(placa): True si entró; False si ya está adentro o está lleno
    #   - salir(placa): True si salió; False si no estaba
    #   - espacios_libres()
    #   - ingresar_multiples(*placas): reutiliza ingresar y devuelve la lista de
    #     placas que fueron RECHAZADAS
    # EJEMPLO: capacidad 2 → ingresar("A") True, ingresar("B") True, ingresar("C") False
    #   ingresar_multiples("D","E") con el lugar lleno → ["D","E"]
    # ===========================================================================
    class Estacionamiento:
        def __init__(self, capacidad):
            self.capacidad = capacidad
            self.placas = set()

        def ingresar(self, placa):
            if placa in self.placas or len(self.placas) >= self.capacidad:
                return False
            self.placas.add(placa)
            return True

        def salir(self, placa):
            if placa in self.placas:
                self.placas.remove(placa)
                return True
            return False

        def espacios_libres(self):
            return self.capacidad - len(self.placas)

        def ingresar_multiples(self, *placas):
            rechazadas = []
            for p in placas:
                if not self.ingresar(p):  # reutiliza ingresar
                    rechazadas.append(p)
            return rechazadas


    # ===========================================================================
    # Ej. 33 — Sistema de votación
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase Votacion con un diccionario {candidato: votos}.
    #   - votar(candidato)
    #   - votar_multiples(*candidatos): reutiliza votar
    #   - total_votos()
    #   - ganador(): candidato con más votos (None si no hay votos)
    #   - porcentaje(candidato): % de votos que obtuvo
    # EJEMPLO: votar_multiples("Ana","Bob","Ana","Ana","Bob")
    #   ganador() → "Ana"    porcentaje("Ana") → 60.0
    # ===========================================================================
    class Votacion:
        def __init__(self):
            self.votos = {}

        def votar(self, candidato):
            self.votos[candidato] = self.votos.get(candidato, 0) + 1

        def votar_multiples(self, *candidatos):
            for c in candidatos:
                self.votar(c)

        def total_votos(self):
            return sum(self.votos.values())

        def ganador(self):
            mejor = None
            for candidato, cantidad in self.votos.items():
                if mejor is None or cantidad > self.votos[mejor]:
                    mejor = candidato
            return mejor

        def porcentaje(self, candidato):
            total = self.total_votos()
            if total == 0:
                return 0
            return self.votos.get(candidato, 0) * 100 / total


    # ===========================================================================
    # Ej. 34 — Ordenador manual (burbuja)
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase OrdenadorManual. SIN usar sort() ni sorted().
    #   - ordenar(lista, descendente=False): devuelve una lista nueva ordenada
    #     usando el método burbuja (comparar vecinos e intercambiar)
    #   - es_ordenada(lista): True si ya está en orden ascendente
    #   - ordenar_multiples(*listas): lista con cada lista ordenada (reutiliza)
    # EJEMPLO: ordenar([5,2,9,1]) → [1,2,5,9]; ordenar([5,2,9,1], True) → [9,5,2,1]
    # ===========================================================================
    class OrdenadorManual:
        def ordenar(self, lista, descendente=False):
            copia = list(lista)  # no modifica la original
            n = len(copia)
            for i in range(n - 1):
                for j in range(n - 1 - i):
                    if descendente:
                        cambiar = copia[j] < copia[j + 1]
                    else:
                        cambiar = copia[j] > copia[j + 1]
                    if cambiar:
                        copia[j], copia[j + 1] = copia[j + 1], copia[j]
            return copia

        def es_ordenada(self, lista):
            for i in range(len(lista) - 1):
                if lista[i] > lista[i + 1]:
                    return False
            return True

        def ordenar_multiples(self, *listas):
            resultado = []
            for lista in listas:
                resultado.append(self.ordenar(lista))  # reutiliza ordenar
            return resultado


    # ===========================================================================
    # Ej. 35 — Diccionario invertido
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase InversorDiccionario.
    #   - invertir(d): devuelve {valor: [claves]} (varias claves pueden compartir valor)
    #   - claves_con_valor(d, valor): lista de claves que tienen ese valor
    #     (reutiliza invertir)
    #   - valores_repetidos(d): conjunto de valores que aparecen en 2+ claves
    # EJEMPLO: d = {"a":1, "b":2, "c":1}
    #   invertir(d) → {1:["a","c"], 2:["b"]}     valores_repetidos(d) → {1}
    # ===========================================================================
    class InversorDiccionario:
        def invertir(self, d):
            resultado = {}
            for clave, valor in d.items():
                if valor not in resultado:
                    resultado[valor] = []
                resultado[valor].append(clave)
            return resultado

        def claves_con_valor(self, d, valor):
            return self.invertir(d).get(valor, [])

        def valores_repetidos(self, d):
            repetidos = set()
            for valor, claves in self.invertir(d).items():
                if len(claves) > 1:
                    repetidos.add(valor)
            return repetidos


    # ===========================================================================
    # Ej. 36 — Ventas mensuales
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase VentasMensuales con un diccionario {mes: [montos]}.
    #   - registrar_venta(mes, monto)
    #   - registrar_multiples(mes, *montos): reutiliza registrar_venta
    #   - total_mes(mes): suma del mes (0 si no hay ventas)
    #   - mes_mayor_venta(): el mes con mayor total (None si no hay)
    #   - total_anual(): suma de todos los meses (reutiliza total_mes)
    # EJEMPLO: enero 100 y 200; febrero 150; marzo 500
    #   total_mes("enero") → 300    mes_mayor_venta() → "marzo"    total_anual() → 950
    # ===========================================================================
    class VentasMensuales:
        def __init__(self):
            self.ventas = {}

        def registrar_venta(self, mes, monto):
            if mes not in self.ventas:
                self.ventas[mes] = []
            self.ventas[mes].append(monto)

        def registrar_multiples(self, mes, *montos):
            for m in montos:
                self.registrar_venta(mes, m)

        def total_mes(self, mes):
            return sum(self.ventas.get(mes, []))

        def mes_mayor_venta(self):
            mejor = None
            for mes in self.ventas:
                if mejor is None or self.total_mes(mes) > self.total_mes(mejor):
                    mejor = mes
            return mejor

        def total_anual(self):
            total = 0
            for mes in self.ventas:
                total += self.total_mes(mes)
            return total


    # ===========================================================================
    # Ej. 37 — Operaciones con conjuntos
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase OperacionesConjuntos. Todos los métodos reciben listas y
    # devuelven una lista ORDENADA sin repetidos.
    #   - union(l1, l2), interseccion(l1, l2)
    #   - diferencia(l1, l2): los de l1 que no están en l2
    #   - diferencia_simetrica(l1, l2): los que están en uno solo de los dos
    #   - interseccion_multiples(*listas): lo común a TODAS (reutiliza interseccion)
    # EJEMPLO: [1,2,3] y [2,3,4] → unión [1,2,3,4], intersección [2,3],
    #   diferencia [1], simétrica [1,4]
    # ===========================================================================
    class OperacionesConjuntos:
        def union(self, l1, l2):
            return sorted(set(l1) | set(l2))

        def interseccion(self, l1, l2):
            return sorted(set(l1) & set(l2))

        def diferencia(self, l1, l2):
            return sorted(set(l1) - set(l2))

        def diferencia_simetrica(self, l1, l2):
            return sorted(set(l1) ^ set(l2))

        def interseccion_multiples(self, *listas):
            if len(listas) == 0:
                return []
            comun = sorted(set(listas[0]))
            for otra in listas[1:]:
                comun = self.interseccion(comun, otra)  # reutiliza interseccion
            return comun


    # ===========================================================================
    # Ej. 38 — Validador de contraseñas
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase ValidadorContrasena con un conjunto "seguras".
    #   - requisitos_faltantes(clave): lista con lo que le falta. Requisitos:
    #     "8 caracteres", "mayúscula", "minúscula", "número"
    #   - es_segura(clave): True si no le falta nada (reutiliza requisitos_faltantes)
    #   - evaluar_multiples(*claves): diccionario {clave: True/False}; guarda las
    #     seguras en el conjunto
    # EJEMPLO: requisitos_faltantes("hola") → ["8 caracteres","mayúscula","número"]
    #   es_segura("Hola1234") → True
    # ===========================================================================
    class ValidadorContrasena:
        def __init__(self):
            self.seguras = set()

        def requisitos_faltantes(self, clave):
            faltan = []
            if len(clave) < 8:
                faltan.append("8 caracteres")
            tiene_may = tiene_min = tiene_num = False
            for c in clave:
                if c.isupper():
                    tiene_may = True
                elif c.islower():
                    tiene_min = True
                elif c.isdigit():
                    tiene_num = True
            if not tiene_may:
                faltan.append("mayúscula")
            if not tiene_min:
                faltan.append("minúscula")
            if not tiene_num:
                faltan.append("número")
            return faltan

        def es_segura(self, clave):
            return len(self.requisitos_faltantes(clave)) == 0

        def evaluar_multiples(self, *claves):
            resultado = {}
            for clave in claves:
                segura = self.es_segura(clave)  # reutiliza es_segura
                resultado[clave] = segura
                if segura:
                    self.seguras.add(clave)
            return resultado


    # ===========================================================================
    # Ej. 39 — Puntos por cuadrante
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase GestorPuntos con una lista de tuplas (x, y).
    #   - cuadrante(punto): 1 (x>0,y>0), 2 (x<0,y>0), 3 (x<0,y<0), 4 (x>0,y<0);
    #     0 si está sobre algún eje
    #   - agrupar_por_cuadrante(*puntos): diccionario {cuadrante: [puntos]}
    #     (reutiliza cuadrante y guarda los puntos en la lista)
    #   - punto_mas_lejano(): el punto más lejos del origen (None si no hay)
    # EJEMPLO: (1,2)→1, (-3,4)→2, (-1,-1)→3, (2,-5)→4, (0,3)→0
    #   punto_mas_lejano() → (2,-5)
    # ===========================================================================
    class GestorPuntos:
        def __init__(self):
            self.puntos = []

        def cuadrante(self, punto):
            x, y = punto
            if x > 0 and y > 0:
                return 1
            if x < 0 and y > 0:
                return 2
            if x < 0 and y < 0:
                return 3
            if x > 0 and y < 0:
                return 4
            return 0

        def agrupar_por_cuadrante(self, *puntos):
            grupos = {}
            for p in puntos:
                self.puntos.append(p)
                q = self.cuadrante(p)  # reutiliza cuadrante
                if q not in grupos:
                    grupos[q] = []
                grupos[q].append(p)
            return grupos

        def punto_mas_lejano(self):
            lejano = None
            for p in self.puntos:
                if lejano is None or math.hypot(*p) > math.hypot(*lejano):
                    lejano = p
            return lejano


    # ===========================================================================
    # Ej. 40 — Generador de secuencias (Fibonacci)
    # ---------------------------------------------------------------------------
    # ENUNCIADO: Clase Secuencias.
    #   - fibonacci(n): lista con los primeros n términos (0, 1, 1, 2, 3, 5...)
    #   - suma_fibonacci(n): suma de esos n términos (reutiliza fibonacci)
    #   - es_fibonacci(numero): True si el número pertenece a la sucesión
    #   - fibonacci_multiples(*ns): diccionario {n: lista} (reutiliza fibonacci)
    # EJEMPLO: fibonacci(7) → [0,1,1,2,3,5,8]     suma_fibonacci(7) → 20
    #   es_fibonacci(21) → True    es_fibonacci(20) → False
    # ===========================================================================
    class Secuencias:
        def fibonacci(self, n):
            terminos = []
            a, b = 0, 1
            for _ in range(n):
                terminos.append(a)
                a, b = b, a + b
            return terminos

        def suma_fibonacci(self, n):
            total = 0
            for t in self.fibonacci(n):
                total += t
            return total

        def es_fibonacci(self, numero):
            k = 2
            terminos = self.fibonacci(k)
            while terminos[-1] < numero:
                k += 1
                terminos = self.fibonacci(k)
            return numero in terminos

        def fibonacci_multiples(self, *ns):
            resultado = {}
            for n in ns:
                resultado[n] = self.fibonacci(n)
            return resultado


    # ===========================================================================
    # PROGRAMA PRINCIPAL — prueba cada ejercicio
    # ===========================================================================
    def mostrar(n, titulo, *resultados):
        print(f"Ej. {n} · {titulo}")
        for r in resultados:
            print("        ", r)


    if __name__ == "__main__":
        # 21
        b = Biblioteca()
        total = b.agregar_multiples(("Rayuela", "Cortázar"), ("Bestiario", "Cortázar"),
                                    ("Ficciones", "Borges"))
        assert total == 3
        assert b.libros_de_autor("Cortázar") == ["Rayuela", "Bestiario"]
        assert b.autores_unicos() == {"Cortázar", "Borges"}
        mostrar(21, "Biblioteca", b.libros_de_autor("Cortázar"), b.autores_unicos())

        # 22
        la = ListaAsistencia()
        curso = ["Ana", "Bob", "Eva", "Leo"]
        la.registrar_multiples("Ana", "Eva")
        assert la.faltantes(curso) == ["Bob", "Leo"]
        assert la.porcentaje_asistencia(curso) == 50.0
        mostrar(22, "ListaAsistencia", la.faltantes(curso), la.porcentaje_asistencia(curso))

        # 23
        ct = ConversorTemperatura()
        assert ct.celsius_a_fahrenheit(100) == 212.0
        assert ct.convertir_multiples(0, 100, -40) == [32.0, 212.0, -40.0]
        assert ct.fahrenheit_a_celsius(212) == 100.0
        assert len(ct.historial) == 4
        mostrar(23, "ConversorTemperatura", ct.convertir_multiples(0, 100, -40), ct.historial)

        # 24
        ap = AnalizadorPalabras()
        assert ap.cargar_texto("Python es muy divertido.") == 4
        assert ap.palabra_mas_larga() == "divertido"
        assert ap.palabras_mayores_a(4) == ["Python", "divertido"]
        assert ap.longitud_promedio() == (6 + 2 + 3 + 9) / 4
        mostrar(24, "AnalizadorPalabras", ap.palabra_mas_larga(), ap.palabras_mayores_a(4),
                ap.longitud_promedio())

        # 25
        p = Pila()
        p.apilar_multiples(1, 2, 3)
        assert p.desapilar() == 3 and p.ver_tope() == 2
        assert p.invertir_texto("hola") == "aloh"
        assert p.elementos == [1, 2]  # la pila quedó como estaba
        assert Pila().desapilar() is None and Pila().esta_vacia()
        mostrar(25, "Pila", p.invertir_texto("hola"), p.elementos)

        # 26
        q = ColaTurnos()
        q.encolar_multiples("Ana", "Bob", "Eva")
        assert q.atender() == "Ana" and q.siguiente() == "Bob"
        assert q.cantidad_en_espera() == 2 and q.atendidos == ["Ana"]
        assert ColaTurnos().atender() is None
        mostrar(26, "ColaTurnos", q.siguiente(), q.cantidad_en_espera(), q.atendidos)

        # 27
        ag = Agenda()
        ag.agregar_contacto("Ana", "0991111111")
        ag.agregar_contacto("Andrés", "0992222222")
        ag.agregar_contacto("Bruno", "0993333333")
        assert ag.buscar_por_prefijo("an") == ["Ana", "Andrés"]
        assert ag.telefono_de("Bruno") == "0993333333" and ag.telefono_de("Zoe") is None
        assert ag.eliminar_contacto("Bruno") is True and ag.eliminar_contacto("Bruno") is False
        mostrar(27, "Agenda", ag.buscar_por_prefijo("an"), ag.contactos)

        # 28
        dp = DetectorPalindromos()
        assert dp.es_palindromo("Anita lava la tina") is True
        assert dp.es_palindromo("hola") is False and dp.es_palindromo("") is False
        assert dp.filtrar_palindromos("ana", "hola", "oso") == ["ana", "oso"]
        assert dp.encontrados == ["ana", "oso"]
        mostrar(28, "DetectorPalindromos", dp.filtrar_palindromos("ana", "hola", "oso"))

        # 29
        est = Estadisticas()
        est.cargar(4, 1, 2, 2, 3)
        assert (est.media(), est.mediana(), est.moda(), est.rango()) == (2.4, 2, 2, 3)
        est2 = Estadisticas()
        est2.cargar(1, 2, 3, 4)
        assert est2.mediana() == 2.5 and est2.moda() == 1  # empate → el menor
        assert Estadisticas().media() is None
        mostrar(29, "Estadisticas", est.media(), est.mediana(), est.moda(), est.rango())

        # 30
        lp = LimpiadorListas()
        assert lp.eliminar_duplicados([1, 2, 2, 3, 1]) == [1, 2, 3]
        assert lp.duplicados_encontrados([1, 2, 2, 3, 1]) == {1, 2}
        assert lp.limpiar_multiples([1, 1, 2], ["a", "a"]) == [[1, 2], ["a"]]
        mostrar(30, "LimpiadorListas", lp.eliminar_duplicados([1, 2, 2, 3, 1]),
                lp.duplicados_encontrados([1, 2, 2, 3, 1]))

        # 31
        m = Matriz()
        m.crear(2, 3, 1)
        m.asignar(0, 1, 5)
        assert m.matriz == [[1, 5, 1], [1, 1, 1]]
        assert m.suma_fila(0) == 7 and m.suma_columna(1) == 6 and m.suma_total() == 10
        assert m.transpuesta() == [[1, 1], [5, 1], [1, 1]]
        mostrar(31, "Matriz", m.matriz, m.transpuesta(), m.suma_total())

        # 32
        e = Estacionamiento(2)
        assert e.ingresar("A") and e.ingresar("B") and not e.ingresar("C")
        assert not e.ingresar("A") and e.espacios_libres() == 0
        assert e.salir("A") is True and e.salir("Z") is False and e.espacios_libres() == 1
        assert e.ingresar_multiples("D", "E") == ["E"]
        mostrar(32, "Estacionamiento", sorted(e.placas), e.espacios_libres())

        # 33
        v = Votacion()
        v.votar_multiples("Ana", "Bob", "Ana", "Ana", "Bob")
        assert v.total_votos() == 5 and v.ganador() == "Ana"
        assert v.porcentaje("Ana") == 60.0 and v.porcentaje("Zoe") == 0
        assert Votacion().ganador() is None
        mostrar(33, "Votacion", v.votos, v.ganador(), v.porcentaje("Ana"))

        # 34
        om = OrdenadorManual()
        original = [5, 2, 9, 1]
        assert om.ordenar(original) == [1, 2, 5, 9] and original == [5, 2, 9, 1]
        assert om.ordenar(original, True) == [9, 5, 2, 1]
        assert om.es_ordenada([1, 2, 3]) and not om.es_ordenada([2, 1])
        assert om.ordenar_multiples([3, 1, 2], [9, 8]) == [[1, 2, 3], [8, 9]]
        mostrar(34, "OrdenadorManual", om.ordenar(original), om.ordenar(original, True))

        # 35
        idct = InversorDiccionario()
        d = {"a": 1, "b": 2, "c": 1}
        assert idct.invertir(d) == {1: ["a", "c"], 2: ["b"]}
        assert idct.claves_con_valor(d, 1) == ["a", "c"] and idct.claves_con_valor(d, 9) == []
        assert idct.valores_repetidos(d) == {1}
        mostrar(35, "InversorDiccionario", idct.invertir(d), idct.valores_repetidos(d))

        # 36
        vm = VentasMensuales()
        vm.registrar_multiples("enero", 100, 200)
        vm.registrar_venta("febrero", 150)
        vm.registrar_venta("marzo", 500)
        assert vm.total_mes("enero") == 300 and vm.total_mes("abril") == 0
        assert vm.mes_mayor_venta() == "marzo" and vm.total_anual() == 950
        mostrar(36, "VentasMensuales", vm.total_mes("enero"), vm.mes_mayor_venta(),
                vm.total_anual())

        # 37
        oc = OperacionesConjuntos()
        a, b2 = [1, 2, 3], [2, 3, 4]
        assert oc.union(a, b2) == [1, 2, 3, 4] and oc.interseccion(a, b2) == [2, 3]
        assert oc.diferencia(a, b2) == [1] and oc.diferencia_simetrica(a, b2) == [1, 4]
        assert oc.interseccion_multiples([1, 2, 3], [2, 3, 4], [3, 4, 5]) == [3]
        mostrar(37, "OperacionesConjuntos", oc.union(a, b2), oc.interseccion(a, b2),
                oc.diferencia(a, b2), oc.diferencia_simetrica(a, b2))

        # 38
        vc = ValidadorContrasena()
        assert vc.requisitos_faltantes("hola") == ["8 caracteres", "mayúscula", "número"]
        assert vc.es_segura("Hola1234") and not vc.es_segura("holaholahola")
        r38 = vc.evaluar_multiples("Hola1234", "hola", "SEGURA123x")
        assert r38 == {"Hola1234": True, "hola": False, "SEGURA123x": True}
        assert vc.seguras == {"Hola1234", "SEGURA123x"}
        mostrar(38, "ValidadorContrasena", r38, vc.requisitos_faltantes("hola"))

        # 39
        gp = GestorPuntos()
        r39 = gp.agrupar_por_cuadrante((1, 2), (-3, 4), (-1, -1), (2, -5), (0, 3))
        assert r39 == {1: [(1, 2)], 2: [(-3, 4)], 3: [(-1, -1)], 4: [(2, -5)], 0: [(0, 3)]}
        assert gp.punto_mas_lejano() == (2, -5)
        assert GestorPuntos().punto_mas_lejano() is None
        mostrar(39, "GestorPuntos", r39, gp.punto_mas_lejano())

        # 40
        sq = Secuencias()
        assert sq.fibonacci(7) == [0, 1, 1, 2, 3, 5, 8] and sq.fibonacci(0) == []
        assert sq.suma_fibonacci(7) == 20
        assert sq.es_fibonacci(21) and sq.es_fibonacci(0) and not sq.es_fibonacci(20)
        assert sq.fibonacci_multiples(1, 5) == {1: [0], 5: [0, 1, 1, 2, 3]}
        mostrar(40, "Secuencias", sq.fibonacci(7), sq.suma_fibonacci(7), sq.es_fibonacci(21))

        print("\n✓ Los 20 ejercicios (21-40) pasaron todas las pruebas.")
