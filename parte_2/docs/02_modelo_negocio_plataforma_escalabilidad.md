# Part II · From Data to Digital Transformation
## 2. Business Model, Digital Platform and Scalability

**Author:** Jonathan · Team 3: Agriculture
**Status:** design proposal; commercial validation and a field pilot have not been completed.

### 6. Business Model

**Proposed initial customer:** avocado producers or associations with managed irrigation and the ability to measure water use by plot. This is a focus decision rather than evidence of demand. The producer or association pays; the agronomist reviews recommendations and the irrigation operator implements decisions. Adaptation to other crops would be assessed later.

| Dimension | Proposed Design | Required Validation |
|---|---|---|
| **Value Creation** | Turn soil moisture, weather and applied water records into recommendations on when and how much to irrigate. Experimental target: reduce applied water by 25% while maintaining yield and quality. | Compare m³/ha, kWh/ha, yield and quality over a crop cycle in comparable plots; record rainfall, soil and management. Randomize treatment where feasible and disclose causal limitations. |
| **Value Delivery** | Web/mobile dashboard, alerts and local storage during outages. An agronomist initially approves recommendations; a technician installs and calibrates equipment. | Measure reading reception, alert delivery, adoption and support response times. |
| **Value Capture** | Proposed subscription of USD 12/ha/month and node sales at USD 180 each. Installation, gateways, connectivity and maintenance require separate quotations. | Interview buyers, obtain quotations and test willingness to pay. Both prices are team design assumptions rather than verified market prices. |

**Illustrative example:** a 100-ha farm with 10 nodes would pay USD 1,200 per month for software and USD 1,800 for nodes at the outset. Software and nodes would total USD 16,200 over 12 months, before installation, gateways, connectivity, maintenance and taxes. One node per 10 ha is a calculation assumption; actual density depends on agronomic sampling.

Customer net benefit = monetary savings in water, energy and inputs + additional production margin − total service cost. Reducing applied water does not imply the same percentage reduction in monetary costs. To recover the first-year outlay in this example, annual benefits before service costs must exceed USD 16,200 plus the omitted costs. Payback is not promised without measurements.

The provider must estimate hardware, cloud, support, site visits, customer acquisition and development costs. Revenue is not profit; a margin cannot be established without quotations.

### 7. Digital Platform and Network Effects

The first stage delivers irrigation SaaS. The second proposes a **two-sided platform** for requesting and comparing quotations and contracting between:

- **Side A:** producers and associations seeking installation, calibration and agricultural inputs.
- **Side B:** suppliers and technicians offering those products and services.

A recommendation may generate a quotation request confirmed by the producer. A directory or exclusive sale of proprietary software does not demonstrate an operational two-sided platform. Insurers would be a future extension requiring separate agreements and validation.

| Mechanism | Hypothesis | Verification |
|---|---|---|
| **Indirect A → B** | More active producers may attract suppliers through greater potential demand. | Active suppliers, quotations and transactions by region. |
| **Indirect B → A** | More relevant suppliers may improve availability and choice. | Response time, request coverage and retention. |
| **Learning from data** | More comparable, high-quality records could improve local recommendations. | Out-of-sample error by crop and soil. This is a learning hypothesis rather than a demonstrated direct network effect. |
| **Negative effects** | Poor supplier quality or recommendations influenced by sales may reduce trust. | Complaints and cancellations; separate agronomic recommendations from commercial offer rankings. |

To launch, the proposal concentrates the pilot in one region with an association and suppliers capable of serving it. Subscriptions fund the initial service; transaction commissions and lower insurance premiums are excluded from projections until validated. Sharing data with suppliers requires authorization and an agreed purpose.

### 8. Scalability: The 10x Scenario

**Exercise assumptions:** 1,000 farms grow to 10,000; each has 100 ha and 10 nodes; each node transmits every 15 minutes; a month contains 30 days and each record occupies 1 decimal kB. There is one paying account per farm, although multiple people may use it. These are not currently deployed customers or sensors.

| Metric | Baseline | 10x Scenario |
|---|---:|---:|
| Farms / paying accounts | 1,000 | 10,000 |
| Contracted hectares | 100,000 | 1,000,000 |
| Nodes | 10,000 | 100,000 |
| Readings per node per day | 96 | 96 |
| Monthly readings | 28,800,000 | 288,000,000 |
| Average readings per second | 11.11 | 111.11 |
| New monthly data, excluding replicas and indexes | 28.8 GB | 288 GB |
| 24 months of data, without compression or overhead | 691.2 GB | 6,912 GB |
| Monthly subscription revenue at USD 12/ha | USD 1,200,000 | USD 12,000,000 |

**Formulas:** monthly readings = nodes × (24 × 60 / 15) × 30; monthly GB = readings × 1,000 / 1,000,000,000; monthly revenue = farms × 100 × 12. Revenue assumes full contracting and collection, without discounts or cancellations; it is not a market forecast.

| Component | Behavior Under These Assumptions | Proposed Response |
|---|---|---|
| Ingestion and processing | Approximately 10x with equal work per reading. Peaks exceed the average. | Distribute transmission times, use queues and batches; test simultaneous sends and reconnections. |
| Storage | 10x with equal retention, record size and replication. | Define retention, compression and aggregates; also measure indexes, copies and traffic. |
| Field support | Grows with nodes, failures and distances; may exceed 10x. | Regional technicians, spare parts, routes and calibration budgets. |
| Acquisition and training | Slow cost growth cannot be assumed without evidence. | Measure cost per customer, churn and training hours. |
| Development | Some costs are shared; new features and operations may increase costs. | Separate fixed and variable costs; review capacity at each stage. |

**Cost model:** C = F + R × c_r + G × c_g + V × c_v + U × c_u. F represents monthly fixed costs; R, readings; G, stored GB; V, visits; and U, supported accounts. Unit costs will come from quotations and tests. With constant unit costs, variable quantities multiplied by ten and unchanged F, C₁₀ = F + 10(C₁ − F). Average cost per customer may decrease without logarithmic processing costs.

AWS Lambda bills functions according to requests and execution duration [1]. **Serverless adjusts capacity but does not guarantee O(log N) costs.** Estimates must include memory, duration, region, databases, networking, messaging, monitoring and support; invocation prices alone are insufficient.

**Validation before expansion:** test 100,000 transmissions concentrated within a 15-minute interval and retries after outages; check duplicate counting, delays and cost per reading. Initial proposed criteria are receipt of at least 95% of readings within their interval and logging of 100% of irrigation decisions. These are design thresholds to agree on rather than completed test results.

### 9. Sources and Pending Decisions

- **[1] AWS:** [official Lambda pricing](https://aws.amazon.com/lambda/pricing/), consulted September 29, 2026. The billing mechanism is used rather than a project quotation.
- **Agronomic reference:** [FAO, Irrigation and Drainage Paper 56](https://www.fao.org/4/x0490e/x0490e00.htm). A comparison baseline rather than evidence for the 25% savings target.
- **Dependency:** [4C assessment and diagnosis](../../docs/parte_1/04_strategic_diagnosis_and_gaps.md).
- **Follow-up:** select sites, interview customers, obtain installation and operating quotations, agree on agronomic criteria and conduct the pilot. These activities have not been performed as part of this documentation work.
