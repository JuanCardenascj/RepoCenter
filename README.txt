Contexto

Este proyecto tiene como objetivo evaluar y desarrollar criterio de diseño, separación de responsabilidades y pensamiento lógico, no solo que el código “funcione”.

No está relacionado con ningún producto real ni sistema en producción.
Es un ejercicio didáctico, pero con estándares profesionales.

Objetivo General

Implementar un motor de reglas simple, extensible y mantenible, con:

Lógica desacoplada de la interfaz

Contratos claros entre componentes

Configuración externa

Ejecución determinística

El proyecto debe poder crecer sin romperse.

Alcance Técnico
Lenguaje

Python 3.10+

Python estándar (no frameworks)

Requisitos Funcionales
1. Rule Engine (núcleo lógico)

Implementar una clase RuleEngine que:

Reciba un input en forma de dict

Ejecute un conjunto de reglas registradas

Devuelva un resultado estructurado (no imprime)

El engine:

❌ No debe leer archivos

❌ No debe imprimir por consola

❌ No debe conocer el CLI

✅ Solo ejecuta lógica

2. Reglas

Implementar al menos 3 reglas distintas

Cada regla debe:

Declarar qué datos necesita del input

Evaluar una condición

Retornar un resultado estructurado (ej: passed, reason, rule_name)

Restricciones:

Las reglas no se llaman entre sí

Las reglas no acceden a archivos

Las reglas no imprimen

No deben tener lógica de ejecución global

3. Registro y Configuración de Reglas

Implementar un registro explícito de reglas

Las reglas activas deben definirse en un archivo de configuración (.json)

El sistema debe poder:

Activar/desactivar reglas sin cambiar código

Fallar de forma controlada si una regla configurada no existe

No se permite:

Autodiscovery mágico

Imports dinámicos sin control

4. CLI (Interfaz)

Implementar un CLI mínimo que:

Reciba:

Path a un archivo JSON de input

Path a un archivo de configuración de reglas

Cargue los datos

Ejecute el engine

Muestre el resultado final por consola

El CLI:

❌ No contiene lógica de negocio

❌ No evalúa reglas

✅ Solo orquesta

Estructura Sugerida (flexible)
project/
├─ core/
│  ├─ engine.py
│  ├─ rule.py
│  └─ registry.py
├─ rules/
│  ├─ rule_age.py
│  ├─ rule_score.py
│  └─ rule_country.py
├─ cli/
│  └─ main.py
├─ config/
│  └─ rules.json
├─ examples/
│  └─ input.json
└─ README.md


La estructura puede variar si está bien justificada.

Qué se Evalúa (criterios reales)

Se evalúa principalmente:

Separación de responsabilidades

Claridad del flujo

Diseño de contratos entre módulos

Nombres de clases, métodos y variables

Facilidad para agregar una regla nueva

Manejo básico de errores

No se evalúa:

Cantidad de líneas

Complejidad innecesaria

Uso de patrones “porque sí”

Errores Comunes a Evitar

Restan puntos significativamente:

Engine imprimiendo cosas

Reglas leyendo archivos

Lógica de negocio en el CLI

if/elif gigantes en lugar de reglas

Acoplamiento fuerte entre módulos

Código “funciona pero no escala”

Entregable

Repositorio con el código

README claro explicando:

cómo ejecutar el proyecto

decisiones de diseño relevantes

Código entendible sin explicación oral

Modalidad de Revisión

No hay guía paso a paso

Se revisan decisiones técnicas

Se señalarán errores de diseño

Se pedirá refactor si es necesario

Deadline sugerido: 7 a 10 días

Nota final

Este proyecto no busca perfección, pero sí criterio.
Es preferible algo simple y bien diseñado que algo complejo y frágil.