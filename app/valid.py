from pydantic import BaseModel, validator
import re


"""This class will be used to validate incoming json files on post request with path '/check ' """
class User(BaseModel):
    email: str
    login: str
    phone: str

    # validation of email
    @validator('email')
    def valid_email(cls, val):
        emailrer = re.match(r'^([a-z0-9]{1})+([a-z0-9.])+(@[a-z0-9.]+\.[a-z]+)$', val)
        if emailrer:
            return val
        else:
            raise ValueError('Phone should be in the form +79XXXXXXXXX')

    @validator('phone')
    def valid_phone(cls, val):
        rer = re.match(r'^(\+79)+(\d{9})$', val)
        if rer:
            return val
        else:
            raise ValueError('Phone should be in the form +79XXXXXXXXX')

    @validator('login')
    def valid_login(cls, val):
        if 3 <= len(val) <= 20:
            loginrer = re.match(r'^[a-z0-9.]+$', val)
            if loginrer:
                return val
            else:
                raise ValueError('The login must include only the characters a-z 0-9 and .')
        else:
            raise ValueError('The login must include only the characters a-z 0-9 and .')
