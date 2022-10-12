import React, { useState } from "react"
import { Button } from "@mui/material"
import Fab from '@mui/material/Fab'
import AddIcon from '@mui/icons-material/Add'
import TextField from '@mui/material/TextField'
import Dialog from '@mui/material/Dialog'
import DialogActions from '@mui/material/DialogActions'
import DialogContent from '@mui/material/DialogContent'
import DialogContentText from '@mui/material/DialogContentText'
import DialogTitle from '@mui/material/DialogTitle'
import '../../App.css'

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
        <DialogTitle>Registrar un nuevo elemento</DialogTitle>
        <DialogContent>
          <DialogContentText>
            Para poder visualizar o controlar los disposivos locales es necesario registrarlos
            según el tipo de hardware y su dirección IP local.
          </DialogContentText>
          <TextField
            autoFocus
            margin="dense"
            id="name"
            label="Dirección Local del Dispositivo IoT"
            fullWidth
            variant="standard"
          />
          <TextField
            autoFocus
            margin="dense"
            id="name"
            label="Nombre del dispositivo"
            fullWidth
            variant="standard"
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={handleClose}>Subscribe</Button>
        </DialogActions>
      </Dialog>
      </div>
    </>
  )
}

export default RegisterElementForm