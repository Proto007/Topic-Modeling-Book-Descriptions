import React, { useEffect, useRef, useState } from "react";
import Chartjs from "chart.js/auto";

const randomInt = () => Math.floor(Math.random() * (10 - 1 + 1)) + 1;
const sample=[
    [
        [
            "philosophy",
            "commentary",
            "greek",
            "japanese",
            "various",
            "effort",
            "band",
            "glossary",
            "criticism",
            "target",
            "prevent",
            "philosopher",
            "generally",
            "socrates",
            "fashion"
        ],
        0.0013888888888921164
    ],
    [
        [
            "printing",
            "life",
            "reprint",
            "school",
            "new",
            "year",
            "author",
            "world",
            "relationship",
            "friend",
            "age",
            "series",
            "middle",
            "struggle",
            "earth"
        ],
        0.047307417097817626
    ],
    [
        [
            "king",
            "art",
            "film",
            "love",
            "artist",
            "star",
            "series",
            "church",
            "work",
            "soul",
            "summer",
            "movie",
            "natural",
            "world",
            "great"
        ],
        0.12377945175139668
    ]
]
const chartConfig = {
    type: "bar",
    data: {
      labels: ["Topic 1", "Topic 2","Topic 3","Topic 4","Topic 5","Topic 6","Topic 7","Topic 8","Topic 9","Topic 10","Topic 11","Topic 12","Topic 13","Topic 14","Topic 15"],
      datasets: [
        {
          label: "frequency",
          data: [sample[0][1] ,sample[1][1],sample[2][1]],
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(255, 206, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(255, 159, 64, 0.2)"
          ],
          borderColor: [
            "rgba(255, 99, 132, 1)",
            "rgba(54, 162, 235, 1)",
            "rgba(255, 206, 86, 1)",
            "rgba(75, 192, 192, 1)",
            "rgba(153, 102, 255, 1)",
            "rgba(255, 159, 64, 1)"
          ],
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true
            }
          }
        ]
      }
    }
  };
  


// Component to display results of model
const Results = (props) => {
    const chartContainer = useRef(null);
  const [chartInstance, setChartInstance] = useState(null);

  useEffect(() => {
    if (chartContainer && chartContainer.current) {
      const newChartInstance = new Chartjs(chartContainer.current, chartConfig);
      setChartInstance(newChartInstance);
    }
  }, [chartContainer]);

  const updateDataset = (datasetIndex, newData) => {
    chartInstance.data.datasets[datasetIndex].data = newData;
    chartInstance.update();
  };

  return (
    <div>
      <canvas ref={chartContainer} />
    </div>
  );
}


export default Results;