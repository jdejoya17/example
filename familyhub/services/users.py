"""
Implements the Jobs services
"""
from typing import Union, List
from familyhub.models import Error, User


def create_user(body) -> Union[User, Error]:
    raise Error(code=501, message="Not Implemented")

def delete_user(user_id) -> Union[None, Error]:
    raise Error(code=501, message="Not Implemented")

def get_user(user_id) -> Union[User, Error]:
    raise Error(code=501, message="Not Implemented")

def list_users() -> Union[List[User], Error]:
    raise Error(code=501, message="Not Implemented")

def update_user() -> Union[User, Error]:
    raise Error(code=501, message="Not Implemented")
