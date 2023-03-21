import umachine
import socket
from HTTP import HTTP
from config import ssid, password
from gpiopico import Led, RaspiTemp

pico_temp_sensor = RaspiTemp()

leds = [
    {
        'pin': 0,
        'name': 'Lampara Led',
        'state': 'off',
        'type': 'simple'
    },
    {
        'pin': 1,
        'name': 'Led',
        'state': 'off',
        'type': 'simple'
    },
    {
        'pin': 2,
        'name': 'Relay 1',
        'state': 'off',
        'type': 'simple'
    }
]

def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage(temperature):
    def create_components(name, state, pin)->str:
        return f'''
            <div class="col s12 m6 l4">
              <div class="card-panel hoverable">
                <span class="grey darken-4">
                    <p>{name} is {state}</p>
                </span>
                <div class="row">
                    <div class="col s6 m6 l6 right-align">
                        <form action="./gpio">
                            <input type="hidden" name="pin" value={pin}>
                            <input class="waves-effect waves-light btn" type="submit" name="state" value="on" />
                        </form>
                    </div>
                    <div class="col s6 m6 l6 left-align">
                        <form action="./gpio">
                            <input type="hidden" name="pin" value={pin}>
                            <input class="waves-effect waves-light btn" type="submit" name="state" value="off" />
                        </form>
                    </div>
                </div>
              </div>
            </div>
        '''
    
    def _create_led_component()->str:
        ref_components = ''
        for led in leds:
            ref_components += create_components(led['name'], led['state'], led['pin'])
        return ref_components
    #Template HTML
    html = f'''
            <!DOCTYPE html>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
                <html>
                <body class="container">
                    <div class="row">
                        <h2 class="text-blue-grey darken-4 right-align">Dashboard Control</h2>
                        {_create_led_component()}
                      </div>
                      <div class="row">
                        <div class="col s12 m6 l4">
                            <div class="card-panel">
                                <span class="grey darken-4">
                                    <p>Raspi temperature sensor {temperature}°C</p>
                                </span>
                            </div>
                        </div>
                      </div>
                </body>
                </html>
            '''
    return str(html)

def update_state(pin, state):
    for led in leds:
        if led['pin'] == int(pin):
            led['state'] = state

def handlerState(path:str):
    def _convert_params(params:str)->dict:
        return {x[0] : x[1] for x in [x.split("=") for x in params.split("&") ]}
    try:
        resources = path.split('/')[1]
        if 'favicon.ico' in resources:
            return None
        params = _convert_params(resources.split('?')[1])
        pico_led = Led(int(params['pin']), inverted_logic=True)
        update_state(params['pin'], params['state'])
        if params['state'] == 'off':
            pico_led.off()
            return 'OFF'
        pico_led.on()
        return 'ON'
    except Exception as e:
        return None

def serve(connection):
    #Start a web server
    state = 'OFF'
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        
        try:
            request = request.split()[1]
        except IndexError:
            pass

        state = handlerState(request)
        temperature = pico_temp_sensor.read()
        html = webpage(temperature)
        client.send(html)
        client.close()

if __name__=='__main__':
    client = None
    try:
        http_wlan = HTTP(ssid, password)
        ip = http_wlan.ip
        socket_connection = open_socket(ip)
        serve(socket_connection)
        
    
    except (KeyboardInterrupt) as err:
        print(err)
        client.close()

