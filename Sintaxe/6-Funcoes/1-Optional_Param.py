
from typing import Optional
from helper.clear import *

clear()

def getName(name: Optional[str] = None, default_name: str = "Soares") -> str:
    if name is not None:
        return name
    return default_name

data = getName('leandro')
print(data)  # Resultado: leandro

