import React from 'react'
import Slider from '@mui/material/Slider'
import { 
	Card, 
	CardContent, 
	Grid, 
	Box, 
	CardHeader 
} from '@mui/material'
import LocalServices from '../HTTPServices/LocalServices'

const SliderButton = (props) => {
	const marks = [
		{
			value: 0,
			label: '0%'
		},
		{
			value: 100,
			label: '100%',
		},
	]

	const theme = {
		padding: '20px 5px 20px 5px'
	}

	const valuetext = (value) => {
		return `${value}%`;
	}

	const handleStateSlider = (value) => {
		const path = `${props.localIp}/${props.type}`
		const value_slider = parseInt(parseInt(value.target.value)*2.55)
		LocalServices.changeState(path, `?id=${props.id}&value=${value_slider}`)
	}
	
  return (
		<>
			<Grid xs={4} md={4} lg={4} sx={{ ...theme }} key={props.name}>
				<Box>
					<Card sx={{maxHeight: '220px', background: '#2c3546', color: '#00c5b9ff' }}>
						<CardHeader
							sx={{ color: '#00c5b9ff' }}
							disableTypography
							subheader={ props.name || '' }
						/>
						<CardContent>
							<Slider
								name='slider'
								aria-label="Always visible"
								defaultValue={props.defaultValue || 0}
								getAriaValueText={valuetext}
								step={10}
								marks={marks}
								valueLabelDisplay="on"
								onChange={handleStateSlider}
								sx={{color: '#00c5b9ff'}}
							/>
							<p>
								{`Pin ${props.id || ''}`}				
							</p>
              <p>
								{`IP ${props.localIp || ''}`}				
							</p>
						</CardContent>
					</Card>
				</Box>
			</Grid>
		</>
  )
}

export default SliderButton