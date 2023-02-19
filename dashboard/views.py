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

from .serializers import *
from .MonthlyViews import *
from .WeeklyExpensesViews import *
from .WeeklyRevenueViews import *
import calendar

from rest_framework.decorators import api_view
from rest_framework.response import Response

year=datetime.now().year
current_month = datetime.now().month
month=calendar.month_name[current_month]
today = datetime.now()


def view_404(request, exception=None):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('news_wall') # or redirect('name-of-index-url')


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

########============>AUTOSUGGEST OF NAMES FROM DATABASES<==============#######
class Autocomplete(autocomplete.Select2QuerySetView):
     
    def get_queryset(self):
        qs = Members.objects.filter(is_active=True)
         
        if self.q:
            qs = qs.filter(Q(First_Name__istartswith=self.q) | Q(Second_Name__istartswith=self.q))
            return qs

########=============>FETCH FROM THE DATABASE TO THE WEBSITE<=====================#######
def web(request):
    #code to delete all the unwanted bots
    try:
        strings = ['bot', 'htm', 'php','spd','bingbot','facebookexternalhit','petalsearch','petalbot']
        for string in strings:
            delete_visitor=Visitor.objects.filter(user_agent__icontains=string)
            delete_visitor.delete()
    except:
        pass
    try:
        
        date= datetime.now()
        month = date.month
        year = date.year
        #da= date.day
        #RUN_EVERY_MONTH=calendar._monthlen(year, month)
        form=ContactForm()
        context = {form:'form'}
        lwaki = LwakiOliMulamu.objects.extra(select={'year': 'extract( year from date )'}).values('year').annotate(dcount=Count('date'))
        try:
            theme = ThemeOfTheYear.objects.get(is_active=True)
            news = News.published.all().order_by('-id')
            events = Event.published.all().order_by('-id')
            images = Image.published.all().order_by('-id')
            members = Members.published.filter(is_active=True).order_by('-id')
            ministry = Ministry.published.all().order_by('-id')
            employees = StaffDetails.published.all()
            sliders = Slider.objects.all().order_by('-id')
            abouts = About.objects.all()
            gospel = News.published.latest('-date')
            feeback= Contact.objects.all().order_by('-id')
            pages = Page.objects.all().order_by('-id')
            blogs = Blog.objects.filter(is_active=True).order_by('-date')[:3]
            form=ContactForm()
            context = { 'lwaki':lwaki,
                'gospel':gospel,'pages' : pages,'feeback':feeback,'images':images,'events': events,'news': news,'theme':theme,'blogs':blogs,
            'abouts': abouts,'sliders' :sliders,'members': members, 'employees': employees,'ministry':ministry,form:'form','year':year}
        except:
            form=ContactForm()
            context = {form:'form'}
    except:
        context={}
    
    return render(request, 'home/index_public.html', context)

def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            #form.save()
            church_email = Church.objects.get(id=1)
            emailing_to=church_email.email_address
            client_name= form.cleaned_data.get('name')
            mail_subject = form.cleaned_data.get('subject')   
            message =  form.cleaned_data.get('message')  
            received_from = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone')
            email = EmailMessage(to=[emailing_to],
                subject='Email from: ' + client_name + ' telephone: ' + phone_number + ' Email Title: ' +mail_subject, body=message,
                from_email=received_from, reply_to=[received_from])   
            email.send()
            messages.success(request, f'Thanks for contacting UCC Bwaise, we shall reply you via your email address.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form=ContactForm()
        return render(request, 'home/contacts.html',{'form':form})
    return render(request, 'home/contacts.html')


###############=======>EMPLOYEE MODULE<=======#############
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
    
#############function to print all registered members######################    
class print_all_members(View):
    def get(self, request):
        all_members = Members.objects.filter(is_active=True).order_by('-id')
        context = {'all_members':all_members, 
                   'request':request
                   }
        return Render.render('Members/print_all_members.html', context)
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
        message="Edited Employee Details"
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
    salaries = SalariesPaid.objects.filter(Archived_Status='NOT-ARCHIVED', Date_of_paying_salary__year=current_year, Date_of_paying_salary__month=current_month)
    if request.method=='POST':
        for item in salaries:
            item.Archived_Status = 'ARCHIVED'
            item.save()
        messages.success(request, f'All Salaries Paid have been Archived')
        return redirect('current-month-salaries')
    years = datetime.now().year
    today = timezone.now()
    day=datetime.now()
    total = salaries.aggregate(totals=models.Sum("Salary_Amount"))
    total_amount = total["totals"]
    context = {'day':day, 'total_amount':total_amount, 'salaries': salaries,'current_month':current_month,'years':years,
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
    today = datetime.now()
    years=today.year
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = SalariesPaid.objects.filter(Date_of_paying_salary__month=report_month, Date_of_paying_salary__year=report_year)
        total = archived_reports.aggregate(totals=models.Sum("Salary_Amount"))
        total_amount = total["totals"]
        mth=int(report_month)
        report_month=calendar.month_name[mth]
        context = {'archived_reports': archived_reports,'years': years,'today': today,
                  'report_year':report_year,'report_month': report_month, 'total_amount':total_amount,}
        return render(request, "Employees/salariespaidarchive.html", context)
    context = {'years': years}
    return render(request, "Employees/salariespaidarchive.html", context)
 

#############=======>MEMBERSHIP MODULE<=======#############
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

#online membership registration view

def Online_Registration(request):
    if request.method=="POST":
        form=MembersForm(request.POST, request.FILES,)
        if form.is_valid():
            human = True
            # email activation '''
            member = form.save(commit=False)
            member.username = request.user
            member.save()
            current_user = request.user.email
            mail_subject = member.First_Name + " " + member.Second_Name + ' Member Creation'  
            mail_message ="This membership needs approval from the Admin"  
            to_email = 'dihfahsihm@gmail.com' 
            from_email = current_user
            if mail_subject and mail_message and from_email:
                try:
                    send_mail(mail_subject, mail_message, from_email, [to_email])
                    messages.success(request, "A member has been created by you, the admin will review your submission!")
                    return redirect('member_profile')
                except BadHeaderError:
                    return HttpResponse('Make sure you enter correct info.')
           
        else:
            form_errors=form.errors
            context={'form':form,'form_errors':form_errors}
            return render(request, 'Members/register_another_member.html', context)   
    else:
        form=MembersForm()
        context={'form':form}
        return render(request, 'Members/register_another_member.html', context)

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

#approve membership request sent from the website
@login_required
def approve_member(request, pk):
    if request.method == "GET":
        item = Members.objects.get(is_active=False, id=pk)
        item.is_active='True'
        item.save()
        messages.success(request, f'Member has been Approved')
        return redirect('un-approved-list')

#reject membership request sent from the website
@login_required
def reject_request(request, pk):
    if request.method == "GET":
        item = Members.objects.get(is_active=False, id=pk)
        item.delete()
        messages.success(request, f'Membership Request has been Rejected')
        return redirect('un-approved-list')

#list of the un-approved members.
@login_required        
def un_approved_members_list(request):        
    get_all_unapproved=Members.objects.filter(is_active=False, Archived_Status='NOT-ARCHIVED')
    context={'get_all_unapproved':get_all_unapproved}
    return render(request,'Members/unapproved-members-list.html', context)

#archiving church members
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

#unarchiving members
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

#list of pastors
def church_pastors(request):
    pastors = Members.published.all()
    return render(request, 'Members/pastoral_team.html', {'pastors': pastors})

#list of church admins
def church_administration(request):
    staffs = User.published.filter(Q(Role='Assistant_Admin') | Q(Role='Admin') | Q(Role='SuperAdmin') | Q(Role='Secretary')| Q(Role='Youth Leader'))
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
        context = {'form': form, 'item':item}
    return render(request, 'Members/edit_member_details.html', context)

#view details of a church member 
def view_member(request, pk):
    members = get_object_or_404(Members, pk=pk)
    if request.method == 'POST':
        form = MembersForm(request.POST, instance=members)
    else:
        form = MembersForm(instance=members)
    return save_news_form(request, form, 'Members/includes/partial_members_view.html') 

#view all church members registered  
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

def system_view_member_details(request, pk):
    member = get_object_or_404(Members, pk=pk)
    return render(request, 'Members/view_member_details.html', {'member':member})
#view member details
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

###### <====VISITORS MODULE====> #####
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
        return render(request, 'Visitors/register_visitors.html',{'form':form})

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
    return render(request, 'Visitors/register_visitors.html', {'form': form})

#delete visitors    
def delete_visitor(request, pk):
    visiting= get_object_or_404(Visitors, id=pk)
    if request.method == "POST":
        visiting.delete()
        messages.success(request, f'Visitor has been deleted')
        return redirect("visitors-list")

    context= {'visiting': visiting}
    return render(request, 'Visitors/visitors_delete.html', context)

#list of church visitors
@login_required
def visitors_list(request):
    visiting = Visitors.objects.all()
    context ={'visiting': visiting}

    return render(request, 'Visitors/visitors_list.html', context)

#############==============>BUILDING MODULE<============#############  

#record building money.     
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

#generate building report
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

##############=====>GENERAL OFFERINGS MODULE<======###################
#record offerings
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
    
    
#monthly offerings report
@login_required
def Offeringsreport (request):
    if request.method=='POST':
        items = Revenues.objects.all().order_by('-id')
        for item in items:
            item.Archived_Status = 'ARCHIVED'
            item.save()
        messages.success(request, f'General Offerings Report has been Archived')
        return redirect('Offeringsreport')
 
    context={}
    year=datetime.now().year
    
    # qs1 = Revenues.objects.filter(Date__year=year,Revenue_filter='offering')
    # qs2=Revenues.objects.filter(Archived_Status="NOT-ARCHIVED", Date__year=year,General_Offering_Amount__gte=1)
    
    qs = Revenues.objects.filter(Archived_Status="NOT-ARCHIVED", Date__year=year, Date__month=current_month, Revenue_filter='offering')
    # qs2=Revenues.objects.filter(Archived_Status="NOT-ARCHIVED", Date__year=year, Date__month=current_month, General_Offering_Amount__gte=1)
    
    
    # qs=qs1.union(qs2)
    context['items']=qs
    context['total']=qs.aggregate(Sum('Amount'))['Amount__sum']
    context['years']=year
    context['today']=today
    return render(request, 'Offerings/offeringsindex.html', context)
    
def individual_offerings(request):
    context={}
    qs=Revenues.objects.filter(Archived_Status="NOT-ARCHIVED", Date__year=year, Date__month=current_month, General_Offering_Amount__gte=1)
    context['items']=qs
    context['total']=qs.aggregate(Sum('General_Offering_Amount'))['General_Offering_Amount__sum']
    context['years']=year
    context['today']=today
    return render(request, 'Offerings/individual_offerings_report.html', context)

@login_required
def edit_individual_offerings(request, pk):
    if request.user.Role == 'SuperAdmin' or 'Secretary ' or 'Admin' or 'Assistant_Admin':
        item = get_object_or_404(Revenues, pk=pk)
        if request.method == "POST":
            form = RevenuesForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                messages.success(request, f'individual offering has been updated')
                return redirect('individual-offering')
        else:
            form = RevenuesForm(instance=item)
        return render(request, 'Offerings/edit_individual_offerings.html', {'form': form})
    else:
        return HttpResponse('You are forbidden from accessing this functionality')  
        
        
#update offerings info
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

#search for the archived offerings
@login_required
def offeringsarchivessearch(request):
    today = datetime.now()
    years=today.year
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = Revenues.objects.filter(Archived_Status='ARCHIVED', Date__month=report_month, Date__year=report_year)
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
        archived_offerings = Revenues.objects.filter(Date__month=month, Date__year=report_year, Archived_Status='ARCHIVED').order_by('-Date')
        today = datetime.now()
        month=today.strftime('%B')
        total = archived_offerings.aggregate(totals=models.Sum("General_Offering_Amount"))
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

#offerings report pdf
class offeringspdf(View):
    def get(self, request):
        current_month = datetime.now().month
        offerings = Revenues.objects.filter(Archived_Status='NOT-ARCHIVED').order_by('-Date')
        today = datetime.now()
        month = today.strftime('%B')
        totalexpense = 0
        for instance in offerings:
            totalexpense += instance.General_Offering_Amount
        context = {
            'month': month,
            'today': today,
            'offerings': offerings,
            'request': request,
            'totalexpense': totalexpense,
        }
        return Render.render('Offerings/offeringspdf.html', context)

##################=====================>SEEDS OFFERING MODULE<=========================#############################   

#this function is not being used.
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
    items = Revenues.objects.filter(Archived_Status="NOT-ARCHIVED")
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
        archived_reports = Revenues.objects.filter(Archived_Status='ARCHIVED', Date__month=report_month, Date__year=report_year)
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
        month = timezone.now().strftime('%B')
        form = RevenuesForm(instance=item)        
        context={'form':form, 'month':month}
    return render(request, 'Seeds/edit_seeds.html', context)

class seed_offering_receipt(View):
    def get(self, request, pk):
        seeds= get_object_or_404(Revenues,pk=pk)
        today = datetime.now()
        context = { 'today': today,'seeds': seeds,'request': request,}
        return Render.render('Seeds/seed_offerings_receipt.html', context)

##############################<===========MINISTRY SUPPORT MODULE===========>################################# 
def record_member_support(request, pk):
    get_member_name=get_object_or_404(Members, pk=pk)
    if request.method=="POST":
        form=RevenuesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'The Support has been recorded')
            return redirect('members-list')
    else:
        form=MembersForm(instance=get_member_name)
        context={'form':form, 'get_member_name':get_member_name}
    return render(request, 'Ministry-Support/record_member_support.html',context)

@login_required
def Supportreport (request):
    context={}
    if request.method=='POST':
        items = Revenues.objects.all().order_by('-id')
        for item in items:
            item.Archived_Status = 'ARCHIVED'
            item.save()
        messages.success(request, f'Support Report has been Archived')
        return redirect('Supportreport')
    month = datetime.now().month
    years=datetime.now().year
    items = Revenues.objects.filter(Archived_Status="NOT-ARCHIVED", Date__year=years).order_by('-Date')

    context['items']=items
    context['years']=years
    context['today']=datetime.now()
    return render(request, 'Ministry-Support/Supportindex.html', context)

def edit_support(request, pk):
    item = Revenues.objects.get(id=pk)
    form = RevenuesForm(instance=item)
    if request.method == "POST":
        form = RevenuesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Support Details have been updated')
            return redirect('Supportreport')
    context={'form':form, 'item':item}
    return render(request, 'Ministry-Support/edit_support.html', context)

class supportreceipt(View):
    def get(self, request, pk):
        support= get_object_or_404(Revenues,pk=pk)
        today = timezone.now()
        context = {'today': today,'support': support, 'request': request,}
        return Render.render('Ministry-Support/supportreceipt.html', context)

##############################<===========TITHES MODULE===========>################################# 
@login_required
def recording_tithes(request):
    if request.method=="POST":
        form=RevenuesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Total Tithes have been recorded')
            return redirect('Tithesreport')
    else:
        form=RevenuesForm()
        context={'form':form}
    return render(request, 'Tithes/record_total_tithes.html',context)
       

def edit_tithes(request, pk):
    item = Revenues.objects.get(id=pk)
    form = RevenuesForm(instance=item)
    if request.method == "POST":
        form = RevenuesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Tithesreport')
    
    context={'form':form, 'item':item}
    return render(request, 'Tithes/edit_tithes.html', context)

@login_required
def Tithesreport (request):
    context={}
    if request.method=='POST':
        items = Revenues.objects.all().order_by('-id')
        for item in items:
            item.Archived_Status = 'ARCHIVED'
            item.save()
        messages.success(request, f'Tithes Report has been Archived')
        return redirect('Tithesreport')
    #month = datetime.now().month
    year=datetime.now().year
    
    service_tithes = Revenues.objects.filter(Archived_Status="NOT-ARCHIVED", Date__year=year, Date__month=current_month, Revenue_filter='tithes')
    
    
    member_tithes=Revenues.objects.filter(Archived_Status="NOT-ARCHIVED", Date__year=year, Date__month=current_month, Tithe_Amount__gte=1)
    
    # qs1 = Revenues.objects.filter(Date__year=year, Revenue_filter='tithes')
    
    # qs2=Revenues.objects.filter(Date__year=year, Tithe_Amount__gte=1)
    # qs=qs1.union(qs2)
    context['sunday']=service_tithes
    context['total']=service_tithes.aggregate(Sum('Amount'))['Amount__sum']
    context['member']=member_tithes
    context['member_totals']=member_tithes.aggregate(Sum('Tithe_Amount'))['Tithe_Amount__sum']
    context['years']=year
    context['today']=datetime.now()
    return render(request, 'Tithes/tithesindex.html', context)    

def monthly_tithes(request):
    
    results = Revenues.objects.filter(Date__month=current_month).aggregate(totals=models.Sum("Tithe_Amount"))
    if (results['totals']):
        all_tithes = results["totals"]
    else:
        all_tithes = 0  
    context={'all_tithes':all_tithes}
    return render(request, "Tithes/current_month_tithes.html", context)
    

@login_required
def Annual_Tithes(request):
    current_year = datetime.now().year
    get_all_members=Members.objects.filter(is_active=True)
    results = Revenues.objects.filter(Date__year=current_year).aggregate(totals=models.Sum("Tithe_Amount"))
    if (results['totals']):
        all_tithes = results["totals"]
    else:
        all_tithes = 0  
    context={'all_tithes': all_tithes,'get_all_members':get_all_members, 'current_year':current_year}
    return render(request, "Tithes/current_year_tithes.html", context)
    
    
#generate individual annual tithe report
class member_annual_tithes_pdf(View):
    def get(self, request, pk):
        today = datetime.now()
        year=today.year
        get_member_name = get_object_or_404(Members, pk=pk)
        tithes = Revenues.objects.filter(Member_Id = pk, Date__year=year).order_by('-Date')
        month=today.strftime('%B')
        total = tithes.aggregate(totals=models.Sum("Tithe_Amount"))
        total_amount = total["totals"]
        context = {'year' : year,'month' : month, 'today': today,'total_amount': total_amount,'request': request,'tithes': tithes,'get_member_name':get_member_name}
        return Render.render('Tithes/memeber_annual_tithes_pdf.html', context)

#retrieve archived tithes after search
@login_required
def tithesarchivessearch(request):
    today = datetime.now()
    years=today.year
    if request.method == 'POST':
        report_year = request.POST['report_year']
        report_month = request.POST['report_month']
        archived_reports = Revenues.objects.filter(Archived_Status='ARCHIVED', Date__month=report_month, Date__year=report_year)
        results =archived_reports.aggregate(totals=models.Sum('Tithe_Amount'))
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

#create a tithe report pdf
class tithespdf(View):
    def get(self, request):
        today = datetime.now()
        mth=today.month
        year=today.year
        tithes = Revenues.objects.filter(Date__month=mth, Date__year=year).order_by('-Date')
        month=today.strftime('%B')
        total = tithes.aggregate(totals=models.Sum("Tithe_Amount"))
        total_amount = total["totals"]
        context = {'year' : year, 'today': today, 'month': month, 'total_amount': total_amount, 'request': request,
            'tithes': tithes,}
        return Render.render('Tithes/tithespdf.html', context)

#genererate a tithe receipt.
class tithesreceipt(View):
    def get(self, request, pk):
        tithes= get_object_or_404(Revenues,pk=pk)
        today = timezone.now()
        context = {'today': today,'tithes': tithes, 'request': request,}
        return Render.render('Tithes/tithesreceipt.html', context)

#generate a tithe archived pdf
class tithesarchivepdf(View):
    def get(self, request, report_month, report_year):        
        month=strptime(report_month, '%B').tm_mon
        archived_tithes = Revenues.objects.filter(Archived_Status='ARCHIVED',Date__month=month, Date__year=report_year)
        today = datetime.now()
        total = archived_tithes.aggregate(totals=models.Sum("Tithe_Amount"))
        total_amount = total["totals"]
        tithescontext = {'report_month': report_month,'report_year':report_year,'today': today,'total_amount': total_amount,
            'request': request,'archived_tithes': archived_tithes,}
        return Render.render('Tithes/tithesarchivepdf.html', tithescontext)

#aggregated annual member tithes
@login_required
def member_annual_tithes(request, pk):
    years = timezone.now().year
    tithes=Revenues.objects.filter(Member_Id=pk, Date__year=years).order_by('-pk')
    total = tithes.aggregate(totals=models.Sum("Tithe_Amount"))
    total_amount = total["totals"]
    members=Members.objects.filter(id=pk)
    tithescontext={'years':years,'tithes':tithes, 'members':members, 'total_amount':total_amount}
    return render(request, 'Tithes/member_annual_tithes.html', tithescontext) 

#####===>THANKS GIVING MODULE<===#####

#This function is not being used for now
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

#generate thanks giving report
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
    month = today.month
    years=today.year
    context={}
    items = Revenues.objects.filter(Archived_Status="NOT-ARCHIVED", Date__year=years)
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

####<=== OTHER REVENUE SOURCES MODULE===>####
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

####<== GENERAL, MAIN, PETTY EXPENSES MODULES [expenses module] ==>###
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
    items = Expenditures.objects.filter(Reason_filtering='general')
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
            return redirect('enter_sundryexpense')
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
            return redirect('enter_expenditure')
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
            return redirect('weekly_main_expenses')
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
    context={}
    items = Expenditures.objects.filter(Archived_Status='NOT-ARCHIVED', Date__year=year, Date__month=current_month)
    context['items']=items
    context['year']=today.year
    context['month']=month
    return render(request, 'Expenses/Main_Expenses_report.html', context)
    
def weekly_main_expenses (request):
    today = datetime.now()
    years=today.year
    context={}
    items = Expenditures.objects.filter(Reason_filtering='main', Archived_Status="NOT-ARCHIVED")
    context['items']=items
    context['year']=today.year
    context['month']=month
    return render(request, 'Expenses/weekly_main_expenses.html', context)

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
        archived = Expenditures.objects.filter(Archived_Status='ARCHIVED',
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
    items = Expenditures.objects.filter(Archived_Status='NOT-ARCHIVED', Date__year=year, Date__month=current_month, Reason_filtering='petty').order_by('-Date')
    context['total']=items.aggregate(Sum('Amount'))['Amount__sum']
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
        expenses = Expenditures.objects.filter(Archived_Status='NOT-ARCHIVED'\
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
    items = Expenditures.objects.filter(Reason_filtering='allowance')
    context['items']=items
    context['years']=years
    context['today']=today
    return render(request, 'Allowances/allowanceindex.html', context)

class allowancespdf(View):
    def get(self, request):
        current_month = datetime.today().month
        current_year = datetime.today().year
        allowances = Expenditures.objects.filter(Archived_Status='NOT-ARCHIVED',Date__month=current_month,Date__year=current_year).order_by('-Date')
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
    years=today.yearsu
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

#########<==============PLEDGES MODULE==============>##############

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
        return render(request, 'Pledges/add_pledge_item.html',context)

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
    if request.method == "POST":
        item.Archived_Status = 'Archived'
        item.save()
        messages.success(request, "Pledge Item successfully Archived!")
        return redirect("list-of-pledge-items")
    context = {'item':item}      
    return render(request, 'Pledges/delete_pledge_item.html', context)
    
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
        item = items.Reason
        name=items.Pledge_Made_By or items.Pledge_Made_By_Visitor
        amount_being_paid=int(request.POST.get('Amount_Paid'))
        date_of_pay=request.POST.get('Date')
        Pledges.objects.create(DateOfPayment=date_of_pay, AmountBeingPaid=amount_being_paid, NameOfPledgee=name, PledgeItem=item)
        total_paid=items.Amount_Paid+amount_being_paid
        get_pledge=Pledges.objects.filter(id=pk)
        Pledges.objects.filter(id=pk).update(Amount_Paid=total_paid)
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
        pledgescontext = {'today': today,'total_amount': total_amount,'request': request, 'archived_pledges': archived_pledges,
        }
        return Render.render('Pledges/pledgesarchivepdf.html', pledgescontext)

class pledge_debt_invoice(View):
    def get(self, request, pk):
        debt = Pledges.objects.get(Q(Status='UNPAID') | Q(Status='PARTIAL'), id=pk)
        today = datetime.now()
        debtcontext = { 'today': today, 'debt': debt, 'request': request,
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

def core_values(request):
    values = About.published.all()
    return render(request, 'abouts/core_values.html', {'values': values})

def church_details(request):
    details = About.published.all()
    return render(request, 'abouts/church_details.html', {'details': details})

class AboutCreateView(CreateView):
    model = About
    template_name = 'abouts/about_create.html'
    fields = ('banner','about_title','about', 'about_image','vision_description','mission_description','Is_View_on_Web')

    def form_valid(self, form):
        about = form.save(commit=False)
        about.save()
        return redirect('about_list')

class AboutUpdateView(UpdateView):
    model = About
    template_name = 'abouts/update_about.html'
    pk_url_kwarg = 'about_pk'
    fields = ('banner','about', 'about_image','vision_description','mission_description','Is_View_on_Web')

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
        form = AboutForm(request.POST, request.FILES, instance=about)
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

#####==>GOSPEL SERMONS MODULE<==#####
class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'

def news_wall(request):
    news = News.published.all().order_by('-date')
    paginator = Paginator(news, 9)
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

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    more_news = News.published.order_by('-date')
    paginator = Paginator(more_news, 18) 
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
# #######################################===>CHURCH MODULE<===######################################
def churchCreateView(request):
    if request.method == "POST":
        form = churchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'The Church details have been Created')
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
        return render(request, 'church/update_church.html', context)


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
    template_name = 'Ministry/ministry_list.html'
    context_object_name = 'ministry'

def ministry_wall(request):
    ministry = Ministry.published.all()
    paginator = Paginator(ministry, 6)  # 6 members on each page
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
current_year = datetime.now().year #Annual
current_month = datetime.now().month #Monthly

one_week_ago = datetime.today() - timedelta(days=7) #Weekly
day = datetime.now().today #Today

    
def _get_dates_of_week(now):
    this_week = ['date' for i in range(7)]
    current_day = now.weekday()
    if current_day == 6:
        this_week[0] = now
        for i in range(1, 7):
            add_date = now + timedelta(days=i)
            this_week[i] = add_date
    else:
        num_things_before = current_day + 1
        num_things_after = 5 - current_day
        sunday = now - timedelta(days=current_day + 1)
        this_week[0] = sunday

        for i in range(0, current_day):
            diff = current_day - i
            add_date = now - timedelta(days=diff)
            this_week[i + 1] = add_date
        for j in range(current_day + 1, 7):
            diff = j - current_day - 1
            add_date = now + timedelta(days=diff)
            this_week[j] = add_date
    return this_week
    
now = datetime.now()
date = datetime.day
current_week = _get_dates_of_week(now)
current_week_dates = [date for date in current_week]



#current week pledges
def current_week_pledges():
    total_weekly_pledges = Pledges.objects.filter(Date__month=current_month,Date__year=current_year).aggregate(totals=models.Sum("Amount_Paid"))
    if (total_weekly_pledges['totals'])!=None:
        int(total_weekly_pledges["totals"])
        d_pledges=total_weekly_pledges["totals"]
    else:
        total_weekly_pledges = 0
        d_pledges = 0
    return d_pledges

def week_of_month(date):
    date= today
    month = date.month
    week = 0
    while date.month == month:
        week += 1
        date -= timedelta(days=7)
    return week

current_year = today.year #Annual
current_month = today.month #Monthly
week=week_of_month(current_month) #Weekly



#current month totals
def current_month_balances():
    revenues=total_current_month_revenue()
    expenses=total_current_month_expenses()
    balance = revenues - expenses
    return balance 
    
     
@login_required
def index(request):
    current_year = today.year
    years = list(range(2023, current_year + 1))
    weekly_balances=total_current_week_revenue() - total_current_week_expenses()
 
    mth=calendar.month_name[current_month]
    context={
            'years':years,
            'day':today,
            'week':week_of_month(current_month), 
            'month':today.strftime('%B'),
            'total_monthly_expenses':total_current_month_expenses(),
            'total_monthly_revenues':total_current_month_revenue(),
            'current_monthly_balance':current_month_balances(),
            'current_year':current_year,
            'weekly_balance':weekly_balances,
            'current_week_total_expenses':total_current_week_expenses(),
            'current_week_total_revenues':total_current_week_revenue(),
            
            #Weekly Expenses
            'total_tot':total_current_week_tot(),
            'total_help':total_current_week_help(), 
            'total_allowances':total_current_week_allowances(),
            'total_others':total_current_week_other_expenses(), 
            'total_bills':total_current_week_bills_expenses(),
            'total_savings':total_current_week_savings(), 
            'total_love':total_current_week_love_offering_expenses(),
            'total_petty':total_current_week_petty_expenses(),
            'total_salaries':total_current_week_salaries(), 'total_main_expenses':total_current_week_main(),
            
            #Weekly Revenues
            'total_tithes':total_current_week_tithes(), 
            'total_offerings':total_current_week_offerings(),
            'total_seeds':total_current_week_seeds(),
            'total_other_sources':total_current_week_other_revenue_sources(), 'total_bills_contrib':total_current_week_bills_contributions(), 
            'total_eva':total_current_week_evanglism_contributions(), 'total_thanks':total_current_week_thanks_giving(),
            'total_love_offer':total_current_week_love_offering(), 
            
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


######################<=======CHURCH GROUPS==========>#######################
@xframe_options_exempt
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
@xframe_options_exempt
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
    Metropolitan = Members.objects.filter(is_active=True, Home_Cell="Kampala Metropolitan")
    context={
        'Church': Church,
        'Kafunda':Kafunda,
        'Kabira':Kabira,
        'Lugoba':Lugoba,
        'Kazo':Kazo,
        'Gombolola':Gombolola,
        'Kawaala':Kawaala,
        'Bombo': Bombo,
        'Katooke': Katooke,
        'Metropolitan': Metropolitan
    }
    return render(request, 'Groups/home_cells.html', context)

#########Conference Module ############
@login_required
def record_annual_conference(request):
    if request.method=="POST":
        form=AnnualConferenceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Conference details have been recorded')
            return redirect('list_of_conferences')
    else:
        form=AnnualConferenceForm()
        return render(request, 'conference/record_conference.html',{'form':form})
@login_required
def list_of_conferences(request):
    details = AnnualConference.objects.all()
    context={'details':details}
    return render(request,'conference/list.html', context)

def edit_conference_details(request, pk):
    qs=AnnualConference.objects.get(id=pk)
    if request.method == "POST":
        form = AnnualConferenceForm(request.POST, instance=qs)
        if form.is_valid():
            form.save()
            messages.success(request, f'The New conference Details Have Been Updated')
            return redirect('list_of_conferences')
    else:
        form = AnnualConferenceForm(instance=qs)
    context = {'form':form}
    return render(request, 'conference/edit_conference.html', context) 

######### New Converts Module ############
def record_new_convert(request):
    if request.method=="POST":
        form=NewConvertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Convert details have been recorded')
            return redirect('record_new_convert')
    else:
        form=NewConvertForm()
        return render(request, 'NewConverts/record_new_convert.html',{'form':form})

def new_converts_list(request):
    qs=NewConvert.objects.all()
    context = {'qs':qs}
    return render(request, 'NewConverts/new_converts_list.html', context)

def edit_new_convert(request, pk):
    qs=NewConvert.objects.get(id=pk)
    if request.method == "POST":
        form = NewConvertForm(request.POST, instance=qs)
        if form.is_valid():
            form.save()
            messages.success(request, f'The New Convert Details Have Been Updated')
            return redirect('new_converts_list')
    else:
        form = NewConvertForm(instance=qs)
    context = {'form':form}
    return render(request, 'NewConverts/edit_new_convert.html', context) 
    
def cells(request):
    return render(request, 'Groups/cells.html')
    
def groups(request):
    return render(request, 'Groups/groups.html')
    
##########lwaki oli mulamu ############
@login_required
def record_lwakiolimulamu(request):
    if request.method=="POST":
        form=LwakiOliMulamuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'details have been recorded')
            return redirect('lwakiolimulamu')
    else:
        form=LwakiOliMulamuForm()
        return render(request, 'lwakiolimulamu/record_lwakiolimulamu.html',{'form':form})
    
@login_required
def lwakiolimulamu_list(request):
    details = LwakiOliMulamu.objects.all()
    context={'details':details}
    return render(request,'lwakiolimulamu/lwakiolimulamu.html', context)

def edit_lwakiolimulamu(request, pk):
    qs=LwakiOliMulamu.objects.get(id=pk)
    if request.method == "POST":
        form = LwakiOliMulamuForm(request.POST, instance=qs)
        if form.is_valid():
            form.save()
            messages.success(request, f'details have been updated')
            return redirect('lwakiolimulamu')
    else:
        form = LwakiOliMulamuForm(instance=qs)
    context = {'form':form}
    return render(request, 'lwakiolimulamu/edit_lwakiolimulamu.html', context) 

def lwakiolimulamu_wall(request): 
    all_sermons = LwakiOliMulamu.objects.all().order_by('-date')
    paginator = Paginator(all_sermons, 4)  
    page = request.GET.get('page')
    try:
       sermon_list = paginator.page(page)
    except PageNotAnInteger:
        sermon_list = paginator.page(1)
    except EmptyPage:
        sermon_list = paginator.page(paginator.num_pages)
    context={'page':page, 'sermon_list': sermon_list}    
    return render(request, 'lwakiolimulamu/lwakiolimulamu_wall.html', context)

def lwakiolimulamu_archives(request, year):
    
    year = request.GET.get('year')
    get_all_details = LwakiOliMulamu.objects.filter(date__year=year)
    get_all_years = LwakiOliMulamu.objects.extra(select={'year': 'extract( year from date )'}).values('year').annotate(dcount=Count('date'))
    paginator = Paginator(get_all_details, 7) 
    page = request.GET.get('page')
    try:
        item_list = paginator.page(page)
    except PageNotAnInteger:
        item_list = paginator.page(1)
    except EmptyPage:
        item_list = paginator.page(paginator.num_pages)
    context = {
        'page':page,
        'item_list': item_list,
        'get_all_details':get_all_details, 'get_all_years':get_all_years
    }
    return render(request,"lwakiolimulamu/archives_of_lwakiolimulamu.html", context)
    
def lwakiolimulamu_detail(request, pk):
    item = get_object_or_404(LwakiOliMulamu, pk=pk)
    year = request.GET.get('year')
    more_details = LwakiOliMulamu.objects.all().order_by('-date')
    paginator = Paginator(more_details, 7) 
    page = request.GET.get('page')
    try:
        item_list = paginator.page(page)
    except PageNotAnInteger:
        item_list = paginator.page(1)
    except EmptyPage:
        item_list = paginator.page(paginator.num_pages)
    context = {
         'page':page,
        'item': item,
        'more_details': more_details,
        'item_list': item_list,
    }
    return render(request, 'lwakiolimulamu/lwakiolimulamu_details.html', context)
    
    
############# Blog Module ##################
def add_blogpost(request): 
    forms = BlogForm(request.POST or None)
    if request.method == 'POST':
        if forms.is_valid():
            forms.save()
            return redirect('BlogPosts')
    context = {
            'form': forms
        }
    return render(request, 'blog/add_blogpost.html', context)

def list_blogs(request):
    posts = Blog.objects.filter(is_active=True).order_by('-created_at')
    context = {
            'posts': posts
        }
    return render(request, 'blog/blogs-list.html', context)

def BlogPosts(request):
    blogposts = Blog.objects.all().order_by('-created_at')
    context = {'blogposts':blogposts, }
    return render(request, 'blog/blogposts.html',context)

def BlogPost_detail(request, slug):
    blogposts = Blog.objects.get(slug=slug)
    more_blogs = Blog.objects.filter(is_active=True).order_by('-date')
    paginator = Paginator(more_blogs, 10) 
    page = request.GET.get('page')
    try:
       blogs_list = paginator.page(page)
    except PageNotAnInteger:
        blogs_list = paginator.page(1)
    except EmptyPage:
        blogs_list = paginator.page(paginator.num_pages)
    context={'blogposts':blogposts,'page':page, 'blogs_list': blogs_list, 'more_blogs': more_blogs}
    return render(request, 'blog/blogpost_details.html',context)
    
def blog_wall(request):
    blogs = Blog.objects.filter(is_active=True).order_by('-date')
    paginator = Paginator(blogs, 12)
    page = request.GET.get('page')
    try:
       blog_list = paginator.page(page)
    except PageNotAnInteger:
        blog_list = paginator.page(1)
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)
    context={'page':page, 'blog_list': blog_list}
    return render(request, 'blog/blogs_wall.html', context)
    
    
def search_tagged_blogs(request):        
    qs=str(request.GET.get('q'))

    get_all_posts = Blog.objects.filter(tags__name=qs).order_by('-date')
    
    context={'get_all_posts':get_all_posts,'qs':qs}
    return render(request,'blog/blogs_searched.html', context)
    
def tagged_articles(request):        
    qs=str(request.GET.get('q'))

    tagged_sermons = News.objects.filter(tags__name=qs).order_by('-date')
    
    context={'tagged_sermons':tagged_sermons,'qs':qs}
    return render(request,'news/tagged_sermons.html', context)

#################Implement rest framework #######################
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import Http404
from .serializers import RegisteredMemberSerializer
class MemberAPIView(APIView):
    
    def get_object(self, pk):
        try:
            return Members.objects.filter(pk=pk)
        except Members.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = Members.objects.all()
        serializer = RegisteredMemberSerializer(data, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):
        data = request.data
        serializer = RegisteredMemberSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()
        response.data = {
            'message': 'member Created Successfully',
            'data': serializer.data
        }
        return response


    def put(self, request, pk=None, format=None):

        todo_to_update = Members.objects.get(pk=pk)

        serializer = RegisteredMemberSerializer(instance=todo_to_update,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()
        response.data = {
            'message': 'member Updated Successfully',
            'data': serializer.data
        }
        return response


    def delete(self, request, pk, format=None):
        todo_to_delete =  Members.objects.get(pk=pk)
        todo_to_delete.delete()

        return Response({
            'message': 'member Deleted Successfully'
        })
        
        
def record_group_contributions(request):
    if request.method=="POST":
        form=GroupContributionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Group Contribution has been recorded')
            return redirect('list-group-contributions')
    else:
        form=GroupContributionForm()
        context={'form':form}
        return render(request, 'Groups/record_contributions.html', context)
    
def list_group_contributions(request):
    qs = Revenues.objects.exclude(Group__exact=None)
    context={'qs':qs, 'today':today}
    return render(request, 'Groups/group_contribution_list.html', context)

def deduct_sunday_expenses(request):
    if request.method == "POST":
        form = SundayExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Sunday expenses have been deducted')
            return redirect('deduct-sunday-expenses')
    form = SundayExpensesForm()
    context = {'form':form}
    return render(request, 'Expenses/deduct_sunday_expenses.html', context)
    
    
def edit_sunday_expense(request, pk):
    item = get_object_or_404(Expenditures, pk=pk)
    if request.method == "POST":
        form = SundayExpensesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('expenditurereport')
    else:
        form = SundayExpensesForm(instance=item)
    return render(request, 'Expenses/edit_sunday_expenses.html', {'form': form})
    
    
    
#=====================REST APIs=========================================

@api_view(['GET'])
def uccbwaise_members_api(request):
  if request.method == 'GET':
    results = Members.objects.all()
    serializer  = RegisteredMemberSerializer(results, many=True)
    return Response(serializer.data)
    
    
@api_view(['GET'])
def revenues_api(request):
  if request.method == 'GET':
    results = Revenues.objects.all()
    serializer  = RevenuesSerializer(results, many=True)
    return Response(serializer.data)
  
    
@api_view(['GET'])
def expenditures_api(request):
  if request.method == 'GET':
    results = Expenditures.objects.all()
    serializer  = ExpendituresSerializer(results, many=True)
    return Response(serializer.data)



from django.shortcuts import render
from .models import Revenues, Expenditures
import datetime

def yearly_comparison(request, year):
    # Retrieve the revenue and expenditure data from the database
    revenue_list = Revenues.objects.all().values('Date', 'Amount','Building_Amount','Love_Offering_Amount','Thanks_Giving_Amount','Bills_Amount','Seed_Amount','Envag_Or_Missions_Amount','Tithe_Amount', 'General_Offering_Amount',)
     
    expenditure_list = Expenditures.objects.all().values('Date', 'Amount', 'Allowances_Amount','Love_Offering_Amount','Help_Amount', 'Bills_Amount', 'Tithe_Of_Tithes_Amount', 'Savings_Amount', 'Seed_Amount', 'Other_Expenses_Amount', 'Transport', 'Lunch', 'Data_or_airtime', 'Renovation', 'Stationery')
     
    salary_paid_list = SalariesPaid.objects.all().values('Date_of_paying_salary', 'Salary_Amount',)
    # Filter the revenue and expenditure data for the specified year
    salary_paid_list = [salary for salary in salary_paid_list if salary['Date_of_paying_salary'].year == year]
    revenue_list = [revenue for revenue in revenue_list if revenue['Date'].year == year]
    expenditure_list = [expenditure for expenditure in expenditure_list if expenditure['Date'].year == year]

    # Create a dictionary to store the monthly revenue and expenditure totals
    monthly_data = {}

    # Loop through each month of the year to calculate the revenue and expenditure totals
    for month in range(1, 13):
        monthly_data[month] = {
            'salary': sum([salary['Salary_Amount'] or 0 for salary in salary_paid_list if salary['Date_of_paying_salary'].month == month]), 
            
            'revenue': sum([revenue['Amount'] or 0 for revenue in revenue_list if revenue['Date'].month == month]),
            
            'building_amount': sum([revenue['Building_Amount'] or 0 for revenue in revenue_list if revenue['Date'].month == month]),
            
            'love_offering_amount': sum([revenue['Love_Offering_Amount'] or 0 for revenue in revenue_list if revenue['Date'].month == month]),
            
            'thanks_giving_amount': sum([revenue['Thanks_Giving_Amount'] or 0 for revenue in revenue_list if revenue['Date'].month == month]),
            
            'bills_amount': sum([revenue['Bills_Amount'] or 0 for revenue in revenue_list if revenue['Date'].month == month]),
            
            'seed_amount': sum([revenue['Seed_Amount'] or 0 for revenue in revenue_list if revenue['Date'].month == month]),
            
            'envag_or_missions_amount': sum([revenue['Envag_Or_Missions_Amount'] or 0 for revenue in revenue_list if revenue['Date'].month == month]),
            
            'tithe_amount': sum([revenue['Tithe_Amount'] or 0 for revenue in revenue_list if revenue['Date'].month == month]),
            
            'general_offering_amount': sum([revenue['General_Offering_Amount'] or 0 for revenue in revenue_list if revenue['Date'].month == month]),
            
            
            
            
            'expenditure': sum([expenditure['Amount'] or 0 for expenditure in expenditure_list if expenditure['Date'].month == month]),
            
            'allowances_amount': sum([expenditure['Allowances_Amount'] or 0 for expenditure in expenditure_list if expenditure['Date'].month == month]),
            
            'love_offering_amount_expenditure': sum([expenditure['Love_Offering_Amount'] or 0 for expenditure in expenditure_list if expenditure['Date'].month == month]),
            
            'help_amount': sum([expenditure['Help_Amount'] or 0 for expenditure in expenditure_list if expenditure['Date'].month == month]),
            
            'Bills_Amount': sum([expenditure['Bills_Amount'] or 0 for expenditure in expenditure_list if expenditure['Date'].month == month]),
            
            'Tithe_Of_Tithes_Amount': sum([expenditure['Tithe_Of_Tithes_Amount'] or 0 for expenditure in expenditure_list if expenditure['Date'].month == month]),
            
            'Savings_Amount': sum([expenditure['Savings_Amount'] or 0 for expenditure in expenditure_list if expenditure['Date'].month == month]),
            
            'Seed_Amount': sum([expenditure['Seed_Amount'] or 0 for expenditure in expenditure_list if expenditure['Date'].month == month]),
            
            'Other_Expenses_Amount': sum([expenditure['Other_Expenses_Amount'] or 0 for expenditure in expenditure_list if expenditure['Date'].month == month]),
            
            'Transport': sum([expenditure['Transport'] or 0 for expenditure in expenditure_list if expenditure['Date'].month == month]),
            
            'Lunch': sum([expenditure['Lunch'] or 0 for expenditure in expenditure_list if expenditure['Date'].month == month]),
            
            'Data_or_airtime': sum([expenditure['Data_or_airtime'] or 0 for expenditure in expenditure_list if expenditure['Date'].month == month]),
            
            'Renovation': sum([expenditure['Renovation'] or 0 for expenditure in expenditure_list if expenditure['Date'].month == month]),
            
            'Stationery': sum([expenditure['Stationery'] or 0 for expenditure in expenditure_list if expenditure['Date'].month == month]),
            
            
            
        }

    # Create a list of labels for the X-axis of the bar chart
    labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Create a list of revenue and expenditure data for the Y-axis of the bar chart
    revenue_data = [monthly_data[month]['revenue'] for month in range(1, 13)]
    expenditure_data = [monthly_data[month]['expenditure'] for month in range(1, 13)]

    # Create a context dictionary containing the revenue and expenditure data, as well as the labels for the X-axis
    context = {
        'revenue_data': revenue_data,
        'expenditure_data': expenditure_data,
        'labels': labels,
        'year': year,
    }

    # Render the template with the context dictionary
    return render(request, 'yearly_comparison.html', context)
