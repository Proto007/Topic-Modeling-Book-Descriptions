import React, { useEffect, useRef, useState } from "react";
import Chartjs from "chart.js/auto";

// Component to display results of model
const Results = (props) => {
  const chartContainer = useRef(null);
  // eslint-disable-next-line no-unused-vars
  const [chartInstance, setChartInstance] = useState(null);

  useEffect(() => {
    const chartConfig = {
      type: "bar",
      data: {
        labels: ["Topic 1", "Topic 2","Topic 3","Topic 4","Topic 5","Topic 6","Topic 7","Topic 8","Topic 9","Topic 10","Topic 11","Topic 12","Topic 13","Topic 14","Topic 15"],
        datasets: [
          {
            label: "frequency",
            data: props.correlations,
            backgroundColor: [
              "rgba(0, 0, 0, 1)",
            ],
            borderColor: [
              "rgba(255, 255, 255, 1)",
            ],
            borderWidth: 4
          }
        ]
      },
      options: {
        plugins: {
          legend: {
            display: false
          },
        },
        scales: {
          xAxis: {
            ticks: {
              color: "white",
              font: {
                family: "monospace",
                weight: "bold"
              }
            }
          },
          yAxis: {
            ticks: {
              color: "white",
              font: {
                family: "monospace",
                weight: "bold"
              }
            },
            min: 0,
            max: 1
          }
        }
      }
    };
    if (chartContainer && chartContainer.current) {
      const newChartInstance = new Chartjs(chartContainer.current, chartConfig);
      setChartInstance(newChartInstance);
    }
  }, [chartContainer, props.correlations]);

  return (
    <div style={{marginTop:"30px"}}>
      <canvas ref={chartContainer} />
    </div>
  );
}

export default Results;
