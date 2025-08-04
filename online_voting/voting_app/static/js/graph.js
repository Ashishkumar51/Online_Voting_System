function replaceDivWithExternalcontent(event) {
    event.preventDefault();
    
    var xhr = new XMLHttpRequest();
    xhr.open('GET', event.target.textContent.trim() == 'Overview'?'demo2.html':'demo.html', true);
    xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 400) {
            console.log(xhr.responseText);
            
            document.getElementById('overview').innerHTML = xhr.responseText;
        } else {
            alert('Error: Failed to load external content');
        }
    };
    xhr.onerror = function () {
        console.error('Request failed');
    };
    xhr.send();
}
    // Line Chart (Votes by Day)
    var ctxLine = document.getElementById('votesByDay').getContext('2d');
    var votesByDay = new Chart(ctxLine, {
        type: 'line',
        data: {
            labels: ['11/27', '11/28', '11/29', '11/30', '12/01'],
            datasets: [{
                label: 'Votes by Day',
                data: [25, 15, 10, 5, 3],
                backgroundColor: 'rgba(58, 123, 213, 0.2)',
                borderColor: 'rgba(58, 123, 213, 1)',
                borderWidth: 3,
                fill: true,
                tension: 0.4,
                pointBackgroundColor: '#fff',
                pointBorderColor: '#3a7bd5',
                pointRadius: 5,
                pointHoverRadius: 8,
                pointHoverBackgroundColor: '#ff6f61',
                pointHoverBorderColor: '#ff6f61',
                pointHitRadius: 12,
                pointStyle: 'rectRounded'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: {
                duration: 1500, // Slow animation duration (in milliseconds)
                easing: 'easeInOutQuad', // Smooth easing function for a better effect
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Votes by Day Over Time',
                    font: {
                        size: 20,
                        weight: 'bold',
                        family: 'Arial, sans-serif'
                    },
                    color: '#3a3a3a',
                    padding: {
                        top: 20,
                        bottom: 20
                    }
                },
                legend: {
                    display: true,
                    position: 'top',
                    labels: {
                        color: '#3a7bd5',
                        font: {
                            size: 14,
                            family: 'Arial, sans-serif'
                        }
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(0, 0, 0, 0.7)',
                    titleFont: {
                        size: 16,
                        weight: 'bold'
                    },
                    bodyFont: {
                        size: 14
                    },
                    borderColor: '#3a7bd5',
                    borderWidth: 1
                }
            },
            scales: {
                x: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        color: '#3a7bd5',
                        font: {
                            size: 12
                        }
                    }
                },
                y: {
                    grid: {
                        color: '#e0e0e0'
                    },
                    ticks: {
                        color: '#3a7bd5',
                        font: {
                            size: 12
                        }
                    }
                }
            }
        }
    });
    
    // Pie Chart (Votes Distribution)
    var ctxPie = document.getElementById('votesDistribution').getContext('2d');
    var votesDistribution = new Chart(ctxPie, {
        type: 'pie',
        data: {
            labels: ['Candidate A', 'Candidate B', 'Candidate C', 'Candidate D'],
            datasets: [{
                label: 'Votes Distribution',
                data: [400, 250, 150, 60],
                backgroundColor: ['#4CAF50', '#fc6c25', '#FFC107', '#ee1c75'],
                hoverBackgroundColor: ['#388E3C', '#D32F2F', '#FFA000', '#ee1c75'],
                borderWidth: 3,
                hoverOffset: 10
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: {
                duration: 3000, // Slow animation duration for pie chart
                easing: 'easeInOutQuad', // Smooth easing function for pie chart
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Votes Distribution Among Candidates',
                    font: {
                        size: 22,
                        weight: 'bold',
                        family: 'Arial, sans-serif'
                    },
                    color: '#3a3a3a',
                    padding: {
                        top: 20,
                        bottom: 20
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(0, 0, 0, 0.7)',
                    titleFont: {
                        size: 16,
                        weight: 'bold'
                    },
                    bodyFont: {
                        size: 14
                    },
                    borderColor: '#fff',
                    borderWidth: 1
                },
                legend: {
                    display: true,
                    position: 'top',
                    labels: {
                        color: '#3a3a3a',
                        font: {
                            size: 14,
                            family: 'Arial, sans-serif'
                        }
                    }
                }
            }
        }
    });
    document.getElementById("")