from email_validate import email_validate
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
        temp = email_validate.validate(email_address=val, check_format=True, check_blacklist=False, check_dns=False,
                                check_smtp=False, smtp_helo_host=False)
        if temp: return val
        else: raise ValueError('ХУИТА')


    @validator('phone')
    def valid_phone(cls, val):
        if len(val) == 12 and val[0:3] == "+79":
            for char in val[3:]:
                if not (48 <= ord(char) <= 57):
                    raise ValueError('Phone should be in the form +79XXXXXXXXX')
        else:
            raise ValueError('Phone should be in the form +79XXXXXXXXX')
        return val

    @validator('login')
    def valid_login(cls, val):
        if 3 <= len(val) <= 20:
            for char in val:
                if not (97 <= ord(char) <= 122 or 48 <= ord(char) <= 57 or ord(char) == 46):
                    raise ValueError('The login must include only the characters a-z 0-9 and .')
        else:
            raise ValueError('The login must include only the characters a-z 0-9 and .')
        return val
