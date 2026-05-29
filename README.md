# MANUAL DE USUARIO

## Sistema de Análisis de Hábitos y Productividad de Estudio

---

# 1. Introducción

El Sistema de Análisis de Hábitos y Productividad de Estudio es una aplicación desarrollada en Python que permite registrar sesiones de estudio, analizar el rendimiento académico y generar recomendaciones personalizadas para mejorar los hábitos de aprendizaje.

El sistema ayuda al estudiante a:

* Organizar sus materias.
* Registrar sesiones de estudio.
* Analizar productividad.
* Medir tiempo efectivo de estudio.
* Recibir recomendaciones académicas.

---

# 2. Requisitos del Sistema

Para ejecutar el programa se necesita:

* Python 3 instalado.
* PyCharm o cualquier editor compatible con Python.

---

# 3. Ejecución del Programa

## Paso 1

Abrir el proyecto en PyCharm.

## Paso 2

Abrir el archivo:

```text
main.py
```

## Paso 3

Presionar el botón:

```text
Run ▶
```

---

# 4. Inicio de Sesión

Al iniciar el programa aparecerá:

```text
========== GESTOR DE ESTUDIO ==========
Ingresa tu nombre:
```

El usuario debe escribir su nombre.

Ejemplo:

```text
Ingresa tu nombre: Dani
```

Luego el sistema mostrará:

```text
Hola Dani, bienvenido al sistema.
```

---

# 5. Menú Principal

El sistema cuenta con un menú interactivo:

```text
========== MENU ==========
1. Registrar materias
2. Registrar sesiones
3. Ver analisis
4. Ver recomendaciones
5. Salir
```

---

# 6. Registrar Materias

## Opción 1

Permite registrar las materias académicas.

El sistema solicitará:

```text
Cuantas materias desea agregar:
```

El usuario debe ingresar un número.

Ejemplo:

```text
2
```

Luego deberá escribir el nombre de cada materia.

Ejemplo:

```text
Nombre de la materia #1: Matematicas
Nombre de la materia #2: Programacion
```

Finalmente aparecerá:

```text
✅ Materia registrada correctamente.
```

---

# 7. Registrar Sesiones de Estudio

## Opción 2

Permite registrar sesiones de estudio.

El sistema mostrará las materias registradas:

```text
1 - Matematicas
2 - Programacion
```

Después solicitará:

* Materia
* Actividad
* Fecha
* Duración
* Concentración

Ejemplo:

```text
Seleccione materia: 1
Actividad: Taller
Fecha: 29/05/2026
Duracion en minutos: 120
Concentracion (1-10): 8
```

Al finalizar aparecerá:

```text
✅ Sesion registrada correctamente.
```

---

# 8. Ver Análisis

## Opción 3

Muestra estadísticas generales del estudiante.

El sistema presenta:

* Promedio de productividad.
* Tiempo total estudiado.
* Tiempo efectivo.
* Tiempo perdido.
* Mejor sesión registrada.
* Productividad por materia.

Ejemplo:

```text
📊 PROMEDIO GENERAL: 640

⏰ Tiempo total: 120

🎯 Tiempo efectivo: 96

💤 Tiempo perdido: 24
```

---

# 9. Ver Recomendaciones

## Opción 4

El sistema genera recomendaciones automáticas según el rendimiento del estudiante.

Ejemplos:

```text
📖 Intenta leer mas sobre los temas que se te dificultan.

🎥 Ver videos educativos puede ayudarte a entender mejor los conceptos.

📝 Realiza resumenes o mapas mentales para reforzar el aprendizaje.
```

También genera mensajes motivacionales:

```text
🌟 Cada esfuerzo que haces hoy te acerca mas a tus metas.
```

---

# 10. Salir del Sistema

## Opción 5

Finaliza la ejecución del programa.

Mensaje mostrado:

```text
👋 Gracias por usar el sistema.
📚 Nunca dejes de aprender.
```

---

# 11. Manejo de Excepciones

El sistema implementa manejo de excepciones utilizando:

```python
try:
except:
```

Esto evita que el programa se cierre cuando el usuario ingresa datos incorrectos.

Ejemplo:

```text
❌ Debes ingresar un numero.
```

---

# 12. Posibles Errores del Usuario

| Error                               | Solución                   |
| ----------------------------------- | -------------------------- |
| Ingresar texto en vez de números    | Escribir un valor numérico |
| Seleccionar una materia inexistente | Elegir una materia válida  |
| Registrar sesiones sin materias     | Registrar materias primero |

---

# 13. Tecnologías Utilizadas

* Python
* Programación Orientada a Objetos (POO)
* Manejo de excepciones
* Consola interactiva

---

# 14. Autores

* Alisson Paola Bonilla
* Karen Daniela Suarez Suarez

---

# 15. Conclusión

El sistema permite analizar hábitos de estudio mediante el registro y análisis de sesiones académicas, ayudando a los estudiantes a mejorar su productividad y organización mediante recomendaciones automáticas y estadísticas de rendimiento.

---

# Identificación de Requerimientos

## Requerimientos Funcionales

**RF1:** El sistema debe permitir registrar sesiones de estudio con información como materia, fecha, duración y tipo de actividad.

**RF2:** El sistema debe permitir registrar el nivel de concentración percibido en cada sesión.

**RF3:** El sistema debe permitir clasificar el tipo de actividad realizada (lectura, ejercicios, repaso, investigación, entre otros).

**RF4:** El sistema debe almacenar el nivel de dificultad del tema estudiado.

**RF5:** El sistema debe calcular un índice de eficiencia de estudio basado en las variables registradas.

**RF6:** El sistema debe generar análisis de productividad de las sesiones de estudio.

**RF7:** El sistema debe permitir visualizar patrones de hábitos de estudio del usuario.

**RF8:** El sistema debe realizar comparaciones entre variables (horario vs rendimiento, duración vs concentración, dificultad vs eficiencia, entre otras).

**RF9:** El sistema debe generar recomendaciones basadas en los datos analizados.

**RF10 (Opcional):** El sistema debe mostrar gráficos de evolución del rendimiento y productividad utilizando Python.

## Requerimientos No Funcionales

**RNF1:** La interfaz debe ser intuitiva y fácil de usar.

**RNF2:** El sistema debe almacenar la información de manera persistente.

**RNF3:** El tiempo de respuesta para generar análisis no debe superar los 3 segundos.

**RNF4:** Los datos del usuario deben mantenerse protegidos y privados.

**RNF5:** El sistema debe permitir exportar resultados en formatos comunes como CSV o PDF.

