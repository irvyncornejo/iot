"""
import sys
sys.implementation
"""

class Component:
    def __init__(
        self,
        name:str,
        pin:str,
        type_component:str,
        reverse_logic=False
    )->None:
        self.name = name
        self.pin = pin
        self.type_component = type_component
        self.reverse_logic = reverse_logic
        self.html_component = self._html_component()

    def _html_component(self):
        _card_components_html = {
            '1': lambda : f'''
                <div class="col s12 m6 l4">
                  <div class="card-panel hoverable card-size">
                    <span class="grey darken-4">
                        <p>{self.name} es <span><strong>%state%</strong></span></p>
                    </span>
                    <p></p>
                    <div class="row">
                        <div class="col s6 m6 l6 right-align">
                            <form action="./gpio">
                                <input type="hidden" name="pin" value={self.pin}>
                                <input type="hidden" name="type" value="simple">
                                <input class="waves-effect waves-light btn" type="submit" name="state" value="ON" />
                            </form>
                        </div>
                        <div class="col s6 m6 l6 left-align">
                            <form action="./gpio">
                                <input type="hidden" name="pin" value={self.pin}>
                                <input type="hidden" name="type" value="simple">
                                <input class="waves-effect waves-light btn" type="submit" name="state" value="OFF" />
                            </form>
                        </div>
                    </div>
                  </div>
                </div>
            ''',
            '2': lambda : f'''
                <div class="col s12 m6 l4">
                    <div class="card-panel hoverable card-size">
                      <span class="grey darken-4">
                            <p>{self.name} es <span><strong>%state%</strong></span>%</p>
                        </span>
                        <div class="row">
                            <form action="./gpio">
                                <div class="col s6 m6 l6">
                                    <p class="range-field">
                                        <input type="hidden" name="pin" value={self.pin}>
                                        <input type="range" min="0" max="100" name="state" value="0" />
                                    </p>
                                </div>    
                                <div class="col s6 m6 l6">
                                    <input class="waves-effect waves-light btn" type="submit" name="type" value="PWM" />
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            ''',
            '3': lambda : f'''
                <div class="col s12 m6 l4">
                    <div class="card-panel hoverable card-size">
                      <span class="grey darken-4">
                            <p>{self.name} es <span><strong>%state%</strong></span></p>
                        </span>
                        <label>Selecciona un color</label>
                        <div class="row">
                                <form action="./gpio">
                                    <div class="col s6 m6 l6">
                                        <input type="hidden" name="pin" value={self.pin}>
                                        <input type="color" id="color" name="state" value="#f73bf1">
                                    </div>    
                                    <div class="col s6 m6 l6">
                                        <input class="waves-effect waves-light btn" type="submit" name="type" value="RGB" />
                                    </div>
                                </form>
                        </div>
                    </div>
                </div>
            '''
        }
        return _card_components_html[self.type_component]()

class DashboardComponents:
    def __init__(self)->None:
        self._components = []

    @property
    def components(self):
        return self._components
    
    def _handler_hardware(self):
        #TODO
        pass
    
    def process_requests(self, path:str):
        
        def _convert_params(params:str)->dict:
            return {x[0] : x[1] for x in [x.split("=") for x in params.split("&") ]}
        
        try:
            resources = path.split('/')[1]
            if 'favicon.ico' in resources:
                return None
            params = _convert_params(resources.split('?')[1])
            self.handler_state(int(params['pin']), params['state'])

        except Exception as e:
            print(f'Error en el procesamiento, {e}')
            return None
        
    def handler_state(self, pin:int, state:str):
        for idx, component in enumerate(self._components):
            if component['pin'] == pin:
                print(f'Actualizando componente... {pin}')
                _component = self._components[idx]
                _component['name']
                result = {
                 'name': _component['name'],
                 'state': state,
                 'pin': pin,
                 'type_component': _component['type_component'],
                 'reverse_logic': _component['reverse_logic'],
                 'html_component': _component['html_component'],
                 'html_component_show': _component['html_component'].replace('%state%', state)
                }
                self._components[idx] = result

    def show(self, temperature:float)->str:
        def _process_components()->str:
            _components = ''
            for elem in self._components:
                _component_html = (
                    elem['html_component_show'] if 'html_component_show' in list(elem.keys()) else elem['html_component']
                )
                _components += _component_html   
            return _components

        html = f'''
            <!DOCTYPE html>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <html>
                    <body class="container">
                        <h2 class="text-blue-grey darken-4 right-align">Dashboard Control</h2>
                        <p class="text-blue-grey darken-4 right-align">Raspberry Temp {temperature} °C</p>
                        <div class="row">
                            {_process_components()}
                        </div>
                    </body>
                </html>
            '''
        return str(html)
    
    def _create_component_hardware(self):
        #TODO
        pass

    def create(self)->None:
        _name = input('Ingresa el nombre(Lámpara, Relevador...)-> ').strip()
        _pin = int(input('Ingresa el pin(0, 1, 2...)-> ').strip())
        _type = input('Ingresa el tipo((1)Simple, (2)PWM o (3)RGB Color)-> ').strip()
        _reverse_logic = input('¿Lógica Inversa(Y/N)?-> ') if _type in ['1', '2'] else 'N'
        #_state = input('Ingresa el estado(off, on, 50)-> ').strip()

        component = Component(
            name=_name,
            pin=_pin,
            type_component=_type,
            reverse_logic= True if _reverse_logic == 'Y' else False
        ).__dict__
        self._components.append(component)


    def run(self)->None:
        self.create()
        _new = input('¿Quieres crear otro componente?(Y/N)-> ').upper().strip()
        while _new == 'Y':
            self.create()
            _new = input('¿Quieres crear otro componente?(Y/N)-> ').upper().strip()


