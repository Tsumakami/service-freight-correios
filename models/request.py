from pydantic import BaseModel

class Request(BaseModel):
    origin_postal_code: str
    destination_postal_code: str
    package_weight: int = 1
    width: int = 30
    height: int = 30
    lenght: int = 30
    declared_value: float = 300.0
