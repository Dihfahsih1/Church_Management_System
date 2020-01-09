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

    return render(request,'index.html', context)


    ##################################
    #        Employee Module         #
    ##################################

def employee_register(request):
    if request.method=="POST":
        form=StaffDetailsForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form=StaffDetailsForm()
        return render(request, 'Employees/record_employee.html',{'form':form})

@login_required
def employee_list(request):
    employees = StaffDetails.objects.all().order_by('-id')
    context ={'employees': employees}
    return render(request, 'Employees/employee_list.html', context)

def paying_employees(request, pk):
    items = get_object_or_404(StaffDetails, id=pk)
    if request.method == "POST":
        form = StaffDetailsForm(request.POST, request.FILES, instance=items)
    else:
        form = StaffDetailsForm(instance=items)
        retrieve_employee_id = StaffDetails.objects.filter(id=pk)
        for i in retrieve_employee_id:
            print(i.Name)
        context = {'form': form, 'retrieve_employee_id': retrieve_employee_id}
        return render(request, 'Employees/pay_employee.html', context)

def paid_salary(request):
    if request.method == "GET":
        form = SalariesPaidForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee-list')
        else:
            form = SalariesPaidForm()
            context = {'form': form}
            return render(request, 'Employees/pay_employee.html', context)

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
    context ={'membership': membership}
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
        return render(request, 'enter_pledge.html',{'form':form})

@login_required
def pledge_view(request, pledge_pk):
    pledge = get_object_or_404(Pledges, pk=pledge_pk)
    if request.method == 'POST':
        form = PledgesForm(request.POST, instance=pledge)
    else:
        form = PledgesForm(instance=pledge)
    context = {'form': form}
    return render(request, 'pledge_view.html', context)

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
        return render(request, 'paying_pledges_update.html', context)

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
            return render(request, 'paying_pledges_update.html', context)

def archived_pledge_debts(request):
    debts=PledgesReportArchive.objects.filter(Q(Status='UNPAID') | Q(Status='PARTIAL'))
    #PledgesReportArchive.objects.filter(Status='PAID').delete()
    context={'debts':debts}
    return render(request, "archived_pledge_debts.html", context)

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
        return render(request, 'settle_pledge_debt.html', context)

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
            return render(request, 'settle_pledge_debt.html', context)

def delete_bad_debt(request, pk):
    retrieving_id=PledgesReportArchive.objects.filter(Pledge_Id=pk)
    retrieving_id.delete()
    message="Bad debt was removed sucessfully!"
    context={'message':message}
    return render(request, "delete_pledge_bad_debt.html", context)

@login_required
def pledges_paid_list(request):
    context = {}
    current_month = datetime.now().month
    lists = PaidPledges.objects.filter(Date__month=current_month)
    context['lists']=lists
    return render(request, 'pledges_paid_list.html',context)

#retrieve all archived pledge debts
#def archived_pledge_debts(request):
#    debts=PledgesReportArchive.objects.all()

def edit_pledges(request, pk):
    item = get_object_or_404(Pledges, pk=pk)
    if request.method == "POST":
        form = PledgesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Pledgesreport')
    else:
        form = PledgesForm(instance=item)
    return render(request, 'enter_pledge.html', {'form': form})

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
        return Render.render('pledgespdf.html', context)

class pledgesreceipt(View):
    def get(self, request, pk):
        pledges= get_object_or_404(Pledges,pk=pk)
        today = timezone.now()
        context = {
            'today': today,
            'pledges': pledges,
            'request': request,
        }
        return Render.render('pledgesreceipt.html', context)
 #####################
#  ARCHIVING PLEDGES  #
 #####################
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
        return render(request, 'pledgesindex.html', context)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'August', 'September', 'October', 'November','December']
    years = [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]
    total = Pledges.objects.aggregate(totals=models.Sum("Amount_Pledged"))
    total_amount = total["totals"]

    '''#calculate all pledges paid for the current month
    current_month = datetime.now().month
    results = PaidPledges.objects.filter(Date__month=current_month).aggregate(tot=models.Sum('Amount_Paid'))
    all_total_amount = results["tot"]

    #calculate the total balance
    total_balance=total_amount-all_total_amount'''
    items =Pledges.objects.all()
    context = {
        'total_amount':total_amount,
        'items':items,
        'months':months,
        'years':years,
    }
    return render(request, 'pledgesindex.html', context)

@login_required
def pledgesarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = PledgesReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August','September', 'October', 'November', 'December']
        years = [2019, 2020, 2021]#getting years automatically without hard coding.... <<pending>>

        pledges = PledgesReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Pledged_Amount"))
        total_amount = total["totals"]
        context = {'archived_reports': archived_reports,'months': months,'years': years,'expenses': pledges,'total_amount': total_amount,'today': today,'report_year': report_year,
                   'report_month': report_month}
        return render(request, "pledgesarchive.html", context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    years = [2019, 2020, 2021]
    pledges = PledgesReportArchive.objects.all()
    pledges.delete()
    context = {'months': months, 'years': years, 'pledges': pledges}
    return render(request, "pledgesarchive.html", context)

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
        return Render.render('pledgesarchivepdf.html', pledgescontext)


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

        return render(request, 'offeringsindex.html', context)

    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August','September', 'October', 'November','December']
    yr = datetime.now().year
    years = [yr,2019,2018]
    today = timezone.now()
    current_month = today.strftime('%B')
    total = Offerings.objects.aggregate(totals=models.Sum("Total_Offering"))
    total_amount = total["totals"]
    items =Offerings.objects.all()
    context = {
        'total_amount':total_amount,
        'items': items,
        'months':months,
        'current_month':current_month,
        'years':years,
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

    context = {'months': months,
               'years': years,
               'offerings': offerings}
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

     ###################################################
              #        TITHES MODULE        #
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
        return render(request, 'record_tithes.html',{'form':form})

def edit_tithes(request, pk):
    item = get_object_or_404(Tithes, pk=pk)
    if request.method == "POST":
        form = TithesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Tithesreport')
    else:
        form = TithesForm(instance=item)
    return render(request, 'record_tithes.html', {'form': form})

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
        return Render.render('tithespdf.html', context)

class tithesreceipt(View):
    def get(self, request, pk):
        tithes= get_object_or_404(Tithes,pk=pk)
        today = timezone.now()
        context = {
            'today': today,
            'tithes': tithes,
            'request': request,
        }
        return Render.render('tithesreceipt.html', context)
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

        return render(request, 'tithesindex.html', context)

    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August','September', 'October', 'November','December']
    yr = datetime.now().year
    years = [yr,2019,2018]
    today = timezone.now()
    current_month = today.strftime('%B')
    total = Tithes.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    items =Tithes.objects.all()
    context = {
        'total_amount':total_amount,
        'items': items,
        'months':months,
        'years':years,
        'current_month':current_month
    }
    return render(request, 'tithesindex.html', context)

@login_required
def tithesarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = TithesReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August','September', 'October', 'November', 'December']
        yr = datetime.now().year
        years = [yr,2019,2018]

        tithes = TithesReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'archived_reports': archived_reports,
                   'months': months,
                   'years': years,
                   'expenses': tithes,
                   'total_amount': total_amount,
                   'today': today,
                   'report_year': report_year,
                   'report_month': report_month
                   }
        return render(request, "tithesarchive.html", context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'November', 'December']
    yr = datetime.now().year
    years = [yr,2019,2018]

    tithes = TithesReportArchive.objects.all()
    context = {'months': months,
               'years': years,
               'tithes': tithes}
    return render(request, "tithesarchive.html", context)

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
        return Render.render('tithesarchivepdf.html', tithescontext)

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
        return Render.render('Allowance/llowancereceipt.html', Allowancecontext)

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
            expense_archiveobj.Name = name
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
    years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]
    total = Allowance.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    items =Allowance.objects.all()
    context = {
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
        years = [2018, 2019, 2020, 2021]

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
        return render(request, "Allowancearchive.html", context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September','October',  'November', 'December']
    years = [2018, 2019, 2020, 2021]

    Allowance=AllowanceReportArchive.objects.all()

    context = {'months': months,
               'years': years,
               'Allowance': Allowance}
    return render(request, "Allowancearchive.html", context)

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
            return redirect('enter_expenditure')
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
            reason=expense.ReasonForPayment
            name=expense.PaymentMadeTo

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
    years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]
    items =Spend.objects.all()
    today = timezone.now()
    current_month = today.strftime('%B')
    total = Spend.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    context = {
         'current_month':current_month,
         'total_amount':total_amount,
        'items': items,
        'months':months,
        'years':years,


    }
    return render(request, 'Expenses/expenditureindex.html', context)

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
            reason=expense.ReasonForPayment
            name=expense.PaymentMadeTo

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
    years = [2019, 2020, 2021]

    total = Sundry.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    items =Sundry.objects.all()
    context = {
        'total_amount':total_amount,
        'items': items,
        'months':months,
        'years':years,
    }
    return render(request, 'Expenses/sundryindex.html', context)


# searching for the archives
@login_required
def expensesarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'August', 'September', 'October', 'November','December']
        years = [2018, 2019, 2020, 2021]
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
    years = [2018, 2019, 2020, 2021]
    expenses=ExpensesReportArchive.objects.all()
    context = {'months': months,
               'years': years,
               'expenses': expenses}
    return render(request, "Expenses/expenditurearchive.html", context)

@login_required
def sundryarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = SundryReportArchive.objects.filter(month=report_month, year=report_year)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'August', 'September', 'October', 'November','December']
        years = [2019, 2020, 2021]

        sundry = SundryReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]

        context = {'archived_reports': archived_reports,
                   'months': months,
                   'years': years,
                   'expenses':sundry,
                   'total_amount': total_amount,
                   'today': today,
                   'report_year': report_year,
                   'report_month': report_month
                   }
        return render(request, "Expenses/sundryarchive.html", context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'August', 'September','October', 'November', 'December']
    years = [2019, 2020, 2021]

    sundry=SundryReportArchive.objects.all()

    context = {'months': months,
               'years': years,
               'sundry': sundry}
    return render(request, "Expenses/sundryarchive.html", context)





        ###############################################
    # GENERATING REPORTS IN FORM OF ANNUAL PDFS   #
    ###############################################


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
