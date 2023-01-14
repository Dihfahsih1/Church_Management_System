from django.db.models import Q, Count
from .forms import *
from .models import *

from .CurrentWeekView import _get_dates_of_week

current_month = datetime.now().month
now = datetime.now()
date = datetime.day
current_week = _get_dates_of_week(now)
current_week_dates = [date for date in current_week]

#CURRENT WEEK EXPENSES
#current week main
def total_current_week_main():
    main  = Expenditures.objects.filter(Date__in=current_week_dates,Reason_filtering='main' ).aggregate(main=Sum('Amount'))
    total_main=main['main']
    
    if total_main == None:
        total_main = 0
    return total_main
    
#current week Allowances_Amount
def total_current_week_allowances():
    i_allowances = Expenditures.objects.filter(Date__in=current_week_dates, Archived_Status='NOT-ARCHIVED').aggregate(i_total_allowances=Sum('Allowances_Amount'))
    i_total_allowances =i_allowances ['i_total_allowances']
    
    s_allowances  = Expenditures.objects.filter(Date__in=current_week_dates,Reason_filtering='allowance' ).aggregate(s_total_allowances=Sum('Amount'))
    
    s_total_allowances=s_allowances['s_total_allowances']   
        
    if s_total_allowances  == None:
        s_total_allowances =0  
        
    if i_total_allowances  == None:
        i_total_allowances = 0
        
    if s_total_allowances == None:
        total_allowances=0  
        
        
    total_allowances  = i_total_allowances + s_total_allowances 
    return total_allowances

#current week help
def total_current_week_help():
    i_help = Expenditures.objects.filter(Date__in=current_week_dates, Archived_Status='NOT-ARCHIVED').aggregate(i_total_help=Sum('Help_Amount'))
    i_total_help=i_help['i_total_help']
    
    if i_total_help == None:
        i_total_help = 0
    total_help = i_total_help
    return total_help

#current week tot
def total_current_week_tot():
    tot = Expenditures.objects.filter(Date__in=current_week_dates, Archived_Status='NOT-ARCHIVED').aggregate(tot=Sum('Tithe_Of_Tithes_Amount'))
    tot_Amount=tot['tot']
    
    main_tot = Expenditures.objects.filter(Date__in=current_week_dates,Main_Expense_Reason='Tithe of Tithes' ).aggregate(total_tot=Sum('Amount'))
    
    
    main_tot=main_tot['total_tot']  
    
    if tot_Amount == None:
        tot_Amount = 0
        
    if main_tot == None:
        main_tot = 0
    return tot_Amount + main_tot

#current week love offering
def total_current_week_love_offering_expenses():
    Love_Offering_Amount = Expenditures.objects.filter(Date__in=current_week_dates, Archived_Status='NOT-ARCHIVED').aggregate(Love_Offering_Amount=Sum('Love_Offering_Amount'))
    Love_Offering_Amount=Love_Offering_Amount['Love_Offering_Amount']
    
    if Love_Offering_Amount == None:
        Love_Offering_Amount = 0
    return Love_Offering_Amount

#current week bills
def total_current_week_bills_expenses():
    Bills_Amount = Expenditures.objects.filter(Date__in=current_week_dates, Archived_Status='NOT-ARCHIVED').aggregate(Bills_Amount=Sum('Bills_Amount'))
    Bills_Amount=Bills_Amount['Bills_Amount']
    if Bills_Amount == None:
        Bills_Amount = 0
    return Bills_Amount

#current week savings
def total_current_week_savings():
    Savings_Amount = Expenditures.objects.filter(Date__in=current_week_dates, Archived_Status='NOT-ARCHIVED').aggregate(Savings_Amount=Sum('Savings_Amount'))
    Savings_Amount=Savings_Amount['Savings_Amount']
    if Savings_Amount == None:
        Savings_Amount = 0
    return Savings_Amount

#current week expenses on other things
def total_current_week_other_expenses():
    others = Expenditures.objects.filter(Date__in=current_week_dates, Archived_Status='NOT-ARCHIVED').aggregate(others=Sum('Other_Expenses_Amount'))
    others=others['others']
    if others == None:
        others = 0
    return others

#current week petty expenses
def total_current_week_petty_expenses():
    weekly_petty_expenses = Expenditures.objects.filter(Reason_filtering='petty',Date__in=current_week_dates,Archived_Status='NOT-ARCHIVED').aggregate(totals=models.Sum("Amount"))
    if (weekly_petty_expenses['totals'])!=None:
        int(weekly_petty_expenses["totals"])
        d_petty=weekly_petty_expenses["totals"]
    else:
        weekly_petty_expenses = 0
        d_petty = 0 
    return d_petty

#Current week salaries
def total_current_week_salaries():
    total_current_salaries = SalariesPaid.objects.filter(Date_of_paying_salary__in=current_week_dates).aggregate(totals=models.Sum("Salary_Amount"))
    if (total_current_salaries['totals'])!=None:
        int(total_current_salaries["totals"])
        salaries=total_current_salaries["totals"]
    else:
        total_current_salaries = 0
        salaries = 0
    return salaries

# Calculate total current week Expenses
def total_current_week_expenses():
    total_tot = total_current_week_tot()
    total_allowances = total_current_week_allowances()
    total_help = total_current_week_help()
    total_petty = total_current_week_petty_expenses()
    
    total_others = total_current_week_other_expenses()
    total_bills = total_current_week_bills_expenses()
    total_love = total_current_week_love_offering_expenses()
    total_savings = total_current_week_savings()
    total_salaries = total_current_week_salaries()
    
    total_main = total_current_week_main()
    
    
    current_week_total_expenses = (total_tot + total_help + total_allowances+ total_others + total_bills + total_savings + total_love + total_petty + total_salaries + total_main)
    return current_week_total_expenses
