from celery import task 
from celery import shared_task 

@shared_task 
def send_notifiction():
     print(‘testing’)