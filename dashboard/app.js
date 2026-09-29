// ==========================================================================
// AGTECH DIGITAL ECONOMY INTELLIGENCE - DASHBOARD SCRIPT (ENGLISH)
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {

  // Official Consolidated Dataset (Year 2023)
  const countriesData = [
    {
      iso3: "MEX",
      name: "Mexico",
      flag: "🇲🇽",
      region: "Latin America",
      income: "Upper-middle income",
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
      drs: 26.57,
      rank: 4,
      profile: {
        strength: "Broad consumer internet penetration (81.2%) and affordable entry-level broadband basket (1.95% of GNI).",
        gap: "Critically low R&D investment (0.27% of GDP) and minimal digital services export share (24.5%).",
        agtechRole: "High production scale across Sinaloa and Bajio regions, but predominantly dependent on imported turnkey technology.",
        aiReadiness: "Moderate-Low backend readiness; urgently requires domestic datacenter capacity and local AgTech software engineering."
      }
    },
    {
      iso3: "NLD",
      name: "Netherlands",
      flag: "🇳🇱",
      region: "Europe",
      income: "High income",
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
      drs: 92.14,
      rank: 1,
      profile: {
        strength: "Global benchmark in secure cloud servers (194k/1M), R&D intensity (2.27%), and patents (118.5/1M).",
        gap: "No structural gaps identified across the 8 analyzed dimensions.",
        agtechRole: "2nd global agri-food exporter; unrivaled pioneer in greenhouse precision agriculture and agricultural biotechnology.",
        aiReadiness: "Outstanding; core European datacenter hub with advanced compute, open agricultural datasets, and top-tier AI researchers."
      }
    },
    {
      iso3: "KEN",
      name: "Kenya",
      flag: "🇰🇪",
      region: "Sub-Saharan Africa",
      income: "Lower-middle income",
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
      drs: 15.42,
      rank: 5,
      profile: {
        strength: "World pioneer in mobile money (M-Pesa) and digital financial inclusion for smallholder farmers.",
        gap: "Low fixed broadband penetration (2.39 subs/100) and elevated relative ICT basket cost (10.4% GNI).",
        agtechRole: "Innovative mobile USSD/SMS platforms providing weather alerts, crop microinsurance, and market price discovery.",
        aiReadiness: "Emerging; dynamic Silicon Savannah tech cluster with high mobile adoption, but constrained by server infrastructure."
      }
    },
    {
      iso3: "ARG",
      name: "Argentina",
      flag: "🇦🇷",
      region: "Latin America",
      income: "Upper-middle income",
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
      drs: 55.72,
      rank: 3,
      profile: {
        strength: "Regional leader in digitally deliverable services exports (64.2%) and ICT services (15.9%).",
        gap: "Modest R&D expenditure compared to OECD benchmarks and macroeconomic currency volatility.",
        agtechRole: "Powerhouse in AgTech software startups, satellite precision seeding mapping, and digital farm management platforms.",
        aiReadiness: "High in software programming and algorithmic talent; moderate in local tier-3/4 datacenter infrastructure."
      }
    },
    {
      iso3: "NZL",
      name: "New Zealand",
      flag: "🇳🇿",
      region: "Asia-Pacific",
      income: "High income",
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
      drs: 60.91,
      rank: 2,
      profile: {
        strength: "High broadband affordability (0.98% GNI), 1.55% GDP in R&D, and 63.8 resident patents per million people.",
        gap: "Moderate ICT services share due to strong trade specialization in dairy and primary commodities.",
        agtechRole: "End-to-end digitalized pastoral farming, pasture biomass sensors, and automated electronic livestock traceability.",
        aiReadiness: "High; robust institutional governance and AI models targeted at primary sector productivity and sustainability."
      }
    }
  ];

  // 8 Indicators Metadata
  const indicatorsMeta = [
    { code: 'IT_NET_BBND', label: 'Fixed Broadband', category: 'Infrastructure', dir: 1, unit: 'subs/100 pop' },
    { code: 'IT_NET_SECR', label: 'Secure Servers', category: 'Infrastructure', dir: 1, unit: 'servers/1M pop' },
    { code: 'IT_NET_USER', label: 'Internet Users', category: 'Access/Usage', dir: 1, unit: '% pop' },
    { code: 'ITU_PRICE_BASKET', label: 'ICT Affordability', category: 'Affordability', dir: -1, unit: '% GNI p.c. [Inv]' },
    { code: 'ICT_SERV_EXP', label: 'ICT Service Exports', category: 'Economic Activity', dir: 1, unit: '% services' },
    { code: 'DIGIT_DELIV_EXP', label: 'Digital Deliverables', category: 'Economic Activity', dir: 1, unit: '% services' },
    { code: 'RD_EXP_GDP', label: 'R&D Expenditure', category: 'Innovation', dir: 1, unit: '% GDP' },
    { code: 'PATENT_RES_PM', label: 'Resident Patents', category: 'Innovation', dir: 1, unit: 'patents/1M pop' }
  ];

  // Weight State for Simulator
  let currentWeights = {
    IT_NET_BBND: 0.125,
    IT_NET_SECR: 0.125,
    IT_NET_USER: 0.125,
    ITU_PRICE_BASKET: 0.125,
    ICT_SERV_EXP: 0.125,
    DIGIT_DELIV_EXP: 0.125,
    RD_EXP_GDP: 0.125,
    PATENT_RES_PM: 0.125
  };

  let selectedSpotlightCountry = countriesData.find(c => c.iso3 === 'MEX');
  let selectedRadarPeer = countriesData.find(c => c.iso3 === 'ARG');

  // 1. Render Country Quick Pills
  const pillsContainer = document.getElementById('countryPillsContainer');
  countriesData.forEach(country => {
    const pill = document.createElement('button');
    pill.className = `country-pill ${country.iso3 === 'MEX' ? 'active' : ''}`;
    pill.dataset.iso = country.iso3;
    pill.innerHTML = `<span>${country.flag}</span> <span>${country.name}</span> <small style="color:var(--emerald-400)">(${country.drs.toFixed(1)} pts)</small>`;
    pill.addEventListener('click', () => {
      document.querySelectorAll('.country-pill').forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      setSpotlightCountry(country.iso3);
    });
    pillsContainer.appendChild(pill);
  });

  // KPI Card clicks
  document.querySelectorAll('.kpi-card[data-country]').forEach(card => {
    card.addEventListener('click', () => {
      const iso = card.dataset.country;
      if (iso) {
        document.querySelectorAll('.country-pill').forEach(p => {
          p.classList.toggle('active', p.dataset.iso === iso);
        });
        setSpotlightCountry(iso);
      }
    });
  });

  // 2. Set Spotlight Country Function
  function setSpotlightCountry(iso) {
    const country = countriesData.find(c => c.iso3 === iso);
    if (!country) return;
    selectedSpotlightCountry = country;

    document.getElementById('spotlightBadge').innerHTML = `${country.flag} ${country.name.toUpperCase()}`;
    
    // Metrics grid
    const metricsContainer = document.getElementById('spotlightMetrics');
    metricsContainer.innerHTML = `
      <div class="spot-stat">
        <div class="spot-stat-label">DRS Score (Overall)</div>
        <div class="spot-stat-value" style="color:var(--emerald-400)">${country.drs.toFixed(2)} pts <small>(Rank #${country.rank})</small></div>
      </div>
      <div class="spot-stat">
        <div class="spot-stat-label">Internet Users</div>
        <div class="spot-stat-value">${country.raw.IT_NET_USER.toFixed(1)}%</div>
      </div>
      <div class="spot-stat">
        <div class="spot-stat-label">Secure Servers / 1M</div>
        <div class="spot-stat-value">${country.raw.IT_NET_SECR.toLocaleString()}</div>
      </div>
      <div class="spot-stat">
        <div class="spot-stat-label">R&D Spend (% GDP)</div>
        <div class="spot-stat-value">${country.raw.RD_EXP_GDP.toFixed(2)}%</div>
      </div>
    `;

    // Profile Analysis
    const analysisContainer = document.getElementById('spotlightAnalysis');
    analysisContainer.innerHTML = `
      <p><strong><i class="fa-solid fa-circle-check" style="color:var(--emerald-400)"></i> Key Strength:</strong> ${country.profile.strength}</p>
      <p style="margin-top:0.4rem;"><strong><i class="fa-solid fa-triangle-exclamation" style="color:var(--rose-500)"></i> Core Gap:</strong> ${country.profile.gap}</p>
      <p style="margin-top:0.4rem;"><strong><i class="fa-solid fa-seedling" style="color:var(--cyan-400)"></i> AgTech Role:</strong> ${country.profile.agtechRole}</p>
      <p style="margin-top:0.4rem;"><strong><i class="fa-solid fa-brain" style="color:var(--violet-400)"></i> AI Readiness:</strong> ${country.profile.aiReadiness}</p>
    `;
  }
  setSpotlightCountry('MEX');

  // 3. Tab Navigation Logic
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));

      btn.classList.add('active');
      const targetId = btn.dataset.tab;
      document.getElementById(targetId).classList.add('active');
    });
  });

  // 4. Render Main Table
  const mainTableBody = document.getElementById('mainTableBody');
  countriesData.forEach(d => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><strong>${d.flag} ${d.name}</strong></td>
      <td>${d.region}</td>
      <td>${d.raw.IT_NET_BBND.toFixed(2)}</td>
      <td>${d.raw.IT_NET_SECR.toLocaleString('en-US', {maximumFractionDigits: 1})}</td>
      <td>${d.raw.IT_NET_USER.toFixed(1)}%</td>
      <td>${d.raw.ITU_PRICE_BASKET.toFixed(2)}%</td>
      <td>${d.raw.ICT_SERV_EXP.toFixed(2)}%</td>
      <td>${d.raw.DIGIT_DELIV_EXP.toFixed(1)}%</td>
      <td>${d.raw.RD_EXP_GDP.toFixed(2)}%</td>
      <td>${d.raw.PATENT_RES_PM.toFixed(1)}</td>
      <td><span class="drs-pill">${d.drs.toFixed(2)}</span></td>
    `;
    mainTableBody.appendChild(tr);
  });

  // 5. Render Dimensions List
  function updateDimensionsList(peerIso) {
    const peer = countriesData.find(c => c.iso3 === peerIso);
    const mex = countriesData.find(c => c.iso3 === 'MEX');
    const listContainer = document.getElementById('dimensionsList');
    listContainer.innerHTML = '';

    indicatorsMeta.forEach(ind => {
      const mexVal = mex.raw[ind.code];
      const peerVal = peer.raw[ind.code];
      
      const item = document.createElement('div');
      item.className = 'dim-item';
      item.innerHTML = `
        <div class="dim-info">
          <span class="dim-title">${ind.label}</span>
          <span class="dim-source">${ind.category} · ${ind.unit}</span>
        </div>
        <div class="dim-values">
          <span class="mex-val">MEX: ${typeof mexVal === 'number' ? (ind.code === 'IT_NET_SECR' ? mexVal.toLocaleString() : mexVal.toFixed(2)) : mexVal}</span> | 
          <span class="peer-val">${peer.iso3}: ${typeof peerVal === 'number' ? (ind.code === 'IT_NET_SECR' ? peerVal.toLocaleString() : peerVal.toFixed(2)) : peerVal}</span>
        </div>
      `;
      listContainer.appendChild(item);
    });
  }
  updateDimensionsList('ARG');

  // 6. Charts Setup (Chart.js)
  // Chart 1: DRS Ranking
  const drsCtx = document.getElementById('drsChart').getContext('2d');
  const sortedByDrs = [...countriesData].sort((a, b) => b.drs - a.drs);
  
  new Chart(drsCtx, {
    type: 'bar',
    data: {
      labels: sortedByDrs.map(c => `${c.flag} ${c.name}`),
      datasets: [{
        label: 'Digital Readiness Score',
        data: sortedByDrs.map(c => c.drs),
        backgroundColor: sortedByDrs.map(c => 
          c.iso3 === 'NLD' ? '#10b981' :
          c.iso3 === 'MEX' ? '#f43f5e' :
          c.iso3 === 'ARG' ? '#3b82f6' :
          c.iso3 === 'NZL' ? '#8b5cf6' : '#f59e0b'
        ),
        borderRadius: 8,
        barThickness: 28
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: (ctx) => ` DRS: ${ctx.raw.toFixed(2)} pts`
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

  // Chart 2: Radar Chart
  const radarCtx = document.getElementById('radarChart').getContext('2d');
  const radarLabels = indicatorsMeta.map(i => i.label);

  const getRadarValues = (country) => [
    country.norm.IT_NET_BBND,
    country.norm.IT_NET_SECR,
    country.norm.IT_NET_USER,
    country.norm.ITU_PRICE_BASKET,
    country.norm.ICT_SERV_EXP,
    country.norm.DIGIT_DELIV_EXP,
    country.norm.RD_EXP_GDP,
    country.norm.PATENT_RES_PM
  ];

  const mexData = countriesData.find(c => c.iso3 === 'MEX');

  const radarChart = new Chart(radarCtx, {
    type: 'radar',
    data: {
      labels: radarLabels,
      datasets: [
        {
          label: 'Mexico 🇲🇽',
          data: getRadarValues(mexData),
          backgroundColor: 'rgba(244, 63, 94, 0.2)',
          borderColor: 'rgba(244, 63, 94, 1)',
          pointBackgroundColor: 'rgba(244, 63, 94, 1)',
          borderWidth: 2.5
        },
        {
          label: `${selectedRadarPeer.name} ${selectedRadarPeer.flag}`,
          data: getRadarValues(selectedRadarPeer),
          backgroundColor: 'rgba(59, 130, 246, 0.2)',
          borderColor: 'rgba(59, 130, 246, 1)',
          pointBackgroundColor: 'rgba(59, 130, 246, 1)',
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
          pointLabels: { color: '#cbd5e1', font: { size: 11, weight: 'bold' } },
          ticks: { backdropColor: 'transparent', color: '#94a3b8', min: 0, max: 100 }
        }
      },
      plugins: {
        legend: { labels: { color: '#fff', font: { size: 12 } } }
      }
    }
  });

  document.getElementById('radarPeerSelect').addEventListener('change', (e) => {
    const peerIso = e.target.value;
    selectedRadarPeer = countriesData.find(c => c.iso3 === peerIso);
    
    radarChart.data.datasets[1] = {
      label: `${selectedRadarPeer.name} ${selectedRadarPeer.flag}`,
      data: getRadarValues(selectedRadarPeer),
      backgroundColor: peerIso === 'NLD' ? 'rgba(16, 185, 129, 0.2)' :
                       peerIso === 'ARG' ? 'rgba(59, 130, 246, 0.2)' :
                       peerIso === 'NZL' ? 'rgba(139, 92, 246, 0.2)' : 'rgba(245, 158, 11, 0.2)',
      borderColor: peerIso === 'NLD' ? 'rgba(16, 185, 129, 1)' :
                   peerIso === 'ARG' ? 'rgba(59, 130, 246, 1)' :
                   peerIso === 'NZL' ? 'rgba(139, 92, 246, 1)' : 'rgba(245, 158, 11, 1)',
      pointBackgroundColor: peerIso === 'NLD' ? 'rgba(16, 185, 129, 1)' :
                            peerIso === 'ARG' ? 'rgba(59, 130, 246, 1)' :
                            peerIso === 'NZL' ? 'rgba(139, 92, 246, 1)' : 'rgba(245, 158, 11, 1)',
      borderWidth: 2.5
    };
    radarChart.update();
    updateDimensionsList(peerIso);
  });

  // Chart 3: Scatter Plot
  const scatterCtx = document.getElementById('scatterChart').getContext('2d');
  new Chart(scatterCtx, {
    type: 'scatter',
    data: {
      datasets: countriesData.map(c => ({
        label: `${c.flag} ${c.name}`,
        data: [{ x: c.raw.RD_EXP_GDP, y: c.raw.DIGIT_DELIV_EXP }],
        backgroundColor: c.iso3 === 'NLD' ? '#10b981' :
                         c.iso3 === 'MEX' ? '#f43f5e' :
                         c.iso3 === 'ARG' ? '#3b82f6' :
                         c.iso3 === 'NZL' ? '#8b5cf6' : '#f59e0b',
        pointRadius: 11,
        pointHoverRadius: 15
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
          title: { display: true, text: 'Digitally Deliverable Services (% Services)', color: '#94a3b8', font: { weight: 'bold' } },
          grid: { color: 'rgba(255,255,255,0.05)' },
          ticks: { color: '#cbd5e1' }
        }
      },
      plugins: {
        legend: { labels: { color: '#fff' } },
        tooltip: {
          callbacks: {
            label: (ctx) => `${ctx.dataset.label}: R&D = ${ctx.raw.x}% | Digital Serv. = ${ctx.raw.y}%`
          }
        }
      }
    }
  });

  // 7. Interactive DRS Simulator Logic
  const simulatorDrawer = document.getElementById('simulatorDrawer');
  const drawerBackdrop = document.getElementById('drawerBackdrop');
  const btnToggleSimulator = document.getElementById('btnToggleSimulator');
  const btnCloseDrawer = document.getElementById('btnCloseDrawer');
  const slidersContainer = document.getElementById('slidersContainer');
  const simRankingList = document.getElementById('simRankingList');

  btnToggleSimulator.addEventListener('click', () => {
    simulatorDrawer.classList.add('open');
    drawerBackdrop.classList.add('open');
  });

  const closeDrawer = () => {
    simulatorDrawer.classList.remove('open');
    drawerBackdrop.classList.remove('open');
  };

  btnCloseDrawer.addEventListener('click', closeDrawer);
  drawerBackdrop.addEventListener('click', closeDrawer);

  // Render Sliders
  indicatorsMeta.forEach(ind => {
    const group = document.createElement('div');
    group.className = 'slider-group';
    group.innerHTML = `
      <div class="slider-label-row">
        <span>${ind.label}</span>
        <span id="label_val_${ind.code}">12.5%</span>
      </div>
      <input type="range" id="slider_${ind.code}" min="0" max="100" value="12.5" step="0.5">
    `;
    slidersContainer.appendChild(group);

    const slider = group.querySelector(`#slider_${ind.code}`);
    slider.addEventListener('input', (e) => {
      document.getElementById(`label_val_${ind.code}`).innerText = `${parseFloat(e.target.value).toFixed(1)}%`;
      recalculateSimulatedDRS();
    });
  });

  function recalculateSimulatedDRS() {
    let sumWeights = 0;
    indicatorsMeta.forEach(ind => {
      const val = parseFloat(document.getElementById(`slider_${ind.code}`).value);
      currentWeights[ind.code] = val;
      sumWeights += val;
    });

    // Normalize weights to sum to 1.0
    const normWeights = {};
    indicatorsMeta.forEach(ind => {
      normWeights[ind.code] = sumWeights > 0 ? currentWeights[ind.code] / sumWeights : 0.125;
    });

    const simScores = countriesData.map(c => {
      let score = 0;
      indicatorsMeta.forEach(ind => {
        score += c.norm[ind.code] * normWeights[ind.code];
      });
      return { ...c, simDrs: score };
    });

    simScores.sort((a, b) => b.simDrs - a.simDrs);

    simRankingList.innerHTML = '';
    simScores.forEach((c, idx) => {
      const item = document.createElement('div');
      item.className = 'sim-rank-item';
      item.innerHTML = `
        <span><strong>#${idx + 1}</strong> ${c.flag} ${c.name}</span>
        <span style="color:var(--emerald-400); font-weight:bold;">${c.simDrs.toFixed(2)} pts</span>
      `;
      simRankingList.appendChild(item);
    });
  }
  recalculateSimulatedDRS();

  document.getElementById('btnResetWeights').addEventListener('click', () => {
    indicatorsMeta.forEach(ind => {
      const slider = document.getElementById(`slider_${ind.code}`);
      slider.value = 12.5;
      document.getElementById(`label_val_${ind.code}`).innerText = '12.5%';
    });
    recalculateSimulatedDRS();
  });

});
