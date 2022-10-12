import React from "react"
import { Chart } from "react-google-charts"
import { Grid } from "@mui/material"

const GraphicsSensors = (props) => {
  const options = {
    chart: {
      title: props.title,
      subtitle: props.description
    },
    curveType: "function",
    width: '100%',
    height: '100%',
    chartArea: { backgroundColor: '#2c3546' },
    backgroundColor: '#2c3546',
    series: {
      0: { axis: props.axis, color: '#f05768' }
    },
    axes: {
      y: {
        Temps: { label: props.label, fontColor: '#f05768' }
      },
      x: {
        Hora: { label: props.label, fontColor: '#f05768' }
      },
    },
  }
  return (
    <>
      <div>
        <Grid 
          xs={12} md={12} lg={6} 
          onClick={() => console.log('Click en el gráfica') } 
          sx={{ background: '#1a212e' }}
        >
          <Chart
            chartType="LineChart"
            data={[["Hora", "Temp °C"], ['12:35', 30], ['12:36', 29.9], ['12:37', 30], ['12:38', 29.9]]}
            options={options}
            legendToggle
          />
        </Grid>
      </div>
    </>
  )
}

export default GraphicsSensors