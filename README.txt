1. Contrato de reglas (core/rule.py)

- Define la **interfaz/base class Rule** que todas las reglas deben cumplir.
- Cada regla debe declarar:
  - name: nombre único de la regla
  - required_fields: campos que necesita del input
  - evaluate(input_data): función que devuelve un resultado estructurado


2. Motor de reglas (core/engine.py)

- Clase RuleEngine que recibe:
  - Un diccionario con datos de entrada
  - Una lista de objetos de tipo Rule
- Ejecuta todas las reglas de forma independiente
- Devuelve un resultado estructurado con:
  - Resultados individuales por regla (passed, reason, rule)
  - Resumen total (passed, failed)
- Manejo básico de errores: captura excepciones de reglas sin detener la ejecución

3. Registro de reglas (core/registry.py)

- Diccionario `RULE_REGISTRY` que mapea nombres de reglas a sus clases concretas
- Función get_rule_class(name) para obtener la clase correspondiente
- Permite activar/desactivar reglas sin cambiar el motor

4. Reglas concretas (rules/)

Se implementaron tres reglas de ejemplo:

1. AgeRule (rule_age.py)
   - Evalúa si la edad es ≥ 18
2. ScoreRule (rule_score.py)
   - Evalúa si el puntaje es ≥ 50
3. CountryRule (rule_country.py)
   - Evalúa si el país está en la lista permitida

Cada regla:

- Cumple el contrato Rule
- Solo accede a los datos que necesita
- Devuelve resultados estructurados
- No imprime, no lee archivos, no se llama entre sí

5. Configuración (config/rules.json)

- Archivo JSON que define qué reglas están activas:
```json
{
  "active_rules": ["age", "score", "country"]
}
-El "score" fue borrado por funcionalidad, segun yo,







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
