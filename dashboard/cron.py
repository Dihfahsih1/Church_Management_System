from .models import *
def my_cron_job():
    theme = Theme.objects.get(is_active='Yes')
    theme.is_active = 'No'
    theme.name = 'jazzberry-jam'
    theme.is_active = 'Yes'
    theme.save()
