# Parte II · From Data to Digital Transformation
## 2. Modelo de Negocio, Plataforma Digital y Escalabilidad

---

### 6. Modelo de Negocio

* **Creación de Valor:** Soluciona el desperdicio de agua y fertirriego mediante recomendaciones automatizadas de riego prescriptivo basadas en telemetría IoT y modelos evapotranspirativos. Dirigido a agroexportadores de alto valor (aguacate, berries, tomate, cítricos) y distritos de riego tecnificados.
* **Entrega de Valor:** El agrónomo o productor accede al valor a través de una aplicación web/móvil responsiva (*AgTech Command Center*) y alertas push/SMS enviadas directamente al regador de campo.
* **Captura de Valor:** Modelo híbrido **B2B SaaS (Software as a Service) + Data-driven On-Demand**:
  - *Suscripción mensual/anual por hectárea monitoreada:* **$12 USD/ha/mes** *(Supuesto financiero proyectado por el equipo de trabajo para viabilidad comercial)* para acceso a plataforma y analítica prescriptiva.
  - *Venta/Arrendamiento de nodos IoT y sensores de suelo:* **$180 USD por nodo sensor** *(Supuesto de costo de hardware estimado por el equipo)* con mantenimiento preventivo incluido.

---

### 7. Plataforma Digital y Efectos de Red

* **Naturaleza de Plataforma:** Sí, opera como una **Plataforma Digital Bilateral (Two-Sided Platform)**:
  - *Lado A:* Productores agrícolas y agrónomos de campo.
  - *Lado B:* Proveedores de insumos agrícolas (fertilizantes solubles, bioestimulantes), casas de seguros agrícolas y compradores de cosechas (agregadores exportadores).
* **Interacción Facilitada:** Conexión automatizada entre prescripciones agronómicas de nitrógeno/agua y ordenamiento automático de fertilizantes con proveedores locales.
* **Efectos de Red:**
  - *Efecto Directo (Same-side):* A mayor número de agricultores en una cuenca hidrográfica, mayor precisión acumulada en los modelos hidrológicos compartidos (calibración regional colectiva).
  - *Efecto Indirecto (Cross-side):* A mayor número de hectáreas bajo la plataforma, más proveedores de bioinsumos y aseguradoras ofrecen tarifas competitivas y primas reducidas por gestión de riesgo basada en datos verificables.

---

### 8. Análisis de Escalabilidad (Escenario 10x Usuarios)

| Dimensión de Infraestructura | Impacto al Escalar 10x | Comportamiento del Costo | Estrategia de Mitigación |
|---|---|---|---|
| **Cómputo e Ingesta de Datos** | De 10,000 a 100,000 sensores transmitiendo lecturas cada 15 min | **Crecimiento Sublineal ($\mathcal{O}(\log N)$)** | Arquitectura Serverless (AWS Lambda / Cloud Functions) e ingesta distribuida con Apache Kafka |
| **Almacenamiento Temporal** | Volumen masivo de series de tiempo | **Crecimiento Lento / Contenido** | Compresión de series temporales y almacenamiento frío (S3 Glacier) para históricos mayores a 2 años |
| **Adquisición de Usuarios** | Expansión de ventas | **Crecimiento Lento** | Alianzas con asociaciones de agroexportadores (APEAM, ANEBERRIES) y distritos de riego |
| **Soporte y Operación en Campo** | Calibración física de sensores en terreno | **Crecimiento Lineal ($\mathcal{O}(N)$)** | Modelo de red de distribuidores técnicos locales y certificaciones de instalación a terceros |

* **¿Por qué escalabilidad no significa costo cero?:** Aunque el software escala con costo marginal cercano a cero, los activos físicos (nodos sensores de suelo, gateways LoRaWAN, visitas de soporte agrónomo y consumo eléctrico de servidores GPU) imponen costos marginales reales no despreciables.
