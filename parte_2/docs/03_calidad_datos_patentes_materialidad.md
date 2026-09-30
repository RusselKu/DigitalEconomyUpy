# Parte II · From Data to Digital Transformation
## 3. Calidad de Datos, Patentes WIPO y Materialidad

---

### 9. Calidad y Responsabilidad de los Datos

* **Calidad de Datos:** Falla por deriva de calibración en sensores de humedad de suelo expuestos a alta salinidad, generando lecturas erróneas de "suelo saturado" que inducen a cancelar riegos necesarios.
* **Representatividad:** Sesgo de muestreo al entrenar modelos algorítmicos exclusivamente con granjas tecnificadas de exportación del norte de México, reduciendo la efectividad del algoritmo en suelos arcillosos del sur/centro.
* **Privacidad:** Exposición no autorizada de mapas de rendimiento de cultivos e itinerarios de cosecha que podrían ser explotados por intermediarios para manipular precios de compra en finca.
* **Sesgo:** Algoritmos prescriptivos que favorecen la aplicación de agroquímicos sintéticos de marcas patrocinadoras sobre soluciones biológicas sustentables.
* **Ejemplo de Correlación Falaz vs. Causalidad:** Se observa una fuerte correlación positiva (**$r = 0.89$**, *Supuesto de diseño del equipo, no validado con fuente oficial*) entre la cantidad de datos LoRaWAN transmitidos por hectárea y el rendimiento total de aguacate por tonelada. Sin embargo, no es la transmisión de datos la que hace crecer los frutos (causalidad), sino que los productores de mayor capacidad financiera invierten simultáneamente en más sensores y en fertilizantes solubles de mayor calidad.

---

### 10. Patentes e Innovación (Consulta en WIPO)

1. **¿Qué es una patente y qué busca proteger?**
   Una patente es un derecho exclusivo concedido sobre una invención. Permite a su titular decidir si terceros pueden utilizar comercialmente la invención durante el periodo y territorio de protección, a cambio de divulgar públicamente la información técnica de la invención.

2. **Conceptos fundamentales:**
   - **Novedad:** la invención debe incorporar una característica que no forme parte del estado de la técnica previo.
   - **Actividad inventiva:** la solución no debe resultar obvia para una persona con conocimientos ordinarios en el campo técnico correspondiente.
   - **Aplicación industrial:** la invención debe poder fabricarse o utilizarse para una finalidad práctica o industrial.

3. **Componente con posible actividad inventiva en la propuesta:**
   El componente con mayor potencial inventivo sería el método de control que combina datos de tensión matricial del suelo, información de evapotranspiración y condiciones operativas para generar dinámicamente órdenes de riego. Que sea realmente patentable requeriría una búsqueda del estado de la técnica previo y una evaluación formal.

4. **Área tecnológica principal:**
   **Tecnología computacional.** El elemento central es el procesamiento algorítmico de datos provenientes de sensores y otras fuentes para convertirlos en decisiones automáticas de riego. Las comunicaciones digitales y redes son tecnologías habilitadoras.

5. **¿Registrar varias patentes garantiza alta innovación, adopción o éxito económico?**
   No. El número de patentes refleja actividad inventiva o esfuerzos de protección de propiedad intelectual, pero no demuestra por sí solo adopción, rentabilidad, impacto productivo, superioridad tecnológica ni éxito comercial.

La evidencia de la consulta WIPO se encuentra en `parte_2/wipo_evidence/`.

---

### 11. Digital No Significa Inmaterial

La propuesta digital depende de infraestructura física y, por lo tanto, tiene costos materiales, energéticos y ambientales.

- **Elementos físicos necesarios:** sensores de humedad o tensión de suelo, microcontroladores, válvulas y bombas, gateways o radiobases LoRaWAN, baterías o sistemas fotovoltaicos, infraestructura de red y servidores.
- **Costo material:** adquisición, instalación, mantenimiento y eventual sustitución de sensores, baterías, válvulas y gateways expuestos a humedad, salinidad, temperatura y condiciones de campo.
- **Costo energético:** las bombas de riego requieren electricidad; además, transmisión, almacenamiento y procesamiento de telemetría e imágenes agrícolas consumen energía.
- **Externalidad ambiental:** el reemplazo de sensores, componentes electrónicos y baterías puede generar residuos electrónicos y demanda de materiales, por lo que deben contemplarse mantenimiento, recuperación y disposición responsable.
