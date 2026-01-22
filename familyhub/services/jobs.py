"""
Implements the Jobs services
"""
from typing import Union, List
from familyhub.models import Error, Job


def action_job(job_id: str, body) -> Union[Job, Error]:
    raise Error(code=501, message="Not Implemented")

def create_job(body) -> Union[Job, Error]:
    raise Error(code=501, message="Not Implemented")

def delete_job(job_id) -> Union[None, Error]:
    raise Error(code=501, message="Not Implemented")

def get_job(job_id) -> Union[Job, Error]:
    raise Error(code=501, message="Not Implemented")

def list_jobs() -> Union[List[Job], Error]:
    raise Error(code=501, message="Not Implemented")

def update_job() -> Union[Job, Error]:
    raise Error(code=501, message="Not Implemented")
