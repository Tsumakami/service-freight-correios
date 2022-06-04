from fastapi import HTTPException, status
from fastapi.security import HTTPBasicCredentials

class Authentication:
    
    @staticmethod
    def authenticate(credentials: HTTPBasicCredentials) -> bool:
        user_expected = 'admin'
        password_expected = 'admin123'

        user_not_valid = credentials.username != user_expected
        password_not_valid = credentials.password != password_expected

        if(user_not_valid or password_not_valid):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
    