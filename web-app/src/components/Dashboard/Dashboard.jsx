import React from 'react'
import { 
  Divider, 
  Chip 
} from '@mui/material'
import Actuators from '../Actuators'
import GraphicsSensors from '../GraphicsSensors'
import RegisterElementForm from '../RegisterElementForm'

const Dashboard = () => {
  return (
    <>
      <Divider textAlign="left" sx={{paddingTop: '10px', paddingBottom: '15px'}}>
        <Chip label="Actuadores" sx={{color: '#00c5b9ff'}} />
      </Divider>
        <Actuators />
      <Divider textAlign="left" sx={{paddingTop: '10px', paddingBottom: '15px'}}>
        <Chip label="Sensores" sx={{color: '#00c5b9ff'}} />
      </Divider>
        <GraphicsSensors />
      <RegisterElementForm />
    </>
  )
}

export default Dashboard