#views
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from datetime import datetime, timedelta
from django.contrib import messages
from django.conf import settings
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
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def web(request):
    news = News.published.all().order_by('-id')
    events = Event.published.all().order_by('-from_date')
    images = Image.published.all().order_by('-id')
    members = Members.published.all().order_by('-id')
    employees = StaffDetails.published.all()
    sliders = Slider.objects.all().order_by('-id')
    abouts = About.objects.all()
    feeback= Contact.objects.all().order_by('-id')
    pages = Page.objects.all().order_by('-id')
   
    context = {
        'pages' : pages,
        'feeback':feeback,
        'images':images,
        'events': events,
        'news': news,
        'abouts': abouts,
        'sliders' :sliders,
        'members': members,
        'employees': employees,
    }
    return render(request, 'home/index_public.html', context)

def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST, request.FILES,)
        if form.is_valid():
                form.save()
                messages.success(request, f'Your Message has been sent successfully')
                return redirect('index_public')
    else:
        form=ContactForm()
        return render(request, 'home/contacts.html',{'form':form})

    return render(request, 'home/contacts.html')

class OnlineRegistrationView(SuccessMessageMixin,CreateView):
    model = Members
    template_name = 'Members/online_registration.html'
    success_message = " Your Membership has been Saved successfully"
    fields = '__all__'
         
    def form_valid(self, form):
        member = form.save(commit=False)
        member.save()
        return redirect('index_public')    
@login_required
def index(request):

    current_month = datetime.now().month
    day = datetime.now().today
    total_current_donations = Donations.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_current_donations['totals'])!=None:
        int(total_current_donations["totals"])
        donations=total_current_donations["totals"]
    else:
        total_current_donations = 0
        donations = 0


    one_week_ago = datetime.today() - timedelta(days=7)
    total_weekly_donations = Donations.objects.filter(Date__gte=one_week_ago).aggregate(totals=models.Sum("Amount"))
    if (total_weekly_donations['totals'])!=None:
        int(total_weekly_donations["totals"])
        d_donations=total_weekly_donations["totals"]
    else:
        total_weekly_donations = 0
        d_donations = 0


    total_current_thanks = ThanksGiving.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_current_thanks['totals'])!=None:
        int(total_current_thanks["totals"])
        thanks=total_current_thanks["totals"]
    else:
        total_current_thanks = 0
        thanks = 0

    total_weekly_thanks = ThanksGiving.objects.filter(Date__gte=one_week_ago).aggregate(totals=models.Sum("Amount"))
    if (total_weekly_thanks['totals'])!=None:
        int(total_weekly_thanks["totals"])
        d_thanks=total_weekly_thanks["totals"]
    else:
        total_weekly_thanks = 0
        d_thanks = 0         

    
    total_current_seeds = Seeds.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_current_seeds['totals'])!=None:
        int(total_current_seeds["totals"])
        seeds=total_current_seeds["totals"]
    else:
        total_current_seeds = 0
        seeds = 0

    
    total_weekly_seeds = Seeds.objects.filter(Date__gte=one_week_ago).aggregate(totals=models.Sum("Amount"))
    if (total_weekly_seeds['totals'])!=None:
        int(total_weekly_seeds["totals"])
        d_seeds=total_weekly_seeds["totals"]
    else:
        total_weekly_seeds = 0
        d_seeds = 0

    total_current_offerings = Offerings.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Total_Offering"))
    if (total_current_offerings['totals'])!=None:
        int(total_current_offerings["totals"])
        offerings=total_current_offerings["totals"]
    else:
        total_current_offerings = 0
        offerings = 0

    total_weekly_offerings = Offerings.objects.filter(Date__gte=one_week_ago).aggregate(totals=models.Sum("Total_Offering"))
    if (total_weekly_offerings['totals'])!=None:
        int(total_weekly_offerings["totals"])
        d_offerings=total_weekly_offerings["totals"]
    else:
        total_weekly_offerings = 0
        d_offerings = 0

#TITHES
    total_current_tithes = Tithes.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_current_tithes['totals'])!=None:
        int(total_current_tithes["totals"])
        tithes=total_current_tithes["totals"]
    else:
        total_current_tithes=0
        tithes = 0

    total_weekly_tithes = Tithes.objects.filter(Date__gte=one_week_ago).aggregate(totals=models.Sum("Amount"))
    if (total_weekly_tithes['totals'])!=None:
        int(total_weekly_tithes["totals"])
        d_tithes=total_weekly_tithes["totals"]
    else:
        total_weekly_tithes=0
        d_tithes = 0 

#BUILDING
    total_current_building = BuildingRenovation.objects.filter(Archived_Status='NOT-ARCHIVED', Date__month=current_month).aggregate(totals=models.Sum("Total_Collection"))
    if (total_current_building['totals'])!=None:
        int(total_current_building["totals"])
        building=total_current_building["totals"]
    else:
        total_current_building=0
        building = 0
    total_weekly_building = BuildingRenovation.objects.filter(Archived_Status='NOT-ARCHIVED', Date__gte=one_week_ago).aggregate(totals=models.Sum("Total_Collection"))
    if (total_weekly_building['totals'])!=None:
        int(total_weekly_building["totals"])
        d_building=total_weekly_building["totals"]
    else:
        total_weekly_building=0
        d_building = 0           
#Calculate Expenditure
    #monthly salary
    total_current_salaries = SalariesPaid.objects.filter(Date_of_paying_salary__month=current_month).aggregate(totals=models.Sum("Salary_Amount"))
    if (total_current_salaries['totals'])!=None:
        int(total_current_salaries["totals"])
        salaries=total_current_salaries["totals"]
    else:
        total_current_salaries = 0
        salaries = 0

    #weekly salaries
    total_weekly_salaries = SalariesPaid.objects.filter(Date_of_paying_salary__gte=one_week_ago).aggregate(totals=models.Sum("Salary_Amount"))
    if (total_weekly_salaries['totals'])!=None:
        int(total_weekly_salaries["totals"])
        d_salaries=total_weekly_salaries["totals"]
    else:
        total_weekly_salaries = 0
        d_salaries = 0
    #mothly pledges    
    total_current_pledges = PaidPledges.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount_Paid"))
    if (total_current_pledges['totals'])!=None:
        int(total_current_pledges["totals"])
        pledges=total_current_pledges["totals"]
    else:
        total_current_pledges = 0
        pledges = 0
    #weekly pledges
    total_weekly_pledges = PaidPledges.objects.filter(Date__gte=one_week_ago).aggregate(totals=models.Sum("Amount_Paid"))
    if (total_weekly_pledges['totals'])!=None:
        int(total_weekly_pledges["totals"])
        d_pledges=total_weekly_pledges["totals"]
    else:
        total_weekly_pledges = 0
        d_pledges = 0    
    
    #monthly main expenses
    total_main_expenses = Spend.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_main_expenses['totals'])!=None:
        int(total_main_expenses["totals"])
        expenses=total_main_expenses["totals"]
    else:
        total_main_expenses = 0
        expenses = 0

        #weekly main expenses
    total_weekly_expenses = Spend.objects.filter(Date__gte=one_week_ago).aggregate(totals=models.Sum("Amount"))
    if (total_weekly_expenses['totals'])!=None:
        int(total_weekly_expenses["totals"])
        d_expenses=total_weekly_expenses["totals"]
    else:
        total_weekly_expenses = 0
        d_expenses = 0  

    #Total general expenses of the current month of the year.
    total_general_expenses = GeneralExpenses.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_general_expenses['totals'])!=None:
        int(total_general_expenses["totals"])
        general=total_general_expenses["totals"]
    else:
        total_general_expenses = 0
        general = 0
        #Total general expenses of the week.
    weekly_general_expenses = GeneralExpenses.objects.filter(Date__gte=one_week_ago).aggregate(totals=models.Sum("Amount"))
    if (weekly_general_expenses['totals'])!=None:
        int(weekly_general_expenses["totals"])
        d_general=weekly_general_expenses["totals"]
    else:
        weekly_general_expenses = 0
        d_general = 0

    #Monthly Petty Cash expenses
    total_petty_expenses = Sundry.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_petty_expenses['totals'])!=None:
        int(total_petty_expenses["totals"])
        petty=total_petty_expenses["totals"]
    else:
        total_petty_expenses = 0
        petty = 0

    #weekly Petty Cash expenses
    weekly_petty_expenses = Sundry.objects.filter(Date__gte=one_week_ago).aggregate(totals=models.Sum("Amount"))
    if (weekly_petty_expenses['totals'])!=None:
        int(weekly_petty_expenses["totals"])
        d_petty=weekly_petty_expenses["totals"]
    else:
        weekly_petty_expenses = 0
        d_petty = 0 

    #monthly allowances       
    total_allowances = Allowance.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount"))
    if (total_allowances['totals'])!=None:
        int(total_allowances["totals"])
        allowances=total_allowances["totals"]    
    else:
        total_allowances = 0
        allowances=0
    #weeky allowances       
    weekly_allowances = Allowance.objects.filter(Date__gte=one_week_ago).aggregate(totals=models.Sum("Amount"))
    if (weekly_allowances['totals'])!=None:
        int(weekly_allowances["totals"])
        d_allowances=weekly_allowances["totals"]    
    else:
        weekly_allowances = 0
        d_allowances=0

    #incase of data has been archived, none is returned, so we have to catch it before it causes trouble
    if (total_current_donations,total_current_thanks,total_current_seeds,total_petty_expenses,total_current_tithes,total_current_salaries, total_general_expenses, total_current_offerings,total_current_pledges,total_allowances,total_main_expenses, total_current_building)== None:
        total_monthly_incomes = 0
        total_monthly_expenditure =  0
        total_general_expenses = 0
        total_current_seeds=0
        total_current_donations=0
        total_current_thanks=0
        total_current_building=0
        pledges = 0
        #calculating net income
        net_income = total_monthly_incomes - total_monthly_expenditure
        today = timezone.now()
        month = today.strftime('%B')

        context={'total_current_donations':total_current_donations,'total_current_thanks':total_current_thanks,'total_current_seeds':total_current_seeds,'total_petty_expenses':total_petty_expenses,'total_general_expenses':total_general_expenses,'total_monthly_incomes':total_monthly_incomes,'salaries':salaries,'total_current_salaries':total_current_salaries,'total_monthly_expenditure':total_monthly_expenditure, 'month': month,
        'petty':petty,'allowances':allowances, 'pledges':pledges, 'general':general,'expenses':expenses,
        'tithes':tithes, 'offerings':offerings, 'seeds':seeds, 'net_income':net_income,'thanks':thanks, 'building':building,
        'donations':donations,'day':day,'total_current_building':total_current_building, 'd_building': d_building,

        'd_petty':d_petty,'d_allowances':d_allowances,'d_salaries':d_salaries, 'd_pledges':d_pledges, 'd_general':d_general,'d_expenses':d_expenses,
        }
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
        context={'total_current_building':total_current_building, 'd_building': d_building, 'building':building, 'total_current_donations':total_current_donations,'total_current_thanks':total_current_thanks,'total_current_seeds':total_current_seeds,'total_general_expenses':total_general_expenses,'total_petty_expenses':total_petty_expenses,'salaries':salaries,'total_current_salaries':total_current_salaries,'total_monthly_incomes':total_monthly_incomes,'total_monthly_expenditure':total_monthly_expenditure, 'month': month,
        'general':general,'allowances':allowances,'seeds':seeds, 'expenses':expenses,'day':day,
        'tithes':tithes, 'offerings':offerings, 'pledges':pledges, 'net_income':net_income,'thanks':thanks,'donations':donations
        ,'d_petty':d_petty,'d_allowances':d_allowances,'d_salaries':d_salaries, 'd_pledges':d_pledges, 'd_general':d_general,'d_expenses':d_expenses,
        }
        return render(request,'index.html', context)

    #if there are moneys, calculate incomes and total expenditure.
    else:
        total_monthly_incomes =  tithes+ offerings + seeds + thanks + donations + building
        total_monthly_expenditure =  allowances + expenses+salaries+ general+ petty
        net_income = total_monthly_incomes - total_monthly_expenditure
        today = timezone.now()
        month = today.strftime('%B')
        context={
        'total_current_building':total_current_building, 'd_building': d_building,"building":building,
        'd_donations':d_donations,'d_tithes':d_tithes,'d_offerings':d_offerings,
        'd_seeds':d_seeds,'d_thanks':d_thanks,'d_pledges':d_pledges,'day':day,
        'total_current_donations':total_current_donations,'total_current_thanks':total_current_thanks,'total_current_seeds':total_current_seeds,'total_petty_expenses':total_petty_expenses,'total_general_expenses':total_general_expenses,'salaries':salaries,'total_current_salaries':total_current_salaries,'total_monthly_incomes':total_monthly_incomes,'total_monthly_expenditure':total_monthly_expenditure, 'month': month,
        'petty':petty,'allowances':allowances,'seeds':seeds,'general':general, 'expenses':expenses,'tithes':tithes, 
        'offerings':offerings, 'pledges':pledges, 'net_income':net_income,'thanks':thanks,'donations':donations,
        'd_petty':d_petty,'d_allowances':d_allowances,'d_salaries':d_salaries, 'd_general':d_general,'d_expenses':d_expenses,
        }
        return render(request,'index.html', context)

    


    ##################################
    #        Employee Module         #
    ##################################

def employee_register(request):
    if request.method=="POST":
        form=StaffDetailsForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            messages.success(request, f'Employee has been successfully add to the system')
            return redirect('employee-list')
    else:
        form=StaffDetailsForm()
        return render(request, 'Employees/record_employee.html',{'form':form})

def delete_employee(request,pk):
    employee= get_object_or_404(StaffDetails, id=pk)
    if request.method == "GET":
        employee.delete()
        messages.success(request, "User successfully deleted!")
        return redirect("employee-list")
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
            messages.success(request, f'Employee has been successfully edited')
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
        form = StaffDetailsForm(request.POST, request.FILES, instance=employee)
        context['form']=form

    else:
        form = StaffDetailsForm(request.POST, request.FILES, instance=employee)
        get_name = StaffDetails.objects.filter(id=pk)
        context['get_name']=get_name
        context['form']=form
        print(form.instance.UCC_Bwaise_Member)
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
            messages.success(request, f'Employee has been paid salary successfully')
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
        message="The Monthly Salaries Paid Report has been Archived"
        context={'message':message, 'mth':mth}
        return render(request, 'Employees/current_month_salaries_paid.html', context)
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August','September', 'October', 'November','December']
    years = datetime.now().year
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

def delete_salary_paid(request,pk):
    salary= get_object_or_404(SalariesPaid, id=pk)
    if request.method == "GET":
        salary.delete()
        messages.success(request, "Salary Paid successfully deleted!")
        return redirect("current-month-salaries")

#Search for the archived salaries reports
def salariespaidarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = SalariesPaidReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August','September', 'October',  'November','December']
        years = datetime.now().year
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
    years = datetime.now().year

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
            messages.success(request, f'Member has been added to system successfully')
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
            messages.success(request, f'The visitor has been recorded')
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

def membership_wall(request):
    all_members = Members.published.all()
    paginator = Paginator(all_members, 8)  # 6 members on each page
    page = request.GET.get('page')
    try:
        members_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        members_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        members_list = paginator.page(paginator.num_pages)
    context={'page':page, 'members_list': members_list}    
    return render(request, 'Members/members_wall.html', context)

#Church Pastors
def church_pastors(request):
    pastors = Members.published.all()
    return render(request, 'Members/pastoral_team.html', {'pastors': pastors})

#Administrative Team
def church_administration(request):
    staffs = User.published.filter(Q(Role='Admin') | Q(Role='SuperAdmin') | Q(Role='Secretary')| Q(Role='Youth Leader'))
    return render(request, 'Members/administration_team.html', {'staffs': staffs})  

#edit member
def edit_member(request, pk):
    item = get_object_or_404(Members, pk=pk)
    if request.method == "POST":
        form = MembersForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Member Information has been updated')
            return redirect('members-list')
    else:
        form = MembersForm(instance=item)
    return render(request, 'Members/register_members.html', {'form': form})

#view member    
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

#delete member
def delete_member(request, pk):
    member= get_object_or_404(Members, id=pk)
    if request.method == "GET":
        member.delete()
        messages.success(request, f'Member has been deleted successfully')
        return redirect("members-list")
    context= {'member': member}
    return render(request, 'Members/members_delete.html', context)

#edit visitor    
def edit_visitor(request, pk):
    item = get_object_or_404(Visitors, pk=pk)
    if request.method == "POST":
        form = VisitorsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'The visitor has been edited')
            return redirect('visitors-list')
    else:
        form = VisitorsForm(instance=item)
    return render(request, 'Members/register_visitors.html', {'form': form})

#delete visitors    
def delete_visitor(request, pk):
    visiting= get_object_or_404(Visitors, id=pk)
    if request.method == "GET":
        visiting.delete()
        messages.success(request, f'Visitor has been deleted')
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
    #                 OFFERINGS MODULE                  #
     ###################################################

#recording offerings
@login_required
def Enter_Offerings(request):
    if request.method=="POST":
        form=OfferingsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Offerings have been recorded')
            return redirect('Offeringsreport')
    else:
        form=OfferingsForm()
        return render(request, 'Offerings/record_offerings.html',{'form':form})

#edit offerings
def edit_offerings(request, pk):
    item = get_object_or_404(Offerings, pk=pk)
    if request.method == "POST":
        form = OfferingsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Offerings have been updated')
            return redirect('Offeringsreport')
    else:
        form = OfferingsForm(instance=item)
    return render(request, 'Offerings/record_offerings.html', {'form': form})

#offering
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
        message="The Monthly Offerings Report has been Archived"
        context={'message':message}
        return render(request, 'Offerings/offeringsindex.html', context)
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August','September', 'October', 'November','December']
    years = datetime.now().year
    today = datetime.now()
    current_month = today.strftime('%B')
    mth = datetime.now().month
    day=datetime.now()
    total = Offerings.objects.aggregate(totals=models.Sum("Total_Offering"))
    total_amount = total["totals"]
    items =Offerings.objects.all()
    context = {'day':day, 'total_amount':total_amount,'items': items,'months':months,'current_month':current_month,'years':years,
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
        years = datetime.now().year
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
    years = datetime.now().year
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
            'archived_offerings': archived_offerings,}
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
        message="The Monthly Seeds Report has been Archived"
        context={'message':message}
        return render(request, 'Seeds/Seedsindex.html', context)
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    years = datetime.now().year
    today = timezone.now()
    current_month = today.strftime('%B')
    total = Seeds.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    mth = datetime.now().month
    items =Seeds.objects.all()
    day=datetime.now()
    context = {'day':day,'total_amount':total_amount,'items': items,'months':months,'years':years,'current_month':current_month
    }
    return render(request, 'Seeds/Seedsindex.html', context)

@login_required
def seedsarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = SeedsReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September', 'October', 'November', 'December']
        years = datetime.now().year
        seeds = SeedsReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'archived_reports': archived_reports,'months': months,'years': years,'seeds': seeds,
                   'total_amount': total_amount,'today': today,'report_year': report_year,'report_month': report_month
                   }
        return render(request, "Seeds/seedsarchive.html", context)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'November', 'December']
    years = datetime.now().year
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
    #                   DONATIONS MODULE                #
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
        message="The Monthly Donations report has been Archived"
        context={'message':message}
        return render(request, 'Donations/donationsindex.html', context)
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August','September', 'October', 'November','December']
    years = datetime.now().year
    total = Donations.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    mth = datetime.now().month
    day=datetime.now()

    items =Donations.objects.all()
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
        today = datetime.now()
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
        years = datetime.now().year
        years = [yr,2019,2018,2017]
        donations = DonationsReportArchive.objects.all()
        today = datetime.now()
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'archived_reports': archived_reports,'months': months,'years': years,'expenses': donations,
                   'total_amount': total_amount,'today': today,'report_year': report_year,'report_month': report_month}
        return render(request, "Donations/donationssarchive.html", context)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'November', 'December']
    years = datetime.now().year
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
        message="The Monthly Thanks Giving report has been Archived"
        context={'message':message}
        return render(request, 'ThanksGiving/thanksgivingindex.html', context)
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August','September', 'October', 'November','December']
    years = datetime.now().year
    total = ThanksGiving.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    mth = datetime.now().month
    day=datetime.now()
    items =ThanksGiving.objects.all()
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
        years = datetime.now().year
        years = [yr,2019,2018,2017]
        thanksgiving = ThanksGivingReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'archived_reports': archived_reports,'months': months,'years': years,'expenses': thanksgiving,
                   'total_amount': total_amount,'today': today,'report_year': report_year,'report_month': report_month}
        return render(request, "ThanksGiving/thanksgivingarchivessearch.html", context)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'November', 'December']
    years = datetime.now().year
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
@login_required
def tithesarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = TithesReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September', 'October', 'November', 'December']
        years = datetime.now().year

        tithes = TithesReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'archived_reports': archived_reports,'months': months,'years': years,'expenses': tithes,
                   'total_amount': total_amount,'today': today,'report_year': report_year,'report_month': report_month
                   }
        return render(request, "Tithes/tithesarchive.html", context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'November', 'December']
    years = datetime.now().year
    tithes = TithesReportArchive.objects.all()
    context = {'months': months,
               'years': years,
               'tithes': tithes}
    return render(request, "Tithes/tithesarchive.html", context)

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
            service=expense.Service
            # the expense archive object
            expense_archiveobj=TithesReportArchive()
            #attached values to expense_archiveobj
            expense_archiveobj.Date=date
            expense_archiveobj.Tithe_Made_By = name
            expense_archiveobj.Service=service
            expense_archiveobj.Amount=amount
            expense_archiveobj.archivedyear = archived_year
            expense_archiveobj.archivedmonth = archived_month
            expense_archiveobj.save()
            #deleting all the expense from reports table
        all_expenses.delete()
        message="The Monthly Tithes Report has been Archived"
        context={'message':message}

        return render(request, 'Tithes/tithesindex.html', context)

    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    years = datetime.now().year
    today = timezone.now()
    current_month = today.strftime('%B')
    total = Tithes.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    mth = datetime.now().month
    items =Tithes.objects.all()
    day=datetime.now()
    context = {'day':day,'total_amount':total_amount,'items': items,
               'months':months,'years':years,'current_month':current_month
    }
    return render(request, 'Tithes/tithesindex.html', context)
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

def member_annual_tithes(request, pk):
    years = datetime.now().year
    tithes=TithesReportArchive.objects.filter(Tithe_Made_By_id=pk, archivedyear=years)
    members=Members.objects.filter(id=pk)
    tithescontext={'tithes':tithes, 'members':members}
    return render(request, 'Tithes/member_annual_tithes.html', tithescontext)        

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
        message="The Monthly Allowances report has been Archived"
        context={'message':message}
        return render(request, 'Allowances/allowanceindex.html', context)
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August','September', 'October', 'November','December']
    years = datetime.now().year
    total = Allowance.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    mth = datetime.now().month
    day=datetime.now()
    items =Allowance.objects.all()
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
        years = datetime.now().year


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
    years = datetime.now().year

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


                 #############################################################
                #          GENERAL, MAIN, PETTY EXPENSES MODULES              #
                 #############################################################

@login_required
def enter_main_expenses(request):
    if request.method=="POST":
        form=ExpendituresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenditurereport')
    else:
        form=ExpendituresForm()
        context = {'form': form, }
        return render(request, 'Expenses/pay_main_expenses.html',context)

@login_required
def enter_general_expenses(request):
    if request.method=="POST":
        form=ExpendituresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('general-expenses-report')
    else:
        form=ExpendituresForm()
        context = {'form': form, }
        return render(request, 'Expenses/pay_general_expenses.html',context)        
@login_required
def enter_petty_expenses(request):
    if request.method == "POST":
        form = ExpendituresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sundryreport')
    else:
        today = timezone.now()
        current_month = today.strftime('%B')
        form = ExpendituresForm()
        context={'form': form, 'current_month': current_month}
        return render(request, 'Expenses/record_petty_expenses.html', context )

def edit_general_expense(request, pk):
    item = get_object_or_404(Expenditures, pk=pk)
    if request.method == "POST":
        form = ExpendituresForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('general-expenses-report')
    else:
        form = ExpendituresForm(instance=item)
    return render(request, 'Expenses/edit_general_expense.html', {'form': form})

def edit_main_expense(request, pk):
    item = get_object_or_404(Expenditures, pk=pk)
    if request.method == "POST":
        form = ExpendituresForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('expenditurereport')
    else:
        form = ExpendituresForm(instance=item)
    return render(request, 'Expenses/edit_main_expense.html', {'form': form})

def edit_petty_cash(request, pk):
    item = get_object_or_404(Expenditures, pk=pk)
    if request.method == "POST":
        form = ExpendituresForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('sundryreport')
    else:
        form = ExpendituresForm(instance=item)
    return render(request, 'Expenses/edit_petty_cash.html', {'form': form, })

# def delete_payment(request,pk):
#     items= Spend.objects.filter(id=pk).delete()
#     context = { 'items':items}
#     return render(request, 'Expenses/expenditureindex.html', context)

# def delete_sundry(request, pk):
#     items = Sundry.objects.filter(id=pk).delete()
#     context = {'items': items}
#     return render(request, 'Expenses/sundryindex.html', context)

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

        message="The Monthly Main Expenses Report has been Archived"
        context={
                 'message':message,
                 }

        return render(request, 'Expenses/expenditureindex.html', context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September',
              'October', 'November',
              'December']
    years = datetime.now().year
    mth = datetime.now().month
    items =Spend.objects.all()
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
        message="The Monthly General Expenses Report has been Archived"
        context={'message':message,}
        return render(request, 'Expenses/generalexpenditureindex.html', context)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September',
              'October', 'November','December']
    years = datetime.now().year
    mth = datetime.now().month
    day=datetime.now()
    items =GeneralExpenses.objects.all()
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

        message="Petty Expenses Monthly Report has been archived"
        context={'message':message}

        return render(request, 'Expenses/sundryindex.html', context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
              'October', 'November',
              'December']
    years = datetime.now().year

    total = Sundry.objects.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    mth = datetime.now().month
    day=datetime.now()
    items =Sundry.objects.all()
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
        years = datetime.now().year

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
    years = datetime.now().year
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
        years = datetime.now().year

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
    years = datetime.now().year
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
    years = datetime.now().year
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
            return redirect('add-pledge-item')
        messages.error(request, "Item Name Already exists in the Database, Choose a different one!")
        return redirect('add-pledge-item')   
    else:
        form=PledgeItemsForm()
        current_year=datetime.now().year
        items = PledgeItem.objects.filter(Date__year=current_year)
        context={'form':form, 'items':items, 'current_year':current_year}
        return render(request, 'Pledges/add_Pledge_Item.html',context)
@login_required
def list_of_pledge_items(request):
    current_year=datetime.now().year
    items = PledgeItem.objects.filter(Date__year=current_year).order_by('-Date')
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

#spending money on the pledged item
def pledge_cash_out(request, pk):
    items = get_object_or_404(PledgeItem, id=pk)
    if request.method == "POST":
        form = PledgeItemsForm(request.POST,instance=items)
        if form.is_valid():
            form.save()
            return redirect('list-of-pledge-items')
    else:
        form = PledgeItemsForm(instance=items)
        cashout=PledgeItem.objects.filter(id=pk)
        context={'form':form, 'cashout': cashout}
        return render(request, 'Pledges/pledge_cash_out.html', context)

def cashing_out_items(request):
    if request.method == "POST":
        form =  PledgesCashedOutForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            
            form.save() 
            #PledgesCashedOut.objects.all().delete()
            messages.success(request, "Cash out was successful")
            return redirect('list-of-pledge-items')    
        else:
            form = PledgesCashedOutForm()
            context={'form':form}
            return render(request, 'Pledges/pledge_cash_out.html', context)

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
    debts=PledgesReportArchive.objects.filter(Q(Status='UNPAID') | Q(Status='PARTIAL') | Q(Status='PAID'))
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
    retrieving_id=PledgesReportArchive.objects.filter(id=pk)
    if request.method == "GET":
        retrieving_id.delete()
        messages.success(request, "Archive successfully deleted!")
        return redirect('archived-pledge-debts')

@login_required
def pledges_paid_list(request):
    context = {}
    today = datetime.now()
    month = today.strftime('%B')
    context['month']=month
    current_month = datetime.now().month
    lists = PaidPledges.objects.all().values('Pledge_Id','Pledge_Made_By__First_Name','Pledge_Made_By__Second_Name','Reason__Item_That_Needs_Pledges').annotate(Amount_Paid=Sum('Amount_Paid'))
    print(lists)
    context['lists']=lists
    return render(request, 'Pledges/pledges_paid_list.html',context)

# def delete_pledges_paid(request, pk):
#     pledges= get_object_or_404(PaidPledges, id=pk)
#     if request.method == "GET":
#         pledges.delete()
#         messages.success(request, "Payment successfully deleted!")
#         return redirect("pledges-paid-list")

def delete_pledge(request, pk):
    pledges= get_object_or_404(Pledges, id=pk)
    if request.method == "GET":
        pledges.delete()
        messages.success(request, "Pledge successfully deleted!")
        return redirect("Pledgesreport")          
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
        today = datetime.now().now()
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
        today = datetime.now()
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
        messages.success(request, "The Pledges Report has been Archived")
        return render(request, 'Pledges/pledgesindex.html')
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'August', 'September', 'October', 'November','December']
    years = datetime.now().year
    total = Pledges.objects.aggregate(totals=models.Sum("Amount_Pledged"))
    total_amount = total["totals"]
    day=datetime.now()
    mth = datetime.now().month
    items =Pledges.objects.all().order_by('-Date')
    context = {
        'day':day,
        'mth':mth,
        'total_amount':total_amount,
        'items':items,
        'months':months,
        'years':years,
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
        years = datetime.now().year
#getting years automatically without hard coding.... <<pending>>

        pledges = PledgesReportArchive.objects.all()
        today = timezone.now()
        total = archived_reports.aggregate(totals=models.Sum("Pledged_Amount"))
        total_amount = total["totals"]
        context = {'archived_reports': archived_reports,'months': months,'years': years,'expenses': pledges,'total_amount': total_amount,'today': today,'report_year': report_year,
                   'report_month': report_month}
        return render(request, "Pledges/pledgesarchive.html", context)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    years = datetime.now().year
    pledges = PledgesReportArchive.objects.all()
    context = {'months': months, 'years': years, 'pledges': pledges}
    return render(request, "Pledges/pledgesarchive.html", context)

class pledgesarchivepdf(View):
    def get(self, request, report_month, report_year):
        archived_pledges = PledgesReportArchive.objects.filter(archivedmonth=report_month, archivedyear=report_year)
        today = datetime.now()
        total = archived_pledges.aggregate(totals=models.Sum("Pledged_Amount"))
        total_amount = total["totals"]
        pledgescontext = {
            'today': today,
            'total_amount': total_amount,
            'request': request,
            'archived_pledges': archived_pledges,
        }
        return Render.render('Pledges/pledgesarchivepdf.html', pledgescontext)

class pledge_debt_invoice(View):
    def get(self, request, pk):
        debt = PledgesReportArchive.objects.get(Q(Status='UNPAID') | Q(Status='PARTIAL'), Pledge_Id=pk)
        today = datetime.now()
        debtcontext = {
            'today': today,
            'debt': debt,
            'request': request,
        }
        return Render.render('Pledges/pledge_debt_invoice.html', debtcontext) 

#invoice of pledges made but pending payment
class pledge_made_invoice(View):
    def get(self, request, pk):
        pledge = Pledges.objects.get(Q(Status='UNPAID') | Q(Status='PARTIAL'), id=pk)
        today = datetime.now()
        debtcontext = {
            'today': today,
            'pledge': pledge,
            'request': request,
        }
        return Render.render('Pledges/pledges_made_invoice.html', debtcontext) 

#print receipt for archived pledges that have been settled.        
class settled_archived_pledge_receipt(View):
    def get(self, request, pk):
        settled= PledgesReportArchive.objects.get(Status='PAID', Pledge_Id=pk)
        today = datetime.now()
        context = {
            'today': today,
            'settled': settled,
            'request': request,
        }
        return Render.render('Pledges/settled_archived_pledges_receipt.html', context)               
#airtime report
def airtime_data_report(request):
    mth = datetime.now().day
    today = datetime.now()
    get_airtime=Sundry.objects.filter(Reason_For_Payment='Airtime/Data', Date__day=mth)
    total = Sundry.objects.filter(Reason_For_Payment='Airtime/Data',Date__day=mth).aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    context={'get_airtime':get_airtime, 'total_amount':total_amount, 'today':today}
    return render(request,'Expenses/airtime_data_report.html', context)



                            #################################
                            #         SLIDER VIEW
                            #################################

class SliderListView(ListView):
    model = Slider
    template_name = 'sliders/slider_list.html'
    context_object_name = 'sliders'


class SliderCreateView(CreateView):
    model = Slider
    template_name = 'sliders/slider_create.html'
    fields = ('slider_image', 'image_title')

    def form_valid(self, form):
        slider = form.save(commit=False)
        slider.save()
        return redirect('slider_list')


class SliderUpdateView(UpdateView):
    model = Slider
    template_name = 'sliders/update_slider.html'
    pk_url_kwarg = 'slider_pk'
    fields = ('slider_image', 'image_title')

    def form_valid(self, form):
        slider = form.save(commit=False)
        slider.save()
        return redirect('slider_list')


def save_slider_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            sliders = Slider.objects.all()
            data['html_slider_list'] = render_to_string('sliders/includes/partial_slider_list.html', {
                'sliders': sliders
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def slider_view(request, slider_pk):
    slider = get_object_or_404(Slider, pk=slider_pk)
    if request.method == 'POST':
        form = SliderForm(request.POST, instance=slider)
    else:
        form = SliderForm(instance=slider)
    return save_slider_form(request, form, 'sliders/includes/partial_slider_view.html')


def slider_delete(request, slider_pk):
    slider = get_object_or_404(Slider, pk=slider_pk)
    data = dict()
    if request.method == 'POST':
        slider.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        sliders = Slider.objects.all()
        data['html_slider_list'] = render_to_string('sliders/includes/partial_slider_list.html', {
            'sliders': sliders
        })
    else:
        context = {'slider': slider}
        data['html_form'] = render_to_string('sliders/includes/partial_slider_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)

##################===>BEGINNING OF ABOUT MODULE<===#########################


class AboutListView(ListView):
    model = About
    template_name = 'abouts/about_list.html'
    context_object_name = 'abouts'

def abouts_vision(request):
    abouts = About.published.all()
    return render(request, 'abouts/abouts_wall.html', {'abouts': abouts})

def abouts_mission(request):
    abouts = About.published.all()
    return render(request, 'abouts/abouts_mission.html', {'abouts': abouts})
class AboutCreateView(CreateView):
    model = About
    template_name = 'abouts/about_create.html'
    fields = ('about_title','about', 'about_image','vision_description','mission_description','Is_View_on_Web')

    def form_valid(self, form):
        about = form.save(commit=False)
        about.save()
        return redirect('about_list')


class AboutUpdateView(UpdateView):
    model = About
    template_name = 'abouts/update_about.html'
    pk_url_kwarg = 'about_pk'
    fields = ('about', 'about_image','vision_description','mission_description','Is_View_on_Web')

    def form_valid(self, form):
        about = form.save(commit=False)
        about.save()
        return redirect('about_list')


def save_about_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            abouts = About.objects.all()
            data['html_about_list'] = render_to_string('abouts/includes/partial_about_list.html', {
                'abouts': abouts
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def about_view(request, about_pk):
    about = get_object_or_404(About, pk=about_pk)
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=about)
    else:
        form = AboutForm(instance=about)
    return save_about_form(request, form, 'abouts/includes/partial_about_view.html')


def about_detail(request, about_pk):
    about = get_object_or_404(About, pk=about_pk)
    context = {
        'about': about,
    }
    return render(request, 'abouts/about_detail.html', context)


def about_delete(request, about_pk):
    about = get_object_or_404(About, pk=about_pk)
    data = dict()
    if request.method == 'POST':
        about.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        abouts = About.objects.all()
        data['html_about_list'] = render_to_string('abouts/includes/partial_about_list.html', {
            'abouts': abouts
        })
    else:
        context = {'about': about}
        data['html_form'] = render_to_string('abouts/includes/partial_about_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)

# ###################################===>BEGINNING OF IMAGE MODULE<===###############################################


class ImageListView(ListView):
    model = Image
    template_name = 'images/image_list.html'
    context_object_name = 'images'


class ImageCreateView(CreateView):
    model = Image
    template_name = 'images/image_create.html'
    fields = ('gallery_title', 'gallery_image', 'image_caption')

    def form_valid(self, form):
        image = form.save(commit=False)
        image.save()
        return redirect('image_list')


class ImageUpdateView(UpdateView):
    model = Image
    template_name = 'images/update_image.html'
    pk_url_kwarg = 'image_pk'
    fields = ('gallery_title', 'gallery_image', 'image_caption')

    def form_valid(self, form):
        image = form.save(commit=False)
        image.save()
        return redirect('image_list')


def save_image_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            images = Image.objects.all()
            data['html_image_list'] = render_to_string('images/includes/partial_image_list.html', {
                'images': images
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def image_view(request, image_pk):
    image = get_object_or_404(Image, pk=image_pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, instance=image)
    else:
        form = ImageForm(instance=image)
    return save_image_form(request, form, 'images/includes/partial_image_view.html')


def image_delete(request, image_pk):
    image = get_object_or_404(Image, pk=image_pk)
    data = dict()
    if request.method == 'POST':
        image.delete()
        data['form_is_valid'] = True
        images = Image.objects.all()
        data['html_image_list'] = render_to_string('images/includes/partial_image_list.html', {
            'images': images
        })
    else:
        context = {'image': image}
        data['html_form'] = render_to_string('images/includes/partial_image_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)



# ###################################===>BEGINNING OF PAGE MODULE<===###############################################


class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'


def page_wall(request, page_pk):
    pager = get_object_or_404(Page, pk=page_pk)
    pages = Page.objects.all()
    header_pages = Page.header.all()
    footer_pages = Page.footer.all()
    context = {
        'pager': pager, 
        'pages': pages,
        'header_pages': header_pages,
        'footer_pages': footer_pages
    }
    return render(request, 'pages/page_wall.html', context)


class PageCreateView(CreateView):
    model = Page
    template_name = 'pages/page_create.html'
    fields = ('page_location', 'page_title', 'page_description', 'page_image')

    def form_valid(self, form):
        page = form.save(commit=False)
        page.save()
        return redirect('page_list')


class PageUpdateView(UpdateView):
    model = Page
    template_name = 'pages/update_page.html'
    pk_url_kwarg = 'page_pk'
    fields = ('page_location', 'page_title', 'page_description', 'page_image')

    def form_valid(self, form):
        page = form.save(commit=False)
        page.save()
        return redirect('page_list')


def save_page_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            pages = Page.objects.all()
            data['html_page_list'] = render_to_string('pages/includes/partial_page_list.html', {
                'pages': pages
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def page_view(request, page_pk):
    page = get_object_or_404(Page, pk=page_pk)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
    else:
        form = PageForm(instance=page)
    return save_page_form(request, form, 'pages/includes/partial_page_view.html')


def page_delete(request, page_pk):
    page = get_object_or_404(Page, pk=page_pk)
    data = dict()
    if request.method == 'POST':
        page.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        pages = Page.objects.all()
        data['html_page_list'] = render_to_string('pages/includes/partial_page_list.html', {
            'pages': pages
        })
    else:
        context = {'page': page}
        data['html_form'] = render_to_string('pages/includes/partial_page_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)

# ###################################===>BEGINNING OF GALLERY MODULE<===###############################################


class GalleryListView(ListView):
    model = Gallery
    template_name = 'galleries/gallery_list.html'
    context_object_name = 'galleries'


def gallery_wall(request):
    galleries = Gallery.published.all()
    images = Image.objects.all()
    context = {
        'galleries': galleries,
        'images': images
    }
    return render(request, 'galleries/gallery_wall.html', context)


class GalleryCreateView(CreateView):
    model = Gallery
    template_name = 'galleries/gallery_create.html'
    fields = ('gallery_title', 'note', 'Is_View_on_Web')

    def form_valid(self, form):
        gallery = form.save(commit=False)
        gallery.save()
        return redirect('gallery_list')


class GalleryUpdateView(UpdateView):
    model = Gallery
    template_name = 'galleries/update_gallery.html'
    pk_url_kwarg = 'gallery_pk'
    fields = ('gallery_title', 'note', 'Is_View_on_Web')

    def form_valid(self, form):
        gallery = form.save(commit=False)
        gallery.save()
        return redirect('gallery_list')


def save_gallery_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            gallerys = Gallery.objects.all()
            data['html_gallery_list'] = render_to_string('galleries/includes/partial_gallery_list.html', {
                'galleries': gallerys
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def gallery_delete(request, gallery_pk):
    gallery = get_object_or_404(Gallery, pk=gallery_pk)
    data = dict()
    if request.method == 'POST':
        gallery.delete()
        data['form_is_valid'] = True
        gallerys = Gallery.objects.all()
        data['html_gallery_list'] = render_to_string('galleries/includes/partial_gallery_list.html', {
            'galleries': gallerys
        })
    else:
        context = {'gallery': gallery}
        data['html_form'] = render_to_string('galleries/includes/partial_gallery_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


# ###################################===>BEGINNING OF IMAGE MODULE<===###############################################
class ImageListView(ListView):
    model = Image
    template_name = 'images/image_list.html'
    context_object_name = 'images'


class ImageCreateView(CreateView):
    model = Image
    template_name = 'images/image_create.html'
    fields = ('gallery_title', 'gallery_image', 'image_caption')

    def form_valid(self, form):
        image = form.save(commit=False)
        image.save()
        return redirect('image_list')


class ImageUpdateView(UpdateView):
    model = Image
    template_name = 'images/update_image.html'
    pk_url_kwarg = 'image_pk'
    fields = ('gallery_title', 'gallery_image', 'image_caption')

    def form_valid(self, form):
        image = form.save(commit=False)
        image.save()
        return redirect('image_list')


def save_image_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            images = Image.objects.all()
            data['html_image_list'] = render_to_string('images/includes/partial_image_list.html', {
                'images': images
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def image_view(request, image_pk):
    image = get_object_or_404(Image, pk=image_pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, instance=image)
    else:
        form = ImageForm(instance=image)
    return save_image_form(request, form, 'images/includes/partial_image_view.html')


def image_delete(request, image_pk):
    image = get_object_or_404(Image, pk=image_pk)
    data = dict()
    if request.method == 'POST':
        image.delete()
        data['form_is_valid'] = True
        images = Image.objects.all()
        data['html_image_list'] = render_to_string('images/includes/partial_image_list.html', {
            'images': images
        })
    else:
        context = {'image': image}
        data['html_form'] = render_to_string('images/includes/partial_image_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)

# ###################################===>BEGINNING OF NEWS MODULE<===###############################################


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'


def news_wall(request):
    news = News.published.all()
    return render(request, 'news/news_wall.html', {'news': news})


class NewsCreateView(CreateView):
    model = News
    template_name = 'news/news_create.html'
    fields = ('news_title', 'image', 'news', 'author','Is_View_on_Web')

    def form_valid(self, form):
        news = form.save(commit=False)
        news.save()
        return redirect('news_list')


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/update_news.html'
    pk_url_kwarg = 'news_pk'
    fields = ('news_title', 'image', 'news', 'Is_View_on_Web')

    def form_valid(self, form):
        news = form.save(commit=False)
        news.save()
        return redirect('news_list')


def save_news_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            newss = News.objects.all()
            data['html_news_list'] = render_to_string('news/includes/partial_news_list.html', {
                'news': newss
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def news_view(request, news_pk):
    news = get_object_or_404(News, pk=news_pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
    else:
        form = NewsForm(instance=news)
    return save_news_form(request, form, 'news/includes/partial_news_view.html')


def news_detail(request, news_pk):
    news = get_object_or_404(News, pk=news_pk)
    more_news = News.published.order_by('-date')[:5]
    context = {
        'news': news,
        'more_news': more_news
    }
    return render(request, 'news/news_detail.html', context)


def news_delete(request, news_pk):
    news = get_object_or_404(News, pk=news_pk)
    data = dict()
    if request.method == 'POST':
        news.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        news = News.objects.all()
        data['html_news_list'] = render_to_string('news/includes/partial_news_list.html', {
            'news': news
        })
    else:
        context = {'news': news}
        data['html_form'] = render_to_string('news/includes/partial_news_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)

# ###################################===>BEGINNING OF EVENT MODULE<===###############################################


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'


def event_wall(request):
    events = Event.published.all()
    return render(request, 'events/events_wall.html', {'events': events})


class EventCreateView(CreateView):
    model = Event
    template_name = 'events/event_create.html'
    fields = ('event_title', 'event_for', 'event_place', 'from_date', 'to_date', 'image', 'note',
              'Is_View_on_Web', 'Start_Time', 'End_Time', 'Day','Activity_Type')

    def get_form(self):
        form = super().get_form()
        form.fields['from_date'].widget = DatePickerInput()
        form.fields['to_date'].widget = DatePickerInput()
        return form

    def form_valid(self, form):
        event = form.save(commit=False)
        event.save()
        return redirect('event_list')


class EventUpdateView(UpdateView):
    model = Event
    template_name = 'events/update_event.html'
    pk_url_kwarg = 'event_pk'
    fields = ('event_title', 'event_for', 'event_place', 'from_date', 'to_date', 'image', 'note',
              'Is_View_on_Web')

    def get_form(self):
        form = super().get_form()
        form.fields['from_date'].widget = DatePickerInput()
        form.fields['to_date'].widget = DatePickerInput()
        return form

    def form_valid(self, form):
        event = form.save(commit=False)
        event.save()
        return redirect('event_list')


def save_event_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            events = Event.objects.all()
            data['html_event_list'] = render_to_string('events/includes/partial_event_list.html', {
                'events': events
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def event_view(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
    else:
        form = EventForm(instance=event)
    return save_vehicle_form(request, form, 'events/includes/partial_event_view.html')


def event_detail(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    more_events = Event.published.order_by('-from_date')[:5]
    context = {
        'event': event,
        'more_events': more_events
    }
    return render(request, 'events/event_detail.html', context)


def event_delete(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    data = dict()
    if request.method == 'POST':
        event.delete()
        data['form_is_valid'] = True
        events = Event.objects.all()
        data['html_event_list'] = render_to_string('events/includes/partial_event_list.html', {
            'events': events
        })
    else:
        context = {'event': event}
        data['html_form'] = render_to_string('events/includes/partial_event_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


# #######################################===>BEGINNING OF CHURCH MODULE<===##########################################

class churchCreateView(CreateView):
    model = Church
    template_name = 'church/create_church.html'
    fields = ('church_vision','church_mission','maps_embedded_link','church_name', 'church_code',
              'address', 'phone', 'registration_date', 'email_address', 'Post_Office_Box',
              'footer', 'enable_frontend', 'latitude', 'longitude', 'facebook_url','twitter_url', 
              'linkedIn_url', 'google_plus_url', 'youtube_url', 'instagram_url', 'pinterest_url',
              'status', 'frontend_Logo', 'backend_Logo')

    def get_form(self):
        form = super().get_form()
        form.fields['registration_date'].widget = DatePickerInput()
        return form

    def form_valid(self, form):
        church = form.save(commit=False)
        church.save()
        return redirect('church_list')


class churchUpdateView(UpdateView):
    model = Church
    template_name = 'church/update_church.html'
    pk_url_kwarg = 'church_pk'
    fields = ('church_vision','church_mission','maps_embedded_link','church_name', 'church_code',
              'address', 'phone', 'registration_date', 'email_address', 'Post_Office_Box',
              'footer', 'enable_frontend', 'latitude', 'longitude', 'facebook_url','twitter_url', 
              'linkedIn_url', 'google_plus_url', 'youtube_url', 'instagram_url', 'pinterest_url',
              'status', 'frontend_Logo', 'backend_Logo')
    def get_form(self):
        form = super().get_form()
        form.fields['registration_date'].widget = DatePickerInput()
        return form

    def form_valid(self, form):
        church = form.save(commit=False)
        church.save()
        return redirect('church_list')


class churchListView(ListView):
    model = Church
    template_name = 'church/church_list.html'
    context_object_name = 'churches'


def save_church_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            churches = Church.objects.all()
            data['html_church_list'] = render_to_string('church/includes/partial_church_list.html', {
                'churches': churches
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def church_view(request, church_pk):
    church = get_object_or_404(Church, pk=church_pk)
    if request.method == 'POST':
        form = churchForm(request.POST, instance=church)
    else:
        form = churchForm(instance=church)
    return save_church_form(request, form, 'church/includes/partial_church_view.html')


def church_delete(request, church_pk):
    church = get_object_or_404(Church, pk=church_pk)
    data = dict()
    if request.method == 'POST':
        church.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        churches = Church.objects.all()
        data['html_church_list'] = render_to_string('church/includes/partial_church_list.html', {
            'churches': churches
        })
    else:
        context = {'church': church}
        data['html_form'] = render_to_string('church/includes/partial_church_delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)



     ###################################################
    #                 BUILDING MODULE                  #
     ###################################################

#recording offerings
@login_required
def record_building_collections(request):
    if request.method=="POST":
        form=BuildingRenovationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Building Collections have been recorded')
            return redirect('record-building-collections')
    else:
        form=BuildingRenovationForm()
        return render(request, 'BuildingRenovation/record_building_collections.html',{'form':form})


def Building_Renovation_report(request):
    if request.method=='POST':
        items = BuildingRenovation.objects.all()
        for item in items:
            item.Archived_Status = 'ARCHIVED'
            item.save()
        messages.success(request, f'All Building Collections have been Archived')
        return redirect('Building-Renovation-report')
    today = datetime.now()
    years=today.year
    context={}
    items = BuildingRenovation.objects.filter(Archived_Status="NOT-ARCHIVED")
    context['items']=items
    context['years']=years
    context['today']=today
    return render(request, 'BuildingRenovation/Building_Renovation_report.html', context)

@login_required
def BuildingRenovationarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = BuildingRenovation.objects.filter(Archived_Status='ARCHIVED', Date__month=report_month, Date__year=report_year)
        years = datetime.now().year
        today = datetime.now()
        context = {'archived_reports': archived_reports,'years': years,
                  'today': today,'report_year': report_year,'report_month': report_month
                   }
        return render(request, "BuildingRenovation/buildingarchive.html", context)
    years = datetime.now().year
    context = {'years': years,}
    return render(request, "BuildingRenovation/buildingarchive.html", context)
