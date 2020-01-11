from django.contrib import admin
from .models import *


class PledgesAdmin(admin.ModelAdmin):
    list_display = ('total_pledge_paid','Pledge_Balance','updatestatus')

class PledgesReportArchiveAdmin(admin.ModelAdmin):
    list_display = ('total_pledge_paid','Pledge_Balance','updatestatus') 
class StaffDetailsAdmin(admin.ModelAdmin):
    list_display = ('total_salary_paid','full_name','Balance','basic_salary')
class MembersAdmin(admin.ModelAdmin):
    list_display = ('full_name') 
class SalariesPaidAdmin(admin.ModelAdmin):
    list_display = ('total_salary_paid','Balance')           
admin.site.register(StaffDetails)
admin.site.register (Allowance)
admin.site.register(Spend)
admin.site.register(Sundry)
admin.site.register(Offerings)
admin.site.register(Tithes)
admin.site.register(Pledges)
admin.site.register(AllowanceReportArchive)
admin.site.register(SundryReportArchive)
admin.site.register(ExpensesReportArchive)
admin.site.register(OfferingsReportArchive)
admin.site.register(PledgesReportArchive)
admin.site.register(TithesReportArchive)
admin.site.register(Members)
admin.site.register(Visitors)