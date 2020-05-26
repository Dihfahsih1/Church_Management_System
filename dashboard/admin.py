from django.contrib import admin
from .models import *

class PledgeItemAdmin(admin.ModelAdmin):
    list_display = (
    	'Total_Amount_Pledged',
    	'Pledge_Amount_Remaining',
    	'Item_money_balance',
    	'Item_money_received',
    	'Amount_needed_after_cashout',
    	'Total_Item_Cashout')  
class PledgesAdmin(admin.ModelAdmin):
    list_display = ('total_pledge_paid','Pledge_Balance','updatestatus')

class StaffDetailsAdmin(admin.ModelAdmin):
    list_display = ('total_salary_paid','full_name','Balance','basic_salary')
class MembersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'total_tithe')
class SalariesPaidAdmin(admin.ModelAdmin):
    list_display = ('total_salary_paid','Balance') 
class OfferingsReportArchiveAdmin(admin.ModelAdmin):
    list_display = ('total_offerings') 
class ExpendituresAdmin(admin.ModelAdmin):
    list_display = ('net_float')                
admin.site.register(StaffDetails)
admin.site.register(CashFloat)
admin.site.register(Revenues)
admin.site.register(Pledges)
admin.site.register(Members)
admin.site.register(SalariesPaid)
admin.site.register(Visitors)
admin.site.register(User)
admin.site.register(PaidPledges)
admin.site.register(PledgesCashedOut)
admin.site.register(PledgeItem)
admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Event)
admin.site.register(ArchivedMembers)
admin.site.register(Expenditures)
admin.site.register(Ministry)
