#########################################################
# GENERATED FILE - DO NOT EDIT
# Safe to regenerate at any time 
#########################################################
from familyhub.services.users import create_user as impl_create_user
from familyhub.services.users import delete_user as impl_delete_user
from familyhub.services.users import get_user as impl_get_user
from familyhub.services.users import list_users as impl_list_users
from familyhub.services.users import update_user as impl_update_user


def create_user(body):
    """
    Create a user
    """

    return impl_create_user(
        body=body
    )


def delete_user(user_id):
    """
    Delete a user
    """

    return impl_delete_user(
        user_id=user_id
    )


def get_user(user_id):
    """
    Query user information
    """

    return impl_get_user(
        user_id=user_id
    )


def list_users():
    """
    List all users
    """

    return impl_list_users(
    )


def update_user(user_id, body):
    """
    Update user information
    """

    return impl_update_user(
        user_id=user_id,
        body=body
    )
