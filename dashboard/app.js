// ==========================================================================
// AGTECH DIGITAL READINESS INTELLIGENCE - BENTO STUDIO SCRIPT
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {

  // 1. Official Dataset (Year 2023)
  const countries = [
    {
      iso3: "MEX",
      name: "Mexico",
      flag: "🇲🇽",
      region: "Latin America · Upper-middle income",
      drs: 26.57,
      rank: 4,
      raw: {
        IT_NET_BBND: 20.75,
        IT_NET_SECR: 412.12,
        IT_NET_USER: 81.18,
        ITU_PRICE_BASKET: 1.95,
        ICT_SERV_EXP: 2.92,
        DIGIT_DELIV_EXP: 24.50,
        RD_EXP_GDP: 0.27,
        PATENT_RES_PM: 8.80
      },
      norm: {
        IT_NET_BBND: 44.92,
        IT_NET_SECR: 0.06,
        IT_NET_USER: 75.62,
        ITU_PRICE_BASKET: 88.20,
        ICT_SERV_EXP: 0.00,
        DIGIT_DELIV_EXP: 0.00,
        RD_EXP_GDP: 0.00,
        PATENT_RES_PM: 3.77
      },
      profile: {
        strength: "Broad consumer internet penetration (81.2%) and affordable entry-level broadband basket (1.95% of GNI).",
        gap: "Critically low R&D investment (0.27% of GDP) and minimal digital services export share (24.5%).",
        ai4c: {
          conn: { tag: "Moderate (Rural Gap)", pct: 55, fill: "fill-cyan" },
          comp: { tag: "Low (412/1M pop)", pct: 15, fill: "fill-rose" },
          cont: { tag: "Moderate (Fragmented)", pct: 48, fill: "fill-amber" },
          talent: { tag: "Moderate (0.27% R&D)", pct: 32, fill: "fill-purple" }
        }
      }
    },
    {
      iso3: "NLD",
      name: "Netherlands",
      flag: "🇳🇱",
      region: "Europe · High income",
      drs: 92.14,
      rank: 1,
      raw: {
        IT_NET_BBND: 43.26,
        IT_NET_SECR: 194962.90,
        IT_NET_USER: 97.01,
        ITU_PRICE_BASKET: 0.82,
        ICT_SERV_EXP: 9.62,
        DIGIT_DELIV_EXP: 58.40,
        RD_EXP_GDP: 2.27,
        PATENT_RES_PM: 118.50
      },
      norm: {
        IT_NET_BBND: 100.00,
        IT_NET_SECR: 100.00,
        IT_NET_USER: 100.00,
        ITU_PRICE_BASKET: 100.00,
        ICT_SERV_EXP: 51.74,
        DIGIT_DELIV_EXP: 85.39,
        RD_EXP_GDP: 100.00,
        PATENT_RES_PM: 100.00
      },
      profile: {
        strength: "Global benchmark in secure cloud servers (194k/1M), R&D intensity (2.27%), and patents (118.5/1M).",
        gap: "No structural gaps identified across the 8 analyzed dimensions.",
        ai4c: {
          conn: { tag: "Outstanding (100%)", pct: 100, fill: "fill-cyan" },
          comp: { tag: "World Leader (194k/1M)", pct: 100, fill: "fill-rose" },
          cont: { tag: "Very High (Open Hub)", pct: 95, fill: "fill-amber" },
          talent: { tag: "Maximum (2.27% R&D)", pct: 100, fill: "fill-purple" }
        }
      }
    },
    {
      iso3: "NZL",
      name: "New Zealand",
      flag: "🇳🇿",
      region: "Asia-Pacific · High income",
      drs: 60.91,
      rank: 2,
      raw: {
        IT_NET_BBND: 37.85,
        IT_NET_SECR: 18993.65,
        IT_NET_USER: 93.33,
        ITU_PRICE_BASKET: 0.98,
        ICT_SERV_EXP: 6.95,
        DIGIT_DELIV_EXP: 44.80,
        RD_EXP_GDP: 1.55,
        PATENT_RES_PM: 63.80
      },
      norm: {
        IT_NET_BBND: 86.77,
        IT_NET_SECR: 9.60,
        IT_NET_USER: 94.33,
        ITU_PRICE_BASKET: 98.33,
        ICT_SERV_EXP: 31.12,
        DIGIT_DELIV_EXP: 51.13,
        RD_EXP_GDP: 64.00,
        PATENT_RES_PM: 52.02
      },
      profile: {
        strength: "High broadband affordability (0.98% GNI), 1.55% GDP in R&D, and 63.8 resident patents per million people.",
        gap: "Moderate ICT services share due to strong trade specialization in dairy and primary commodities.",
        ai4c: {
          conn: { tag: "Very High (Rural Fiber)", pct: 90, fill: "fill-cyan" },
          comp: { tag: "High (18.9k/1M)", pct: 75, fill: "fill-rose" },
          cont: { tag: "Very High (Ag Data)", pct: 88, fill: "fill-amber" },
          talent: { tag: "High (1.55% R&D)", pct: 80, fill: "fill-purple" }
        }
      }
    },
    {
      iso3: "ARG",
      name: "Argentina",
      flag: "🇦🇷",
      region: "Latin America · Upper-middle income",
      drs: 55.72,
      rank: 3,
      raw: {
        IT_NET_BBND: 25.36,
        IT_NET_SECR: 5451.20,
        IT_NET_USER: 89.23,
        ITU_PRICE_BASKET: 2.90,
        ICT_SERV_EXP: 15.87,
        DIGIT_DELIV_EXP: 64.20,
        RD_EXP_GDP: 0.60,
        PATENT_RES_PM: 9.20
      },
      norm: {
        IT_NET_BBND: 56.20,
        IT_NET_SECR: 2.65,
        IT_NET_USER: 88.02,
        ITU_PRICE_BASKET: 78.29,
        ICT_SERV_EXP: 100.00,
        DIGIT_DELIV_EXP: 100.00,
        RD_EXP_GDP: 16.50,
        PATENT_RES_PM: 4.12
      },
      profile: {
        strength: "Regional leader in digitally deliverable services exports (64.2%) and ICT services (15.9%).",
        gap: "Modest R&D expenditure compared to OECD benchmarks and macroeconomic currency volatility.",
        ai4c: {
          conn: { tag: "Moderate-High", pct: 70, fill: "fill-cyan" },
          comp: { tag: "Moderate (5.4k/1M)", pct: 45, fill: "fill-rose" },
          cont: { tag: "High (Pampas Data)", pct: 78, fill: "fill-amber" },
          talent: { tag: "High (Software Talent)", pct: 75, fill: "fill-purple" }
        }
      }
    },
    {
      iso3: "KEN",
      name: "Kenya",
      flag: "🇰🇪",
      region: "Sub-Saharan Africa · Lower-middle income",
      drs: 15.42,
      rank: 5,
      raw: {
        IT_NET_BBND: 2.39,
        IT_NET_SECR: 297.13,
        IT_NET_USER: 32.07,
        ITU_PRICE_BASKET: 10.40,
        ICT_SERV_EXP: 10.67,
        DIGIT_DELIV_EXP: 39.20,
        RD_EXP_GDP: 0.80,
        PATENT_RES_PM: 4.50
      },
      norm: {
        IT_NET_BBND: 0.00,
        IT_NET_SECR: 0.00,
        IT_NET_USER: 0.00,
        ITU_PRICE_BASKET: 0.00,
        ICT_SERV_EXP: 59.85,
        DIGIT_DELIV_EXP: 37.03,
        RD_EXP_GDP: 26.50,
        PATENT_RES_PM: 0.00
      },
      profile: {
        strength: "World pioneer in mobile money (M-Pesa) and digital financial inclusion for smallholder farmers.",
        gap: "Low fixed broadband penetration (2.39 subs/100) and elevated relative ICT basket cost (10.4% GNI).",
        ai4c: {
          conn: { tag: "Low (Cellular Dominant)", pct: 30, fill: "fill-cyan" },
          comp: { tag: "Low (297/1M)", pct: 10, fill: "fill-rose" },
          cont: { tag: "Targeted (Mobile Data)", pct: 40, fill: "fill-amber" },
          talent: { tag: "Emerging Tech Hub", pct: 45, fill: "fill-purple" }
        }
      }
    }
  ];

  // Indicators Metadata
  const indicatorsMeta = [
    { code: 'IT_NET_BBND', label: 'Fixed Broadband', short: 'Broadband', unit: 'subs/100 pop' },
    { code: 'IT_NET_SECR', label: 'Secure Servers', short: 'Servers', unit: 'servers/1M pop' },
    { code: 'IT_NET_USER', label: 'Internet Users', short: 'Users', unit: '% pop' },
    { code: 'ITU_PRICE_BASKET', label: 'ICT Affordability', short: 'Affordability', unit: '% GNI [Inv]' },
    { code: 'ICT_SERV_EXP', label: 'ICT Service Exports', short: 'ICT Exports', unit: '% services' },
    { code: 'DIGIT_DELIV_EXP', label: 'Digital Deliverables', short: 'Digital Exports', unit: '% services' },
    { code: 'RD_EXP_GDP', label: 'R&D Expenditure', short: 'R&D', unit: '% GDP' },
    { code: 'PATENT_RES_PM', label: 'Resident Patents', short: 'Patents', unit: 'patents/1M pop' }
  ];

  let selectedCountry = countries.find(c => c.iso3 === 'MEX');
  let selectedPeer = countries.find(c => c.iso3 === 'ARG');
  let currentChartType = 'radar';
  let studioChartInstance = null;

  // 2. Initialize Country Switcher Bar (in Navbar)
  const switchBar = document.getElementById('countrySwitchBar');
  countries.forEach(c => {
    const btn = document.createElement('button');
    btn.className = `switch-country-btn ${c.iso3 === 'MEX' ? 'active' : ''}`;
    btn.dataset.iso = c.iso3;
    btn.innerHTML = `<span>${c.flag}</span> <span>${c.name}</span>`;
    btn.addEventListener('click', () => {
      document.querySelectorAll('.switch-country-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      setTargetCountry(c.iso3);
    });
    switchBar.appendChild(btn);
  });

  // 3. Render Leaderboard Podium
  function renderLeaderboard() {
    const container = document.getElementById('leaderboardList');
    container.innerHTML = '';
    const sorted = [...countries].sort((a, b) => b.drs - a.drs);

    sorted.forEach((c, idx) => {
      const item = document.createElement('div');
      item.className = `leader-item ${c.iso3 === selectedCountry.iso3 ? 'active' : ''}`;
      item.dataset.iso = c.iso3;
      
      const fillGradient = c.iso3 === 'NLD' ? 'linear-gradient(90deg, #10b981, #34d399)' :
                           c.iso3 === 'NZL' ? 'linear-gradient(90deg, #a855f7, #c084fc)' :
                           c.iso3 === 'ARG' ? 'linear-gradient(90deg, #3b82f6, #60a5fa)' :
                           c.iso3 === 'MEX' ? 'linear-gradient(90deg, #f43f5e, #fb7185)' :
                                              'linear-gradient(90deg, #f59e0b, #fbbf24)';

      item.innerHTML = `
        <div class="leader-rank-badge">#${idx + 1}</div>
        <div class="leader-meta">
          <div class="leader-name-row">
            <span>${c.flag} ${c.name}</span>
            <small style="color:var(--text-muted)">${c.region.split('·')[0].trim()}</small>
          </div>
          <div class="leader-track">
            <div class="leader-fill" style="width: ${c.drs}%; background: ${fillGradient};"></div>
          </div>
        </div>
        <div class="leader-score-val">${c.drs.toFixed(1)} <small style="font-size:0.65rem; color:var(--text-muted)">pts</small></div>
      `;

      item.addEventListener('click', () => {
        document.querySelectorAll('.switch-country-btn').forEach(b => {
          b.classList.toggle('active', b.dataset.iso === c.iso3);
        });
        setTargetCountry(c.iso3);
      });

      container.appendChild(item);
    });
  }

  // 4. Update Spotlight Card & AI 4C Gauge
  function setTargetCountry(iso) {
    const country = countries.find(c => c.iso3 === iso);
    if (!country) return;
    selectedCountry = country;

    // Header Spotlight Info
    document.getElementById('spotlightFlag').innerText = country.flag;
    document.getElementById('spotlightCountryName').innerText = country.name;
    document.getElementById('spotlightRankTag').innerText = `Rank #${country.rank}`;
    document.getElementById('spotlightRegion').innerText = country.region;
    document.getElementById('spotlightDrsVal').innerText = country.drs.toFixed(2);

    // 4 KPI Stats
    document.getElementById('spotUsers').innerText = `${country.raw.IT_NET_USER.toFixed(1)}%`;
    document.getElementById('spotServers').innerText = country.raw.IT_NET_SECR.toLocaleString('en-US', { maximumFractionDigits: 0 });
    document.getElementById('spotRd').innerText = `${country.raw.RD_EXP_GDP.toFixed(2)}%`;
    document.getElementById('spotDigServ').innerText = `${country.raw.DIGIT_DELIV_EXP.toFixed(1)}%`;

    // Narrative
    document.getElementById('spotStrength').innerText = country.profile.strength;
    document.getElementById('spotGap').innerText = country.profile.gap;

    // AI 4C Progress Bars
    const ai = country.profile.ai4c;
    document.getElementById('ai4cConn').innerText = ai.conn.tag;
    document.getElementById('barConn').style.width = `${ai.conn.pct}%`;
    document.getElementById('barConn').className = `progress-fill ${ai.conn.fill}`;

    document.getElementById('ai4cComp').innerText = ai.comp.tag;
    document.getElementById('barComp').style.width = `${ai.comp.pct}%`;
    document.getElementById('barComp').className = `progress-fill ${ai.comp.fill}`;

    document.getElementById('ai4cCont').innerText = ai.cont.tag;
    document.getElementById('barCont').style.width = `${ai.cont.pct}%`;
    document.getElementById('barCont').className = `progress-fill ${ai.cont.fill}`;

    document.getElementById('ai4cCompTalent').innerText = ai.talent.tag;
    document.getElementById('barTalent').style.width = `${ai.talent.pct}%`;
    document.getElementById('barTalent').className = `progress-fill ${ai.talent.fill}`;

    renderLeaderboard();
    renderStudioChart();
  }

  // 5. Interactive Studio Chart Controller
  const ctx = document.getElementById('studioChartCanvas').getContext('2d');
  const radarPeerControl = document.getElementById('radarPeerControl');
  const heatmapContainer = document.getElementById('heatmapContainer');
  const canvasHolder = document.querySelector('.canvas-holder');

  function renderStudioChart() {
    if (studioChartInstance) {
      studioChartInstance.destroy();
    }

    radarPeerControl.style.display = currentChartType === 'radar' ? 'flex' : 'none';
    heatmapContainer.style.display = currentChartType === 'heatmap' ? 'block' : 'none';
    canvasHolder.style.display = currentChartType === 'heatmap' ? 'none' : 'block';

    const getNormArray = (c) => indicatorsMeta.map(i => c.norm[i.code]);

    if (currentChartType === 'radar') {
      document.getElementById('visualizerMainTitle').innerHTML = `<i class="fa-solid fa-spider"></i> Dimensional Radar Benchmark (${selectedCountry.name} vs ${selectedPeer.name})`;
      document.getElementById('visualizerMainSubtitle').innerText = "Comparing 8 normalized indicators on an equitable [0, 100] scale";

      document.getElementById('insightObserve').innerText = `Observing ${selectedCountry.name} vs ${selectedPeer.name}: ${selectedCountry.name} records high user penetration and affordability, but is outpaced in compute infrastructure and R&D.`;
      document.getElementById('insightMeaning').innerText = `A wide divergence in radar shapes illustrates structural asymmetry: ${selectedPeer.name} has stronger specialized export intensity or backend servers.`;
      document.getElementById('insightLimit').innerText = `Radar scores represent relative position within this 5-country cohort, not absolute global maximums.`;

      studioChartInstance = new Chart(ctx, {
        type: 'radar',
        data: {
          labels: indicatorsMeta.map(i => i.short),
          datasets: [
            {
              label: `${selectedCountry.flag} ${selectedCountry.name}`,
              data: getNormArray(selectedCountry),
              backgroundColor: 'rgba(244, 63, 94, 0.25)',
              borderColor: '#f43f5e',
              pointBackgroundColor: '#f43f5e',
              pointBorderColor: '#fff',
              pointRadius: 4,
              borderWidth: 2.5
            },
            {
              label: `${selectedPeer.flag} ${selectedPeer.name}`,
              data: getNormArray(selectedPeer),
              backgroundColor: 'rgba(16, 185, 129, 0.2)',
              borderColor: '#10b981',
              pointBackgroundColor: '#10b981',
              pointBorderColor: '#fff',
              pointRadius: 4,
              borderWidth: 2.5
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            r: {
              angleLines: { color: 'rgba(255,255,255,0.08)' },
              grid: { color: 'rgba(255,255,255,0.08)' },
              pointLabels: { color: '#cbd5e1', font: { size: 11, weight: 'bold', family: "'Plus Jakarta Sans'" } },
              ticks: { backdropColor: 'transparent', color: '#64748b', min: 0, max: 100 }
            }
          },
          plugins: {
            legend: { labels: { color: '#f8fafc', font: { size: 12, weight: 'bold' } } },
            tooltip: {
              callbacks: {
                label: (c) => ` ${c.dataset.label}: ${c.raw.toFixed(1)} / 100`
              }
            }
          }
        }
      });
    } else if (currentChartType === 'scatter') {
      document.getElementById('visualizerMainTitle').innerHTML = `<i class="fa-solid fa-cubes"></i> Knowledge Capital vs Digital Trade Specialization`;
      document.getElementById('visualizerMainSubtitle').innerText = "R&D Expenditure (% GDP) plotted against Digitally Deliverable Services (% Exports)";

      document.getElementById('insightObserve').innerText = "Argentina (64.2%) and Netherlands (58.4%) occupy the high-specialization tier. Mexico is located in the lower-left quadrant (0.27% R&D, 24.5% digital exports).";
      document.getElementById('insightMeaning').innerText = "Economies with supportive software policies capture higher export margins independently of physical manufacturing assembly lines.";
      document.getElementById('insightLimit').innerText = "Scatter placement does not establish single-variable causality; export performance is also shaped by time zones and tax incentives.";

      studioChartInstance = new Chart(ctx, {
        type: 'scatter',
        data: {
          datasets: countries.map(c => ({
            label: `${c.flag} ${c.name}`,
            data: [{ x: c.raw.RD_EXP_GDP, y: c.raw.DIGIT_DELIV_EXP }],
            backgroundColor: c.iso3 === 'NLD' ? '#10b981' :
                             c.iso3 === 'NZL' ? '#a855f7' :
                             c.iso3 === 'ARG' ? '#3b82f6' :
                             c.iso3 === 'MEX' ? '#f43f5e' : '#f59e0b',
            pointRadius: c.iso3 === selectedCountry.iso3 ? 14 : 9,
            pointHoverRadius: 16
          }))
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            x: {
              title: { display: true, text: 'R&D Expenditure (% of GDP)', color: '#94a3b8', font: { weight: 'bold' } },
              grid: { color: 'rgba(255,255,255,0.05)' },
              ticks: { color: '#cbd5e1' }
            },
            y: {
              title: { display: true, text: 'Digitally Deliverable Services (% Total Service Exports)', color: '#94a3b8', font: { weight: 'bold' } },
              grid: { color: 'rgba(255,255,255,0.05)' },
              ticks: { color: '#cbd5e1' }
            }
          },
          plugins: {
            legend: { labels: { color: '#fff' } },
            tooltip: {
              callbacks: {
                label: (c) => `${c.dataset.label}: R&D = ${c.raw.x}% | Digital Serv. = ${c.raw.y}%`
              }
            }
          }
        }
      });
    } else if (currentChartType === 'bars') {
      document.getElementById('visualizerMainTitle').innerHTML = `<i class="fa-solid fa-chart-bar"></i> Normalized Indicator Profile for ${selectedCountry.name}`;
      document.getElementById('visualizerMainSubtitle').innerText = "Evaluating relative strengths and vulnerabilities across all 8 dimensions";

      document.getElementById('insightObserve').innerText = `${selectedCountry.name} exhibits maximum scores in internet users and affordability, but near-zero scores in R&D, secure servers, and digital exports.`;
      document.getElementById('insightMeaning').innerText = "The bar profile cleanly highlights the dual nature of Mexico's digital economy: advanced consumption vs. lagging technological production.";
      document.getElementById('insightLimit').innerText = "Zero-normalized scores reflect the lowest value within the 5-country dataset, not absolute absence in the physical world.";

      const vals = getNormArray(selectedCountry);

      studioChartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: indicatorsMeta.map(i => i.short),
          datasets: [{
            label: 'Normalized Score [0 - 100]',
            data: vals,
            backgroundColor: vals.map(v => v >= 75 ? '#10b981' : v >= 40 ? '#06b6d4' : '#f43f5e'),
            borderRadius: 6,
            barThickness: 24
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
            tooltip: {
              callbacks: {
                label: (c) => ` Score: ${c.raw.toFixed(1)} / 100`
              }
            }
          },
          scales: {
            y: {
              beginAtZero: true,
              max: 100,
              grid: { color: 'rgba(255,255,255,0.05)' },
              ticks: { color: '#94a3b8' }
            },
            x: {
              grid: { display: false },
              ticks: { color: '#cbd5e1', font: { weight: 'bold' } }
            }
          }
        }
      });
    } else if (currentChartType === 'heatmap') {
      document.getElementById('visualizerMainTitle').innerHTML = `<i class="fa-solid fa-table-cells"></i> Comparative AgTech Readiness Heatmap Matrix`;
      document.getElementById('visualizerMainSubtitle').innerText = "Heat intensity of all 5 economies across the 8 normalized dimensions";

      document.getElementById('insightObserve').innerText = "The Netherlands shows an uninterrupted emerald profile across almost all dimensions. Mexico and Kenya exhibit high heat in specific niches (users and mobile).";
      document.getElementById('insightMeaning').innerText = "Heatmap gradients immediately reveal the digital readiness tiers separating Northern Europe / Oceania from Latin America and Africa.";
      document.getElementById('insightLimit').innerText = "Gradients reflect min-max relative performance across the 5 assigned economies.";

      renderHeatmapTable();
    }
  }

  function renderHeatmapTable() {
    let html = `
      <table class="heatmap-table">
        <thead>
          <tr>
            <th style="text-align:left;">Economy</th>
            ${indicatorsMeta.map(i => `<th>${i.short}</th>`).join('')}
            <th>DRS</th>
          </tr>
        </thead>
        <tbody>
    `;

    countries.forEach(c => {
      html += `<tr><td style="text-align:left; font-weight:800;">${c.flag} ${c.name}</td>`;
      indicatorsMeta.forEach(i => {
        const val = c.norm[i.code];
        const alpha = Math.max(0.12, val / 100);
        const bg = val >= 70 ? `rgba(16, 185, 129, ${alpha})` :
                   val >= 35 ? `rgba(6, 182, 212, ${alpha})` : `rgba(244, 63, 94, ${alpha})`;
        html += `<td><span class="heatmap-cell" style="background:${bg};">${val.toFixed(0)}</span></td>`;
      });
      html += `<td><strong style="color:var(--emerald-neon); font-size:0.9rem;">${c.drs.toFixed(1)}</strong></td></tr>`;
    });

    html += '</tbody></table>';
    heatmapContainer.innerHTML = html;
  }

  // Peer dropdown for Radar
  document.getElementById('selectRadarPeer').addEventListener('change', (e) => {
    selectedPeer = countries.find(c => c.iso3 === e.target.value);
    renderStudioChart();
  });

  // Studio View Switcher Tabs
  document.querySelectorAll('.studio-tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.studio-tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentChartType = btn.dataset.chart;
      renderStudioChart();
    });
  });

  // 6. Accordion for Executive Diagnosis
  document.querySelectorAll('.diag-card').forEach(card => {
    card.addEventListener('click', () => {
      const wasActive = card.classList.contains('active');
      document.querySelectorAll('.diag-card').forEach(c => c.classList.remove('active'));
      if (!wasActive) {
        card.classList.add('active');
      }
    });
  });

  // 7. Render Consolidated Data Matrix Table & Search Filter
  function renderMatrixTable(filterText = '') {
    const tbody = document.getElementById('matrixTableBody');
    tbody.innerHTML = '';
    const filtered = countries.filter(c => c.name.toLowerCase().includes(filterText.toLowerCase()) || c.region.toLowerCase().includes(filterText.toLowerCase()));

    filtered.forEach(d => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td><strong>${d.flag} ${d.name}</strong></td>
        <td>${d.raw.IT_NET_BBND.toFixed(2)}</td>
        <td>${d.raw.IT_NET_SECR.toLocaleString('en-US', {maximumFractionDigits: 0})}</td>
        <td>${d.raw.IT_NET_USER.toFixed(1)}%</td>
        <td>${d.raw.ITU_PRICE_BASKET.toFixed(2)}%</td>
        <td>${d.raw.ICT_SERV_EXP.toFixed(2)}%</td>
        <td>${d.raw.DIGIT_DELIV_EXP.toFixed(1)}%</td>
        <td>${d.raw.RD_EXP_GDP.toFixed(2)}%</td>
        <td>${d.raw.PATENT_RES_PM.toFixed(1)}</td>
        <td><span class="table-drs-tag">${d.drs.toFixed(2)}</span></td>
      `;
      tbody.appendChild(tr);
    });
  }
  renderMatrixTable();

  document.getElementById('tableFilterInput').addEventListener('input', (e) => {
    renderMatrixTable(e.target.value);
  });

  // 8. Interactive Policy Simulator Logic with Presets
  const simulatorDrawer = document.getElementById('simulatorDrawer');
  const simulatorBackdrop = document.getElementById('simulatorBackdrop');
  const btnOpenSimulator = document.getElementById('btnOpenSimulator');
  const btnCloseSimulator = document.getElementById('btnCloseSimulator');
  const slidersContainer = document.getElementById('simulatorSliders');
  const simRankingContainer = document.getElementById('simulatedRankingContainer');

  btnOpenSimulator.addEventListener('click', () => {
    simulatorDrawer.classList.add('open');
    simulatorBackdrop.classList.add('open');
  });

  const closeSim = () => {
    simulatorDrawer.classList.remove('open');
    simulatorBackdrop.classList.remove('open');
  };

  btnCloseSimulator.addEventListener('click', closeSim);
  simulatorBackdrop.addEventListener('click', closeSim);

  let currentWeights = {
    IT_NET_BBND: 12.5,
    IT_NET_SECR: 12.5,
    IT_NET_USER: 12.5,
    ITU_PRICE_BASKET: 12.5,
    ICT_SERV_EXP: 12.5,
    DIGIT_DELIV_EXP: 12.5,
    RD_EXP_GDP: 12.5,
    PATENT_RES_PM: 12.5
  };

  // Render Sliders
  indicatorsMeta.forEach(ind => {
    const div = document.createElement('div');
    div.className = 'slider-unit';
    div.innerHTML = `
      <div class="slider-top-label">
        <span>${ind.label}</span>
        <span id="slider_num_${ind.code}">12.5%</span>
      </div>
      <input type="range" id="slider_ctrl_${ind.code}" min="0" max="100" value="12.5" step="0.5">
    `;
    slidersContainer.appendChild(div);

    const range = div.querySelector(`#slider_ctrl_${ind.code}`);
    range.addEventListener('input', (e) => {
      document.getElementById(`slider_num_${ind.code}`).innerText = `${parseFloat(e.target.value).toFixed(1)}%`;
      document.querySelectorAll('.btn-preset').forEach(b => b.classList.remove('active'));
      recomputeSimulatedDRS();
    });
  });

  function applyPreset(presetKey) {
    if (presetKey === 'equal') {
      indicatorsMeta.forEach(i => currentWeights[i.code] = 12.5);
    } else if (presetKey === 'innovation') {
      indicatorsMeta.forEach(i => currentWeights[i.code] = (i.code === 'RD_EXP_GDP' || i.code === 'PATENT_RES_PM') ? 35 : 5);
    } else if (presetKey === 'exports') {
      indicatorsMeta.forEach(i => currentWeights[i.code] = (i.code === 'ICT_SERV_EXP' || i.code === 'DIGIT_DELIV_EXP') ? 35 : 5);
    } else if (presetKey === 'infrastructure') {
      indicatorsMeta.forEach(i => currentWeights[i.code] = (i.code === 'IT_NET_SECR' || i.code === 'IT_NET_BBND') ? 35 : 5);
    }

    indicatorsMeta.forEach(i => {
      const ctrl = document.getElementById(`slider_ctrl_${i.code}`);
      if (ctrl) {
        ctrl.value = currentWeights[i.code];
        document.getElementById(`slider_num_${i.code}`).innerText = `${currentWeights[i.code].toFixed(1)}%`;
      }
    });

    recomputeSimulatedDRS();
  }

  document.querySelectorAll('.btn-preset').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.btn-preset').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      applyPreset(btn.dataset.preset);
    });
  });

  function recomputeSimulatedDRS() {
    let sumW = 0;
    indicatorsMeta.forEach(i => {
      const v = parseFloat(document.getElementById(`slider_ctrl_${i.code}`).value);
      currentWeights[i.code] = v;
      sumW += v;
    });

    const normW = {};
    indicatorsMeta.forEach(i => {
      normW[i.code] = sumW > 0 ? currentWeights[i.code] / sumW : 0.125;
    });

    const simList = countries.map(c => {
      let score = 0;
      indicatorsMeta.forEach(i => {
        score += c.norm[i.code] * normW[i.code];
      });
      return { ...c, simDrs: score };
    });

    simList.sort((a, b) => b.simDrs - a.simDrs);

    simRankingContainer.innerHTML = '';
    simList.forEach((c, idx) => {
      const row = document.createElement('div');
      row.className = 'sim-rank-row';
      row.innerHTML = `
        <span><strong>#${idx + 1}</strong> ${c.flag} ${c.name}</span>
        <span style="color:var(--emerald-neon); font-weight:800;">${c.simDrs.toFixed(2)} pts</span>
      `;
      simRankingContainer.appendChild(row);
    });
  }

  // Initial Load
  setTargetCountry('MEX');
  applyPreset('equal');
});
