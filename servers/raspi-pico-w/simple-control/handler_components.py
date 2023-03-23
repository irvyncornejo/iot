from dataclasses import dataclass

@dataclass
class Component:
    def __init__(
        self,
        name:str,
        state:str,
        pin:str,
        type:str,
        control:str
    )->None:
        self.name = name
        self.state = state
        self.pin = pin
        self.type = type
        self.control = control

class HandlerComponents:
    def __init__(self)->None:
        self._components = []

    def create(self, name, state, pin, type, control):
        component = Component(
            name=name,
            state=state,
            pin=pin,
            type=type,
            control=control
        ).__dict__
        self._components.append(component)
        return True

    def _get_attributes(self):
        _name = input('Ingresa el nombre: ')
        _pin = input('Ingresa el pin: ')
        _type = input('Ingresa el tipo: ')
        _control = input('Ingresa el control: ') 
        _state = input('Ingresa el estado: ')

    def run(self, name):
        return self._components[name]
