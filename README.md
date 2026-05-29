# Manual de Usuario

## Proyecto POO en Python – Analizador de Sesiones de Estudio

---

# 1. Introducción

Este proyecto fue desarrollado en Python utilizando Programación Orientada a Objetos (POO). El sistema permite registrar sesiones de estudio de un estudiante y calcular su nivel de productividad promedio.

El programa está diseñado para:

* Registrar materias estudiadas.
* Guardar duración de estudio.
* Registrar nivel de concentración.
* Calcular productividad.
* Mostrar promedios de rendimiento.

---

# 2. Requisitos del Sistema

Para ejecutar el programa se necesita:

* Python 3 instalado

* Visual Studio Code

* PyCharm

* IDLE de Python

* Sistema operativo:

  * Windows
  * Linux
  * MacOS

---

# 3. Ejecución del Programa

## Paso 1: Abrir el archivo

Abrir el archivo:

```python
Proyecto_POO.py
```

---

## Paso 2: Compilar

Presionar:

* Ejecutar el archivo desde VS Code.
* O usar el comando:

```python
python Proyecto_POO.py
```

---

## Paso 3: Ejecutar

El programa abrirá una consola donde se mostrarán los resultados del análisis.

---

# 4. Funcionamiento del Sistema

El sistema está dividido en 3 clases principales:

## 4.1 Clase SesionEstudio

Esta clase almacena la información de cada sesión de estudio.

### Datos registrados

* Materia
* Duración
* Concentración

### Ejemplo

```python
SesionEstudio s1("POO", 2, 8);
```

Significa:

* Materia: POO
* Duración: 2 horas
* Concentración: 8/10

---

## 4.2 Clase Estudiante

Representa al estudiante y almacena sus sesiones.

### Funciones principales

* Guardar sesiones.
* Llevar conteo de sesiones.

### Ejemplo

```python
Estudiante e("Dani");
```

---

## 4.3 Clase Analizador

Se encarga de calcular el promedio de productividad.

### Fórmula utilizada

La productividad se calcula así:

```python
productividad = duracion * concentracion
```

### Ejemplo

```python
2 * 8 = 16
```

---

# 5. Ejemplo Completo de Uso

## Crear sesiones

```python
SesionEstudio s1("POO", 2, 8);
SesionEstudio s2("Calculo", 3, 7);
```

---

## Crear estudiante

```python
Estudiante e("Dani");
```

---

## Agregar sesiones

```python
e.agregarSesion(s1);
e.agregarSesion(s2);
```

---

## Calcular promedio

```python
Analizador a;
cout << a.promedio(e);
```

---

# 6. Resultado Esperado

El programa calculará:

* Productividad de cada sesión.
* Promedio total de productividad.

Ejemplo:

| Materia | Duración | Concentración | Productividad |
| ------- | -------- | ------------- | ------------- |
| POO     | 2        | 8             | 16            |
| Cálculo | 3        | 7             | 21            |

Promedio:

```python
(16 + 21) / 2 = 18
```

---

# 7. Validaciones del Sistema

El programa evita dividir entre cero mediante:

```python
if (e.cantidad == 0)
```

Esto evita errores cuando no existen sesiones registradas.

---

# 8. Ventajas del Proyecto

* Uso de Programación Orientada a Objetos.
* Código organizado.
* Fácil mantenimiento.
* Fácil ampliación.
* Permite análisis básico de productividad.

---

# 9. Conclusión

Este proyecto permite comprender conceptos fundamentales de Programación Orientada a Objetos en Python, incluyendo:

* Clases
* Objetos
* Constructores
* Métodos
* Encapsulamiento
* Arreglos de objetos

Además, muestra cómo analizar información académica mediante cálculos simples de productividad.

