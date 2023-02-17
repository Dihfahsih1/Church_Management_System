

from django.db.models import Q, Count
from .forms import *
from .models import *

from .CurrentWeekView import _get_dates_of_week

current_month = datetime.now().month
now = datetime.now()
date = datetime.day
current_week = _get_dates_of_week(now)
current_week_dates = [date for date in current_week]

#CURRENT WEEK REVENUES

#current week tithes
def total_current_week_tithes():
    i_tithes = Revenues.objects.filter(Date__in=current_week_dates, Archived_Status='NOT-ARCHIVED').aggregate(i_total_tithes=Sum('Tithe_Amount'))
    i_total_tithes=i_tithes['i_total_tithes']
    
    s_tithes = Revenues.objects.filter(Date__in=current_week_dates,Revenue_filter='tithes', Archived_Status='NOT-ARCHIVED').aggregate(s_total_tithes=Sum('Amount'))
    
    s_total_tithes=s_tithes['s_total_tithes']   
        
    if s_total_tithes == None:
        s_total_tithes=0  
    if i_total_tithes == None:
        i_total_tithes = 0
        
    if s_total_tithes == None or i_total_tithes == None:
        total_tithes=0  
        
    total_tithes = i_total_tithes + s_total_tithes
    return total_tithes

#current week offerings
def total_current_week_offerings():
    i_offerings = Revenues.objects.filter(Date__in=current_week_dates, Archived_Status='NOT-ARCHIVED').aggregate(i_total_offerings=Sum('General_Offering_Amount'))
    i_total_offerings=i_offerings['i_total_offerings']
    
    s_offerings = Revenues.objects.filter(Date__in=current_week_dates, Revenue_filter="offering", Archived_Status='NOT-ARCHIVED').aggregate(s_total_offerings=Sum('Amount'))
    s_total_offerings=s_offerings['s_total_offerings']
    
    if s_total_offerings== None:
        s_total_offerings=0  
    if i_total_offerings == None:
        i_total_offerings = 0
        
    if s_total_offerings == None and i_total_offerings == None:
        total_offerings=0  
        
    total_offerings = i_total_offerings + s_total_offerings
    return total_offerings

#current week seeds
def total_current_week_seeds():
    Seed_Amount = Revenues.objects.filter(Date__in=current_week_dates, Archived_Status='NOT-ARCHIVED').aggregate(Seed_Amount=Sum('Seed_Amount'))
    Seed_Amount=Seed_Amount['Seed_Amount']
    
    if Seed_Amount == None:
        Seed_Amount = 0
    return Seed_Amount

#current week love offering
def total_current_week_love_offering():
    Love_Offering_Amount = Revenues.objects.filter(Date__in=current_week_dates, Archived_Status='NOT-ARCHIVED').aggregate(Love_Offering_Amount=Sum('Love_Offering_Amount'))
    Love_Offering_Amount=Love_Offering_Amount['Love_Offering_Amount']
    
    if Love_Offering_Amount == None:
        Love_Offering_Amount = 0
    return Love_Offering_Amount

#current week thanks giving
def total_current_week_thanks_giving():
    Thanks_Giving_Amount = Revenues.objects.filter(Date__in=current_week_dates, Archived_Status='NOT-ARCHIVED').aggregate(Thanks_Giving_Amount=Sum('Thanks_Giving_Amount'))
    Thanks_Giving_Amount=Thanks_Giving_Amount['Thanks_Giving_Amount']
    
    if Thanks_Giving_Amount == None:
        Thanks_Giving_Amount = 0
    return Thanks_Giving_Amount

#current week bills
def total_current_week_bills_contributions():
    Bills_Amount = Revenues.objects.filter(Date__in=current_week_dates, Archived_Status='NOT-ARCHIVED').aggregate(Bills_Amount=Sum('Bills_Amount'))
    Bills_Amount=Bills_Amount['Bills_Amount']
    if Bills_Amount == None:
        Bills_Amount = 0
    return Bills_Amount

#current week contributions towards envagelism
def total_current_week_evanglism_contributions():
    Envag_Or_Missions_Amount = Revenues.objects.filter(Date__in=current_week_dates, Archived_Status='NOT-ARCHIVED').aggregate(Envag_Or_Missions_Amount=Sum('Envag_Or_Missions_Amount'))
    Envag_Or_Missions_Amount=Envag_Or_Missions_Amount['Envag_Or_Missions_Amount']
    if Envag_Or_Missions_Amount == None:
        Envag_Or_Missions_Amount = 0
    return Envag_Or_Missions_Amount

#current week revenue from other sources
def total_current_week_other_revenue_sources():
    others = Revenues.objects.filter(Date__in=current_week_dates, Revenue_filter="others", Archived_Status='NOT-ARCHIVED').aggregate(others=Sum('Amount'))
    others=others['others']
    if others == None:
        others = 0
    return others

# Calculate total current week revenues
def total_current_week_revenue():
    total_tithes = total_current_week_tithes()
    total_offerings = total_current_week_offerings()
    total_seeds = total_current_week_seeds()
    
    total_others = total_current_week_other_revenue_sources()
    total_bills = total_current_week_bills_contributions()
    total_eva = total_current_week_evanglism_contributions()
    total_thanks = total_current_week_thanks_giving()
    total_love = total_current_week_love_offering()
    
    current_week_total_revenues = (total_tithes + total_offerings + total_seeds + total_others + total_bills + total_eva + total_thanks + total_love )
    return current_week_total_revenues
