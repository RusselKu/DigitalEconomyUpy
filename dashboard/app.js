// Digital Economy Intelligence Lab - Dashboard Logic
document.addEventListener('DOMContentLoaded', async () => {

  // Dataset oficial integrado (Año 2023)
  const rawData = [
    {
      country_iso3: "MEX",
      country_name: "México",
      flag: "🇲🇽",
      region: "América Latina",
      IT_NET_BBND: 20.75,
      IT_NET_SECR: 412.12,
      IT_NET_USER: 81.18,
      ITU_PRICE_BASKET: 1.95,
      ICT_SERV_EXP: 2.92,
      DIGIT_DELIV_EXP: 24.50,
      RD_EXP_GDP: 0.27,
      PATENT_RES_PM: 8.80,
      DRS: 26.57,
      DRS_RANK: 4,
      norm: {
        IT_NET_BBND: 44.92,
        IT_NET_SECR: 0.06,
        IT_NET_USER: 75.62,
        ITU_PRICE_BASKET: 88.20,
        ICT_SERV_EXP: 0.00,
        DIGIT_DELIV_EXP: 0.00,
        RD_EXP_GDP: 0.00,
        PATENT_RES_PM: 3.77
      }
    },
    {
      country_iso3: "NLD",
      country_name: "Países Bajos",
      flag: "🇳🇱",
      region: "Europa",
      IT_NET_BBND: 43.26,
      IT_NET_SECR: 194962.90,
      IT_NET_USER: 97.01,
      ITU_PRICE_BASKET: 0.82,
      ICT_SERV_EXP: 9.62,
      DIGIT_DELIV_EXP: 58.40,
      RD_EXP_GDP: 2.27,
      PATENT_RES_PM: 118.50,
      DRS: 92.14,
      DRS_RANK: 1,
      norm: {
        IT_NET_BBND: 100.00,
        IT_NET_SECR: 100.00,
        IT_NET_USER: 100.00,
        ITU_PRICE_BASKET: 100.00,
        ICT_SERV_EXP: 51.74,
        DIGIT_DELIV_EXP: 85.39,
        RD_EXP_GDP: 100.00,
        PATENT_RES_PM: 100.00
      }
    },
    {
      country_iso3: "KEN",
      country_name: "Kenia",
      flag: "🇰🇪",
      region: "África Subsahariana",
      IT_NET_BBND: 2.39,
      IT_NET_SECR: 297.13,
      IT_NET_USER: 32.07,
      ITU_PRICE_BASKET: 10.40,
      ICT_SERV_EXP: 10.67,
      DIGIT_DELIV_EXP: 39.20,
      RD_EXP_GDP: 0.80,
      PATENT_RES_PM: 4.50,
      DRS: 15.42,
      DRS_RANK: 5,
      norm: {
        IT_NET_BBND: 0.00,
        IT_NET_SECR: 0.00,
        IT_NET_USER: 0.00,
        ITU_PRICE_BASKET: 0.00,
        ICT_SERV_EXP: 59.85,
        DIGIT_DELIV_EXP: 37.03,
        RD_EXP_GDP: 26.50,
        PATENT_RES_PM: 0.00
      }
    },
    {
      country_iso3: "ARG",
      country_name: "Argentina",
      flag: "🇦🇷",
      region: "América Latina",
      IT_NET_BBND: 25.36,
      IT_NET_SECR: 5451.20,
      IT_NET_USER: 89.23,
      ITU_PRICE_BASKET: 2.90,
      ICT_SERV_EXP: 15.87,
      DIGIT_DELIV_EXP: 64.20,
      RD_EXP_GDP: 0.60,
      PATENT_RES_PM: 9.20,
      DRS: 55.72,
      DRS_RANK: 3,
      norm: {
        IT_NET_BBND: 56.20,
        IT_NET_SECR: 2.65,
        IT_NET_USER: 88.02,
        ITU_PRICE_BASKET: 78.29,
        ICT_SERV_EXP: 100.00,
        DIGIT_DELIV_EXP: 100.00,
        RD_EXP_GDP: 16.50,
        PATENT_RES_PM: 4.12
      }
    },
    {
      country_iso3: "NZL",
      country_name: "Nueva Zelanda",
      flag: "🇳🇿",
      region: "Asia-Pacífico",
      IT_NET_BBND: 37.85,
      IT_NET_SECR: 18993.65,
      IT_NET_USER: 93.33,
      ITU_PRICE_BASKET: 0.98,
      ICT_SERV_EXP: 6.95,
      DIGIT_DELIV_EXP: 44.80,
      RD_EXP_GDP: 1.55,
      PATENT_RES_PM: 63.80,
      DRS: 60.91,
      DRS_RANK: 2,
      norm: {
        IT_NET_BBND: 86.77,
        IT_NET_SECR: 9.60,
        IT_NET_USER: 94.33,
        ITU_PRICE_BASKET: 98.33,
        ICT_SERV_EXP: 31.12,
        DIGIT_DELIV_EXP: 51.13,
        RD_EXP_GDP: 64.00,
        PATENT_RES_PM: 52.02
      }
    }
  ];

  // 1. Populate Table
  const tableBody = document.getElementById('tableBody');
  rawData.forEach(d => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td class="country-cell">${d.flag} ${d.country_name}</td>
      <td>${d.region}</td>
      <td>${d.IT_NET_BBND.toFixed(2)}</td>
      <td>${d.IT_NET_SECR.toLocaleString('es-MX', {maximumFractionDigits: 1})}</td>
      <td>${d.IT_NET_USER.toFixed(1)}%</td>
      <td>${d.ITU_PRICE_BASKET.toFixed(2)}%</td>
      <td>${d.ICT_SERV_EXP.toFixed(2)}%</td>
      <td>${d.DIGIT_DELIV_EXP.toFixed(1)}%</td>
      <td>${d.RD_EXP_GDP.toFixed(2)}%</td>
      <td>${d.PATENT_RES_PM.toFixed(1)}</td>
      <td><span class="score-badge">${d.DRS.toFixed(2)}</span></td>
    `;
    tableBody.appendChild(tr);
  });

  // 2. Render DRS Ranking Bar Chart
  const drsCtx = document.getElementById('drsRankingChart').getContext('2d');
  const sortedData = [...rawData].sort((a, b) => b.DRS - a.DRS);

  new Chart(drsCtx, {
    type: 'bar',
    data: {
      labels: sortedData.map(d => `${d.flag} ${d.country_name}`),
      datasets: [{
        label: 'DRS Score',
        data: sortedData.map(d => d.DRS),
        backgroundColor: sortedData.map(d => 
          d.country_iso3 === 'NLD' ? '#10b981' :
          d.country_iso3 === 'MEX' ? '#ef4444' :
          d.country_iso3 === 'ARG' ? '#3b82f6' :
          d.country_iso3 === 'NZL' ? '#8b5cf6' : '#f59e0b'
        ),
        borderRadius: 8
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: (ctx) => ` DRS: ${ctx.raw.toFixed(2)} puntos`
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

  // 3. Render Radar Chart (Dimensional Comparison)
  const radarCtx = document.getElementById('radarChart').getContext('2d');
  const categories = [
    'Banda Ancha Fija', 'Servidores Seguros', 'Usuarios Internet',
    'Asequibilidad TIC', 'Export. Serv. TIC', 'Serv. Digitalizables',
    'Gasto I+D', 'Patentes Residentes'
  ];

  const mexData = rawData.find(d => d.country_iso3 === 'MEX');
  let selectedPeer = rawData.find(d => d.country_iso3 === 'ARG');

  const getRadarDataset = (country, color, label) => ({
    label: label,
    data: [
      country.norm.IT_NET_BBND,
      country.norm.IT_NET_SECR,
      country.norm.IT_NET_USER,
      country.norm.ITU_PRICE_BASKET,
      country.norm.ICT_SERV_EXP,
      country.norm.DIGIT_DELIV_EXP,
      country.norm.RD_EXP_GDP,
      country.norm.PATENT_RES_PM
    ],
    backgroundColor: color.replace('1)', '0.2)'),
    borderColor: color,
    pointBackgroundColor: color,
    borderWidth: 2
  });

  let radarChart = new Chart(radarCtx, {
    type: 'radar',
    data: {
      labels: categories,
      datasets: [
        getRadarDataset(mexData, 'rgba(239, 68, 68, 1)', 'México 🇲🇽'),
        getRadarDataset(selectedPeer, 'rgba(59, 130, 246, 1)', `${selectedPeer.country_name} ${selectedPeer.flag}`)
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
        legend: {
          labels: { color: '#fff', font: { size: 12 } }
        }
      }
    }
  });

  document.getElementById('peerSelect').addEventListener('change', (e) => {
    const iso = e.target.value;
    selectedPeer = rawData.find(d => d.country_iso3 === iso);
    radarChart.data.datasets[1] = getRadarDataset(
      selectedPeer,
      iso === 'NLD' ? 'rgba(16, 185, 129, 1)' :
      iso === 'ARG' ? 'rgba(59, 130, 246, 1)' :
      iso === 'NZL' ? 'rgba(139, 92, 246, 1)' : 'rgba(245, 158, 11, 1)',
      `${selectedPeer.country_name} ${selectedPeer.flag}`
    );
    radarChart.update();
  });

  // 4. Render Scatter Plot (R&D vs Digital Services Exports)
  const scatterCtx = document.getElementById('scatterChart').getContext('2d');
  new Chart(scatterCtx, {
    type: 'scatter',
    data: {
      datasets: rawData.map(d => ({
        label: `${d.flag} ${d.country_name}`,
        data: [{ x: d.RD_EXP_GDP, y: d.DIGIT_DELIV_EXP }],
        backgroundColor: 
          d.country_iso3 === 'NLD' ? '#10b981' :
          d.country_iso3 === 'MEX' ? '#ef4444' :
          d.country_iso3 === 'ARG' ? '#3b82f6' :
          d.country_iso3 === 'NZL' ? '#8b5cf6' : '#f59e0b',
        pointRadius: 10,
        pointHoverRadius: 13
      }))
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: {
          title: { display: true, text: 'Gasto en I+D (% del PIB)', color: '#94a3b8', font: { weight: 'bold' } },
          grid: { color: 'rgba(255,255,255,0.05)' },
          ticks: { color: '#cbd5e1' }
        },
        y: {
          title: { display: true, text: 'Servicios Digitalmente Entregables (%)', color: '#94a3b8', font: { weight: 'bold' } },
          grid: { color: 'rgba(255,255,255,0.05)' },
          ticks: { color: '#cbd5e1' }
        }
      },
      plugins: {
        legend: {
          labels: { color: '#fff' }
        },
        tooltip: {
          callbacks: {
            label: (ctx) => `${ctx.dataset.label}: I+D = ${ctx.raw.x}% | Serv. Digitales = ${ctx.raw.y}%`
          }
        }
      }
    }
  });

});
