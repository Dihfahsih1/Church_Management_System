#views
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import *
from .models import *
from .render import Render
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
@login_required
def index(request):
    current_month = datetime.now().month
    total_current_donations = Donations.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_current_donations['totals'])!=None:
        int(total_current_donations["totals"])
        donations=total_current_donations["totals"]
    else:
        total_current_donations = 0
        donations = 0

    total_current_thanks = ThanksGiving.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_current_thanks['totals'])!=None:
        int(total_current_thanks["totals"])
        thanks=total_current_thanks["totals"]
    else:
        total_current_thanks = 0
        thanks = 0    

    current_month = datetime.now().month
    total_current_seeds = Seeds.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_current_seeds['totals'])!=None:
        int(total_current_seeds["totals"])
        seeds=total_current_seeds["totals"]
    else:
        total_current_seeds = 0
        seeds = 0

    total_current_offerings = Offerings.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Total_Offering"))
    if (total_current_offerings['totals'])!=None:
        int(total_current_offerings["totals"])
        offerings=total_current_offerings["totals"]
    else:
        total_current_offerings = 0
        offerings = 0

    total_current_tithes = Tithes.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_current_tithes['totals'])!=None:
        int(total_current_tithes["totals"])
        tithes=total_current_tithes["totals"]
    else:
        total_current_tithes=0
        tithes = 0

    total_current_salaries = SalariesPaid.objects.filter(Date_of_paying_salary__month=current_month).aggregate(totals=models.Sum("Salary_Amount"))
    if (total_current_salaries['totals'])!=None:
        int(total_current_salaries["totals"])
        salaries=total_current_salaries["totals"]
    else:
        total_current_salaries = 0
        salaries = 0

    total_current_pledges = PaidPledges.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount_Paid"))
    if (total_current_pledges['totals'])!=None:
        int(total_current_pledges["totals"])
        pledges=total_current_pledges["totals"]
    else:
        total_current_pledges = 0
        pledges = 0

    total_main_expenses = Spend.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_main_expenses['totals'])!=None:
        int(total_main_expenses["totals"])
        expenses=total_main_expenses["totals"]
    else:
        total_main_expenses = 0
        expenses = 0
    #Total general expenses of the current month of the year.
    total_general_expenses = GeneralExpenses.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_general_expenses['totals'])!=None:
        int(total_general_expenses["totals"])
        general=total_general_expenses["totals"]
    else:
        total_general_expenses = 0
        general = 0

    #Petty Cash expenses
    total_petty_expenses = Sundry.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_petty_expenses['totals'])!=None:
        int(total_petty_expenses["totals"])
        petty=total_petty_expenses["totals"]
    else:
        total_petty_expenses = 0
        petty = 0
    total_allowances = Allowance.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_allowances['totals'])!=None:
        int(total_allowances["totals"])
        allowances=total_allowances["totals"]    
    else:
        total_allowances = 0
        allowances=0

    #incase of data has been archived, none is returned, so we have to catch it before it causes trouble
    if (total_current_donations,total_current_thanks,total_current_seeds,total_petty_expenses,total_current_tithes,total_current_salaries, total_general_expenses, total_current_offerings,total_current_pledges,total_allowances,total_main_expenses)== None:
        total_monthly_incomes = 0
        total_monthly_expenditure =  0
        total_general_expenses = 0
        total_current_seeds=0
        total_current_donations=0
        total_current_thanks=0
        pledges = 0
        #calculating net income
        net_income = total_monthly_incomes - total_monthly_expenditure
        today = timezone.now()
        month = today.strftime('%B')

        context={'total_current_donations':total_current_donations,'total_current_thanks':total_current_thanks,'total_current_seeds':total_current_seeds,'total_petty_expenses':total_petty_expenses,'total_general_expenses':total_general_expenses,'total_monthly_incomes':total_monthly_incomes,'salaries':salaries,'total_current_salaries':total_current_salaries,'total_monthly_expenditure':total_monthly_expenditure, 'month': month,
        'petty':petty,'allowances':allowances,'seeds':seeds, 'general':general,'expenses':expenses,
        'tithes':tithes, 'offerings':offerings, 'pledges':pledges, 'net_income':net_income,
        'thanks':thanks,'donations':donations}
        return render(request,'index.html', context)
    #in case the totals are Zero
    elif (total_petty_expenses,total_current_tithes,total_general_expenses, total_current_salaries, total_current_offerings,total_current_pledges,total_allowances,total_main_expenses)== 0:
        total_monthly_incomes = 0
        total_monthly_expenditure =  0
        total_general_expenses = 0
        pledges = 0
        #calculating net income
        net_income = total_monthly_incomes - total_monthly_expenditure
        today = timezone.now()
        month = today.strftime('%B')
        context={'total_current_donations':total_current_donations,'total_current_thanks':total_current_thanks,'total_current_seeds':total_current_seeds,'total_general_expenses':total_general_expenses,'total_petty_expenses':total_petty_expenses,'salaries':salaries,'total_current_salaries':total_current_salaries,'total_monthly_incomes':total_monthly_incomes,'total_monthly_expenditure':total_monthly_expenditure, 'month': month,
        'general':general,'allowances':allowances,'seeds':seeds, 'expenses':expenses,
        'tithes':tithes, 'offerings':offerings, 'pledges':pledges, 'net_income':net_income,'thanks':thanks,'donations':donations}
        return render(request,'index.html', context)

    #if there are moneys, calculate incomes and total expenditure.
    else:
        total_monthly_incomes =  tithes+ offerings + seeds + thanks + donations
        total_monthly_expenditure =  allowances + expenses+salaries+ general+ petty
        net_income = total_monthly_incomes - total_monthly_expenditure
        today = timezone.now()
        month = today.strftime('%B')
        context={'total_current_donations':total_current_donations,'total_current_thanks':total_current_thanks,'total_current_seeds':total_current_seeds,'total_petty_expenses':total_petty_expenses,'total_general_expenses':total_general_expenses,'salaries':salaries,'total_current_salaries':total_current_salaries,'total_monthly_incomes':total_monthly_incomes,'total_monthly_expenditure':total_monthly_expenditure, 'month': month,
        'petty':petty,'allowances':allowances,'seeds':seeds,'general':general, 'expenses':expenses,'tithes':tithes, 
        'offerings':offerings, 'pledges':pledges, 'net_income':net_income,'thanks':thanks,'donations':donations}
        return render(request,'index.html', context)

    


    ##################################
    #        Employee Module         #
    ##################################

def employee_register(request):
    if request.method=="POST":
        form=StaffDetailsForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            return redirect('employee-list')
    else:
        form=StaffDetailsForm()
        return render(request, 'Employees/record_employee.html',{'form':form})

def delete_employee(request,pk):
    employee= get_object_or_404(StaffDetails, id=pk)
    if request.method == "GET":
        employee.delete()
        messages.success(request, "Post successfully deleted!")
        return redirect("members-list")
    context= {'employee': employee}
    return render(request, 'Employees/employee_delete.html', context)

@login_required
def employee_list(request):
    employees = StaffDetails.objects.all().order_by('-id')
    today = timezone.now()
    mth = today.strftime('%B')
    context ={'mth':mth,'employees': employees}
    return render(request, 'Employees/employee_list.html', context)
def edit_employee(request, pk):
    item = get_object_or_404(StaffDetails, pk=pk)
    if request.method == "POST":
        form = StaffDetailsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('employee-list')
    else:
        today = timezone.now()
        month = today.strftime('%B')
        message="Edit Employee Details"
        get_name = StaffDetails.objects.filter(id=pk)
        form = StaffDetailsForm(instance=item)        
        context={'form':form, 'month':month, 'message':message, 'get_name':get_name}
    return render(request, 'Employees/record_employee.html', context)
def view_employee(request, pk):
    context={}
    employee = get_object_or_404(StaffDetails, id=pk)
    if request.method == 'POST':
        form = StaffDetailsForm(request.POST, instance=employee)
        context['form']=form
    else:
        form = StaffDetailsForm(instance=employee)
        get_name = StaffDetails.objects.filter(id=pk)
        context['get_name']=get_name
        context['form']=form
    return render(request,'Employees/employee_view.html',context)
def paying_employees(request, pk):
    items = get_object_or_404(StaffDetails, id=pk)
    if request.method == "POST":
        form = StaffDetailsForm(request.POST, request.FILES, instance=items)
    else:
        form = StaffDetailsForm(instance=items)
        retrieve_employee_id = StaffDetails.objects.filter(id=pk)
        context = {'form': form, 'retrieve_employee_id': retrieve_employee_id}
        return render(request, 'Employees/pay_employee.html', context)

def paid_salary(request):
    if request.method == "POST":
        form = SalariesPaidForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('current-month-salaries')
        else:
            form = SalariesPaidForm()
            context = {'form': form}
            return render(request, 'Employees/pay_employee.html', context)

 #archive salaries report           
def current_month_salary_paid(request):
    current_month = datetime.now().month
    current_year = datetime.now().year
    today = timezone.now()
    mth = today.strftime('%B')
    salaries = SalariesPaid.objects.filter(Date_of_paying_salary__year=current_year, Date_of_paying_salary__month=current_month)
    context={'mth':mth, 'salaries':salaries}
    if request.method=='POST':
        archived_year=request.POST['archived_year']
        archived_month = request.POST['archived_month']

        #all the available expense in the expenses table
        current_month = datetime.now().month
        current_year = datetime.now().year
        today = timezone.now()
        day=datetime.now()
        mth = today.strftime('%B')
        salaries = SalariesPaid.objects.filter(Date_of_paying_salary__year=current_year, Date_of_paying_salary__month=current_month)
        context={'day':day,'mth':mth, 'salaries':salaries}
        for sal in salaries:
            date=sal.Date_of_paying_salary
            salary_id=sal.Salary_Id
            amount=sal.Salary_Amount
            name=sal.Name
            mth=sal.Month_being_cleared
            # the expense archive object
            sal_archiveobj=SalariesPaidReportArchive()
            #attached values to expense_archiveobj
            sal_archiveobj.Date_of_paying_salary=date
            sal_archiveobj.Salary_Amount=amount
            sal_archiveobj.Salary_Id=salary_id
            sal_archiveobj.Name=name
            sal_archiveobj.Month_being_cleared=mth
            sal_archiveobj.archivedyear= archived_year
            sal_archiveobj.archivedmonth =archived_month
            sal_archiveobj.save()
        #deleting all the expense from reports table
        salaries.delete()
        message="The Monthly Salaries Paid Report has been Achived"
        context={'message':message, 'mth':mth}
        return render(request, 'Employees/current_month_salaries_paid.html', context)
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August','September', 'October', 'November','December']
    yr = datetime.now().year
    years = [yr,2019,2018]
    today = timezone.now()
    day=datetime.now()
    total = SalariesPaid.objects.filter(Date_of_paying_salary__year=current_year, Date_of_paying_salary__month=current_month).aggregate(totals=models.Sum("Salary_Amount"))
    total_amount = total["totals"]
    context = {
         'day':day, 'mth':mth,'total_amount':total_amount, 'salaries': salaries, 'months':months,
        'current_month':current_month,
        'years':years,
    }
    return render(request, 'Employees/current_month_salaries_paid.html',context) 
#Search for the archived salaries reports
def salariespaidarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = SalariesPaidReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August','September', 'October',  'November','December']
        yr = datetime.now().year
        years = [yr,2019,2018]

        archived_salaries = SalariesPaidReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Salary_Amount"))
        total_amount = total["totals"]

        context = {'archived_reports': archived_reports,
                   'months': months,
                   'years': years,
                   'archived_salaries':archived_salaries,
                   'total_amount': total_amount,
                   'today': today,
                   'report_year': report_year,
                   'report_month': report_month
                   }
        return render(request, "Employees/salariespaidarchive.html", context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September','October',  'November', 'December']
    yr = datetime.now().year
    years = [yr,2019,2018]

    archived_salaries=SalariesPaidReportArchive.objects.all()

    context = {'months': months,
               'years': years,
               'archived_salaries': archived_salaries}
    return render(request, "Employees/salariespaidarchive.html", context)    

      ####################################################
    #       REGISTERING CHURCH MEMBERS AND VISITORS      #
     ####################################################


    #members
@login_required
def register_members(request):
    if request.method=="POST":
        form=MembersForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            return redirect('members-list')
    else:
        form=MembersForm()
        return render(request, 'Members/register_members.html',{'form':form})

        #visitors
@login_required
def register_visitors(request):
    if request.method=="POST":
        form=VisitorsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitors-list')
    else:
        form=VisitorsForm()
        return render(request, 'Members/register_visitors.html',{'form':form})

#list of church members
@login_required
def members_list(request):
    membership = Members.objects.all().order_by('-id')
    day=datetime.now()
    context ={'membership': membership, 'day':day}
    return render(request, 'Members/members_list.html', context)

def edit_member(request, pk):
    item = get_object_or_404(Members, pk=pk)
    if request.method == "POST":
        form = MembersForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('members-list')
    else:
        form = MembersForm(instance=item)
    return render(request, 'Members/register_members.html', {'form': form})
def view_member(request, pk):
    context={}
    member = get_object_or_404(Members, id=pk)
    if request.method == 'POST':
        form = MembersForm(request.POST, instance=member)
        context['form']=form
    else:
        form = MembersForm(instance=member)
        get_name = Members.objects.filter(id=pk)
        context['get_name']=get_name
        context['form']=form
    return render(request,'Members/members_view.html',context)

def delete_member(request, pk):
    member= get_object_or_404(Members, id=pk)
    if request.method == "GET":
        member.delete()
        messages.success(request, "Post successfully deleted!")
        return redirect("members-list")
    context= {'member': member}
    return render(request, 'Members/members_delete.html', context)
def edit_visitor(request, pk):
    item = get_object_or_404(Visitors, pk=pk)
    if request.method == "POST":
        form = VisitorsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('visitors-list')
    else:
        form = VisitorsForm(instance=item)
    return render(request, 'Members/register_visitors.html', {'form': form})
def delete_visitor(request, pk):
    visiting= get_object_or_404(Visitors, id=pk)
    if request.method == "GET":
        visiting.delete()
        messages.success(request, "Post successfully deleted!")
        return redirect("visitors-list")

    context= {'visiting': visiting}
    return render(request, 'Members/visitor_delete.html', context)

    #list of church visitors
@login_required
def visitors_list(request):
    visiting = Visitors.objects.all()
    context ={'visiting': visiting}
    return render(request, 'Members/visitors_list.html', context)






     ###################################################
              #        OFFERINGS MODULE        #
     ###################################################
@login_required
def Enter_Offerings(request):
    if request.method=="POST":
        form=OfferingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Offeringsreport')
    else:
        form=OfferingsForm()
        return render(request, 'Offerings/record_offerings.html',{'form':form})
def edit_offerings(request, pk):
    item = get_object_or_404(Offerings, pk=pk)
    if request.method == "POST":
        form = OfferingsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Offeringsreport')
    else:
        form = OfferingsForm(instance=item)
    return render(request, 'Offerings/record_offerings.html', {'form': form})

class offeringspdf(View):
    def get(self, request):
        current_month = datetime.now().month
        offerings = Offerings.objects.filter(Date__month=current_month).order_by('-Date')

        today = timezone.now()
        month = today.strftime('%B')
        totalexpense = 0
        for instance in offerings:
            totalexpense += instance.Total_Offering
        context = {

            'month': month,
            'today': today,
            'offerings': offerings,
            'request': request,
            'totalexpense': totalexpense,
        }
        return Render.render('Offerings/offeringspdf.html', context)

class offeringsreceipt(View):
    def get(self, request, pk):
        offerings= get_object_or_404(Offerings,pk=pk)
        today = timezone.now()
        context = {
            'today': today,
            'offerings': offerings,
            'request': request,
        }
        return Render.render('Offerings/offeringsreceipt.html', context)

@login_required
def Offeringsreport (request):
    if request.method=='POST':
        archived_year=request.POST['archived_year']
        archived_month = request.POST['archived_month']

        #all the available expense in the expenses table
        all_expenses = Offerings.objects.all()
        for expense in all_expenses:
            date=expense.Date
            service=expense.Service
            amount=expense.Total_Offering

            # the expense archive object
            expense_archiveobj=OfferingsReportArchive()

            #attached values to expense_archiveobj
            expense_archiveobj.Date=date
            expense_archiveobj.Amount=amount
            expense_archiveobj.Service=service
            expense_archiveobj.archivedyear= archived_year
            expense_archiveobj.archivedmonth =archived_month

            expense_archiveobj.save()

        #deleting all the expense from reports table
        all_expenses.delete()

        message="The Monthly Offerings Report has been Achived"
        context={'message':message}
        return render(request, 'Offerings/offeringsindex.html', context)

    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August','September', 'October', 'November','December']
    yr = datetime.now().year
    years = [yr,2019,2018]
    today = timezone.now()
    current_month = today.strftime('%B')
    mth = datetime.now().month
    day=datetime.now()
    total = Offerings.objects.aggregate(totals=models.Sum("Total_Offering"))
    total_amount = total["totals"]
    items =Offerings.objects.all()
    context = {'day':day,'yr':yr, 'total_amount':total_amount,'items': items,'months':months,'current_month':current_month,'years':years,
    }
    return render(request, 'Offerings/offeringsindex.html', context)

@login_required
def offeringsarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = OfferingsReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December']
        yr = datetime.now().year
        years = [yr,2019,2018]

        offerings = OfferingsReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'archived_reports': archived_reports,
                   'months': months,
                   'years': years,
                   'expenses': offerings,
                   'total_amount': total_amount,
                   'today': today,
                   'report_year': report_year,
                   'report_month': report_month
                   }
        return render(request, "Offerings/offeringsarchive.html", context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'November', 'December']
    yr = datetime.now().year
    years = [yr,2019,2018]

    offerings = OfferingsReportArchive.objects.all()

    context = {'months': months,'years': years,'offerings': offerings}
    return render(request, "Offerings/offeringsarchive.html", context)

class offeringsarchivepdf(View):
    def get(self, request, report_month, report_year):
        archived_offerings = OfferingsReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        today = timezone.now()
        total = archived_offerings.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        offeringscontext = {
            'today': today,
            'total_amount': total_amount,
            'request': request,
            'archived_offerings': archived_offerings,
        }
        return Render.render('Offerings/offeringsarchivepdf.html', offeringscontext)

    
        #################################################
        #        SEEDS OFFERING MODULE                  #
        #################################################
def add_seeds(request):

    if request.method=="POST":
        form=SeedsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Seeds-report')
    else:
        form=SeedsForm()
        today = timezone.now()
        month = today.strftime('%B')
        context={'form':form, 'month':month}
        return render(request, 'Seeds/add_seeds.html',context)  
@login_required
def Seedsreport (request):
    if request.method=='POST':
        archived_year=request.POST['archived_year']
        archived_month = request.POST['archived_month']
        #all the available expense in the expenses table
        all_expenses = Seeds.objects.all()
        for expense in all_expenses:
            date=expense.Date
            name=expense.Seed_Made_By
            amount=expense.Amount
            # the expense archive object
            expense_archiveobj=SeedsReportArchive()
            #attached values to expense_archiveobj
            expense_archiveobj.Date=date
            expense_archiveobj.Seed_Made_By = name
            expense_archiveobj.Amount=amount
            expense_archiveobj.archivedyear = archived_year
            expense_archiveobj.archivedmonth = archived_month
            expense_archiveobj.save()
            #deleting all the expense from reports table
        all_expenses.delete()
        message="The Monthly Seeds Report has been Achived"
        context={'message':message}
        return render(request, 'Seeds/Seedsindex.html', context)
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    yr = datetime.now().year
    years = [yr,2019,2018]
    today = timezone.now()
    current_month = today.strftime('%B')
    total = Seeds.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    mth = datetime.now().month
    items =Seeds.objects.all()
    day=datetime.now()
    context = {'day':day,'yr':yr,'total_amount':total_amount,'items': items,'months':months,'years':years,'current_month':current_month
    }
    return render(request, 'Seeds/Seedsindex.html', context)

@login_required
def seedsarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = SeedsReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September', 'October', 'November', 'December']
        yr = datetime.now().year
        years = [yr,2019,2018]
        seeds = SeedsReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'archived_reports': archived_reports,'months': months,'years': years,'seeds': seeds,
                   'total_amount': total_amount,'today': today,'report_year': report_year,'report_month': report_month
                   }
        return render(request, "Seeds/seedsarchive.html", context)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'November', 'December']
    yr = datetime.now().year
    years = [yr,2019,2018]
    seeds = SeedsReportArchive.objects.all()
    context = {'months': months,'years': years,'seeds': seeds}
    return render(request, "Seeds/seedsarchive.html", context)

def edit_seed(request, pk):
    item = get_object_or_404(Seeds, pk=pk)
    if request.method == "POST":
        form = SeedsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Seeds-report')
    else:
        today = timezone.now()
        month = today.strftime('%B')
        form = SeedsForm(instance=item)        
        context={'form':form, 'month':month}
    return render(request, 'Seeds/edit_seeds.html', context)

class seed_offering_receipt(View):
    def get(self, request, pk):
        seeds= get_object_or_404(Seeds,pk=pk)
        today = timezone.now()
        context = { 'today': today,'seeds': seeds,'request': request,}
        return Render.render('Seeds/seed_offerings_receipt.html', context)


     ###################################################
              #        DONATIONS MODULE        #
     ###################################################
@login_required
def record_donations(request):
    if request.method=="POST":
        form=DonationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donations-report')
    else:
        form=DonationsForm()
        today = timezone.now()
        month = today.strftime('%B')
        context={'form':form, 'month':month}
        return render(request, 'Donations/record_donations.html',context)
@login_required
def donations_report(request):
    if request.method=='POST':
        archived_year=request.POST['archived_year']
        archived_month = request.POST['archived_month']
        all_expenses = Donations.objects.all()
        for expense in all_expenses:
            date=expense.Date
            amount=expense.Amount
            name = expense.Donated_By
            reason = expense.Reason
            expense_archiveobj=DonationsReportArchive()
            expense_archiveobj.Name = name
            expense_archiveobj.Date=date
            expense_archiveobj.Reason=reason
            expense_archiveobj.Amount=amount
            expense_archiveobj.archivedyear= archived_year
            expense_archiveobj.archivedmonth =archived_month
            expense_archiveobj.save()
        all_expenses.delete()
        message="The Monthly Donations report has been Achived"
        context={'message':message}
        return render(request, 'Donations/donationsindex.html', context)
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August','September', 'October', 'November','December']
    yr = datetime.now().year
    years = [yr,2019,2018]
    total = Donations.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    mth = datetime.now().month
    day=datetime.now()
    items =Donations.objects.filter(Date__month=mth)
    context = {'day':day,'total_amount':total_amount,'items': items,'months':months,'years':years,}
    return render(request, 'Donations/donationsindex.html', context)

def edit_donation(request, pk):
    item = get_object_or_404(Donations, pk=pk)
    if request.method == "POST":
        form = DonationsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('donations-report')
    else:
        today = timezone.now()
        month = today.strftime('%B')
        form = DonationsForm(instance=item)        
        context={'form':form, 'month':month}
    return render(request, 'Donations/edit_donations.html', context)
@login_required
def donationsarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = DonationsReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September', 'October', 'November', 'December']
        yr = datetime.now().year
        years = [yr,2019,2018,2017]
        donations = DonationsReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'archived_reports': archived_reports,'months': months,'years': years,'expenses': donations,
                   'total_amount': total_amount,'today': today,'report_year': report_year,'report_month': report_month}
        return render(request, "Donations/donationssarchive.html", context)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'November', 'December']
    yr = datetime.now().year
    years = [yr,2019,2018,2017]
    donations = DonationsReportArchive.objects.all()
    context = {'months': months,'years': years,'donations': donations}
    return render(request, "Donations/donationssarchive.html", context)


     ###################################################
    #               THANKS GIVING MODULE                #
     ###################################################
@login_required
def record_thanks_giving(request):
    if request.method=="POST":
        form=ThanksGivingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks-giving-report')
    else:
        form=ThanksGivingForm()
        today = timezone.now()
        month = today.strftime('%B')
        context={'form':form, 'month':month}
        return render(request, 'ThanksGiving/record_thanks_giving.html',context)
@login_required
def thanks_giving_report(request):
    if request.method=='POST':
        archived_year=request.POST['archived_year']
        archived_month = request.POST['archived_month']
        all_expenses = ThanksGiving.objects.all()
        for expense in all_expenses:
            date=expense.Date
            amount=expense.Amount
            name = expense.Thanks_Giving_By
            reason = expense.Service
            expense_archiveobj=ThanksGivingReportArchive()
            expense_archiveobj.Thanks_Giving_By = name
            expense_archiveobj.Date=date
            expense_archiveobj.Service=reason
            expense_archiveobj.Amount=amount
            expense_archiveobj.archivedyear= archived_year
            expense_archiveobj.archivedmonth =archived_month
            expense_archiveobj.save()
        all_expenses.delete()
        message="The Monthly Thanks Giving report has been Achived"
        context={'message':message}
        return render(request, 'ThanksGiving/thanksgivingindex.html', context)
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August','September', 'October', 'November','December']
    yr = datetime.now().year
    years = [yr,2019,2018]
    total = ThanksGiving.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    mth = datetime.now().month
    day=datetime.now()
    items =ThanksGiving.objects.filter(Date__month=mth)
    context = {'day':day,'total_amount':total_amount,'items': items,'months':months,'years':years,}
    return render(request, 'ThanksGiving/thanksgivingindex.html', context)

def edit_thanks_giving(request, pk):
    item = get_object_or_404(ThanksGiving, pk=pk)
    if request.method == "POST":
        form = ThanksGivingForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('thanks-giving-report')
    else:
        today = timezone.now()
        month = today.strftime('%B')
        form = ThanksGivingForm(instance=item)        
        context={'form':form, 'month':month}
    return render(request, 'ThanksGiving/edit_thanks_giving.html', context)
@login_required
def thanksgivingarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = ThanksGivingReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September', 'October', 'November', 'December']
        yr = datetime.now().year
        years = [yr,2019,2018,2017]
        thanksgiving = ThanksGivingReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'archived_reports': archived_reports,'months': months,'years': years,'expenses': thanksgiving,
                   'total_amount': total_amount,'today': today,'report_year': report_year,'report_month': report_month}
        return render(request, "ThanksGiving/thanksgivingarchivessearch.html", context)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'November', 'December']
    yr = datetime.now().year
    years = [yr,2019,2018,2017]
    thanksgiving = ThanksGivingReportArchive.objects.all()
    context = {'months': months,'years': years,'thanksgiving': thanksgiving}
    return render(request, "ThanksGiving/thanksgivingarchivessearch.html", context)


     ###################################################
    #                  TITHES MODULE        #
     ###################################################
@login_required
def Enter_Tithes(request):
    if request.method=="POST":
        form=TithesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Tithesreport')
    else:
        form=TithesForm()
        today = timezone.now()
        month = today.strftime('%B')
        context={'form':form, 'month':month}
        return render(request, 'Tithes/record_tithes.html',context)

def edit_tithes(request, pk):
    item = get_object_or_404(Tithes, pk=pk)
    if request.method == "POST":
        form = TithesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Tithesreport')
    else:
        today = timezone.now()
        month = today.strftime('%B')
        form = TithesForm(instance=item)        
        context={'form':form, 'month':month}
    return render(request, 'Tithes/record_tithes.html', context)

class tithespdf(View):
    def get(self, request):
        current_month = datetime.now().month
        tithes = Tithes.objects.filter(Date__month=current_month).order_by('-Date')
        today = timezone.now()
        month = today.strftime('%B')
        totalexpense = 0
        for instance in tithes:
            totalexpense += instance.Amount
        context = {

            'month': month,
            'today': today,
            'tithes': tithes,
            'request': request,
            'totalexpense': totalexpense,
        }
        return Render.render('Tithes/tithespdf.html', context)

class tithesreceipt(View):
    def get(self, request, pk):
        tithes= get_object_or_404(Tithes,pk=pk)
        today = timezone.now()
        context = {
            'today': today,
            'tithes': tithes,
            'request': request,
        }
        return Render.render('Tithes/tithesreceipt.html', context)
@login_required
def Tithesreport (request):
    if request.method=='POST':
        archived_year=request.POST['archived_year']
        archived_month = request.POST['archived_month']
        #all the available expense in the expenses table
        all_expenses = Tithes.objects.all()
        for expense in all_expenses:
            date=expense.Date
            name=expense.Tithe_Made_By
            amount=expense.Amount
            # the expense archive object
            expense_archiveobj=TithesReportArchive()
            #attached values to expense_archiveobj
            expense_archiveobj.Date=date
            expense_archiveobj.Tithe_Made_By = name
            expense_archiveobj.Amount=amount
            expense_archiveobj.archivedyear = archived_year
            expense_archiveobj.archivedmonth = archived_month
            expense_archiveobj.save()
            #deleting all the expense from reports table
        all_expenses.delete()
        message="The Monthly Tithes Report has been Achived"
        context={'message':message}

        return render(request, 'Tithes/tithesindex.html', context)

    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    yr = datetime.now().year
    years = [yr,2019,2018]
    today = timezone.now()
    current_month = today.strftime('%B')
    total = Tithes.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    mth = datetime.now().month
    items =Tithes.objects.all()
    day=datetime.now()
    context = {'day':day,'yr':yr,'total_amount':total_amount,'items': items,'months':months,'years':years,'current_month':current_month
    }
    return render(request, 'Tithes/tithesindex.html', context)

@login_required
def tithesarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = TithesReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September', 'October', 'November', 'December']
        yr = datetime.now().year
        years = [yr,2019,2018]
        tithes = TithesReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'archived_reports': archived_reports,'months': months,'years': years,'expenses': tithes,
                   'total_amount': total_amount,'today': today,'report_year': report_year,'report_month': report_month
                   }
        return render(request, "Tithes/tithesarchive.html", context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'November', 'December']
    yr = datetime.now().year
    years = [yr,2019,2018]
    tithes = TithesReportArchive.objects.all()
    context = {'months': months,
               'years': years,
               'tithes': tithes}
    return render(request, "Tithes/tithesarchive.html", context)

class tithesarchivepdf(View):
    def get(self, request, report_month, report_year):
        archived_tithes = TithesReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        today = timezone.now()
        total = archived_tithes.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        tithescontext = {
            'today': today,
            'total_amount': total_amount,
            'request': request,
            'archived_tithes': archived_tithes,
        }
        return Render.render('Tithes/tithesarchivepdf.html', tithescontext)

                #########################################
                #          ALLOWANCES MODULE            #
                #########################################

def give_allowance(request):
    if request.method=="POST":
        form=AllowanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allowancereport')
    else:
        today = timezone.now()
        current_month = today.strftime('%B')
        form = AllowanceForm()
        context={'form': form, 'current_month': current_month}
        return render(request, 'Allowances/record_new_allowance.html',context)

def edit_allowance(request, pk):
    item = get_object_or_404(Allowance, pk=pk)
    if request.method == "POST":
        form = AllowanceForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('give-allowance')
    else:
        form = AllowanceForm(instance=item)
    return render(request, 'Allowances/record_new_allowance.html', {'form': form})

class allowancereceipt(View):
    def get(self, request, pk):
        Allowance= get_object_or_404(Allowance,pk=pk)
        today = timezone.now()
        Allowancecontext = {
            'today': today,
            'Allowance': Allowance,
            'request': request,
        }
        return Render.render('Allowance/allowancereceipt.html', Allowancecontext)

#Printing allowances Report
class allowancespdf(View):
    def get(self, request):
        current_month = datetime.now().month
        allowances = Allowance.objects.filter(Date__month=current_month).order_by('-Date')
        today = timezone.now()
        month = today.strftime('%B')
        totalAllowance = 0
        for instance in allowances:
            totalAllowance += instance.Amount
        Allowancecontext ={
            'month': month,
            'today':today,
            'allowances':allowances,
            'request': request,
            'totalAllowance': totalAllowance,
        }
        return Render.render('Allowances/allowancespdf.html',Allowancecontext)
# Printing allowances archived Report
class allowancearchivepdf(View):
    def get(self, request, report_month, report_year):
        archived_Allowance = AllowanceReportArchive.objects.filter(month=report_month, year=report_year)
        today = timezone.now()
        total = archived_Allowance.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        Allowancecontext = {
            'today': today,
            'total_amount': total_amount,
            'request': request,
            'archived_Allowance': archived_Allowance,
        }
        return Render.render('Allowances/allowancearchivepdf.html', Allowancecontext)

@login_required
def allowancereport(request):
    if request.method=='POST':
        archived_year=request.POST['archived_year']
        archived_month = request.POST['archived_month']
        #all the available expense in the expenses table
        all_expenses = Allowance.objects.all()
        for expense in all_expenses:
            date=expense.Date
            Manth = expense.Month
            amount=expense.Amount
            name = expense.Name
            # the expense archive object
            expense_archiveobj=AllowanceReportArchive()
            #attached values to expense_archiveobj
            expense_archiveobj.Staff = name
            expense_archiveobj.Date=date
            expense_archiveobj.Month=Manth
            expense_archiveobj.Amount=amount
            expense_archiveobj.archivedyear= archived_year
            expense_archiveobj.archivedmonth =archived_month
            expense_archiveobj.save()
        #deleting all the expense from reports table
        all_expenses.delete()
        message="The Monthly Allowances report has been Achived"
        context={'message':message}
        return render(request, 'Allowances/allowanceindex.html', context)
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August','September', 'October', 'November','December']
    yr = datetime.now().year
    years = [yr,2019,2018]
    total = Allowance.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    mth = datetime.now().month
    day=datetime.now()
    items =Allowance.objects.filter(Date__month=mth)
    context = {'day':day,
        'total_amount':total_amount,
        'items': items,
        'months':months,
        'years':years,
    }
    return render(request, 'Allowances/allowanceindex.html', context)

@login_required
def allowancearchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = AllowanceReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August','September', 'October',  'November','December']
        yr = datetime.now().year
        years = [yr,2019,2018]

        Allowance = AllowanceReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]

        context = {'archived_reports': archived_reports,
                   'months': months,
                   'years': years,
                   'expenses':Allowance,
                   'total_amount': total_amount,
                   'today': today,
                   'report_year': report_year,
                   'report_month': report_month
                   }
        return render(request, "Allowances/allowancearchive.html", context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September','October',  'November', 'December']
    yr = datetime.now().year
    years = [yr,2019,2018]

    Allowance=AllowanceReportArchive.objects.all()

    context = {'months': months,
               'years': years,
               'Allowance': Allowance}
    return render(request, "Allowances/allowancearchive.html", context)

def allowancearchive(request):
    Allowancearchived = AllowanceReportArchive.objects.all().order_by('-Date')
    total = AllowanceReportArchive.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    context = {
        'total_amount':total_amount,
        'Allowancearchived': Allowancearchived
               }
    return render(request, 'Allowances/allowancearchive.html', context)
def delete_allowance(request,pk):
    items= Spend.objects.filter(id=pk).delete()
    context = { 'items':items}
    return render(request, 'Allowances/allowanceindex.html', context)

#CURRENT MONTH BALANCE SHEET
def total_monthly_incomes(request):
    current_month = datetime.now().month
    total_current_offerings = Offerings.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Total_Offering"))
    if (total_current_offerings['totals']):
        total_current_offerings["totals"]
        offerings=total_current_offerings["totals"]
    else:
        0

    total_current_tithes = Tithes.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_current_tithes['totals']):
        total_current_tithes["totals"]
        tithes=total_current_tithes["totals"]
    else:
        0

    total_current_pledges = PaidPledges.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount_Paid"))
    if (total_current_pledges['totals']):
        total_current_pledges["totals"]
        pledges=total_current_pledges["totals"]
    else:
        0
    total_main_expenses = Spend.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_main_expenses['totals']):
        total_main_expenses["totals"]
        expenses=total_main_expenses["totals"]
    else:
        0

    total_allowances = Allowance.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_allowances['totals']):
        total_allowances["totals"]
        allowances=total_allowances["totals"]
    else:
        0
    total_monthly_incomes =  int(total_current_tithes["totals"]) + int(total_current_offerings["totals"])+ int(total_current_pledges["totals"])
    total_monthly_expenditure =  int(total_allowances["totals"]) + int(total_main_expenses["totals"])
    net_income = total_monthly_incomes - total_monthly_expenditure
    today = timezone.now()
    month = today.strftime('%B')
    context={'total_monthly_incomes':total_monthly_incomes,'total_monthly_expenditure':total_monthly_expenditure, 'month': month,
    'allowances':allowances, 'expenses':expenses,'tithes':tithes, 'offerings':offerings, 'pledges':pledges, 'net_income':net_income}
    return render(request, 'total_monthly_incomes.html', context)
@login_required
def enter_expenditure(request):
    if request.method=="POST":
        form=SpendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenditurereport')
    else:
        form=SpendForm()
        items = Spend.objects.all()
        context = {'items': items, 'form': form, }
        return render(request, 'Expenses/pay_expenditure.html',context)

@login_required
def enter_general_expenses(request):
    if request.method=="POST":
        form=GeneralExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('general-expenses-report')
    else:
        form=GeneralExpensesForm()
        items = GeneralExpenses.objects.all()
        context = {'items': items, 'form': form, }
        return render(request, 'Expenses/pay_generalexpenditure.html',context)        
@login_required
def enter_sundryexpense(request):
    if request.method == "POST":
        form = SundryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sundryreport')
    else:
        today = timezone.now()
        current_month = today.strftime('%B')
        form = SundryForm()
        context={'form': form, 'current_month': current_month}
        return render(request, 'Expenses/record_petty_expenses.html', context )
 #####################################################################
# EDITING, DELETING AND PRINTING OF RECEIPT OF EACH TRANSACTION MADE  #
 #####################################################################

def edit_payment(request, pk):
    item = get_object_or_404(Spend, pk=pk)
    if request.method == "POST":
        form = SpendForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('expenditurereport')
    else:
        form = SpendForm(instance=item)
    return render(request, 'Expenses/pay_expenditure.html', {'form': form})

def delete_payment(request,pk):
    items= Spend.objects.filter(id=pk).delete()
    context = { 'items':items}
    return render(request, 'Expenses/expenditureindex.html', context)
def edit_sundry(request, pk):
    item = get_object_or_404(Sundry, pk=pk)
    if request.method == "POST":
        form = SundryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('enter_sundryexpense')
    else:
        form = SundryForm(instance=item)
    return render(request, 'add_new.html', {'form': form, })

def delete_sundry(request, pk):
    items = Sundry.objects.filter(id=pk).delete()
    context = {'items': items}
    return render(request, 'Expenses/sundryindex.html', context)

       ####################################################
      #        GENERATING REPORTS IN FORM OF PDFS         #
      ####################################################

#Printing Expenditure Report
class expenditurepdf(View):
    def get(self, request):
        current_month = datetime.now().month
        expense = Spend.objects.filter(Date__month=current_month).order_by('-Date')

        today = timezone.now()
        month = today.strftime('%B')
        totalexpense = 0
        for instance in expense:
            totalexpense += instance.Amount
        expensecontext ={

            'month': month,
            'today':today,
            'expense':expense,
            'request': request,
            'totalexpense': totalexpense,
        }
        return Render.render('Expenses/expenditurepdf.html',expensecontext)


#Printing Sundry Expenses Report
class sundrypdf(View):
    def get(self, request):
        current_month = datetime.now().month
        sundry = Sundry.objects.all()
        today = timezone.now()
        month = today.strftime('%B')
        totalsundry = 0
        for instance in sundry:
            totalsundry += instance.Amount
        sundrycontext ={
            ''
            'month': month,
            'today':today,
            'sundry':sundry,
            'request': request,
            'totalsundry': totalsundry,
        }
        return Render.render('Expenses/sundrypdf.html',sundrycontext)



        ####################################################
        #        ARCHIVING OF THE MONTHLY REPORTS           #
        ####################################################



def expenditurearchive(request):
    expensesarchived = ExpensesReportArchive.objects.all().order_by('-Date')
    total = AllowanceReportArchive.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    context = {
        'total_amount':total_amount,
        'expensesarchived':expensesarchived
    }
    return render(request, 'Expenses/expenditurearchive.html', context)


        # calculating totals in sundryexpense report
def sundryarchive(request):
    sundryarchived = SundryReportArchive.objects.all().order_by('-Date')
    total = SundryReportArchive.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    context = {
        'total_amount':total_amount,
        'sundryarchived': sundryarchived
               }
    return render(request, 'Expenses/sundryarchive.html', context)





 ####################################################
#       PRINTING THE RECEIPTS                        #
 ####################################################

class expensereceipt(View):
    def get(self, request, pk):
        expense = get_object_or_404(Spend,pk=pk)
        today = timezone.now()
        expensecontext = {
            'today': today,
            'expense': expense,
            'request': request,
        }
        return Render.render('Expenses/expensereceipt.html', expensecontext)
class sundryreceipt(View):
    def get(self, request, pk):
        sundry = get_object_or_404(Sundry,pk=pk)
        today = timezone.now()
        sundrycontext = {
            'today': today,
            'sundry': sundry,
            'request': request,
        }
        return Render.render('Expenses/sundryreceipt.html', sundrycontext)


    ############################################################
   # SUBMISSION OF MONTHLY REPORTS TO BE ARCHIVED              #
    ############################################################

#####################
# EXPENSES ARCHIVING#
#####################
@login_required
def expenditurereport (request):
    if request.method=='POST':
        archived_year=request.POST['archived_year']
        archived_month = request.POST['archived_month']

        #all the available expense in the expenses table
        all_expenses = Spend.objects.all()

        for expense in all_expenses:
            date=expense.Date
            amount=expense.Amount
            reason=expense.Reason_For_Payment
            name=expense.Payment_Made_To

            # the expense archive object
            expense_archiveobj=ExpensesReportArchive()

            #attached values to expense_archiveobj
            expense_archiveobj.Name=name
            expense_archiveobj.Date=date
            expense_archiveobj.Amount=amount
            expense_archiveobj.Reason=reason
            expense_archiveobj.year=archived_year
            expense_archiveobj.month=archived_month

            expense_archiveobj.save()

        #deleting all the expense from reports table


        #paid = Spend.objects.all().aggregate(Sum('Amount'))
        all_expenses.delete()

        message="The Monthly Main Expenses Report has been Achived"
        context={
                 'message':message,
                 }

        return render(request, 'Expenses/expenditureindex.html', context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September',
              'October', 'November',
              'December']
    yr = datetime.now().year
    years = [yr,2019,2018]
    mth = datetime.now().month
    items =Spend.objects.filter(Date__month=mth)
    today = timezone.now()
    day=datetime.now()
    current_month = today.strftime('%B')
    total = Spend.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    context = {'day':day,
         'current_month':current_month,
         'total_amount':total_amount,
        'items': items,
        'months':months,
        'years':years,


    }
    return render(request, 'Expenses/expenditureindex.html', context)

#GENERAL EXPENSES REPORT    
@login_required
def general_expenses_report (request):
    if request.method=='POST':
        archived_year=request.POST['archived_year']
        archived_month = request.POST['archived_month']
        all_expenses = GeneralExpenses.objects.all()
        for expense in all_expenses:
            date=expense.Date
            amount=expense.Amount
            reason=expense.Expense_Reason
            name=expense.Payment_Made_To
            expense_archiveobj=GeneralExpensesReportArchive()
            expense_archiveobj.Name=name
            expense_archiveobj.Date=date
            expense_archiveobj.Amount=amount
            expense_archiveobj.Reason=reason
            expense_archiveobj.year=archived_year
            expense_archiveobj.month=archived_month
            expense_archiveobj.save()
        all_expenses.delete()
        message="The Monthly General Expenses Report has been Achived"
        context={'message':message,}
        return render(request, 'Expenses/generalexpenditureindex.html', context)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September',
              'October', 'November','December']
    yr = datetime.now().year
    years = [yr,2019,2018]
    mth = datetime.now().month
    day=datetime.now()
    items =GeneralExpenses.objects.filter(Date__month=mth)
    today = timezone.now()
    current_month = today.strftime('%B')
    total = GeneralExpenses.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    context = {'day':day, 'current_month':current_month, 'total_amount':total_amount,'items': items,'months':months,
        'years':years,}
    return render(request, 'Expenses/generalexpenditureindex.html', context)



@login_required
def sundryreport (request):
    if request.method=='POST':
        archived_year=request.POST['archived_year']
        archived_month = request.POST['archived_month']
        #all the available expense in the expenses table
        all_expenses = Sundry.objects.all()
        for expense in all_expenses:
            date=expense.Date
            amount=expense.Amount
            reason=expense.Reason_For_Payment
            name=expense.Payment_Made_To

            # the expense archive object
            expense_archiveobj=SundryReportArchive()

            #attached values to expense_archiveobj
            expense_archiveobj.Name=name
            expense_archiveobj.Date=date
            expense_archiveobj.Amount=amount
            expense_archiveobj.Reason=reason
            expense_archiveobj.year=archived_year
            expense_archiveobj.month=archived_month

            expense_archiveobj.save()

        #deleting all the expense from reports table
        all_expenses.delete()

        message="The expenses report has been made"
        context={'message':message}

        return render(request, 'Expenses/sundryindex.html', context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
              'October', 'November',
              'December']
    yr = datetime.now().year
    years = [yr,2019,2018]

    total = Sundry.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    mth = datetime.now().month
    day=datetime.now()
    items =Sundry.objects.filter(Date__month=mth)
    context = {'day':day,
        'total_amount':total_amount,
        'items': items,
        'months':months,
        'years':years,
    }
    return render(request, 'Expenses/sundryindex.html', context)
@login_required
def generalexpensesarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'August', 'September', 'October', 'November','December']
        yr = datetime.now().year
        years = [yr,2019,2018]
        today = timezone.now()
        archived_reports = GeneralExpensesReportArchive.objects.filter(month=report_month, year=report_year)
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'archived_reports':archived_reports,
                   'months': months,
                   'years': years,
                   'total_amount': total_amount,
                   'today': today,
                   'report_year': report_year,
                   'report_month': report_month
                   }
        return render(request, "Expenses/generalexpenditurearchive.html", context)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August','September','October', 'November', 'November', 'December']
    yr = datetime.now().year
    years = [yr,2019,2018]
    expenses=GeneralExpensesReportArchive.objects.all()
    context = {'months': months,
               'years': years,
               'expenses': expenses}
    return render(request, "Expenses/generalexpenditurearchive.html", context)

# searching for the archives
@login_required
def expensesarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'August', 'September', 'October', 'November','December']
        yr = datetime.now().year
        years = [yr,2019,2018]
        today = timezone.now()
        archived_reports = ExpensesReportArchive.objects.filter(month=report_month, year=report_year)
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'archived_reports':archived_reports,
                   'months': months,
                   'years': years,
                   'total_amount': total_amount,
                   'today': today,
                   'report_year': report_year,
                   'report_month': report_month
                   }
        return render(request, "Expenses/expenditurearchive.html", context)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August','September','October', 'November', 'November', 'December']
    yr = datetime.now().year
    years = [yr,yr-1,yr-2,yr-3,yr-4,2018]
    expenses=ExpensesReportArchive.objects.all()
    context = {'months': months,
               'years': years,
               'expenses': expenses}
    return render(request, "Expenses/expenditurearchive.html", context)

@login_required
def sundryarchivessearch(request):
    yrs = SundryReportArchive.objects.all().order_by('-year')
    archived_years=[]
    for i in yrs:
        x=i.year
        archived_years.append(x)
    years=archived_years
    #remove duplicate years in the search dropdown menu for years field        
    def remove_dup(a):
        i = 0
        while i < len(a):
            j = i + 1
            while j < len(a):
                if a[i] == a[j]:
                    del a[j]
                else:
                    j += 1
            i += 1
    s = years
    remove_dup(s) 
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = SundryReportArchive.objects.filter(month=report_month, year=report_year)
        months = ['January','February','March', 'April','May','June','July','August','September', 'October', 'November','December']
        sundry = SundryReportArchive.objects.all()
        today = timezone.now()
        day=datetime.now()
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'day':day, 'archived_reports': archived_reports,'months': months,'years': years,'expenses':sundry,
                   'total_amount': total_amount,'today': today,'report_year': report_year,'report_month': report_month
                   }
        return render(request, "Expenses/sundryarchive.html", context)
    months = ['January','February','March','April','May','June','July','August','September','October', 'November', 'December']
    yr = datetime.now().year
    sundry=SundryReportArchive.objects.all()
    context = {'months': months,'years': years,'sundry': sundry}
    return render(request, "Expenses/sundryarchive.html", context)

# Printing Expenditure archived Report
class expenditurearchivepdf(View):
    def get(self, request, report_month, report_year):
        archived_expenses = ExpensesReportArchive.objects.filter(month=report_month, year=report_year)
        today = timezone.now()
        month = today.strftime('%B')
        total = archived_expenses.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        expensecontext = {
            'today': today,
            'total_amount': total_amount,
            'request': request,
            'archived_expenses': archived_expenses,
            'report_year': report_year,
            'report_month': report_month
        }
        return Render.render('Expenses/expenditurearchivepdf.html', expensecontext)

# Printing Sundry Expenses archived Report
class sundryarchivepdf(View):
    def get(self, request, report_month, report_year):
        archived_sundry = SundryReportArchive.objects.filter(month=report_month, year=report_year)
        today = timezone.now()
        month = today.strftime('%B')
        total = archived_sundry.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        sundrycontext = {
            'today': today,
            'total_amount': total_amount,
            'request': request,
            'archived_sundry': archived_sundry,
        }
        return Render.render('Expenses/sundryarchivepdf.html', sundrycontext)
###############################
      # PLEDGES MODULE#
###############################

@login_required
def Enter_Pledges(request):
    if request.method=="POST":
        form=PledgesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Pledgesreport')
    else:
        form=PledgesForm()
        return render(request, 'Pledges/enter_pledge.html',{'form':form})
@login_required
def add_Pledge_Items(request):
    if request.method=="POST":
        form=PledgeItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-of-pledge-items')
    else:
        form=PledgeItemsForm()
        return render(request, 'Pledges/add_Pledge_Item.html',{'form':form})
@login_required
def list_of_pledge_items(request):
    items = PledgeItem.objects.all().order_by('-id')
    context ={'items': items}
    return render(request, 'Pledges/list_of_pledge_items.html',context)

def edit_pledge_item(request, pk):
    item = get_object_or_404(PledgeItem, pk=pk)
    if request.method == "POST":
        form = PledgeItemsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list-of-pledge-items')
    else:
        messages='Pledge Item has been Updated'
        form = PledgeItemsForm(instance=item)
    return render(request, 'Pledges/edit_pledge_item.html', {'form': form}, {'messages': messages})

def delete_pledge_item(request, pk):
    item= get_object_or_404(PledgeItem, id=pk)
    if request.method == "GET":
        item.delete()
        messages.success(request, "Pledge Item successfully deleted!")
        return redirect("list-of-pledge-items")      
@login_required
def pledge_view(request, pledge_pk):
    pledge = get_object_or_404(Pledges, pk=pledge_pk)
    if request.method == 'POST':
        form = PledgesForm(request.POST, instance=pledge)
    else:
        form = PledgesForm(instance=pledge)
    context = {'form': form}
    return render(request, 'Pledges/pledge_view.html', context)

#function that invokes the template for inputing the date and pledge amount paid by the member
@login_required
def paying_pledges(request, pk):
    items = get_object_or_404(Pledges, id=pk)
    if request.method == "POST":
        form = UpdatePledgesForm(request.POST, request.FILES, instance=items)
        if form.is_valid():
            form.save()
            return redirect('Pledgesreport')
    else:
        form = UpdatePledgesForm(instance=items)
        retrieving_id=Pledges.objects.filter(id=pk)
        context={'form':form, 'retrieving_id': retrieving_id}
        return render(request, 'Pledges/paying_pledges_update.html', context)

#processing the pledge payment that the member has made
@login_required
def member_pledges_paid(request):
    if request.method == "POST":
        form =  PaidPledgesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Pledgesreport')
        else:
            form = PaidPledgesForm()
            context={'form':form}
            return render(request, 'Pledges/paying_pledges_update.html', context)

def archived_pledge_debts(request):
    debts=PledgesReportArchive.objects.filter(Q(Status='UNPAID') | Q(Status='PARTIAL'))
    #PledgesReportArchive.objects.filter(Status='PAID').delete()
    context={'debts':debts}
    return render(request, "Pledges/archived_pledge_debts.html", context)

def settle_pledge_debt(request, pk):
    items = get_object_or_404(PledgesReportArchive, Pledge_Id=pk)
    if request.method == "POST":
        form = PledgesReportArchiveForm(request.POST, request.FILES, instance=items)
        if form.is_valid():
            form.save()
            return redirect('pledges-paid-list')
    else:
        form = PledgesReportArchiveForm(instance=items)
        retrieving_id=PledgesReportArchive.objects.filter(Pledge_Id=pk)
        context={'form':form,'retrieving_id':retrieving_id}
        return render(request, 'Pledges/settle_pledge_debt.html', context)

def member_settle_pledge_debt(request):
    if request.method == "POST":
        form =  PaidPledgesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('archived-pledge-debts')
        else:
            form = PaidPledgesForm()
            message="Pledge amount updated saccessfully!"
            context={'form':form,'message':message}
            return render(request, 'Pledges/settle_pledge_debt.html', context)

def delete_bad_debt(request, pk):
    retrieving_id=PledgesReportArchive.objects.filter(Pledge_Id=pk)
    retrieving_id.delete()
    message="Bad debt was removed sucessfully!"
    context={'message':message}
    return render(request, "Pledges/delete_pledge_bad_debt.html", context)

@login_required
def pledges_paid_list(request):
    context = {}
    today = timezone.now()
    month = today.strftime('%B')
    context['month']=month
    current_month = datetime.now().month
    lists = PaidPledges.objects.filter(Date__month=current_month).order_by('-id')
    context['lists']=lists
    return render(request, 'Pledges/pledges_paid_list.html',context)

def edit_pledges(request, pk):
    item = get_object_or_404(Pledges, pk=pk)
    if request.method == "POST":
        form = PledgesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Pledgesreport')
    else:
        form = PledgesForm(instance=item)
    return render(request, 'Pledges/enter_pledge.html', {'form': form})

class pledgespdf(View):
    def get(self, request):
        current_month = datetime.now().month
        ple = Pledges.objects.all().order_by('-Date')
        today = timezone.now()
        month = today.strftime('%B')
        totalexpense = 0
        for instance in ple:
            totalexpense += instance.Amount_Pledged
        context = {

            'month': month,
            'today': today,
            'ple': ple,
            'request': request,
            'totalexpense': totalexpense,
        }
        return Render.render('Pledges/pledgespdf.html', context)

class pledgesreceipt(View):
    def get(self, request, pk):
        pledges= get_object_or_404(Pledges,pk=pk)
        today = timezone.now()
        context = {
            'today': today,
            'pledges': pledges,
            'request': request,
        }
        return Render.render('Pledges/pledgesreceipt.html', context)

@login_required
def Pledgesreport(request):
    if request.method=='POST':
        archived_year=request.POST['archived_year']
        archived_month = request.POST['archived_month']
        all_expenses = Pledges.objects.all()
        for expense in all_expenses:
            pledge_id=expense.id
            status = expense.Status
            date=expense.Date
            name=expense.Pledge_Made_By
            reason=expense.Reason
            pledged_amount= expense.Amount_Pledged
            expense_archiveobj=PledgesReportArchive()
            expense_archiveobj.Pledge_Id=pledge_id
            expense_archiveobj.Status=status
            expense_archiveobj.Date=date
            expense_archiveobj.Pledge_Made_By = name
            expense_archiveobj.Reason = reason
            expense_archiveobj.Pledged_Amount=pledged_amount
            expense_archiveobj.archivedyear= archived_year
            expense_archiveobj.archivedmonth =archived_month
            expense_archiveobj.save()
        all_expenses.delete()
        message="The Monthly Pledges Report has been Achived"
        context={'message':message}
        return render(request, 'Pledges/pledgesindex.html', context)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'August', 'September', 'October', 'November','December']
    yr = datetime.now().year
    years = [yr,2019,2018]
    total = Pledges.objects.aggregate(totals=models.Sum("Amount_Pledged"))
    total_amount = total["totals"]
    today = timezone.now()
    day=datetime.now()
    current_month = today.strftime('%B')
    mth = datetime.now().month
    items =Pledges.objects.filter(Date__month=mth).order_by('-Date')
    context = {'day':day,
        'total_amount':total_amount,
        'items':items,
        'months':months,
        'years':years,
        'current_month':current_month
    }
    return render(request, 'Pledges/pledgesindex.html', context)

@login_required
def pledgesarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = PledgesReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August','September', 'October', 'November', 'December']
        yr = datetime.now().year
        years = [yr,2019,2018]#getting years automatically without hard coding.... <<pending>>

        pledges = PledgesReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Pledged_Amount"))
        total_amount = total["totals"]
        context = {'archived_reports': archived_reports,'months': months,'years': years,'expenses': pledges,'total_amount': total_amount,'today': today,'report_year': report_year,
                   'report_month': report_month}
        return render(request, "Pledges/pledgesarchive.html", context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    yr = datetime.now().year
    years = [yr,2019,2018]
    pledges = PledgesReportArchive.objects.all()
    context = {'months': months, 'years': years, 'pledges': pledges}
    return render(request, "Pledges/pledgesarchive.html", context)

class pledgesarchivepdf(View):
    def get(self, request, report_month, report_year):
        archived_pledges = PledgesReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        today = timezone.now()
        total = archived_pledges.aggregate(totals=models.Sum("Pledged_Amount"))
        total_amount = total["totals"]
        pledgescontext = {
            'today': today,
            'total_amount': total_amount,
            'request': request,
            'archived_pledges': archived_pledges,
        }
        return Render.render('Pledges/pledgesarchivepdf.html', pledgescontext)
#airtime report
def airtime_data_report(request):
    mth = datetime.now().day
    today = datetime.now()
    get_airtime=Sundry.objects.filter(Reason_For_Payment='Airtime/Data', Date__day=mth)
    total = Sundry.objects.filter(Reason_For_Payment='Airtime/Data',Date__day=mth).aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    context={'get_airtime':get_airtime, 'total_amount':total_amount, 'today':today}
    return render(request,'Expenses/airtime_data_report.html', context)


  