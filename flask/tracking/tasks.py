from . import app, celery, mail
 
@celery.task
def send_mail(msg):
    with app.app_context():
        mail.send(msg)