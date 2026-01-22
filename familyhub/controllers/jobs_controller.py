#########################################################
# GENERATED FILE - DO NOT EDIT
# Safe to regenerate at any time 
#########################################################
from familyhub.services.jobs import action_job as impl_action_job
from familyhub.services.jobs import create_job as impl_create_job
from familyhub.services.jobs import delete_job as impl_delete_job
from familyhub.services.jobs import get_job as impl_get_job
from familyhub.services.jobs import list_jobs as impl_list_jobs
from familyhub.services.jobs import update_job as impl_update_job


def action_job(job_id, body):
    """
    Make an action towards a job
    """

    return impl_action_job(
        job_id=job_id,
        body=body
    )


def create_job(body):
    """
    Create a job
    """

    return impl_create_job(
        body=body
    )


def delete_job(job_id):
    """
    Delete a job
    """

    return impl_delete_job(
        job_id=job_id
    )


def get_job(job_id):
    """
    Query job information
    """

    return impl_get_job(
        job_id=job_id
    )


def list_jobs():
    """
    List all jobs
    """

    return impl_list_jobs(
    )


def update_job(job_id, body):
    """
    Update job information
    """

    return impl_update_job(
        job_id=job_id,
        body=body
    )
