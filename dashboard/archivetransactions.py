from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from dashboard.models import Expenditures, Revenues

def archive_transactions():
    today = datetime.now().date()
    last_month = today - relativedelta(months=1)
    start_date = last_month.replace(day=1)
    end_date = last_month.replace(day=1) + relativedelta(months=1) - relativedelta(days=1)
    # Filter expenditures for the previous month
    expenditures = Expenditures.objects.filter(
        Date__month__gte=start_date.month,
        Date__year__lte=end_date.year,
        Archived_Status='NOT-ARCHIVED'
    )
    for expenditure in expenditures:
        expenditure.Archived_Status = 'ARCHIVED'
        expenditure.save()
    
    # Filter revenues for the previous month
    revenues = Revenues.objects.filter(
        Date__month__gte=start_date.month,
        Date__year__lte=start_date.year,
        Archived_Status='NOT-ARCHIVED'
    )
    for revenue in revenues:
        revenue.Archived_Status = 'ARCHIVED'
        revenue.save()