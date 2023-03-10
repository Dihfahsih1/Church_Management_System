from datetime import datetime, timedelta
from django.utils import timezone
from dashboard.models import Expenditures, Revenues

def archive_transactions():
    try:
        today = datetime.now().date()
        last_month = today - timedelta(days=30)
        start_date = last_month.replace(day=1)
        end_date = (start_date + timedelta(days=32)).replace(day=1) - timedelta(days=1)

        # Filter expenditures for the previous month
        expenditures = Expenditures.objects.filter(
            Date__range=(start_date, end_date),
            Archived_Status='NOT-ARCHIVED'
        )
        for expenditure in expenditures:
            expenditure.Archived_Status = 'ARCHIVED'
            expenditure.save()

        # Filter revenues for the previous month
        revenues = Revenues.objects.filter(
            Date__range=(start_date, end_date),
            Archived_Status='NOT-ARCHIVED'
        )
        for revenue in revenues:
            revenue.Archived_Status = 'ARCHIVED'
            revenue.save()

    except Exception as e:
        print(f"An error occurred: {e}")
