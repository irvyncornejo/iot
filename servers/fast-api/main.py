#scp -r fast-api pi@192.168.1.79:/home/pi/Documentos
#uvicorn main:app --host 0.0.0.0
from typing import Any
from fastapi import FastAPI

from hardware.components_type import Component
from hardware.create import CreateComponents

app = FastAPI()

components: Any = CreateComponents()


@app.get('/')
def read_root():
    return {'message': 'Server started', 'error': False}

@app.post('/components/')
async def create_components(component: Component):
    return components.execute(component.__dict__)

@app.put('/logic-control/{pin}')
async def logic_control(pin):
    if components.exists_component(pin):
        components.components[f'{pin}'].change_state()
        return {'message': 'Component updated', 'error': False}
    return {'message': 'Component not exists', 'error': True}