import React from "react"
import TwoStateButtons from './TwoStateButton'
import SliderButton from "./SliderButton"
import { Box, Grid } from '@mui/material'

const actuators = [
  {
    name:'Luz Oficina', 
    id:'2', 
    type:'generic-digital',
    typeValue: 'boolean',
    localIp: '192.168.1.141'
  },
  {
    name:'Cafetera', 
    id:'4', 
    type:'generic-digital',
    typeValue: 'boolean',
    localIp: '192.168.1.141'
  },
  {
    name:'Luz Verde', 
    id:'16', 
    type:'generic-digital',
    typeValue: 'slider',
    localIp: '192.168.1.141'
  },
  {
    name:'Lámpara', 
    id:'0', 
    type:'generic-digital',
    typeValue: 'slider',
    localIp: '192.168.1.141'
  }
]

const Actuators = () => {
    return (
      <>
        <Box container sx={{ flexGrow: 1 }}>
          <Grid container spacing={2} >
            { actuators.map(
                actuator => {
                  return actuator.typeValue === 'boolean' 
                    ? <TwoStateButtons { ...actuator } /> 
                    : <SliderButton { ...actuator } />
                }
              ) 
            }
          </Grid>
        </Box>
      </>
    )
}

export default Actuators