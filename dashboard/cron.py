from .models import *
import calendar
def my_cron_job():
    theme = Theme.objects.get(is_active='Yes')
    theme.is_active = 'No'
    theme.name = 'jazzberry-jam'
    theme.is_active = 'Yes'
    theme.save()
def archiving_data():
    items = Expenditures.objects.all()
    for item in items:
        item.Archived_Status = 'ARCHIVED'
        item.save()
