import React, { useState } from 'react'
import { 
  FormControlLabel, 
  Switch, 
  Card, 
  CardContent, 
  Grid, 
  CardHeader  
} from '@mui/material'

import LocalServices from '../HTTPServices/LocalServices'

const TwoStateButtons = (props) => {
		const theme = {
			padding: '20px 5px 20px 5px'
		}
    const [loading, setLoading] = useState(true)
		
		const queryParams = loading 
			? `?id=${props.id}&status=on`
			: `?id=${props.id}&status=off`
		
		const handleState = () => {
      const path = `${props.localIp}/${props.type}`
			LocalServices.changeState(path, queryParams)
			setLoading(!loading)
		}
  
    return (
      <>
				<Grid xs={4} md={4} lg={2} sx={{ ...theme }}>
					<Card sx={{ maxHeight: '220px', background: '#2c3546', color: '#00c5b9ff' }}>
            <CardHeader 
              sx={{ color: '#00c5b9ff' }}
							subheader={ props.name || '' }
              disableTypography
						/>
						<CardContent>
							<FormControlLabel
								value="top"
								control={
									<Switch
										onChange={ () => handleState() }
										name="loading"
										color="primary" 
							    />
								}
							/>
							<p>
								{`Pin ${props.id}`}				
							</p>
              <p>
								{`IP ${props.localIp}`}				
							</p>
						</CardContent>
					</Card>
				</Grid>
      </>
    )
  }

export default TwoStateButtons