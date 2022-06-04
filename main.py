from email.policy import HTTP
from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from CorreiosPrecoPrazo.core import Correios

from services.authentication import Authentication
from models.cod_service import CodServices
from models.format import Format
from models.request import Request

app = FastAPI()

security = HTTPBasic()

@app.post('/quote')
async def quote(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    Authentication.authenticate(credentials= credentials)
    
    method = 'CalcPrecoPrazo'
    
    request = {
        'cd_servico': CodServices.SEDEX_A_VISTA.value,
        'cep_origem': request.origin_postal_code,
        'cep_destino': request.destination_postal_code,
        'vl_peso': request.package_weight,
        'cd_formato': Format.BOX.value,
        'vl_largura': request.width,
        'vl_altura': request.height,
        'vl_comprimento': request.lenght,
        'valor_declarado': request.declared_value,
    }

    print(request)

    response = Correios().calculate(method = method, input = request)

    return response

