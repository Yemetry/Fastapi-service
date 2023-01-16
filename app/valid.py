from pydantic import BaseModel, validator
import re


# This class is used to validate data from the user
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
            raise ValueError('Your email is not entered correctly, enter your email using @ and "."')

    # validation of phone
    @validator('phone')
    def valid_phone(cls, val):
        rer = re.match(r'^(\+79)+(\d{9})$', val)
        if rer:
            return val
        else:
            raise ValueError('You entered the data incorrectly, you must enter +79XXXXXXXXX')

    # validation of login
    @validator('login')
    def valid_login(cls, val):
        if 3 <= len(val) <= 20:
            loginrer = re.match(r'^[a-z0-9.]+$', val)
            if loginrer:
                return val
            else:
                raise ValueError('Your login is entered incorrectly, enter your login using the characters a-z, 0-9 and "."')
        else:
            raise ValueError('Your login is entered incorrectly, enter your login using the characters a-z, 0-9 and "."')
