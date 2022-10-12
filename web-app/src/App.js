import './App.css'
import { Grid } from '@mui/material'
import Dashboard from './components/Dashboard'

const App = () => {
  return (
    <div className="App">
      <Grid container spacing={2}>
        <Grid xs={4} md={4} lg={4}>
        </Grid>
        <Grid xs={8} md={8} lg={8}>
          <Dashboard />
        </Grid>
      </Grid>
    </div>
  )
}

export default App
