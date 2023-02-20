from typing import Literal, Union

from pydantic import BaseModel

class Component(BaseModel):
    name: str
    pin: int
    action: Literal['sensor', 'actuador']
    invert_logic: bool = True
    description: Union[str, None] = None
