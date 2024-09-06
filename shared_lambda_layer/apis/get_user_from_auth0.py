from pydantic import BaseModel, Field, EmailStr


class MappedUser(BaseModel):
    id: int
    firstName: str = Field(alias="first_name")
    lastName: str = Field(alias="first_name")
    email: EmailStr
    phone: str
    '''
    Same format from api
    '''
    addressLine1: str = Field(alias="address_line_1")
    '''
    Street address
    '''
    addressLine2: str = Field(alias="address_line_2")
    '''
    PO box, room, apt #, etc
    '''
    state: str
    '''
    Two letter
    '''
    zipCode: str = Field(alias="zip_code")
    country: str
    '''
    Two letter
    '''

'''
TODO: 
1. Get users from GET https://api.auth0.com/users using the requests package (this is a fake url)
2. Map user data to the pydantic BaseModel class
3. Return a single mapped user MappedUser
'''
def get_user_from_auth0(user_id: str) -> MappedUser:
