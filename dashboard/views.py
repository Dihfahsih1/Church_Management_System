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
from django.db.models import Q
from .forms import *
from .models import *
from time import strptime
from .render import Render
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import calendar
from dal import autocomplete
import json
import urllib
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string
from .tokens import account_activation_token  
from django.core.mail import EmailMessage

# #######################################===>BEGINNING OF THEME MODULE<===############################################
class ThemeListView(ListView):
    model = Theme
    template_name = 'themes/theme.html'
    context_object_name = 'themes'

def theme_activate(request, theme_pk):
    theme = Theme.objects.get(pk=theme_pk)
    unset_theme = Theme.objects.get(is_active='Yes')
    unset_theme.is_active = 'No'
    theme.is_active = 'Yes'
    theme.save()
    unset_theme.save()
    return redirect('theme_list')

########========================>AUTOSUGGEST OF NAMES FROM DATABASES<==============================#######
class Autocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Members.objects.all()
        if self.q:
            qs = qs.filter(Q(First_Name__istartswith=self.q) | Q(Second_Name__istartswith=self.q))
            return qs

########========================>FETCH FROM THE DATABASE TO THE WEBSITE<==========================#######
def web(request):
    news = News.published.all().order_by('-id')
    events = Event.published.all().order_by('-id')
    images = Image.published.all().order_by('-id')
    members = Members.published.filter(is_active=True).order_by('-id')
    ministry = Ministry.published.all().order_by('-id')
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
        'ministry':ministry,
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


###############=============================>EMPLOYEE MODULE<====================================###################
@login_required
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
@login_required
def edit_employee(request, pk):
    item = get_object_or_404(StaffDetails, pk=pk)
    if request.method == "POST":
        form = StaffDetailsForm(request.POST, request.FILES, instance=item)
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
    return render(request, 'Employees/edit_employee.html', context)
@login_required
def view_employee(request, pk):
    employees = get_object_or_404(StaffDetails, pk=pk)
    if request.method == 'POST':
        form = StaffDetailsForm(request.POST, instance=employees)
    else:
        form = StaffDetailsForm(instance=employees)
    return save_news_form(request, form, 'Employees/includes/partial_employee_view.html')

@login_required
def paying_employees(request, pk):
    items = get_object_or_404(StaffDetails, id=pk)
    if request.method == "POST":
        form = StaffDetailsForm(request.POST, request.FILES, instance=items)
    else:
        form = StaffDetailsForm(instance=items)
        retrieve_employee_id = StaffDetails.objects.filter(id=pk)
        context = {'form': form, 'retrieve_employee_id': retrieve_employee_id}
        return render(request, 'Employees/pay_employee.html', context)
@login_required
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
@login_required          
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
            sal_archiveobj=SalariesPaidReportArchive()
            sal_archiveobj.Date_of_paying_salary=date
            sal_archiveobj.Salary_Amount=amount
            sal_archiveobj.Salary_Id=salary_id
            sal_archiveobj.Name=name
            sal_archiveobj.Month_being_cleared=mth
            sal_archiveobj.archivedyear= archived_year
            sal_archiveobj.archivedmonth =archived_month
            sal_archiveobj.save()

        
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

@login_required
def delete_salary_paid(request,pk):
    salary= get_object_or_404(SalariesPaid, id=pk)
    if request.method == "GET":
        salary.delete()
        messages.success(request, "Salary Paid successfully deleted!")
        return redirect("current-month-salaries")

@login_required
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
                   'months': months,'years': years,'archived_salaries':archived_salaries,
                   'total_amount': total_amount,'today': today,'report_year': report_year,
                   'report_month': report_month}
        return render(request, "Employees/salariespaidarchive.html", context)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September','October',  'November', 'December']
    years = datetime.now().year
    archived_salaries=SalariesPaidReportArchive.objects.all()
    context = {'months': months,'years': years,'archived_salaries': archived_salaries}
    return render(request, "Employees/salariespaidarchive.html", context)    

    ####################================>MEMBERSHIP MODULE<=================####################
@login_required
def register_members(request):
    if request.method=="POST":
        form=MembersForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            messages.success(request, f'Member has been registered successfully')
            return redirect('members-list')
    else:
        form=MembersForm()
        return render(request, 'Members/register_members.html',{'form':form})

def Online_Registration(request):
    if request.method=="POST":
        form=MembersForm(request.POST, request.FILES,)
        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' email activation '''
            member = form.save(commit=False)
            member.save()
            current_site = get_current_site(request)  
            mail_subject = 'Activate your account.'  
            message = render_to_string('acc_active_email.html', {  
                'member': member,  
                'domain': current_site.domain,  
                'uid': urlsafe_base64_encode(force_bytes(member.pk)),  
                'token': account_activation_token.make_token(member),  
                }) 
            to_email = form.cleaned_data.get('Email')  
            email = EmailMessage(  
                mail_subject, message, to=[to_email]  
            )  
            email.send()
            context={'member':member}
            return render(request, 'activation_email_sent.html', context) 

        else:
            form_errors=form.errors
            context={'form':form,'form_errors':form_errors}
            return render(request, 'Members/online_registration.html', context)   
    else:
        form=MembersForm()
        context={'form':form}
        return render(request, 'Members/online_registration.html', context)
#activate your email address
def activate_email(request, uidb64, token):  
        try:  
            uid = force_text(urlsafe_base64_decode(uidb64)) 
            member = Members.objects.get(id=uid)  
        except(TypeError, ValueError, OverflowError, Members.DoesNotExist):  
            member = None  
        if member is not None and account_activation_token.check_token(member, token): 
            # member.is_active=True
            # member.save()
            context={'first_name':member}
            return render(request, 'email_confirmed.html', context)  
        else:  
            return HttpResponse('Activation link is invalid!')
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

@login_required
def members_list(request):
    membership = Members.objects.filter(is_active=True).order_by('-id')
    day=datetime.now()
    context ={'membership': membership, 'day':day}
    return render(request, 'Members/members_list.html', context)

@login_required
def members_archived(request):
    membership = Members.objects.filter(is_active=False, Archived_Status='ARCHIVED').order_by('-id')
    for i in membership:
        (i.Home_Cell)
    day=datetime.now()
    context ={'membership': membership, 'day':day}
    return render(request, 'Members/members_archived.html',context) 
# @login_required
# def view_request_details(request,pk):
#     members = get_object_or_404(Members, pk=pk)
#     if request.method == 'POST':
#         form = MembersForm(request.POST, instance=members)
#     else:
#         form = MembersForm(instance=members)
#     return save_news_form(request, form, 'Members/includes/partial_members_view.html') 
@login_required
def approve_member(request, pk):
    if request.method == "GET":
        item = Members.objects.get(is_active=False, id=pk)
        item.is_active='True'
        item.save()
        messages.success(request, f'Member has been Approved')
        return redirect('un-approved-list')

@login_required
def reject_request(request, pk):
    if request.method == "GET":
        item = Members.objects.get(is_active=False, id=pk)
        item.delete()
        messages.success(request, f'Membership Request has been Rejected')
        return redirect('un-approved-list')

@login_required        
def un_approved_members_list(request):        
    get_all_unapproved=Members.objects.filter(is_active=False, Archived_Status='NOT-ARCHIVED')
    context={'get_all_unapproved':get_all_unapproved}
    return render(request,'Members/unapproved-members-list.html', context)

@login_required
def archive_member(request, pk):
    if request.method == "GET":
        item = Members.objects.get(id=pk)
        try:
            if User.objects.get(full_name = item):
                get_user=User.objects.get(full_name = item)
                get_user.is_active ='False'
                get_user.save() 
        except:
            item.is_active='False'    
            item.Archived_Status='ARCHIVED'
            item.save()
        messages.success(request, f'Member has been Archived')
        return redirect('members-list')

@login_required            
def unarchive_member(request, pk):
   if request.method == "GET":
        item = Members.objects.get(id=pk)
        try:
            if User.objects.get(full_name = item):
                get_user=User.objects.get(full_name = item)
                get_user.is_active ='True'
                get_user.save() 
        except:
            item.is_active='True'    
            item.Archived_Status='NOT-ARCHIVED'
            item.save()
        messages.success(request, f'Member has been un Archived successfully')
        return redirect('members-list')


def church_pastors(request):
    pastors = Members.published.all()
    return render(request, 'Members/pastoral_team.html', {'pastors': pastors})

def church_administration(request):
    staffs = User.published.filter(Q(Role='Assistant_Admin') | Q(Role='Admin') | Q(Role='SuperAdmin') | Q(Role='Secretary')| Q(Role='Youth Leader'))
    return render(request, 'Members/administration_team.html', {'staffs': staffs})  

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
        context = {'form': form, 'item':item}
    return render(request, 'Members/edit_member_details.html', context)

  
def view_member(request, pk):
    members = get_object_or_404(Members, pk=pk)
    if request.method == 'POST':
        form = MembersForm(request.POST, instance=members)
    else:
        form = MembersForm(instance=members)
    return save_news_form(request, form, 'Members/includes/partial_members_view.html') 

  
def membership_wall(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(First_Name__icontains=query) | Q(Second_Name__icontains=query)
            results= Members.objects.filter(lookups, is_active=True).distinct()
            content={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'Members/members_wall.html', content)
    
    all_members = Members.published.filter(is_active=True).order_by('-id')
    paginator = Paginator(all_members, 9)  
    page = request.GET.get('page')
    try:
        members_list = paginator.page(page)
    except PageNotAnInteger:
        members_list = paginator.page(1)
    except EmptyPage:
        members_list = paginator.page(paginator.num_pages)
    context={'page':page, 'members_list': members_list}    
    return render(request, 'Members/members_wall.html', context)

def member_detail(request, pk):
    member = get_object_or_404(Members, pk=pk)
    mem_details=Members.objects.filter(is_active=True)
    number_of_registered_members=mem_details.count()
    more_details = Members.published.order_by('-date')
    paginator = Paginator(mem_details, 7) 
    page = request.GET.get('page')
    try:
        members_list = paginator.page(page)
    except PageNotAnInteger:
        members_list = paginator.page(1)
    except EmptyPage:
        members_list = paginator.page(paginator.num_pages)
    context = {
         'page':page,
        'member': member,
        'more_details': more_details,
        'members_list': members_list,
        'number_of_registered_members':number_of_registered_members
    }
    return render(request, 'Members/member_details.html', context)

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

     #############==============>BUILDING MODULE<============#############  
      
@login_required
def record_building_collections(request):
    if request.method=="POST":
        form=RevenuesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Building Collections have been recorded')
            return redirect('Building-Renovation-report')
    else:
        form=RevenuesForm()
        return render(request, 'BuildingRenovation/record_building_collections.html',{'form':form})

#editing building collections
@login_required
def edit_building_collections(request, pk):
    item = get_object_or_404(Revenues, pk=pk)
    if request.method == "POST":
        form = RevenuesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Building Collections have been updated')
            return redirect('Building-Renovation-report')
    else:
        form = RevenuesForm(instance=item)
    return render(request, 'BuildingRenovation/edit_building_collections.html', {'form': form})

# generate building report
def Building_Renovation_report(request):
    if request.method=='POST':
        items = Revenues.objects.all().order_by('-id')
        for item in items:
            item.Archived_Status = 'ARCHIVED'
            item.save()
        messages.success(request, f'All Building Collections have been Archived')
        return redirect('Building-Renovation-report')
    today = datetime.now()
    years=today.year
    context={}
    items = Revenues.objects.filter(Archived_Status="NOT-ARCHIVED",Revenue_filter='build').order_by('-id')
    context['items']=items
    context['years']=years
    context['today']=today
    return render(request, 'BuildingRenovation/Building_Renovation_report.html', context)

#Search for archived building reports
@login_required
def BuildingRenovationarchivessearch(request):
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = Revenues.objects.filter(Archived_Status='ARCHIVED',Revenue_filter='build', Date__month=report_month, Date__year=report_year)
        years = datetime.now().year
        today = datetime.now()
        context = {'archived_reports': archived_reports,'years': years,
                  'today': today,'report_year': report_year,'report_month': report_month
                   }
        return render(request, "BuildingRenovation/buildingarchive.html", context)
    years = datetime.now().year
    context = {'years': years,}
    return render(request, "BuildingRenovation/buildingarchive.html", context)

####################=================>GENERAL OFFERINGS MODULE<===================###################
@login_required
def Enter_Offerings(request):
    if request.method=="POST":
        form=RevenuesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Offerings have been recorded')
            return redirect('Offeringsreport')
    else:
        form=RevenuesForm()
        return render(request, 'Offerings/record_offerings.html',{'form':form})

#edit offerings
@login_required
def edit_offerings(request, pk):
    if request.user.Role == 'SuperAdmin' or 'Secretary ' or 'Admin' or 'Assistant_Admin':
        item = get_object_or_404(Revenues, pk=pk)
        if request.method == "POST":
            form = RevenuesForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                messages.success(request, f'Offerings have been updated')
                return redirect('Offeringsreport')
        else:
            form = RevenuesForm(instance=item)
        return render(request, 'Offerings/edit_offerings.html', {'form': form})
    else:
        return HttpResponse('You are forbidden from accessing this functionality')    

# generating offerings report
@login_required
def Offeringsreport (request):
    if request.method=='POST':
        items = Revenues.objects.all().order_by('-id')
        for item in items:
            item.Archived_Status = 'ARCHIVED'
            item.save()
        messages.success(request, f'General Offerings Report has been Archived')
        return redirect('Offeringsreport')
    today = datetime.now()
    years=today.year
    context={}
    items = Revenues.objects.filter(Archived_Status="NOT-ARCHIVED",Revenue_filter='offering')
    context['items']=items
    context['years']=years
    context['today']=today
    return render(request, 'Offerings/offeringsindex.html', context)

#search for the archived offerings
@login_required
def offeringsarchivessearch(request):
    today = datetime.now()
    years=today.year
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = Revenues.objects.filter(Archived_Status='ARCHIVED',Revenue_filter='offering', Date__month=report_month, Date__year=report_year)
        mth=int(report_month)
        report_month=calendar.month_name[mth]
        context = {'archived_reports': archived_reports,'years': years,'today': today,
                  'report_year':report_year,'report_month': report_month}
        return render(request, "Offerings/offeringsarchive.html", context)
    context = {'years': years}
    return render(request, "Offerings/offeringsarchive.html", context)

#generate offering archived report pdf    
class offeringsarchivepdf(View):
    def get(self, request, report_year, report_month):
        month=strptime(report_month, '%B').tm_mon
        archived_offerings = Revenues.objects.filter(Date__month=month, Date__year=report_year, Archived_Status='ARCHIVED',Revenue_filter='offering').order_by('-Date')
        today = datetime.now()
        month=today.strftime('%B')
        total = archived_offerings.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        offeringscontext = {
            'report_year':report_year,
            'report_month':report_month,
            'today': today,
            'month': month,
            'total_amount': total_amount,
            'request': request,
            'archived_offerings': archived_offerings,}
        return Render.render('Offerings/offeringsarchivepdf.html', offeringscontext)  

#offering
class offeringspdf(View):
    def get(self, request):
        current_month = datetime.now().month
        offerings = Revenues.objects.filter(Archived_Status='NOT-ARCHIVED',Revenue_filter='offering').order_by('-Date')
        today = datetime.now()
        month = today.strftime('%B')
        totalexpense = 0
        for instance in offerings:
            totalexpense += instance.Amount
        context = {
            'month': month,
            'today': today,
            'offerings': offerings,
            'request': request,
            'totalexpense': totalexpense,
        }
        return Render.render('Offerings/offeringspdf.html', context)

##################=====================>SEEDS OFFERING MODULE<=========================#############################   
@login_required
def add_seeds(request):
    if request.method=="POST":
        form=RevenuesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Seeds-report')
    else:
        form=RevenuesForm()
        context={'form':form}
        return render(request, 'Seeds/add_seeds.html',context)  

@login_required
def Seedsreport (request):
    if request.method=='POST':
        items = Revenues.objects.all().order_by('-id')
        for item in items:
            item.Archived_Status = 'ARCHIVED'
            item.save()
        messages.success(request, f'Seeds Offerings Report has been Archived')
        return redirect('Seeds-report')
    today = datetime.now()
    years=today.year
    context={}
    items = Revenues.objects.filter(Archived_Status="NOT-ARCHIVED",Revenue_filter='seeds')
    context['items']=items
    context['years']=years
    context['today']=today
    return render(request, 'Seeds/Seedsindex.html', context)

@login_required
def seedsarchivessearch(request):
    today = datetime.now()
    years=today.year
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = Revenues.objects.filter(Archived_Status='ARCHIVED',Revenue_filter='seeds', Date__month=report_month, Date__year=report_year)
        mth=int(report_month)
        report_month=calendar.month_name[mth]
        context = {'archived_reports': archived_reports,'years': years,'today': today,
                  'report_year':report_year,'report_month': report_month}
        return render(request, "Seeds/seedsarchive.html", context)
    context = {'years': years}
    return render(request, "Seeds/seedsarchive.html", context)

def edit_seed(request, pk):
    item = get_object_or_404(Revenues, pk=pk)
    if request.method == "POST":
        form = RevenuesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Seeds-report')
    else:
        today = timezone.now()
        month = today.strftime('%B')
        form = RevenuesForm(instance=item)        
        context={'form':form, 'month':month}
    return render(request, 'Seeds/edit_seeds.html', context)

class seed_offering_receipt(View):
    def get(self, request, pk):
        seeds= get_object_or_404(Revenues,pk=pk)
        today = datetime.now()
        context = { 'today': today,'seeds': seeds,'request': request,}
        return Render.render('Seeds/seed_offerings_receipt.html', context)

##############################<===========TITHES MODULE===========>################################# 
@login_required
def recording_tithes(request):
    if request.method=="POST":
        form=RevenuesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Member Tithe has been recorded')
            return redirect('Tithesreport')
    else:
        form=RevenuesForm()
        today = datetime.now()
        context={'form':form}
        return render(request, 'Tithes/record_tithes.html',context)

#record member tithes after name search        
def record_member_tithe(request, pk):
    if Revenues.objects.filter(Member_Name__id=pk).exists():
        get_member_name=get_object_or_404(Members, pk=pk)
        current_year = datetime.now().year
        get_latest_tithe = Revenues.objects.filter(Member_Name__id=pk, Date__year=current_year, Revenue_filter='tithes').latest('Date')
        if request.method=="POST":
            form=RevenuesForm(request.POST)
            messages.success(request, f'Member Tithe has been recorded')
            if form.is_valid():
                form.save()
                return redirect('Tithesreport')
        else:
            form=RevenuesForm(instance=get_latest_tithe)
            
            context={'form':form, 'get_member_name':get_member_name}
        return render(request, 'Tithes/record_member_tithe.html',context)
    else:
        return redirect('Enter_Tithes')

def edit_tithes(request, pk):
    item = get_object_or_404(Revenues, pk=pk)
    if request.method == "POST":
        form = RevenuesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Tithesreport')
    else:
        form = RevenuesForm(instance=item)       
        context={'form':form, 'item':item}
    return render(request, 'Tithes/edit_tithes.html', context)

@login_required
def Tithesreport (request):
    if request.method=='POST':
        items = Revenues.objects.all().order_by('-id')
        for item in items:
            item.Archived_Status = 'ARCHIVED'
            item.save()
        messages.success(request, f'Tithes Report has been Archived')
        return redirect('Tithesreport')
    today = datetime.now()
    month = today.month
    years=today.year
    context={}
    items = Revenues.objects.filter(Archived_Status="NOT-ARCHIVED",Revenue_filter='tithes', Date__year=years).order_by('-Date')
    context['items']=items
    context['years']=years
    context['today']=today
    return render(request, 'Tithes/tithesindex.html', context)    


@login_required
def Annual_Tithes(request):
    current_year = datetime.now().year
    get_all_members=Members.objects.filter(is_active=True)
    results = Revenues.objects.filter(Archived_Status='ARCHIVED',
                                          Revenue_filter='tithes', Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    if (results['totals']):
        all_tithes = results["totals"]
    else:
        all_tithes = 0  
    context={'all_tithes': all_tithes,'get_all_members':get_all_members, 'current_year':current_year}
    return render(request, "Tithes/current_year_tithes.html", context)

class member_annual_tithes_pdf(View):
    def get(self, request, pk):
        today = datetime.now()
        year=today.year
        get_member_name = get_object_or_404(Members, pk=pk)
        tithes = Revenues.objects.filter(Member_Name__id = pk, Revenue_filter='tithes', Date__year=year).order_by('-Date')
        month=today.strftime('%B')
        total = tithes.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'year' : year,'month' : month, 'today': today,'total_amount': total_amount,
            'request': request,'tithes': tithes,'get_member_name':get_member_name}
        return Render.render('Tithes/memeber_annual_tithes_pdf.html', context)

@login_required
def tithesarchivessearch(request):
    today = datetime.now()
    years=today.year
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = Revenues.objects.filter(Archived_Status='ARCHIVED',Revenue_filter='tithes', Date__month=report_month, Date__year=report_year)
        results =archived_reports.aggregate(totals=models.Sum('Amount'))
        if results['totals']:
            total_tithes = results['totals']
        else:
            total_tithes = 0    
        mth=int(report_month)
        report_month=calendar.month_name[mth]
        context = {'total_tithes': total_tithes, 'archived_reports': archived_reports, 'years': years, 'today': today,
                  'report_year':report_year,'report_month': report_month}
        return render(request, "Tithes/tithesarchive.html", context)
    context = {'years': years}
    return render(request, "Tithes/tithesarchive.html", context)

class tithespdf(View):
    def get(self, request):
        today = datetime.now()
        mth=today.month
        year=today.year
        tithes = Revenues.objects.filter(Revenue_filter='tithes',Date__month=mth, Date__year=year).order_by('-Date')
        month=today.strftime('%B')
        total = tithes.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {
           'year' : year,
            'today': today,
            'month': month,
            'total_amount': total_amount,
            'request': request,
            'tithes': tithes,}
        return Render.render('Tithes/tithespdf.html', context)

class tithesreceipt(View):
    def get(self, request, pk):
        tithes= get_object_or_404(Revenues,pk=pk)
        today = timezone.now()
        context = {
            'today': today,
            'tithes': tithes,
            'request': request,
        }
        return Render.render('Tithes/tithesreceipt.html', context)

class tithesarchivepdf(View):
    def get(self, request, report_month, report_year):        
        month=strptime(report_month, '%B').tm_mon
        archived_tithes = Revenues.objects.filter(Archived_Status='ARCHIVED',Revenue_filter='tithes',Date__month=month, Date__year=report_year)
        today = datetime.now()
        total = archived_tithes.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        tithescontext = {'report_month': report_month,'report_year':report_year,'today': today,'total_amount': total_amount,
            'request': request,'archived_tithes': archived_tithes,}
        return Render.render('Tithes/tithesarchivepdf.html', tithescontext)

@login_required
def member_annual_tithes(request, pk):
    years = timezone.now().year
    tithes=Revenues.objects.filter(Member_Name_id=pk, Date__year=years,Revenue_filter='tithes').order_by('-pk')
    total = tithes.aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    members=Members.objects.filter(id=pk)
    tithescontext={'years':years,'tithes':tithes, 'members':members, 'total_amount':total_amount}
    return render(request, 'Tithes/member_annual_tithes.html', tithescontext) 

     #####################===============>THANKS GIVING MODULE<=================###########################

@login_required
def record_thanks_giving(request):
    if request.method=="POST":
        form=RevenuesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks-giving-report')
    else:
        form=RevenuesForm()
        today = datetime.now()
        month = today.strftime('%b')
        context={'form':form, 'month':month}
        return render(request, 'ThanksGiving/record_thanks_giving.html',context)

@login_required
def thanks_giving_report(request):
    if request.method=='POST':
        items = Revenues.objects.all()
        for item in items:
            item.Archived_Status = 'ARCHIVED'
            item.save()
        messages.success(request, f'Thanks Giving Report has been Archived')
        return redirect('thanks-giving-report')
    today = datetime.now()
    years=today.year
    context={}
    items = Revenues.objects.filter(Archived_Status="NOT-ARCHIVED",Revenue_filter='thanks')
    context['items']=items
    context['years']=years
    context['today']=today
    return render(request, 'ThanksGiving/thanksgivingindex.html', context)

def edit_thanks_giving(request, pk):
    item = get_object_or_404(Revenues, pk=pk)
    if request.method == "POST":
        form = RevenuesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('thanks-giving-report')
    else:
        today = timezone.now()
        form = RevenuesForm(instance=item)        
        context={'form':form}
    return render(request, 'ThanksGiving/edit_thanks_giving.html', context)

@login_required
def thanksgivingarchivessearch(request):
    today = datetime.now()
    years=today.year
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = Revenues.objects.filter(Archived_Status='ARCHIVED',Revenue_filter='thanks', Date__month=report_month, Date__year=report_year)
        mth=int(report_month)
        report_month=calendar.month_name[mth]
        context = {'archived_reports': archived_reports,'years': years,'today': today,
                  'report_year':report_year,'report_month': report_month}
        return render(request, "ThanksGiving/thanksgivingarchivessearch.html", context)
    context = {'years': years}
    return render(request, "ThanksGiving/thanksgivingarchivessearch.html", context)

     ################<=================== OTHER REVENUE SOURCES MODULE==================>######################
@login_required
def record_donations(request):
    if request.method=="POST":
        form=RevenuesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donations-report')
    else:
        form=RevenuesForm()
        context={'form':form,}
        return render(request, 'Donations/record_donations.html',context)

@login_required
def donations_report(request):
    if request.method=='POST':
        items = Revenues.objects.all()
        for item in items:
            item.Archived_Status = 'ARCHIVED'
            item.save()
        messages.success(request, f'Other Sources Of Revenue Report has been Archived')
        return redirect('donations-report')
    today = datetime.now()
    years=today.year
    context={}
    items = Revenues.objects.filter(Archived_Status="NOT-ARCHIVED",Revenue_filter='others')
    context['items']=items
    context['years']=years
    context['today']=today
    return render(request, 'Donations/donationsindex.html', context)

def edit_donation(request, pk):
    item = get_object_or_404(Revenues, pk=pk)
    if request.method == "POST":
        form = RevenuesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('donations-report')
    else:
        today = datetime.now()
        month = today.strftime('%B')
        form = RevenuesForm(instance=item)        
        context={'form':form, 'month':month}
    return render(request, 'Donations/edit_donations.html', context)

@login_required
def donationsarchivessearch(request):
    today = datetime.now()
    years=today.year
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = Revenues.objects.filter(Archived_Status='ARCHIVED',Revenue_filter='others', Date__month=report_month, Date__year=report_year)
        mth=int(report_month)
        report_month=calendar.month_name[mth]
        context = {'archived_reports': archived_reports,'years': years,'today': today,
                  'report_year':report_year,'report_month': report_month}
        return render(request, "Donations/donationssarchive.html", context)
    context = {'years': years}
    return render(request, "Donations/donationssarchive.html", context)


####################<============== GENERAL, MAIN, PETTY EXPENSES MODULES [expenses module] ==========>############################
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

@login_required
def general_expenses_archives_search(request):
    today = datetime.now()
    years=today.year
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = Expenditures.objects.filter(Archived_Status='ARCHIVED', Reason_filtering='general',Date__month=report_month, Date__year=report_year)
        mth=int(report_month)
        report_month=calendar.month_name[mth]
        context = {'archived_reports': archived_reports,'years': years,'today': today,
                  'report_year': report_year,'report_month': report_month}
        return render(request, "Expenses/general_expenses_archived_search.html", context)
    context = {'years': years}
    return render(request, "Expenses/general_expenses_archived_search.html", context) 
    
class general_expenses_archived_pdf(View):
    def get(self, request, report_month, report_year):        
        month=strptime(report_month, '%B').tm_mon
        archived = Expenditures.objects.filter(Archived_Status='ARCHIVED', Reason_filtering='general',Date__month=month, Date__year=report_year)
        today = datetime.now()
        total = archived.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'report_month': report_month,'report_year':report_year,'today': today,
        'total_amount': total_amount,'request': request,'archived': archived,}
        return Render.render('Expenses/generel_expenses_archived_pdf.html', context)


@login_required
def general_expenses_report (request):
    if request.method=='POST':
        items = Expenditures.objects.all()
        for item in items:
            item.Archived_Status = 'ARCHIVED'
            item.save()
        messages.success(request, f'All General Expenses have been Archived')
        return redirect('general-expenses-report')
    today = datetime.now()
    years=today.year
    context={}
    items = Expenditures.objects.filter(Archived_Status="NOT-ARCHIVED",Reason_filtering='general')
    context['items']=items
    context['years']=years
    context['today']=today
    return render(request, 'Expenses/General_Expenses_report.html', context)

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


@login_required
def enter_main_expenses(request):
    if request.method=="POST":
        form=ExpendituresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenditurereport')
    else:
        form=ExpendituresForm()
        context = {'form': form}
        return render(request, 'Expenses/pay_main_expenses.html',context)

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
    return render(request, 'Expenses/edit_petty_cash.html', {'item':item,'form': form})

@login_required
def main_expenses_report (request):
    if request.method=='POST':
        items = Expenditures.objects.all()
        for item in items:
            item.Archived_Status = 'ARCHIVED'
            item.save()
        messages.success(request, f'All Main Expenses have been Archived')
        return redirect('expenditurereport')
    today = datetime.now()
    years=today.year
    context={}
    items = Expenditures.objects.filter(Archived_Status="NOT-ARCHIVED",Reason_filtering='main')
    context['items']=items
    context['years']=years
    context['today']=today
    return render(request, 'Expenses/Main_Expenses_report.html', context)

@login_required
def main_expenses_archives_search(request):
    today = datetime.now()
    years=today.year
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = Expenditures.objects.filter(Archived_Status='ARCHIVED',Reason_filtering='main', Date__month=report_month, Date__year=report_year)
        mth=int(report_month)
        report_month=calendar.month_name[mth]
        context = {'archived_reports': archived_reports,'years': years,'today': today,
                  'report_year': report_year,'report_month': report_month}
        return render(request, "Expenses/main_expenses_archived_search.html", context)
    context = {'years': years}
    return render(request, "Expenses/main_expenses_archived_search.html", context)

class main_expenses_archived_pdf(View):
    def get(self, request, report_month, report_year):        
        month=strptime(report_month, '%B').tm_mon
        archived = Expenditures.objects.filter(Archived_Status='ARCHIVED', Reason_filtering='main',\
        Date__month=month, Date__year=report_year)
        today = datetime.now()
        total = archived.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'report_month': report_month,'report_year':report_year,'today': today,
        'total_amount': total_amount,'request': request,'archived': archived,}
        return Render.render('Expenses/main_expenses_archived_pdf.html', context)

class petty_expenses_archived_pdf(View):
    def get(self, request, report_month, report_year):        
        month=strptime(report_month, '%B').tm_mon
        archived = Expenditures.objects.filter(Archived_Status='ARCHIVED', Reason_filtering='petty',\
        Date__month=month, Date__year=report_year)
        today = datetime.now()
        total = archived.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        context = {'report_month': report_month,'report_year':report_year,'today': today,
        'total_amount': total_amount,'request': request,'archived': archived,}
        return Render.render('Expenses/sundryarchivepdf.html', context)

def petty_cash_report (request):
    if request.method=='POST':
        items = Expenditures.objects.all()
        for item in items:
            item.Archived_Status = 'ARCHIVED'
            item.save()
        messages.success(request, f'All Petty Cash have been Archived')
        return redirect('sundryreport')
    today = datetime.now()
    years=today.year
    context={}
    items = Expenditures.objects.filter(Archived_Status="NOT-ARCHIVED",Reason_filtering='petty').order_by('-Date')
    context['items']=items
    context['years']=years
    context['today']=today
    return render(request, 'Expenses/Petty_Cash_report.html', context)
    
@login_required
def petty_cash_archives_search(request):
    today = datetime.now()
    years=today.year
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = Expenditures.objects.filter(Archived_Status='ARCHIVED',Reason_filtering='petty', Date__month=report_month, Date__year=report_year)
        mth=int(report_month)
        report_month=calendar.month_name[mth]
        context = {'archived_reports': archived_reports,'years': years,'today': today,
                  'report_year': report_year,'report_month': report_month}
        return render(request, "Expenses/petty_cash_archived_search.html", context)
    context = {'years': years}
    return render(request, "Expenses/petty_cash_archived_search.html", context)

class main_expenditure_report_pdf(View):
    def get(self, request):
        current_month = datetime.now().month
        current_year = datetime.now().year
        expenses = Expenditures.objects.filter(Archived_Status='NOT-ARCHIVED', Reason_filtering='main'\
        ,Date__year=current_year)
        today = datetime.now()
        year=today.year
        month = today.strftime('%B')
        totalexpense = 0
        for instance in expenses:
            totalexpense += instance.Amount
        context ={'year':year,'month': month,'today':today,'expenses':expenses,'request': request,'totalexpense': totalexpense,
        }
        return Render.render('Expenses/pdf_main_expenditure_report.html',context)

class general_expenditure_report_pdf(View):
    def get(self, request):
        current_month = datetime.now().month
        current_year = datetime.now().year
        expenses = Expenditures.objects.filter(Archived_Status='NOT-ARCHIVED', Reason_filtering='general'\
        ,Date__year=current_year)
        today = datetime.now()
        year=today.year
        month = today.strftime('%B')
        totalexpense = 0
        for instance in expenses:
            totalexpense += instance.Amount
        context ={'year':year,'month': month,'today':today,'expenses':expenses,'request': request,'totalexpense': totalexpense,
        }
        return Render.render('Expenses/pdf_general_expenditure_report.html',context)



class petty_expenditure_report_pdf(View):
    def get(self, request):
        current_month = datetime.now().month
        current_year = datetime.now().year
        expenses = Expenditures.objects.filter(Archived_Status='NOT-ARCHIVED', Reason_filtering='petty'\
        ,Date__year=current_year)
        today = datetime.now()
        year=today.year
        month = today.strftime('%B')
        totalexpense = 0
        for instance in expenses:
            totalexpense += instance.Amount
        context ={'year':year,'month': month,'today':today,'expenses':expenses,'request': request,'totalexpense': totalexpense,
        }
        return Render.render('Expenses/sundrypdf.html',context)

#Allowances Module
@login_required
def give_allowance(request):
    month = datetime.now().month
    current_month = calendar.month_name[month]
    if request.method=="POST":
        form=ExpendituresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allowancereport')   
    else:
        form = ExpendituresForm()
        context={'form': form, 'current_month': current_month}
        return render(request, 'Allowances/record_new_allowance.html',context)

@login_required
def edit_allowance(request, pk):
    item = get_object_or_404(Expenditures, pk=pk)
    if request.method == "POST":
        form = ExpendituresForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('allowancereport')
    else:
        form = ExpendituresForm(instance=item)
    return render(request, 'Allowances/edit_allowance.html', {'form': form})

@login_required
def allowancereport(request):
    if request.method=='POST':
        items = Expenditures.objects.all()
        for item in items:
            item.Archived_Status = 'ARCHIVED'
            item.save()
        messages.success(request, f'All Allowances Given Out have been Archived')
        return redirect('allowancereport')
    today = datetime.now()
    years=today.year
    context={}
    items = Expenditures.objects.filter(Archived_Status="NOT-ARCHIVED",Reason_filtering='allowance')
    context['items']=items
    context['years']=years
    context['today']=today
    return render(request, 'Allowances/allowanceindex.html', context)

class allowancespdf(View):
    def get(self, request):
        current_month = datetime.now().month
        current_year = datetime.now.year
        allowances = Expenditures.objects.filter( Archived_Status='NOT-ARCHIVED',Date__month=current_month,Date__year=current_year).order_by('-Date')
        today = datetime.now()
        year=today.year
        month = today.strftime('%b')
        totalAllowance = 0
        for instance in allowances:
            totalAllowance += instance.Amount
        Allowancecontext ={
            'year':year,
            'month': month,
            'today':today,
            'allowances':allowances,
            'request': request,
            'totalAllowance': totalAllowance,
        }
        return Render.render('Allowances/allowancespdf.html',Allowancecontext)

@login_required
def allowancearchivessearch(request):
    today = datetime.now()
    years=today.year
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = Expenditures.objects.filter(Archived_Status='ARCHIVED',Reason_filtering='allowance', Date__month=report_month, Date__year=report_year)
        mth=int(report_month)
        report_month=calendar.month_name[mth]
        context = {'archived_reports': archived_reports,'years': years,'today': today,
                  'report_year': report_year,'report_month': report_month}
        return render(request, "Allowances/allowancearchive.html", context)
    context = {'years': years}
    return render(request, "Allowances/allowancearchive.html", context)        

class allowances_archived_pdf(View):
    def get(self, request, report_month, report_year):        
        month=strptime(report_month, '%B').tm_mon
        archived = Expenditures.objects.filter(Archived_Status='ARCHIVED', Reason_filtering='allowance',Date__month=month, Date__year=report_year)
        today = datetime.now()
        total = archived.aggregate(totals=models.Sum("Amount"))
        total_amount = total["totals"]
        allowancecontext = {'report_month': report_month,'report_year':report_year,'today': today,
        'total_amount': total_amount,'request': request,'archived': archived,}
        return Render.render('Allowances/allowancearchivepdf.html', allowancecontext)

class allowancereceipt(View):
    def get(self, request, pk):
        data= get_object_or_404(Expenditures,pk=pk)
        today = datetime.now()
        context = {
            'today': today,
            'data': data,
            'request': request,
        }
        return Render.render('Allowances/allowance_receipt.html', context) 

################################<==============PLEDGES MODULE==============>################################

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
        items = PledgeItem.objects.filter(Date__year=current_year, Archived_Status='NOT-ARCHIVED')
        context={'form':form, 'items':items, 'current_year':current_year}
        return render(request, 'Pledges/add_Pledge_Item.html',context)
@login_required
def list_of_pledge_items(request):
    if request.method=='POST':
        items = PledgeItem.objects.all()
        for item in items:
            item_id=item.id
            results=PledgesCashedOut.objects.filter(Item_Id=item_id).aggregate(totals=models.Sum("Amount_Cashed_Out"))
            tots=results['totals'] or 0
            if(tots>=item.Amount_Needed):
                item.Archived_Status = 'ARCHIVED'
                item.save()
        messages.success(request, f'All Pledges have been Archived')
        return redirect('list-of-pledge-items')
    current_year=datetime.now().year
    items = PledgeItem.objects.filter(Archived_Status='NOT-ARCHIVED').order_by('-Date')
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

@login_required
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


@login_required
def cashing_out_items(request):
    if request.method == "POST":
        form =  PledgesCashedOutForm(request.POST,request.FILES)
        (form)
        if form.is_valid():
            
            form.save() 
            messages.success(request, "Cash out was successful")
            return redirect('list-of-pledge-items')    
        else:
            form = PledgesCashedOutForm()
            context={'form':form}
            return render(request, 'Pledges/pledge_cash_out.html', context)


@login_required
def delete_pledge_item(request, pk):
    item= get_object_or_404(PledgeItem, id=pk)
    if request.method == "GET":
        item.Archived_Status = 'Archived'
        item.save()
        messages.success(request, "Pledge Item successfully Archived!")
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

@login_required
def paying_pledges(request, pk):
    context={}
    items = get_object_or_404(Pledges, id=pk)
    if request.method == "POST":
        form = TestingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Pledgesreport')
    else:
        form = UpdatePledgesForm(instance=items)
        retrieving_id=Pledges.objects.filter(id=pk)
        context['form']=form
        context['items']=items
        context['retrieving_id']=retrieving_id
        return render(request, 'Pledges/paying_pledges_update.html', context)
                
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
        ple = Pledges.objects.filter(Archived_Status='NOT-ARCHIVED').order_by('-Date')
        today = datetime.now().now()
        month = today.strftime('%B')
        expense=ple.aggregate(y=models.Sum('Amount_Paid'))
        bal=ple.aggregate(x=models.Sum('Balance'))
        totalexpense=expense['y']
        balance=bal['x']
        context = {'month': month,'today': today,'ple': ple,'request': request,'totalexpense': totalexpense,
        'balance':balance
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
        items = Pledges.objects.filter(Status='PAID')
        for i in items:
            i.Archived_Status='ARCHIVED'
            i.save()  
            messages.success(request, f'All Pledges Paid have been Archived')
            return redirect('Pledgesreport')
    today = datetime.now()
    years=today.year
    context={}
    items = list(Pledges.objects.filter(Archived_Status="NOT-ARCHIVED").order_by('-Date'))
    context['items']=items
    context['years']=years
    context['today']=today
    return render(request, 'Pledges/pledgesindex.html', context)

@login_required
def pledgesarchivessearch(request):
    today = datetime.now()
    years=today.year 
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = Pledges.objects.filter(Archived_Status='ARCHIVED', Date__month=report_month, Date__year=report_year)
        mth=int(report_month)
        report_month=calendar.month_name[mth]
        context = {'archived_reports': archived_reports,'years': years,'today': today,
                  'report_year': report_year,'report_month': report_month}
        return render(request, "Pledges/pledgesarchive.html", context)
    context = {'years': years}
    return render(request, "Pledges/pledgesarchive.html", context)   


class pledgesarchivepdf(View):
    def get(self, request, report_month, report_year):
        month=strptime(report_month, '%B').tm_mon
        archived_pledges = Pledges.objects.filter(Archived_Status='ARCHIVED', Date__year=report_year, Date__month=month)
        today = datetime.now()
        total = archived_pledges.aggregate(totals=models.Sum("Amount_Paid"))
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
        debt = Pledges.objects.get(Q(Status='UNPAID') | Q(Status='PARTIAL'), id=pk)
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

               
#airtime report
@login_required
def airtime_data_report(request):
    mth = datetime.now().day
    today = datetime.now()
    get_airtime=Expenditures.objects.filter(Petty_Cash_Reason='Airtime/Data', Date__day=mth)
    total = Expenditures.objects.filter(Petty_Cash_Reason='Airtime/Data',Date__day=mth).aggregate(totals=models.Sum("Amount"))
    total_amount = total["totals"]
    context={'get_airtime':get_airtime, 'total_amount':total_amount, 'today':today}
    return render(request,'Expenses/airtime_data_report.html', context)

    ##################################<==========SLIDER VIEW================>#################################

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
        data['form_is_valid'] = True 
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

##################===>ABOUT MODULE<===#########################


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
        data['form_is_valid'] = True  
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


#########################===>PAGE MODULE<===########################


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
        data['form_is_valid'] = True 
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

###################===>GALLERY MODULE<===#########################

class GalleryListView(ListView):
    model = Gallery
    template_name = 'galleries/gallery_list.html'
    context_object_name = 'galleries'


def gallery_wall(request):
    galleries = Gallery.published.all().order_by('-date')
    images = Image.objects.all()
    paginator = Paginator(galleries, 3)
    page = request.GET.get('page')
    try:
        gallery_list = paginator.page(page)
    except PageNotAnInteger:
        gallery_list = paginator.page(1)
    except EmptyPage:
        gallery_list = paginator.page(paginator.num_pages)
    context = {
        'page':page,
        'galleries': galleries,
        'images': images,
        'gallery_list': gallery_list,
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
        data['html_form'] = render_to_string('galleries/includes/partial_gallery_delete.html',context, request=request,
                                             )
    return JsonResponse(data)


#####################===>IMAGE MODULE<===##########################
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
    mem_details=Image.objects.all()
    more_details = Image.published.all()
    paginator = Paginator(mem_details, 5)
    page = request.GET.get('page')
    try:
        images_list = paginator.page(page)
    except PageNotAnInteger:
        images_list = paginator.page(1)
    except EmptyPage:
        images_list = paginator.page(paginator.num_pages)
    context = {
        'page':page,
        'image': image,
        'more_details': more_details,
        'images_list': images_list,
    }
    return render(request, 'images/image_details.html', context)

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

###################=============>GOSPEL SERMONS MODULE<================########################
class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'

def news_wall(request):
    news = News.published.all()
    paginator = Paginator(news, 3)
    page = request.GET.get('page')
    try:
       news_list = paginator.page(page)
    except PageNotAnInteger:
        news_list = paginator.page(1)
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)
    context={'page':page, 'news_list': news_list}
    return render(request, 'news/news_wall.html', context)

class NewsCreateView(CreateView):
    model = News
    template_name = 'news/news_create.html'
    fields = ('news_title', 'image', 'audio_file','news', 'author','Is_View_on_Web')

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
            data['html_news_list'] = render_to_string('news/includes/partial_news_list.html', {'news': newss})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def NewsUpdate(request, news_pk):
    news = get_object_or_404(News, pk=news_pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, f'The Sermon has been updated Successfully')
            return redirect('news_list')

    else:
        form = NewsForm(instance=news)
    return save_news_form(request, form, 'news/update_news.html')

def news_view(request, news_pk):
    news = get_object_or_404(News, pk=news_pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
    else:
        form = NewsForm(instance=news)
    return save_news_form(request, form, 'news/includes/partial_news_view.html')

def news_detail(request, news_pk):
    news = get_object_or_404(News, pk=news_pk)
    more_news = News.published.order_by('-date')
    paginator = Paginator(more_news, 10) 
    page = request.GET.get('page')
    try:
       news_list = paginator.page(page)
    except PageNotAnInteger:
        news_list = paginator.page(1)
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)
    context={'news':news,'page':page, 'news_list': news_list, 'more_news': more_news}
    return render(request, 'news/news_detail.html', context)


def news_delete(request, news_pk):
    news = get_object_or_404(News, pk=news_pk)
    data = dict()
    if request.method == 'POST':
        news.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        news = News.objects.all()
        data['html_news_list'] = render_to_string('news/includes/partial_news_list.html', {
            'news': news})
    else:
        context = {'news': news}
        data['html_form'] = render_to_string('news/includes/partial_news_delete.html',
                                             context, request=request,)
    return JsonResponse(data)

###################=============>CHURCH PROJECT MODULE<================########################
class ProjectsListView(ListView):
    model = Project
    template_name = 'Church-Projects/projects_list.html'
    context_object_name = 'projects'

def projects_wall(request):
    projects = Project.published.all()
    context = {'projects': projects}
    return render(request, 'Church-Projects/projects_wall.html', context )

def ProjectsCreateView(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'The Project has been Created')
            return redirect('projects_list')   
    else:
        form=ProjectForm()
        context = {'form': form}
        return render(request, 'Church-Projects/projects_create.html',context)

def save_projects_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            projects = Project.objects.all()
            data['html_projects_list'] = render_to_string('Church-Projects/projects_list.html', {'projects': projects})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def projects_view(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
    else:
        form = ProjectForm(instance=project)
    return save_projects_form(request, form, 'Church-Projects/includes/partial_project_view.html')

def ProjectUpdate(request, project_pk):
    item = get_object_or_404(Project, pk=project_pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('projects_list')
    else:
        form = ProjectForm(instance=item)
    return render(request, 'Church-Projects/update_project.html', {'form': form})

def project_detail(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    more_projects = Project.published.order_by('-start_date')[:15]
    context = {'project': project, 'more_projects': more_projects}
    return render(request, 'Church-Projects/projects_detail.html', context)


####################========>EVENT MODULE<============#####################
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
        context={
            'form':form
        }
    return render(request, context, 'events/includes/partial_event_view.html')


def event_detail(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    more_events = Event.published.order_by('-id')[:15]
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


# #######################################===>CHURCH MODULE<===##########################################

def churchCreateView(request):
    if request.method == "POST":
        form = churchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'The details have been Created')
            return redirect('church_list')   
    else:
        form=churchForm()
        context = {'form': form}
        return render(request, 'church/create_church.html',context)

def churchUpdateView(request, church_pk):
    item = get_object_or_404(Church, pk=church_pk)
    if request.method == "POST":
        form = churchForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'The Church Details have been updated')
            return redirect('church_list')
    else:
        form = churchForm(instance=item)
        context={'form':form, 'item':item}
        return render(request, 'Church/update_church.html', context)


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
        data['form_is_valid'] = True 
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


###################===> MINISTRIES MODULE<===###################

class MinistryListView(ListView):
    model = Ministry
    template_name = 'Ministry/Ministry_list.html'
    context_object_name = 'ministry'

def ministry_wall(request):
    ministry = Ministry.published.all()
    paginator = Paginator(ministry, 3)  # 6 members on each page
    page = request.GET.get('page')
    try:
       minisitries_list = paginator.page(page)
    except PageNotAnInteger:
        minisitries_list = paginator.page(1)
    except EmptyPage:
        minisitries_list = paginator.page(paginator.num_pages)
    context={'page':page, 'minisitries_list': minisitries_list}
    return render(request, 'Ministry/ministry_wall.html', context)


class MinistryCreateView(CreateView):
    model = Ministry
    template_name = 'Ministry/ministry_create.html'
    fields = ('name', 'leader', 'details', 'photos','Is_View_on_Web')

    def form_valid(self, form):
        ministry = form.save(commit=False)
        ministry.save()
        return redirect('ministry-list')


class MinistryUpdateView(UpdateView):
    model = Ministry
    template_name = 'Ministry/update_ministry.html'
    pk_url_kwarg = 'ministry_pk'
    fields = ('name', 'leader', 'details', 'photos','Is_View_on_Web')
    def form_valid(self, form):
        ministry = form.save(commit=False)
        ministry.save()
        return redirect('ministry-list')


def save_ministry_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            ministry = Ministry.objects.all()
            data['html_ministry_list'] = render_to_string('Ministry/ministry_list.html', {
                'ministry': ministry
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def ministry_view(request, ministry_pk):
    ministry = get_object_or_404(Ministry, pk=ministry_pk)
    if request.method == 'POST':
        form = MinistryForm(request.POST, instance=ministry)
    else:
        form = MinistryForm(instance=ministry)
    return redirect(request, form, 'Ministry/ministry_view.html')

#ministry details and paginated list of the others
def ministry_detail(request, ministry_pk):
    ministry = get_object_or_404(Ministry, pk=ministry_pk)
    more_details = Ministry.published.all()
    paginator = Paginator(more_details, 8)  # 8 ministries on each page
    page = request.GET.get('page')
    try:
       min_list = paginator.page(page)
    except PageNotAnInteger: # If page is not an integer deliver the first page
        min_list = paginator.page(1)
    except EmptyPage:# If page is out of range deliver last page of results
        min_list = paginator.page(paginator.num_pages)
    context={'ministry':ministry,'page':page, 'min_list': min_list, 'paginator': paginator}
    return render(request, 'Ministry/ministry_detail.html', context)


########========================>DASHBOARD DATA CALCULATIONS<=====================#######
@login_required
def index(request):

    current_year = datetime.now().year #Annual
    current_month = datetime.now().month #Monthly

    one_week_ago = datetime.today() - timedelta(days=7) #Weekly
    day = datetime.now().today #Today

   #WEEKLY REVENUES
    total_weekly_donations = Revenues.objects.filter(Revenue_filter='others',Date__gte=one_week_ago,Archived_Status='NOT-ARCHIVED').aggregate(totals=models.Sum("Amount"))
    if (total_weekly_donations['totals'])!=None:
        int(total_weekly_donations["totals"])
        d_donations=total_weekly_donations["totals"]
    else:
        total_weekly_donations = 0
        d_donations = 0

    total_weekly_offerings = Revenues.objects.filter(Revenue_filter='offering',Date__gte=one_week_ago,Archived_Status='NOT-ARCHIVED').aggregate(totals=models.Sum("Amount"))
    if (total_weekly_offerings['totals'])!=None:
        int(total_weekly_offerings["totals"])
        d_offerings=total_weekly_offerings["totals"]
    else:
        total_weekly_offerings = 0
        d_offerings = 0

    total_weekly_tithes = Revenues.objects.filter(Revenue_filter='tithes',Date__gte=one_week_ago,Archived_Status='NOT-ARCHIVED').aggregate(totals=models.Sum("Amount"))
    if (total_weekly_tithes['totals'])!=None:
        int(total_weekly_tithes["totals"])
        d_tithes=total_weekly_tithes["totals"]
    else:
        total_weekly_tithes=0
        d_tithes = 0 

    total_weekly_seeds = Revenues.objects.filter(Revenue_filter='seeds',Date__gte=one_week_ago,Archived_Status='NOT-ARCHIVED').aggregate(totals=models.Sum("Amount"))
    if (total_weekly_seeds['totals'])!=None:
        int(total_weekly_seeds["totals"])
        d_seeds=total_weekly_seeds["totals"]
    else:
        total_weekly_seeds = 0
        d_seeds = 0

    total_weekly_building = Revenues.objects.filter(Revenue_filter='build',Date__gte=one_week_ago,Archived_Status='NOT-ARCHIVED').aggregate(totals=models.Sum("Amount"))
    if (total_weekly_building['totals'])!=None:
        int(total_weekly_building["totals"])
        d_building=total_weekly_building["totals"]
    else:
        total_weekly_building=0
        d_building = 0 
    total_weekly_thanks = Revenues.objects.filter(Revenue_filter='thanks',Date__gte=one_week_ago,Archived_Status='NOT-ARCHIVED').aggregate(totals=models.Sum("Amount"))
    if (total_weekly_thanks['totals'])!=None:
        int(total_weekly_thanks["totals"])
        d_thanks=total_weekly_thanks["totals"]
    else:
        total_weekly_thanks = 0
        d_thanks = 0 

    total_current_donations = Revenues.objects.filter(Revenue_filter='others',Archived_Status='NOT-ARCHIVED',Date__month=current_month,Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    if (total_current_donations['totals'])!=None:
        int(total_current_donations["totals"])
        donations=total_current_donations["totals"]
    else:
        total_current_donations = 0 
        donations = 0


    #WEEKLY EXPENSES    
     #weekly Petty Cash expenses
    weekly_petty_expenses = Expenditures.objects.filter(Reason_filtering='petty',Date__gte=one_week_ago,Archived_Status='NOT-ARCHIVED').aggregate(totals=models.Sum("Amount"))
    if (weekly_petty_expenses['totals'])!=None:
        int(weekly_petty_expenses["totals"])
        d_petty=weekly_petty_expenses["totals"]
    else:
        weekly_petty_expenses = 0
        d_petty = 0 
    
    weekly_allowances = Expenditures.objects.filter(Reason_filtering='allowance',Date__gte=one_week_ago,Archived_Status='NOT-ARCHIVED').aggregate(totals=models.Sum("Amount"))
    if(weekly_allowances['totals'])!=None:
        int(weekly_allowances["totals"])
        d_allowances=weekly_allowances["totals"]    
    else:
        weekly_allowances = 0
        d_allowances=0

    #Total general expenses of the week.
    weekly_general_expenses = Expenditures.objects.filter(Reason_filtering='general',Date__gte=one_week_ago,Archived_Status='NOT-ARCHIVED').aggregate(totals=models.Sum("Amount"))
    if (weekly_general_expenses['totals'])!=None:
        int(weekly_general_expenses["totals"])
        d_general=weekly_general_expenses["totals"]
    else:
        weekly_general_expenses = 0
        d_general = 0

    #weekly main expenses
    total_weekly_expenses = Expenditures.objects.filter(Reason_filtering='main',Date__gte=one_week_ago,Archived_Status='NOT-ARCHIVED').aggregate(totals=models.Sum("Amount"))
    if (total_weekly_expenses['totals'])!=None:
        int(total_weekly_expenses["totals"])
        d_expenses=total_weekly_expenses["totals"]
    else:
        total_weekly_expenses = 0
        d_expenses = 0  

    #weekly salaries
    total_weekly_salaries = SalariesPaid.objects.filter(Date_of_paying_salary__gte=one_week_ago).aggregate(totals=models.Sum("Salary_Amount"))
    if (total_weekly_salaries['totals'])!=None:
        int(total_weekly_salaries["totals"])
        d_salaries=total_weekly_salaries["totals"]
    else:
        total_weekly_salaries = 0
        d_salaries = 0    
    
    #MONTHLY REVENUES
    total_weekly_pledges = Pledges.objects.filter(Date__month=current_month,Date__year=current_year).aggregate(totals=models.Sum("Amount_Paid"))
    if (total_weekly_pledges['totals'])!=None:
        int(total_weekly_pledges["totals"])
        d_pledges=total_weekly_pledges["totals"]
    else:
        total_weekly_pledges = 0
        d_pledges = 0

    total_current_thanks = Revenues.objects.filter(Revenue_filter='thanks',Archived_Status='NOT-ARCHIVED',Date__month=current_month,Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    if (total_current_thanks['totals'])!=None:
        int(total_current_thanks["totals"])
        thanks=total_current_thanks["totals"]
    else:
        total_current_thanks = 0
        thanks = 0  
    
    total_current_seeds = Revenues.objects.filter(Revenue_filter='seeds',Archived_Status='NOT-ARCHIVED',Date__month=current_month,Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    if (total_current_seeds['totals'])!=None:
        int(total_current_seeds["totals"])
        seeds=total_current_seeds["totals"]
    else:
        total_current_seeds = 0
        seeds = 0

    total_current_offerings = Revenues.objects.filter(Revenue_filter='offering',Archived_Status='NOT-ARCHIVED',Date__month=current_month,Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    if (total_current_offerings['totals'])!=None:
        int(total_current_offerings["totals"])
        offerings=total_current_offerings["totals"]
    else:
        total_current_offerings = 0
        offerings = 0

#TITHES
    total_current_tithes = Revenues.objects.filter(Revenue_filter='tithes',Archived_Status='NOT-ARCHIVED',Date__month=current_month,Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    if (total_current_tithes['totals'])!=None:
        int(total_current_tithes["totals"])
        tithes=total_current_tithes["totals"]
    else:
        total_current_tithes=0
        tithes = 0 

#BUILDING
    total_current_building = Revenues.objects.filter(Revenue_filter='build',Archived_Status='NOT-ARCHIVED',Date__month=current_month,Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    if (total_current_building['totals'])!=None:
        int(total_current_building["totals"])
        building=total_current_building["totals"]
    else:
        total_current_building=0
        building = 0
          
#Calculate Expenditure
    #monthly salary
    total_current_salaries = SalariesPaid.objects.filter(Date_of_paying_salary__month=current_month).aggregate(totals=models.Sum("Salary_Amount"))
    if (total_current_salaries['totals'])!=None:
        int(total_current_salaries["totals"])
        salaries=total_current_salaries["totals"]
    else:
        total_current_salaries = 0
        salaries = 0
    
    #mothly pledges    
    total_current_pledges = Pledges.objects.filter(Date__month=current_month,Date__year=current_year).aggregate(totals=models.Sum("Amount_Paid"))
    if (total_current_pledges['totals'])!=None:
        int(total_current_pledges["totals"])
        pledges=total_current_pledges["totals"]
    else:
        total_current_pledges = 0
        pledges = 0
    
    #monthly main expenses
    total_main_expenses = Expenditures.objects.filter(Reason_filtering='main',Archived_Status='NOT-ARCHIVED',Date__month=current_month,Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    if (total_main_expenses['totals'])!=None:
        int(total_main_expenses["totals"])
        expenses=total_main_expenses["totals"]
    else:
        total_main_expenses = 0
        expenses = 0

    #Total general expenses of the current month of the year.
    total_general_expenses = Expenditures.objects.filter(Reason_filtering='general',Archived_Status='NOT-ARCHIVED',Date__month=current_month,Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    if (total_general_expenses['totals'])!=None:
        int(total_general_expenses["totals"])
        general=total_general_expenses["totals"]
    else:
        total_general_expenses = 0
        general = 0

    #Monthly Petty Cash expenses
    total_petty_expenses = Expenditures.objects.filter(Reason_filtering='petty',Archived_Status='NOT-ARCHIVED',Date__month=current_month,Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    if (total_petty_expenses['totals'])!=None:
        int(total_petty_expenses["totals"])
        petty=total_petty_expenses["totals"]
    else:
        total_petty_expenses = 0
        petty = 0

    #monthly allowances       
    total_allowances = Expenditures.objects.filter(Reason_filtering='allowance',Archived_Status='NOT-ARCHIVED',Date__month=current_month,Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    if (total_allowances['totals'])!=None:
        int(total_allowances["totals"])
        allowances=total_allowances["totals"]    
    else:
        total_allowances = 0
        allowances=0

    #ANNUAL EXPENSES AND REVENUES
    A_thanks = Revenues.objects.filter(Revenue_filter='thanks',Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    Annualthanks=(A_thanks["totals"])
    if Annualthanks is None:
        Annualthanks =0

    A_others=Revenues.objects.filter(Revenue_filter='others',Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    Annualothers=(A_others["totals"])
    if Annualothers is None:
        Annualothers =0

    A_offering = Revenues.objects.filter(Revenue_filter='offering',Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    Annualoffering=(A_offering["totals"])
    if Annualoffering is None:
        Annualoffering =0

    A_tithes=Revenues.objects.filter(Revenue_filter='tithes',Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    Annualtithes=(A_tithes["totals"])
    if Annualtithes is None:
        Annualtithes =0

    A_seeds = Revenues.objects.filter(Revenue_filter='seeds',Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    Annualseeds=(A_seeds["totals"])
    if Annualseeds is None:
        Annualseeds =0

    A_build= Revenues.objects.filter(Revenue_filter='build',Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    Annualbuilding=(A_build["totals"])
    if Annualbuilding is None:
        Annualbuilding =0
     
    #expenses
    A_general=Expenditures.objects.filter(Reason_filtering='general',Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    Annualgeneral=(A_general["totals"])
    if Annualgeneral is None:
        Annualgeneral =0

    A_main=Expenditures.objects.filter(Reason_filtering='main',Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    Annualmain=(A_main["totals"])
    if Annualmain is None:
        Annualmain =0

    A_petty = Expenditures.objects.filter(Reason_filtering='petty',Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    Annualpetty=(A_petty["totals"])
    if Annualpetty is None:
        Annualpetty =0

    A_allowance=Expenditures.objects.filter(Reason_filtering='allowance',Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    Annualallowances=(A_allowance["totals"])
    if Annualallowances is None:
        Annualallowances =0

    #current month pledges paid
    pledgecash = PledgesCashedOut.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Amount_Cashed_Out"))
    if (pledgecash['totals'])!=None:
        int(pledgecash["totals"])
        total_cash_out=pledgecash["totals"]    
    else:
        pledgecash = 0
        total_cash_out=0       
 
    #ANNUAL REVENUE
    annual_revenue=Revenues.objects.filter(Date__year=current_year).exclude(Revenue_filter='build').aggregate(totals=models.Sum("Amount"))
    revenues_in_a_year=(annual_revenue["totals"])
    if revenues_in_a_year is None:
        revenues_in_a_year =0

    #ANNUAL PLEDGES PAID
    annual_paid_pledges = Pledges.objects.filter(Date__year=current_year).aggregate(totals=models.Sum("Amount_Paid"))
    annual_pledges_paid=(annual_paid_pledges["totals"])
    if annual_pledges_paid is None:
        annual_pledges_paid =0

    #ANNUAL EXPENDITURE
    annual_expenses=Expenditures.objects.filter(Date__year=current_year).aggregate(totals=models.Sum("Amount"))
    expenses_in_a_year=(annual_expenses["totals"])
    if expenses_in_a_year is None:
        expenses_in_a_year =0

    A_salaries=SalariesPaid.objects.filter(Date_of_paying_salary__year=current_year).aggregate(totals=models.Sum("Salary_Amount"))
    Annualsalaries=(A_salaries["totals"])
    if Annualsalaries is None:
        Annualsalaries =0

    #annuall pledges cashed out
    pledgecash = PledgesCashedOut.objects.filter(Date__year=current_year).aggregate(totals=models.Sum("Amount_Cashed_Out"))
    Annualpledgecashed=(pledgecash["totals"])
    if Annualpledgecashed is None:
        Annualpledgecashed =0
   
    #in case the totals are Zero
    if (annual_revenue, annual_paid_pledges,annual_expenses,A_salaries,pledgecash,
        total_petty_expenses,total_current_tithes,total_general_expenses, total_current_salaries, 
        total_current_offerings,total_current_pledges,total_allowances,total_main_expenses,total_cash_out)== 0:
        total_monthly_incomes = 0
        annual_revenues = 0
        annual_expenditure = 0
        total_monthly_expenditure =  0
        total_general_expenses = 0
        pledges = 0

        #calculating net income
        net_income = total_monthly_incomes - total_monthly_expenditure
        annual_net = annual_revenues - annual_expenditure
        today = timezone.now()
        month = today.strftime('%B')
        context={
        'total_current_salaries':total_current_salaries,
        'annual_revenues':annual_revenues, 'annual_expenditure':annual_expenditure,
        'annual_net':annual_net, 'total_current_building':total_current_building, 'd_building': d_building, 'building':building, 'total_current_donations':total_current_donations,'total_current_thanks':total_current_thanks,'total_current_seeds':total_current_seeds,'total_general_expenses':total_general_expenses,'total_petty_expenses':total_petty_expenses,'salaries':salaries,'total_current_salaries':total_current_salaries,'total_monthly_incomes':total_monthly_incomes,'total_monthly_expenditure':total_monthly_expenditure, 'month': month,
        'general':general,'allowances':allowances,'seeds':seeds, 'expenses':expenses,'day':day,
        'tithes':tithes, 'offerings':offerings, 'pledges':pledges, 'net_income':net_income,'thanks':thanks,'donations':donations
        ,'d_petty':d_petty,'d_allowances':d_allowances,'d_salaries':d_salaries, 'd_pledges':d_pledges, 'd_general':d_general,'d_expenses':d_expenses,
        }
        #return the index of the user dashboard
        return render(request,'index.html', context)

    #if there are moneys, calculate revenues, incomes and total expenditure.
    else:
        annual_expenditure =   expenses_in_a_year + Annualsalaries 
        total_monthly_incomes =  tithes + offerings + seeds + thanks + donations 
        total_monthly_expenditure =  allowances + expenses + general + petty + salaries 
        net_income = total_monthly_incomes - total_monthly_expenditure
        #calculating annual cashfloat given out

        #Weekly cash float given out.
        one_week_ago = datetime.today() - timedelta(days=7) 
        cash_float= CashFloat.objects.filter(Date__gte=one_week_ago, Date__year=current_year)
        if cash_float:
            for i in cash_float:
                if (one_week_ago): 
                    get_cash_float= i.Amount
                    net_float = int(get_cash_float) - total_monthly_expenditure
                    new_float = net_float + get_cash_float
        else:
            get_cash_float = 0
            net_float = 0
            new_float = 0

        annual_float= CashFloat.objects.filter(Date__year=current_year)
        annual_cashfloat=annual_float.aggregate(totals=Sum('Amount'))
        total_annual_float=annual_cashfloat['totals']
        if total_annual_float is None:
            total_annual_float=0
        annual_revenues = (revenues_in_a_year)
        annual_net = annual_revenues-annual_expenditure  
        today = timezone.now()
        month = today.strftime('%B')
        mth=calendar.month_name[current_month]

        context={
        'Annualthanks':Annualthanks, 'Annualothers':Annualothers, 'Annualoffering':Annualoffering,
        'Annualtithes':Annualtithes,'Annualseeds':Annualseeds,'Annualbuilding':Annualbuilding,
        'Annualgeneral':Annualgeneral,'Annualmain':Annualmain,'Annualpetty':Annualpetty,
        'Annualallowances':Annualallowances,'annual_pledges_paid':annual_pledges_paid, 'Annualsalaries':Annualsalaries, 
        'Annualpledgecashed':Annualpledgecashed,'total_annual_float':total_annual_float,

        'get_cash_float':get_cash_float,'net_float':net_float,'new_float':new_float,
        'mth':mth, 'current_year':current_year,'current_month': current_month,
        'annual_revenues':annual_revenues, 'annual_expenditure':annual_expenditure,'annual_net':annual_net,
        'total_current_building':total_current_building, 'd_building': d_building,"building":building,
        'd_donations':d_donations,'d_tithes':d_tithes,'d_offerings':d_offerings,
        'd_seeds':d_seeds,'d_thanks':d_thanks,'d_pledges':d_pledges,'day':day,

        'total_current_donations':total_current_donations,'total_current_thanks':total_current_thanks,
        'total_current_seeds':total_current_seeds,'total_petty_expenses':total_petty_expenses,'total_cash_out':total_cash_out,
        'total_general_expenses':total_general_expenses,'salaries':salaries,'total_current_salaries':total_current_salaries,
        'total_monthly_incomes':total_monthly_incomes,'total_monthly_expenditure':total_monthly_expenditure, 'month': month,
        'petty':petty,'allowances':allowances,'seeds':seeds,'general':general, 'expenses':expenses,'tithes':tithes, 
        'offerings':offerings,'pledges':pledges,'net_income':net_income,'thanks':thanks,'donations':donations,
        'd_petty':d_petty,'d_allowances':d_allowances,'d_salaries':d_salaries, 'd_general':d_general,'d_expenses':d_expenses,
        }
        return render(request,'index.html', context)

#All monthly revenues not yet archived
def total_revenues(request):
    current_month = datetime.now().month #Monthly
    current_year = datetime.now().year
    total_revenues = Revenues.objects.filter(Date__month=current_month, Archived_Status='NOT-ARCHIVED').exclude(Revenue_filter='build')\
    .values('Date','Revenue_filter').annotate(Amount=Sum('Amount'))
    total = total_revenues.aggregate(total_amount=models.Sum("Amount"))
    x=total['total_amount']
    if x is None:
        x=0

    total_current_pledges = Pledges.objects.filter(Archived_Status='NOT-ARCHIVED')\
    .values('Date','Reason__Item_That_Needs_Pledges').annotate(Amount_Paid=Sum('Amount_Paid'))
    pledges = total_current_pledges.aggregate(total_paid=models.Sum("Amount_Paid"))
    month=calendar.month_name[current_month]
    y=pledges['total_paid']
    if y is None:
        y=0
    #total current month revenue not yet archived is equal to all revenues plus pledges paid
    total_amount = x
    context={'total_revenues':total_revenues,'total_amount':total_amount,'month':month, \
    'total_current_pledges':total_current_pledges}
    return render(request, 'total_revenues.html', context)

#All monthly expenditures not archived
def total_expenses(request):
    current_year = datetime.now().year
    current_month = datetime.now().month #Monthly
    total_expenses = Expenditures.objects.filter(Archived_Status='NOT-ARCHIVED')\
    .values('Date','Reason_filtering','Member_Name', 'Member_Name__First_Name','Member_Name__Second_Name','Payment_Made_To').annotate(Amount=Sum('Amount'))
    total = total_expenses.aggregate(totals=models.Sum("Amount"))
    y= total['totals']
    if y is None:
        y = 0

    month=calendar.month_name[current_month]
    total_current_salaries = SalariesPaid.objects.filter(Date_of_paying_salary__year=current_year\
    ,Date_of_paying_salary__month=current_month).values('Name','Date_of_paying_salary').annotate(Salary_Amount=Sum("Salary_Amount"))
    totalSalaries = total_current_salaries.aggregate(totalsal=models.Sum("Salary_Amount"))
    x=totalSalaries['totalsal']
    if x is None :
        x = 0
    #total current month expenses = all expenses plus salaries    
    total_amount = y + x 
    pledgecash = PledgesCashedOut.objects.filter(Date__month=current_month)\
    .values('Date','Item_That_Needs_Pledges').annotate(Amount_Cashed_Out=Sum('Amount_Cashed_Out'))
    cash = pledgecash.aggregate(total=models.Sum("Amount_Cashed_Out"))
    z=cash['total']
    if z is None:
        z=0
   
     
    context={'total_current_salaries':total_current_salaries,'total_expenses':total_expenses,
    'total_amount':total_amount,'pledgecash': pledgecash, 'month':month}
    return render(request, 'total_expenses.html', context)

########========================>CASHFLOAT MODULE<=====================#######
@login_required
def record_cashfloat(request):
    one_week_ago = datetime.today() - timedelta(days=7) #Weekly
    current_year = datetime.now().year
    current_month = datetime.now().month
    month=calendar.month_name[current_month]
    get_data = CashFloat.objects.filter(Date__gte=one_week_ago or None)
    total_amount = get_data.aggregate(totals=models.Sum('Amount'))
    total_float = total_amount["totals"]
    if request.method=="POST":
        form=CashFloatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cashfloat-list')
    else:
        if get_data:
            mesg="You have already given out the float"
            context={'mesg':mesg, 'get_data':get_data,'month':month, 'current_year':current_year,'total_float':total_float}
            return render(request, 'give_cash_float.html',context) 
        form=CashFloatForm()
        context={'form':form,}
        return render(request, 'give_cash_float.html',context)    
        
#list of all cash float given out
def cashfloat_lst(request):
    x = datetime.now() - timedelta(days=7)
    one_week_ago=x.day
    mth = datetime.now().month
    current_year = datetime.now().year
    lists=CashFloat.objects.filter(Date__year=current_year).order_by('-Date')
    return render(request, 'cashfloat_list.html',{'one_week_ago':one_week_ago,'lists':lists,'current_year':current_year, 'mth': mth})

def edit_cash_float(request, pk):
    item = get_object_or_404(CashFloat, pk=pk)
    if request.method == "POST":
        form = CashFloatForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Cashfloat Update was successful")
            return redirect('cashfloat-list')
    else:
        form = CashFloatForm(instance=item)
        return render(request, 'edit_cash_float.html', {'form': form})

######################<=======CHURCH GROUPS==========>#######################
def church_groups(request):
    able_group=Members.objects.filter(is_active=True, Group="God is Able")
    winners_group=Members.objects.filter(is_active=True, Group="Winners")
    overcomers_group=Members.objects.filter(is_active=True, Group="Overcomers")
    biyinzika_group=Members.objects.filter(is_active=True, Group="Biyinzika")
    victors_group=Members.objects.filter(is_active=True, Group="Victors")
    Issachar_group=Members.objects.filter(is_active=True, Group="Issachar")
    context={
        'able_group':able_group,
        'winners_group':winners_group,
        'overcomers_group':overcomers_group,
        'biyinzika_group':biyinzika_group,
        'victors_group':victors_group,
        'Issachar_group': Issachar_group,
    }
    return render(request, 'Groups/church_groups.html', context)

######################<=======HOME CELLS==========>######################
def home_cells(request):
    Church = Members.objects.filter(is_active=True, Home_Cell="Church Zone")
    Kabira=Members.objects.filter(is_active=True, Home_Cell="Kabira Zone")
    Kafunda=Members.objects.filter(is_active=True, Home_Cell="Kafunda Zone")
    Lugoba=Members.objects.filter(is_active=True, Home_Cell="Lugoba Zone")
    Kazo=Members.objects.filter(is_active=True, Home_Cell="Kazo Zone")
    Gombolola=Members.objects.filter(is_active=True, Home_Cell="Gombolola Zone")
    Kawaala=Members.objects.filter(is_active=True, Home_Cell="Kawaala Zone")
    Katooke = Members.objects.filter(is_active=True, Home_Cell="Katooke Zone")
    Bombo = Members.objects.filter(is_active=True, Home_Cell="Bombo Rd Zone")
    context={
        'Church': Church,
        'Kafunda':Kafunda,
        'Kabira':Kabira,
        'Lugoba':Lugoba,
        'Kazo':Kazo,
        'Gombolola':Gombolola,
        'Kawaala':Kawaala,
        'Bombo': Bombo,
        'Katooke': Katooke
    }
    return render(request, 'Groups/home_cells.html', context)
