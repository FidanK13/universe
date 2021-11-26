import task as task


@task(ignore_result=True)
def celery_send_email(email):
    pass
    #<send_your_mail>