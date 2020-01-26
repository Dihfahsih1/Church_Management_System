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
class OfferingsReportArchiveAdmin(admin.ModelAdmin):
    list_display = ('total_offerings')
class PledgeItemAdmin(admin.ModelAdmin):
    list_display = ('Total_Amount_Pledged','Pledge_Amount_Remaining','Item_money_balance','Item_money_received')              
admin.site.register(StaffDetails)
admin.site.register (Allowance)
admin.site.register(Spend)
admin.site.register(Sundry)
admin.site.register(Offerings)
admin.site.register(Tithes)
admin.site.register(Pledges)
admin.site.register(PledgeItem)
admin.site.register(AllowanceReportArchive)
admin.site.register(SundryReportArchive)
admin.site.register(ExpensesReportArchive)
admin.site.register(OfferingsReportArchive)
admin.site.register(PledgesReportArchive)
admin.site.register(TithesReportArchive)
admin.site.register(Members)
admin.site.register(SalariesPaid)
admin.site.register(Visitors)
admin.site.register(User)
admin.site.register(PaidPledges)
admin.site.register(PledgesCashedOut)