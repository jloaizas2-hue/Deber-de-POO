"""
20 EJERCICIOS MÁS (21 al 40) — YA RESUELTOS
Clases y Colecciones con Métodos Reutilizables · Python · Unidad 1-2 (sin herencia)

Mismo estilo que la guía anterior:
  - una clase con colecciones creadas en __init__
  - un método base + métodos que lo REUTILIZAN (algunos con *args)
  - cada ejercicio trae ENUNCIADO, EJEMPLO y la SOLUCIÓN
  - al final hay un programa principal que prueba todo con assert

Ejecuta:  python ejercicios_21_a_40_resueltos.py
"""

import math


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
        self.libros = {}                     # {titulo: autor}

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
            self.agregar_libro(titulo, autor)    # reutiliza agregar_libro
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
        vinieron = len(curso) - len(self.faltantes(curso))   # reutiliza faltantes
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
        self.historial = []                  # [(celsius, fahrenheit)]

    def celsius_a_fahrenheit(self, c):
        f = c * 9 / 5 + 32
        self.historial.append((c, f))
        return f

    def fahrenheit_a_celsius(self, f):
        return (f - 32) * 5 / 9

    def convertir_multiples(self, *celsius):
        resultado = []
        for c in celsius:
            resultado.append(self.celsius_a_fahrenheit(c))   # reutiliza
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
            self.apilar(e)                   # reutiliza apilar

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
            self.encolar(c)                  # reutiliza encolar

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
            if self.es_palindromo(t):        # reutiliza es_palindromo
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
        for valor in sorted(frecuencias):            # ordenado → gana el menor en empate
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
            resultado.append(self.eliminar_duplicados(lista))   # reutiliza
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
            total += self.suma_fila(i)       # reutiliza suma_fila
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
            if not self.ingresar(p):         # reutiliza ingresar
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
        copia = list(lista)                  # no modifica la original
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
            resultado.append(self.ordenar(lista))        # reutiliza ordenar
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
            comun = self.interseccion(comun, otra)       # reutiliza interseccion
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
            segura = self.es_segura(clave)               # reutiliza es_segura
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
            q = self.cuadrante(p)                        # reutiliza cuadrante
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
    assert p.elementos == [1, 2]                         # la pila quedó como estaba
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
    assert est2.mediana() == 2.5 and est2.moda() == 1    # empate → el menor
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
