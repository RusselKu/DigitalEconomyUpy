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

### 10. Patentes e Innovación (Consulta en WIPO IP Statistics y PATENTSCOPE)

1. **Distinción entre Fuentes WIPO Consultadas:**
   - *WIPO IP Statistics Data Center:* Fuente oficial utilizada para indicadores macroeconómicos agregados por país (solicitudes de patentes por residentes por millón de habitantes: México 8.8/1M vs Países Bajos 118.5/1M).
   - *WIPO PATENTSCOPE (patentscope.wipo.int):* Base de datos de patentes individuales consultada para extraer números reales de publicación, títulos, solicitantes y clasificaciones IPC (ej. `WO2021080415A1` de Priva/Wageningen UR, `MX2021008912A` del IMTA).
2. **¿Qué es una patente y qué busca proteger?:** Un título de propiedad intelectual otorgado por el Estado que concede el derecho exclusivo de explotar comercialmente una invención durante 20 años, impidiendo que terceros la fabriquen, usen o vendan sin consentimiento.
3. **Conceptos Fundamentales:**
   - *Novedad:* La invención no debe existir en el estado de la técnica accesible públicamente a nivel mundial antes de la fecha de solicitud.
   - *Actividad Inventiva:* La solución no debe ser evidente ni deducible de forma trivial por un experto en la materia.
   - *Aplicación Industrial:* La invención puede ser fabricada o utilizada en cualquier tipo de industria.
4. **Componente de Actividad Inventiva en la Propuesta:** Algoritmo dinámico de control distribuido para fertirriego autorregulado que combina lecturas de tensión matricial en suelo con tasas instantáneas de transpiración calculadas mediante sensores foliares ópticos.
5. **Clasificación Tecnológica Principal WIPO (IPC):**
   - *IPC Class G05D 7/00 / A01G 25/16:* Tecnología computacional aplicada al control automático de flujo de líquidos, riego y procesamiento de datos agrícolas.
6. **¿Registrar patentes garantiza éxito económico?:** No. Una patente protege la propiedad intelectual, pero no garantiza adopción en el mercado, viabilidad financiera, usabilidad ni rendimiento agronómico superior.

---

### 11. Digital No Significa Inmaterial

La economía digital requiere una infraestructura física intensiva con costos materiales y energéticos concretos:

* **Elementos Físicos Necesarios:** Sensores de capacitancia TDR en acero inoxidable, microcontroladores ARM, radiobases LoRaWAN, baterías de litio, módulos fotovoltaicos, servidores en datacenters y cables subterráneos.
* **Costo Material:** Reemplazo periódico de sondas de suelo degradadas por corrosión química y fertilizantes solubles (**$180 USD por nodo sensor** cada 24 meses, *Supuesto de diseño del equipo, no validado con fuente oficial*).
* **Costo Energético:** Consumo continuo de energía eléctrica en datacenters para procesamiento de imágenes de satélite NDVI y entrenamiento de modelos de Deep Learning en clústeres GPU.
* **Externalidad Ambiental:** Generación de e-waste (basura electrónica con metales pesados como litio, cobalto y cobre) al desechar sensores y baterías al final de su vida útil en zonas rurales.
