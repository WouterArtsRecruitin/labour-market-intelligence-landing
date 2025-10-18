// Charts.js - Executive Market Intelligence Data Visualization
// Recruitin Brand Colors
const recruitinColors = {
    primary: '#4B4F51',
    accent: '#EF7D00',
    success: '#10B981',
    background: '#F8FAFC',
    text: '#1F2937'
};

// Chart.js Global Configuration
Chart.defaults.font.family = 'Inter, system-ui, sans-serif';
Chart.defaults.font.size = 11;
Chart.defaults.color = recruitinColors.text;

// Initialize all charts when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeSalaryChart();
    initializeGrowthChart();
    initializeSkillsChart();
    initializeCompetitionChart();
});

// 1. SALARY BENCHMARK BAR CHART
function initializeSalaryChart() {
    const ctx = document.getElementById('salaryChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Junior\n(0-3j)', 'Medior\n(3-7j)', 'Senior\n(7+j)', 'Lead\n(10+j)'],
            datasets: [{
                label: 'Markt Minimum',
                data: [35000, 48000, 58000, 70000],
                backgroundColor: 'rgba(75, 79, 81, 0.6)',
                borderColor: recruitinColors.primary,
                borderWidth: 1
            }, {
                label: 'Markt Maximum',
                data: [48000, 65000, 75000, 95000],
                backgroundColor: 'rgba(239, 125, 0, 0.6)',
                borderColor: recruitinColors.accent,
                borderWidth: 1
            }, {
                label: 'Jouw Target',
                data: [null, null, 62000, null],
                backgroundColor: recruitinColors.success,
                borderColor: recruitinColors.success,
                borderWidth: 2,
                type: 'line',
                pointBackgroundColor: recruitinColors.success,
                pointBorderColor: '#FFFFFF',
                pointBorderWidth: 2,
                pointRadius: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        usePointStyle: true,
                        padding: 15,
                        font: {
                            size: 10
                        }
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.dataset.label + ': €' + context.parsed.y.toLocaleString();
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: false,
                    min: 30000,
                    max: 100000,
                    ticks: {
                        callback: function(value) {
                            return '€' + (value/1000) + 'k';
                        },
                        font: {
                            size: 10
                        }
                    },
                    grid: {
                        color: 'rgba(0,0,0,0.05)'
                    }
                },
                x: {
                    ticks: {
                        font: {
                            size: 9
                        }
                    },
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
}

// 2. MARKET GROWTH LINE CHART
function initializeGrowthChart() {
    const ctx = document.getElementById('growthChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec'],
            datasets: [{
                label: '2024 Vacatures',
                data: [720, 680, 790, 850, 920, 880, 760, 690, 840, 950, 1050, 1150],
                borderColor: recruitinColors.primary,
                backgroundColor: 'rgba(75, 79, 81, 0.1)',
                borderWidth: 2,
                fill: true,
                tension: 0.4
            }, {
                label: '2025 Forecast',
                data: [null, null, null, null, null, null, null, null, null, 1247, 1380, 1520],
                borderColor: recruitinColors.accent,
                backgroundColor: 'rgba(239, 125, 0, 0.1)',
                borderWidth: 2,
                borderDash: [5, 5],
                fill: false,
                tension: 0.4,
                pointBackgroundColor: recruitinColors.accent
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        usePointStyle: true,
                        padding: 15,
                        font: {
                            size: 10
                        }
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.dataset.label + ': ' + context.parsed.y + ' vacatures';
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: false,
                    min: 600,
                    max: 1600,
                    ticks: {
                        font: {
                            size: 10
                        }
                    },
                    grid: {
                        color: 'rgba(0,0,0,0.05)'
                    }
                },
                x: {
                    ticks: {
                        font: {
                            size: 9
                        }
                    },
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
}

// 3. SKILLS DEMAND RADAR CHART
function initializeSkillsChart() {
    const ctx = document.getElementById('skillsChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'radar',
        data: {
            labels: ['Digital Marketing', 'SEO/SEM', 'Analytics', 'Leadership', 'Strategy', 'Content', 'Social Media', 'Automation'],
            datasets: [{
                label: 'Markt Vraag',
                data: [95, 88, 92, 76, 85, 82, 90, 78],
                backgroundColor: 'rgba(239, 125, 0, 0.2)',
                borderColor: recruitinColors.accent,
                borderWidth: 2,
                pointBackgroundColor: recruitinColors.accent,
                pointBorderColor: '#FFFFFF',
                pointBorderWidth: 2
            }, {
                label: 'Jouw Profiel Match',
                data: [92, 85, 88, 82, 90, 78, 85, 75],
                backgroundColor: 'rgba(75, 79, 81, 0.2)',
                borderColor: recruitinColors.primary,
                borderWidth: 2,
                pointBackgroundColor: recruitinColors.primary,
                pointBorderColor: '#FFFFFF',
                pointBorderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        usePointStyle: true,
                        padding: 15,
                        font: {
                            size: 10
                        }
                    }
                }
            },
            scales: {
                r: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        display: false
                    },
                    grid: {
                        color: 'rgba(0,0,0,0.1)'
                    },
                    angleLines: {
                        color: 'rgba(0,0,0,0.1)'
                    },
                    pointLabels: {
                        font: {
                            size: 9
                        },
                        color: recruitinColors.text
                    }
                }
            }
        }
    });
}

// 4. COMPETITION ANALYSIS PIE CHART
function initializeCompetitionChart() {
    const ctx = document.getElementById('competitionChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Qualified', 'Semi-qualified', 'Niet geschikt'],
            datasets: [{
                data: [29, 33, 38],
                backgroundColor: [
                    recruitinColors.accent,
                    recruitinColors.primary,
                    recruitinColors.success
                ],
                borderWidth: 2,
                borderColor: '#FFFFFF'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '50%',
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.label + ': ' + context.parsed + '%';
                        }
                    }
                }
            }
        }
    });
}

// Animation delays for progressive loading
setTimeout(() => {
    document.querySelectorAll('.metric-bar .bar-fill').forEach((bar, index) => {
        bar.style.transitionDelay = (index * 0.2) + 's';
    });
}, 500);

setTimeout(() => {
    document.querySelectorAll('.geo-fill').forEach((bar, index) => {
        bar.style.transitionDelay = (index * 0.15) + 's';
    });
}, 800);