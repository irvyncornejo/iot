import React, { useState } from "react"
import { Button, FormControl, InputLabel, Select, MenuItem } from "@mui/material"
import Fab from '@mui/material/Fab'
import AddIcon from '@mui/icons-material/Add'
import TextField from '@mui/material/TextField'
import Dialog from '@mui/material/Dialog'
import DialogActions from '@mui/material/DialogActions'
import DialogContent from '@mui/material/DialogContent'
import DialogContentText from '@mui/material/DialogContentText'
import DialogTitle from '@mui/material/DialogTitle'
import '../../App.css'


const typeSensors = ['Digital', 'Análogico']
const typeActuators = ['Boleano', 'PWM']

const RegisterElementForm = () => {
  const [open, setOpen] = useState(false)

  const handleClickOpen = () => {
    setOpen(true)
  }

  const handleClose = () => {
    setOpen(false)
  }
  return (
    <>
      <div className='button-add-element'>
        <Fab aria-label="add" sx={{ color:'#00c5b9ff' }} onClick={handleClickOpen}>
          <AddIcon />
        </Fab>
        <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Registrar un nuevo dispositivo.</DialogTitle>
        <DialogContent>
          <DialogContentText style={{paddingBottom:'20px'}}>
            Para poder visualizar o controlar los disposivos locales es necesario registrarlos
            según el tipo de hardware y su dirección IP local.
          </DialogContentText>
          <FormControl variant="standard" fullWidth>
            <InputLabel id="demo-simple-select-standard-label">Tipo de componente</InputLabel>
            <Select
              labelId="demo-simple-select-standard-label"
              id="demo-simple-select-standard"
              label="Componente"
            >
              <MenuItem value={'sensor'}>Sensor</MenuItem>
              <MenuItem value={'actuador'}>Actuador</MenuItem>
            </Select>
          </FormControl>
          <FormControl variant="standard" fullWidth>
            <InputLabel id="demo-simple-select-standard-label">Tipo de elemento</InputLabel>
            <Select
              labelId="demo-simple-select-standard-label"
              id="demo-simple-select-standard"
              label="elemento"
            >
              <MenuItem value={'sensor'}>Sensor</MenuItem>
              <MenuItem value={'actuador'}>Actuador</MenuItem>
            </Select>
          </FormControl>
          <TextField
            autoFocus
            margin="dense"
            id="name"
            label="Dirección Local del Dispositivo IoT"
            fullWidth
            variant="standard"
          />
          <TextField
            margin="dense"
            id="name"
            label="Nombre del dispositivo"
            fullWidth
            variant="standard"
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancelar</Button>
          <Button onClick={handleClose}>Añadir</Button>
        </DialogActions>
      </Dialog>
      </div>
    </>
  )
}

export default RegisterElementForm