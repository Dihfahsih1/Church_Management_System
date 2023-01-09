from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
from datetime import datetime, timedelta   
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from .forms import *
from .models import *
from time import strptime
from .render import Render
from django.template.loader import render_to_string
from django.http import Http404, JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import calendar
from dal import autocomplete
 
from django.utils.encoding import force_text  
from django.utils.http import urlsafe_base64_decode  
from .tokens import account_activation_token  
from django.core.mail import EmailMessage,send_mail, BadHeaderError
from django.views.decorators.clickjacking import xframe_options_exempt
from tracking.models import Visitor

from .serializers import RegisteredMemberSerializer


now = datetime.now()
date = datetime.day

#CURRENT month EXPENSES
#current month main

current_month = datetime.now().month
current_year = datetime.now().year
def total_current_month_main():
    main  = Expenditures.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED',Reason_filtering='main' ).aggregate(main=Sum('Amount'))
    total_main=main['main']
    
    if total_main == None:
        total_main = 0
    return total_main
    
#current month Allowances_Amount
def total_current_month_allowances():
    i_allowances = Expenditures.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED').aggregate(i_total_allowances=Sum('Allowances_Amount'))
    i_total_allowances =i_allowances ['i_total_allowances']
    
    s_allowances  = Expenditures.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED',Reason_filtering='allowance' ).aggregate(s_total_allowances=Sum('Amount'))
    
    s_total_allowances=s_allowances['s_total_allowances']   
        
    if s_total_allowances  == None:
        s_total_allowances =0  
        
    if i_total_allowances  == None:
        i_total_allowances = 0
        
    if s_total_allowances == None:
        total_allowances=0  
        
        
    total_allowances  = i_total_allowances + s_total_allowances 
    return total_allowances

#current month help
def total_current_month_help():
    i_help = Expenditures.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED').aggregate(i_total_help=Sum('Help_Amount'))
    i_total_help=i_help['i_total_help']
    
    if i_total_help == None:
        i_total_help = 0
    total_help = i_total_help
    return total_help

#current month tot
def total_current_month_tot():
    tot = Expenditures.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED').aggregate(tot=Sum('Tithe_Of_Tithes_Amount'))
    tot_Amount=tot['tot']
    
    main_tot = Expenditures.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED',Main_Expense_Reason='Tithe of Tithes' ).aggregate(total_tot=Sum('Amount'))
    
    
    main_tot=main_tot['total_tot']  
    
    if tot_Amount == None:
        tot_Amount = 0
        
    if main_tot == None:
        main_tot = 0
    return tot_Amount + main_tot

#current month love offering
def total_current_month_love_offering_expenses():
    Love_Offering_Amount = Expenditures.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED').aggregate(Love_Offering_Amount=Sum('Love_Offering_Amount'))
    Love_Offering_Amount=Love_Offering_Amount['Love_Offering_Amount']
    
    if Love_Offering_Amount == None:
        Love_Offering_Amount = 0
    return Love_Offering_Amount

#current month bills
def total_current_month_bills_expenses():
    Bills_Amount = Expenditures.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED').aggregate(Bills_Amount=Sum('Bills_Amount'))
    Bills_Amount=Bills_Amount['Bills_Amount']
    if Bills_Amount == None:
        Bills_Amount = 0
    return Bills_Amount

#current month savings
def total_current_month_savings():
    Savings_Amount = Expenditures.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED').aggregate(Savings_Amount=Sum('Savings_Amount'))
    Savings_Amount=Savings_Amount['Savings_Amount']
    if Savings_Amount == None:
        Savings_Amount = 0
    return Savings_Amount

#current month expenses on other things
def total_current_month_other_expenses():
    others = Expenditures.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED').aggregate(others=Sum('Other_Expenses_Amount'))
    others=others['others']
    if others == None:
        others = 0
    return others

#current month petty expenses
def total_current_month_petty_expenses():
    monthly_petty_expenses = Expenditures.objects.filter(Reason_filtering='petty',Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED').aggregate(totals=models.Sum("Amount"))
    if (monthly_petty_expenses['totals'])!=None:
        int(monthly_petty_expenses["totals"])
        d_petty=monthly_petty_expenses["totals"]
    else:
        monthly_petty_expenses = 0
        d_petty = 0 
    return d_petty

#Current month salaries
def total_current_month_salaries():
    total_current_salaries = SalariesPaid.objects.filter(Date_of_paying_salary__month=current_month,Date_of_paying_salary__year=current_year, Archived_Status='NOT-ARCHIVED').aggregate(totals=models.Sum("Salary_Amount"))
    if (total_current_salaries['totals'])!=None:
        int(total_current_salaries["totals"])
        salaries=total_current_salaries["totals"]
    else:
        total_current_salaries = 0
        salaries = 0
    return salaries

# Calculate total current month Expenses
def total_current_month_expenses():
    total_tot = total_current_month_tot()
    total_allowances = total_current_month_allowances()
    total_help = total_current_month_help()
    total_petty = total_current_month_petty_expenses()
    
    total_others = total_current_month_other_expenses()
    total_bills = total_current_month_bills_expenses()
    total_love = total_current_month_love_offering_expenses()
    total_savings = total_current_month_savings()
    total_salaries = total_current_month_salaries()
    
    total_main = total_current_month_main()
    
    
    current_month_total_expenses = (total_tot + total_help + total_allowances+ total_others + total_bills + total_savings + total_love + total_petty + total_salaries + total_main)
    return current_month_total_expenses


#CURRENT month REVENUES
#current month tithes
def total_current_month_tithes():
    i_tithes = Revenues.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED').aggregate(i_total_tithes=Sum('Tithe_Amount'))
    i_total_tithes=i_tithes['i_total_tithes']
    
    s_tithes = Revenues.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED',Revenue_filter='tithes').aggregate(s_total_tithes=Sum('Amount'))
    
    s_total_tithes=s_tithes['s_total_tithes']   
        
    if s_total_tithes == None:
        s_total_tithes=0  
    if i_total_tithes == None:
        i_total_tithes = 0
        
    if s_total_tithes == None or i_total_tithes == None:
        total_tithes=0  
        
    total_tithes = i_total_tithes + s_total_tithes
    return total_tithes

#current month offerings
def total_current_month_offerings():
    i_offerings = Revenues.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED').aggregate(i_total_offerings=Sum('General_Offering_Amount'))
    i_total_offerings=i_offerings['i_total_offerings']
    
    s_offerings = Revenues.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED', Revenue_filter="offering").aggregate(s_total_offerings=Sum('Amount'))
    s_total_offerings=s_offerings['s_total_offerings']
    
    if s_total_offerings== None:
        s_total_offerings=0  
    if i_total_offerings == None:
        i_total_offerings = 0
        
    if s_total_offerings == None and i_total_offerings == None:
        total_offerings=0  
        
    total_offerings = i_total_offerings + s_total_offerings
    return total_offerings

#current month seeds
def total_current_month_seeds():
    Seed_Amount = Revenues.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED').aggregate(Seed_Amount=Sum('Seed_Amount'))
    Seed_Amount=Seed_Amount['Seed_Amount']
    
    if Seed_Amount == None:
        Seed_Amount = 0
    return Seed_Amount

#current month love offering
def total_current_month_love_offering():
    Love_Offering_Amount = Revenues.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED').aggregate(Love_Offering_Amount=Sum('Love_Offering_Amount'))
    Love_Offering_Amount=Love_Offering_Amount['Love_Offering_Amount']
    
    if Love_Offering_Amount == None:
        Love_Offering_Amount = 0
    return Love_Offering_Amount

#current month thanks giving
def total_current_month_thanks_giving():
    Thanks_Giving_Amount = Revenues.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED').aggregate(Thanks_Giving_Amount=Sum('Thanks_Giving_Amount'))
    Thanks_Giving_Amount=Thanks_Giving_Amount['Thanks_Giving_Amount']
    
    if Thanks_Giving_Amount == None:
        Thanks_Giving_Amount = 0
    return Thanks_Giving_Amount

#current month bills
def total_current_month_bills_contributions():
    Bills_Amount = Revenues.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED').aggregate(Bills_Amount=Sum('Bills_Amount'))
    Bills_Amount=Bills_Amount['Bills_Amount']
    if Bills_Amount == None:
        Bills_Amount = 0
    return Bills_Amount

#current month contributions towards envagelism
def total_current_month_evanglism_contributions():
    Envag_Or_Missions_Amount = Revenues.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED').aggregate(Envag_Or_Missions_Amount=Sum('Envag_Or_Missions_Amount'))
    Envag_Or_Missions_Amount=Envag_Or_Missions_Amount['Envag_Or_Missions_Amount']
    if Envag_Or_Missions_Amount == None:
        Envag_Or_Missions_Amount = 0
    return Envag_Or_Missions_Amount

#current month revenue from other sources
def total_current_month_other_revenue_sources():
    others = Revenues.objects.filter(Date__month=current_month,Date__year=current_year, Archived_Status='NOT-ARCHIVED', Revenue_filter="others", ).aggregate(others=Sum('Amount'))
    others=others['others']
    if others == None:
        others = 0
    return others

# Calculate total current month revenues
def total_current_month_revenue():
    total_tithes = total_current_month_tithes()
    total_offerings = total_current_month_offerings()
    total_seeds = total_current_month_seeds()
    
    total_others = total_current_month_other_revenue_sources()
    total_bills = total_current_month_bills_contributions()
    total_eva = total_current_month_evanglism_contributions()
    total_thanks = total_current_month_thanks_giving()
    total_love = total_current_month_love_offering()
    
    current_month_total_revenues = (total_tithes + total_offerings + total_seeds + total_others + total_bills + total_eva + total_thanks + total_love )
    return current_month_total_revenues

#current month pledges
def current_month_pledges():
    total_monthly_pledges = Pledges.objects.filter(Date__month=current_month,Date__year=current_year).aggregate(totals=models.Sum("Amount_Paid"))
    if (total_monthly_pledges['totals'])!=None:
        int(total_monthly_pledges["totals"])
        d_pledges=total_monthly_pledges["totals"]
    else:
        total_monthly_pledges = 0
        d_pledges = 0
    return d_pledges

def month_of_month(date):
    date= datetime.now()
    month = date.month
    month = 0
    while date.month == month:
        month += 1
        date -= timedelta(days=7)
    return month