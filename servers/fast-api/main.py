#scp -r fast-api pi@192.168.1.79:/home/pi/Documentos
from typing import Any

import uvicorn
from fastapi import FastAPI
import paho.mqtt.client as mqtt
from gpiozero import Button

from hardware.components_type import Component
from hardware.create import CreateComponents
from setting import logger

app = FastAPI()

client = mqtt.Client()
client.connect("mqtt.eclipseprojects.io", 1883, 60)

components: Any = CreateComponents()

def say_hello():
    print(button.pin)
    logger.info('Presionado..')
    client.publish("sensor/uno", 'presionado')

button = Button(14)


@app.get('/')
def read_root():
    return {'message': 'Server started', 'error': False}

@app.post('/actuators/')
async def create_components(component: Component):
    return components.execute(component.__dict__)

@app.put('/actuators/{pin}')
async def logic_control(pin):
    if components.exists_component(pin):
        components.components[f'{pin}'].change_state()
        return {'message': 'Component updated', 'error': False}
    return {'message': 'Component not exists', 'error': True}


if __name__ == '__main__':
    button.when_pressed = say_hello
    uvicorn.run(app, host="0.0.0.0", port=8000)