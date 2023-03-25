from dataclasses import dataclass

@dataclass
class Component:
    def __init__(
        self,
        name:str,
        state:str,
        pin:str,
        type_component:str,
        reverse_logic=False
    )->None:
        self.name = name
        self.state = state
        self.pin = pin
        self.type_component = type_component
        self.reverse_logic = reverse_logic
        self.html_component = self._html_component()

    def _html_component(self):
        return f'<p>{self.name} %state%</p>'

class HandlerComponents:
    def __init__(self)->None:
        self._components = []

    def _handler_hardware(self):
        pass

    def handler_state(self, pin:int, state:str)->None:
        for idx, component in enumerate(self._components):
            if component['pin'] == pin:
                component['state'] = state
                self._components[idx] = component
        print(self._components)

    def show(self)->str:
        pass
    
    def _create_component_hardware(self):
        pass

    def _create(self)->None:
        _name = input('Ingresa el nombre(Lámpara, Relevador...)-> ').strip()
        _pin = int(input('Ingresa el pin(1, 2, 3...)-> ').strip())
        _type = input('Ingresa el tipo((1)simple, (2)pwm o (3)neopixel)-> ').strip()
        _reverse_logic = input('¿Lógica Inversa(Y/N)?-> ') if _type in ['1', '2'] else 'N'
        _state = input('Ingresa el estado(off, on, 50)-> ').strip()

        component = Component(
            name=_name,
            state=_state,
            pin=_pin,
            type_component=_type,
            reverse_logic= True if _reverse_logic == 'Y' else False
        ).__dict__
        self._components.append(component)


    def run(self)->None:
        try:
            self._create()
            _new = input('¿Quieres crear otro componente?(Y/N)-> ').upper().strip()

            while _new == 'Y':
                self._create()
                _new = input('¿Quieres crear otro componente?(Y/N)-> ').upper().strip()
            
            print(self._components)
        except Exception as err:
            print(f'Error {err}')

components = HandlerComponents()
components.run()
components.handler_state(1, 'on')
