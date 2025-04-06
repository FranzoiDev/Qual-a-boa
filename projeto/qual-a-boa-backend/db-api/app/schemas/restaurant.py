from pydantic import BaseModel, Field, field_validator
import re

class RestaurantCreate(BaseModel):
    cnpj: str = Field(..., description="CNPJ of the restaurant (xx.xxx.xxx/xxxx-xx)")
    name: str = Field(..., min_length=1, max_length=100, description="Name of the restaurant")
    state: str = Field(..., min_length=2, max_length=2, description="State abbreviation (UF)")
    city: str = Field(..., min_length=1, max_length=100, description="City name")
    type: str = Field(..., min_length=1, max_length=50, description="Restaurant type/cuisine")
    operating_hours: str = Field(None, max_length=200, description="Operating hours")
    postal_code: str = Field(..., min_length=8, max_length=9, description="Postal code (CEP)")
    street_number: str = Field(..., min_length=1, max_length=10, description="Street number")
    
    @field_validator('cnpj')
    def validate_cnpj(cls, v):
        pattern = r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'
        if not re.match(pattern, v):
            raise ValueError('CNPJ must be in format: xx.xxx.xxx/xxxx-xx')
        return v
    
    @field_validator('state')
    def validate_state(cls, v):
        states = [
            'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 
            'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
        ]
        if v.upper() not in states:
            raise ValueError('Invalid state abbreviation')
        return v.upper()
    
    @field_validator('postal_code')
    def validate_postal_code(cls, v):
        v = re.sub(r'[^0-9]', '', v)
        if len(v) != 8:
            raise ValueError('Postal code must have 8 digits')
        return '{}-{}'.format(v[:5], v[5:]) if '-' not in v else v

class RestaurantUpdate(RestaurantCreate):
    pass

class RestaurantResponse(BaseModel):
    id: int
    cnpj: str
    name: str
    state: str
    city: str
    type: str
    operating_hours: str = None
    postal_code: str
    street_number: str 