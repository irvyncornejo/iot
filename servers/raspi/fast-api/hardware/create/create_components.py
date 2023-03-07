from custom_types import MappingType
from .actuators import Actuators

class CreateComponents:
    def __init__(self) -> None:
        self.components: MappingType = {}
        self._requests: MappingType = {}
    
    def exists_component(self, pin: int) -> bool:
        return bool(
            str(pin) in list(self.components.keys())
        )

    def execute(self, component) -> MappingType:
        self._requests = component
        if not self.exists_component(self._requests["pin"]):
            self.components[f'{self._requests["pin"]}'] = Actuators(self._requests["pin"])
            return {'message': 'Component exists', 'error': True}
        return {'message': 'Component exists', 'error': False}