from gpiozero import LED

class Actuators:
    def __init__(self, pin:int, invert_logic:bool=True) -> None:
        self._relay = LED(pin)
        self._invert_logic = invert_logic
        self._state = True if self._invert_logic else False
        self._relay.value = self._state

    @staticmethod
    def _validate_pwm():
        pass
    
    def change_state(self):
        self._relay.value = not self._state
        self._state = not self._state