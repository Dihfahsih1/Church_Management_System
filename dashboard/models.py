from django.utils.timezone import now
from datetime import datetime
from django.db import models
from django.urls import reverse
from django.db.models import Model
from django.db.models import Sum
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import PermissionsMixin

ministries=(
    ('Pastoral', 'Pastoral'),
    ('Discipleship', 'Discipleship'),
    ('Worship Team', 'Worship Team'),
    ('Ushering', 'Ushering'),
    ('Orchestra', 'Orchestra'),
    ('Youth Leadership', 'Youth Leadership'),
    ('Teens', 'Teens'),)
OPTIONS = (('Yes', 'Yes'),
           ('No', 'No'))
ROLE_CHOICES = (
    ('SuperAdmin', 'SuperAdmin'),
    ('Members', 'Members'),
    ('Secretary', 'Secretary'),
    ('Admin', 'Admin'),
    ('Building Chair', 'Building Chair'),
    ('Marrieds Leader', 'Marrieds Leader'),
    ('Youth Leader', 'Youth Leader'),
)
Week_Days = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)
class PublishedStatusManager(models.Manager):
    def get_queryset(self):
        return super(PublishedStatusManager, self).get_queryset().filter(Is_View_on_Web='Yes')

class UserManager(BaseUserManager):
    def create_user(self, username,password=None):
        if not username:
            raise ValueError('User must have a username.')
            
        if not password:
            raise ValueError('User must have a password.')    
        user_obj = self.model(username=username,)
        user_obj.set_password(password) 
        user_obj.save(using=self._db)
        return user_obj 
    def create_superuser(self, username,password):
        user_obj = self.create_user(
            password=password,
            username=username,
        )
        user_obj.is_admin = True
        user_obj.is_staff = True
        user_obj.is_superuser = True
        user_obj.save(using=self._db)
        return user_obj    
class User(AbstractBaseUser , PermissionsMixin):
    roles=(
        ('Admin','Admin'),('Secretary','Secretary') ,('SuperAdmin','SuperAdmin') ,
        ('Building Chair', 'Building Chair'),
       ('Marrieds Leader', 'Marrieds Leader'),
       ('Youth Leader', 'Youth Leader'),   
    )
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True)
    Role = models.CharField(max_length=250, choices=roles)
    full_name =  models.ForeignKey('Members', on_delete=models.SET_NULL,  max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)   # can login
    is_staff = models.BooleanField(default=False)  # staff user non superuser
    is_superuser = models.BooleanField(default=False)
    Is_View_on_Web = models.CharField(max_length=20, default='Yes', choices=OPTIONS,null=True,blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FILEDS = []
    objects = UserManager()
    published = PublishedStatusManager()
    def __str__(self):
        return self.Role
class Sundry(Model):
    reason=(
        ('Lunch','Lunch'),('Upkeep','Upkeep'),('Airtime/Data','Airtime/Data')      
    )
    Date = models.DateField(null=True, blank=True)
    Payment_Made_To = models.CharField(max_length=100, blank=False)
    Reason_For_Payment = models.CharField(max_length=250, choices=reason)
    Amount = models.IntegerField()
    def __str__(self):
        return self.Payment_Made_To

class Offerings(Model):
    services = (('Home Cell Service','Home Cell Service'),('Youth Service','Youth Service'),('Wednesday Service','Wednesday Service'),
        ('Bible Study Service','Bible Study Service'),('Friday Overnight','Friday Overnight'),('SundayFirst Service','Sunday First Service'),
        ('Sunday Second Service','Sunday Second Service'),('Sunday Third Service','Sunday Third Service'),
        )
    Date = models.DateField(null=True, blank=True)
    Total_Offering = models.IntegerField()
    Service=models.CharField(max_length=100, choices=services, blank=False)
    def __str__(self):
        return self.Total_Offering

class GeneralExpenses(Model):
    expenses = (('Generator Mechanic','Generator Mechanic'),('Instruments','Servicing Music Instruments'),('Condolences','Condolences'),
        ('Stationery','Stationery'),('Repair','Any Other Repair'),('Purchase','Purchase'),
        ('Renovations','Renovations')
        )
    Date = models.DateField(null=True, blank=True)
    Payment_Made_To = models.CharField(max_length=100,blank=False)
    Amount = models.IntegerField()
    Expense_Reason=models.CharField(max_length=100, choices=expenses, blank=False)
    def __str__(self):
        return self.Expense_Reason
class Spend(models.Model):
    reason=(
        ('Water Bills','Water Bills'),('Yaka Bills','Yaka Bills'),
        ('Transport','Transport'), ('Love Offering','Love Offering'),('Medical Bills','Medical Bills'),('Rent','Rent'),
        ('Help','Help'),('Drinks','Drinks'),('Savings','Savings'),
        ('Evangelism','Evangelism')
    )
    Date = models.DateField(null=True, blank=True)
    Payment_Made_To = models.CharField(max_length=100,blank=False)
    Reason_For_Payment = models.CharField(max_length=100, choices=reason)
    Amount = models.IntegerField()

    def __str__(self):
        return 'Name:{0}, Reason:{1}, Amount: {2}'.format(self.Payment_Made_To, self.Reason_For_Payment, self.Amount)

##########################################
# REPORT ARCHIVING MODELS AFTER SUBMISSION #
##########################################

class ExpensesReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Name = models.CharField(max_length=100, default='Name', null=True)
    Amount = models.FloatField( null=True)
    Reason = models.CharField(max_length=100,null=True)
    month = models.CharField(max_length=100,null=True)
    year = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1} Reason:{2} Amount:{0}'.format(self.Name,self.Reason, self.Amount)

class GeneralExpensesReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Name = models.CharField(max_length=100, default='Name', null=True)
    Amount = models.FloatField(.0, null=True)
    Reason = models.CharField(max_length=100,null=True)
    month = models.CharField(max_length=100,null=True)
    year = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1} Reason:{2} Amount:{0}'.format(self.Name,self.Reason, self.Amount)        
class SundryReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Name = models.CharField(max_length=100, default='Name', null=True)
    Amount = models.FloatField(.0, null=True)
    Reason = models.CharField(max_length=100,null=True)
    month = models.CharField(max_length=100,null=True)
    year = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1} Reason:{2} Amount:{0}'.format(self.Name,self.Reason, self.Amount)

class AllowanceReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Staff = models.CharField( max_length=100,null=True)
    Month = models.CharField(max_length=100,null=True)
    Amount = models.IntegerField()
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1}  Amount:{0}'.format(self.Staff, self.Amount)

class OfferingsReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Service = models.CharField( max_length=100,null=True)
    Amount = models.IntegerField()
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1}  Amount:{0}'.format(self.Day, self.Amount)  
        
class Members(models.Model):
    sex=(('Female','Female'),('Male','Male'))
    ini=(('Mr.','Mr.'),('Mrs.','Mrs.'),('Ms.','Ms.'),('Pr.','Pr.'),('Dr.','Dr.'),('Eng.','Eng.'))
    status=(('Married','Married'),('Single','Single'),('Divorced','Divorced'),('Widower','Widower'),('Widow','Widow'))
    marriage=(('Church_Marriage','Church_Marriage'),('Customary','Customary'),('Legal','Legal'),('Cohabiting','Cohabiting'))
    education=(('Masters','Master'),('Degree','Degree'),('Diploma','Diploma'),('Certificate','Certificate'),('None','None'),
        ('Still_Studying','Still_Studying'),('Primary_Graduate','Primary_Graduate'),('O_Level_Graduate','O_Level_Graduate'),('A_Level_Graduate','A_Level_Graduate'))
    employment=(('Employed','Employed'),('Unemployed','Unemployed'))
    cell=(
        ('Church Zone','Church Zone'),('Kabira Zone','Kabira Zone'),('Kafunda Zone','Kafunda Zone'),('Lugoba Zone','Lugoba Zone') ,('Katooke Zone','Katooke Zone'),
        ('Kazo Zone','Kazo Zone'),('Gombolola Zone','Gombolola Zone'),('Kawaala Zone','Kawaala Zone'),('Bombo Rd Zone','Bombo Rd Zone')
        )
    grouping=(
        ('God is Able','God is Able'),('Winners','Winners'),('Overcomers','Overcomers'),('Biyinzika','Biyinzika') ,
        ('Victors','Victors'),('Issachar','Issachar')
        )
    Group=models.CharField(max_length=100, choices=grouping, null=True, blank=True, default="God Is Able")
    Initials=models.CharField(max_length=100, choices=ini,null=True, blank=True)
    First_Name=models.CharField(max_length=100,null=True)
    Second_Name=models.CharField(max_length=100,null=True)
    Home_Cell=models.CharField(max_length=100, choices=cell,null=True)
    Residence=models.CharField(max_length=100,null=True)
    Telephone=models.CharField(max_length=100,null=True)
    Email=models.CharField(max_length=100,null=True, blank=True)
    Photo=models.ImageField(upload_to='avatars/', blank=False)
    Gender=models.CharField(max_length=100, choices=sex, null=True, blank=True)
    Marital_Status=models.CharField(max_length=100, choices=status,null=True, blank=True)
    Marriage_Kind=models.CharField(max_length=100, choices=marriage,null=True, blank=True)
    Education_Level=models.CharField(max_length=100, choices=education,null=True, blank=True)
    Profession=models.CharField(max_length=100, choices=employment,null=True, blank=True)
    Type_of_Work=models.CharField(max_length=100,null=True, blank=True)
    Place_of_Work=models.CharField(max_length=100,null=True, blank=True)
    Country=models.CharField(max_length=100,null=True, blank=True)
    County=models.CharField(max_length=100,null=True, blank=True)
    Parish=models.CharField(max_length=100,null=True, blank=True)
    District=models.CharField(max_length=100,null=True, blank=True)
    Sub_County=models.CharField(max_length=100,null=True, blank=True)
    Village=models.CharField(max_length=100,null=True, blank=True)
    Date_Of_Salvation=models.DateField(null=True,blank=True)
    Date_Of_Birth=models.DateField(null=True,blank=True)
    Date_Of_Joining_UCC_Bwaise=models.DateField(null=True,blank=True)
    Ministry_Involved_In=models.CharField(max_length=100, default='Discipleship', choices=ministries,null=True,blank=True)
    Name_Of_Next_Of_Kin=models.CharField(max_length=100,null=True,blank=True)
    Contact_Of_Next_Of_Kin=models.CharField(max_length=100,null=True,blank=True)
    Residence_Of_Next_Of_Kin=models.CharField(max_length=100,null=True,blank=True)
    More_Info =models.TextField(max_length=1000000,null=True,blank=True)
    Is_View_on_Web = models.CharField(max_length=20, default='Yes', choices=OPTIONS,null=True,blank=True)
    objects = models.Manager()
    published = PublishedStatusManager()
    def __str__(self):
        return self.First_Name + ' ' + self.Second_Name
    @property
    def full_name(self):
        return str(self.First_Name) + ' ' + str(self.Second_Name)

    objects = models.Manager()
    published = PublishedStatusManager()
class Visitors(models.Model):

    Photo=models.ImageField(upload_to='avatars/', blank=False)
    First_Name=models.CharField(max_length=100, null=True)
    Second_Name=models.CharField(max_length=100, null=True)
    Address=models.CharField(max_length=100, null=True)
    Telephone=models.CharField(max_length=100, null=True)
    Church=models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.First_Name + ' ' + self.Second_Name

class StaffDetails(models.Model):
    rol=(('Security','Security'),('Secretary','Secretary'),('Church-Welfare','Church-Welfare'),('Admin','Admin'))
    sex=(('Male','Male'),('Female','Female'))
    education=(('Masters','Master'),('Degree','Degree'),('Diploma','Diploma'),('Certificate','Certificate'))
    rel =(('Born Again','Born Again'),('Others','Others'))
    member=(('Yes','Yes'),('No','No'))
    UCC_Bwaise_Member=models.CharField(max_length=100, choices=member,blank=True, null=True)
    Church_Member=models.ForeignKey(Members, on_delete=models.SET_NULL,  max_length=100, null=True, blank=True)
    First_Name=models.CharField(max_length=100,blank=True,null=True)
    Second_Name=models.CharField(max_length=100,blank=True,null=True)
    Gender=models.CharField(max_length=100, choices=sex, null=True, blank=True)
    Date_Of_Birth=models.DateField(null=True, blank=True)
    Education_Level=models.CharField(max_length=100, choices=education,null=True, blank=True)
    Residence=models.CharField(max_length=100,null=True, blank=True)
    Telephone=models.CharField(max_length=100,null=True, blank=True)
    Photo=models.ImageField(upload_to='avatars/', null=True, blank=True)
    Faith=models.CharField(max_length=100, choices=rel, null=True, blank=True)
    Date_of_paying_salary = models.DateField(null=True, blank=True)
    Month_being_cleared = models.DateField(null=True, blank=True)
    Salary_Amount = models.IntegerField()
    Role = models.CharField(max_length=200, choices=rol, blank=True, null=True)
    Date_of_employment=models.DateField(null=False, blank=False)
    End_of_contract=models.DateField(null=False, blank=False)
    Is_View_on_Web = models.CharField(max_length=20, default='Yes', choices=OPTIONS,null=True,blank=True)
    objects = models.Manager()
    published = PublishedStatusManager()
    @property
    def total_salary_paid(self):
        current_month = datetime.now().month
        current_year = datetime.now().year
        if self.UCC_Bwaise_Member == 'Yes':
            bal = SalariesPaid.objects.filter(Salary_Id=self.Church_Member_id, Date_of_paying_salary__year=current_year, Date_of_paying_salary__month=current_month).aggregate(totals=models.Sum("Salary_Amount"))
            if bal['totals'] == None:
                return 0
            else:    
                return bal['totals']
        else:
            bal = SalariesPaid.objects.filter(Salary_Id=self.id, Date_of_paying_salary__year=current_year, Date_of_paying_salary__month=current_month).aggregate(totals=models.Sum("Salary_Amount"))
            if bal['totals'] == None:
                return 0
            else:    
                return bal['totals']

                
    @property
    def Balance(self):
       bal=(self.Salary_Amount) - (self.total_salary_paid)
       return bal
    @property
    def full_name(self):
        return str(self.First_Name)+ ' ' + str(self.Second_Name)

class SalariesPaid(models.Model):
    Salary_Id = models.CharField(max_length=200,null=True, blank=True)
    Name = models.CharField(max_length=200,null=True, blank=True)
    Salary_Amount = models.IntegerField()
    Month_being_cleared = models.DateField(null=True, blank=True)
    Date_of_paying_salary = models.DateField(null=True, blank=True)
    @property
    def basic_salary(self):
        if StaffDetails.objects.filter(Church_Member_id=self.Salary_Id):
            staffs=StaffDetails.objects.filter(Church_Member_id=self.Salary_Id)
            for i in staffs:
                salary=i.Salary_Amount
                return salary
        else:
            staffs=StaffDetails.objects.filter(id=self.Salary_Id)
            for i in staffs:
                salary=i.Salary_Amount
                return salary
                
    
    @property
    def total_salary_paid(self):
        if StaffDetails.objects.filter(Church_Member_id=self.Salary_Id):
            staffs=StaffDetails.objects.filter(Church_Member_id=self.Salary_Id)
            for i in staffs:
                s_id=i.Church_Member_id
                current_month = datetime.now().month
                current_year = datetime.now().year
                bal = SalariesPaid.objects.filter(Salary_Id=s_id, Date_of_paying_salary__year=current_year, Date_of_paying_salary__month=current_month).aggregate(totals=models.Sum("Salary_Amount"))
                if bal['totals'] == None:
                    return 0
                else:    
                    return bal['totals']
        else:
            staffs=StaffDetails.objects.filter(id=self.Salary_Id)
            for i in staffs:
                s_id=i.id
                current_month = datetime.now().month
                current_year = datetime.now().year
                bal = SalariesPaid.objects.filter(Salary_Id=s_id, Date_of_paying_salary__year=current_year, Date_of_paying_salary__month=current_month).aggregate(totals=models.Sum("Salary_Amount"))
                if bal['totals'] == None:
                    return 0
                else:    
                    return bal['totals']
                    
    @property
    def Balance(self):
        if StaffDetails.objects.filter(Church_Member_id=self.Salary_Id):
            staffs=StaffDetails.objects.filter(Church_Member_id=self.Salary_Id)
            for i in staffs:
                s_id=i.Church_Member_id
                a_amount=i.Salary_Amount
                current_month = datetime.now().month
                current_year = datetime.now().year
                bal = SalariesPaid.objects.filter(Salary_Id=s_id, Date_of_paying_salary__year=current_year, Date_of_paying_salary__month=current_month).aggregate(totals=models.Sum("Salary_Amount"))
                balance =a_amount - bal['totals']
                return balance
        else:
            staffs=StaffDetails.objects.filter(id=self.Salary_Id)
            for i in staffs:
                s_id=i.id
                a_amount=i.Salary_Amount
                current_month = datetime.now().month
                current_year = datetime.now().year
                bal = SalariesPaid.objects.filter(Salary_Id=s_id, Date_of_paying_salary__year=current_year, Date_of_paying_salary__month=current_month).aggregate(totals=models.Sum("Salary_Amount"))
                balance =a_amount - bal['totals']
                return balance
          

class ThanksGiving(Model):
    services = (('Home Cell Service','Home Cell Service'),('Youth Service','Youth Service'),('Wednesday Service','Wednesday Service'),
        ('Bible Study Service','Bible Study Service'),('Friday Overnight','Friday Overnight'),('SundayFirst Service','Sunday First Service'),
        ('Sunday Second Service','Sunday Second Service'),('Sunday Third Service','Sunday Third Service'))
    Date = models.DateField(null=True, blank=True)
    Thanks_Giving_By = models.ForeignKey(Members, on_delete=models.SET_NULL,  max_length=100, null=True, blank=True)
    Amount = models.IntegerField()
    Service=models.CharField(max_length=100, choices=services, blank=False)
    def __str__(self):
        return self.Thanks_Giving_By
class ThanksGivingReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Thanks_Giving_By = models.ForeignKey(Members, on_delete=models.SET_NULL,  max_length=100, null=True, blank=True)
    Amount = models.IntegerField()
    Service=models.CharField(max_length=100, null=True, blank=False)
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)
    def __str__(self):
        return 'Name: {1}  Amount:{0}'.format(self.Thanks_Giving_By, self.Amount)        

class Seeds(Model):
    services = (('Home Cell Service','Home Cell Service'),('Youth Service','Youth Service'),('Wednesday Service','Wednesday Service'),
        ('Bible Study Service','Bible Study Service'),('Friday Overnight','Friday Overnight'),('SundayFirst Service','Sunday First Service'),
        ('Sunday Second Service','Sunday Second Service'),('Sunday Third Service','Sunday Third Service'))
    Date = models.DateField(null=True, blank=True)
    Seed_Made_By = models.ForeignKey(Members, on_delete=models.SET_NULL,  max_length=100, null=True, blank=True)
    Amount = models.IntegerField()
    Service=models.CharField(max_length=100, choices=services, blank=False)
    def __str__(self):
        return self.Seed_Made_By  
class Donations(Model):
    Date = models.DateField(null=True, blank=True)
    Donated_By = models.CharField(max_length=100, null=True, blank=True)
    Amount = models.IntegerField()
    Reason=models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.Donated_By

class SeedsReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Seed_Made_By = models.ForeignKey(Members, on_delete=models.SET_NULL,  max_length=100, null=True, blank=True)
    Amount = models.IntegerField()
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)

class DonationsReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Reason = models.CharField(max_length=100, null=True, blank=True)
    Amount = models.IntegerField()
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)

class Tithes(Model):
    services = (('Home Cell Service','Home Cell Service'),('Youth Service','Youth Service'),('Wednesday Service','Wednesday Service'),
        ('Bible Study Service','Bible Study Service'),('Friday Overnight','Friday Overnight'),('SundayFirst Service','Sunday First Service'),
        ('Sunday Second Service','Sunday Second Service'),('Sunday Third Service','Sunday Third Service'))
    Date = models.DateField(null=True, blank=True)
    Tithe_Made_By = models.ForeignKey(Members, on_delete=models.SET_NULL,  max_length=100, null=True, blank=True)
    Amount = models.IntegerField()
    Service=models.CharField(max_length=100, choices=services, blank=False)
    def __str__(self):
        return self.Tithe_Made_By

class TithesReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Tithe_Made_By = models.ForeignKey(Members, on_delete=models.SET_NULL,  max_length=100, null=True, blank=True)
    Amount = models.IntegerField()
    Service = models.CharField(max_length=100,null=True, blank=True, default="Third Service")
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)
    def __str__(self):
        return 'Name: {1}  Amount:{0}'.format(self.Tithe_Made_By, self.Amount)
class SalariesPaidReportArchive(models.Model):
    Salary_Id = models.CharField(max_length=200,null=True, blank=True)
    Name = models.CharField(max_length=200,null=True, blank=True)
    Salary_Amount = models.IntegerField()
    Month_being_cleared = models.DateField(null=True, blank=True)
    Date_of_paying_salary = models.DateField(null=True, blank=True)
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.Name
class Allowance(models.Model):
    months = (
        ('January','January'),('February','February'),('March', 'March'),('April', 'April')
        ,('May','May'),('June', 'June'),('July', 'July'),('August','August'),
        ('September', 'September'),('October', 'October'),('November','November'),('December', 'December')
    )
    Date = models.DateField(null=True, blank=True)
    Name =  models.ForeignKey(Members, on_delete=models.SET_NULL,  max_length=100, null=True, blank=True)
    Month = models.CharField(max_length=12,choices=months, blank=False)
    Amount = models.IntegerField()
    def __str__(self):
        return self.Name 
#PLEDGES MODEL
class PledgeItem(Model):
    Date = models.DateField(blank=True, null=True)
    Item_That_Needs_Pledges = models.CharField(max_length=100, unique=True)
    Amount_Needed = models.IntegerField(blank=True, null=True)
    Pledge_Deadline = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.Item_That_Needs_Pledges
    @property 
    def Total_Item_Cashout(self):
        results = PledgesCashedOut.objects.filter(Item_Id=self.id).aggregate(totals=models.Sum("Amount_Cashed_Out"))
        
        if (results['totals']):
            return results["totals"]
        else:
            return 0 
    @property 
    def Amount_needed_after_cashout(self):
        results=self.Amount_Needed-self.Total_Item_Cashout
        return results
             
    @property
    def Total_Amount_Pledged(self):
        results = Pledges.objects.filter(Reason__Item_That_Needs_Pledges=self.Item_That_Needs_Pledges).aggregate(totals=models.Sum("Amount_Pledged"))
        if (results['totals']):
            return results["totals"]
        else:
            return 0 
    @property
    def Pledge_Amount_Remaining(self):
        results=self.Amount_Needed-self.Total_Amount_Pledged
        return results
    #total money paid for a particular item
    @property
    def Item_money_received(self):
        results=PaidPledges.objects.filter(Reason__Item_That_Needs_Pledges=self.Item_That_Needs_Pledges).aggregate(totals=models.Sum("Amount_Paid"))
        if (results['totals']):
            return results["totals"]
        else:
            return 0 
    @property
    def Item_money_balance(self):
        results=self.Total_Amount_Pledged-self.Item_money_received
        return results
class PledgesCashedOut(Model):
    Date = models.DateField(blank=True, null=True)
    Item_That_Needs_Pledges = models.CharField( max_length=100, blank=True, null=True)
    Item_Id = models.CharField(max_length=100, blank=True, null=True)
    Amount_Needed = models.IntegerField(blank=True, null=True)
    Amount_Cashed_Out = models.IntegerField(blank=True, null=True)
    
class Pledges(Model):
    paid = 'PAID'
    partial = 'PARTIAL'
    unpaid = 'UNPAID'
    state = ((paid, 'Paid'), (partial, 'Partial'), (unpaid, 'Unpaid'))
    Status=models.CharField(max_length=100, choices=state, null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    Pledge_Made_By = models.ForeignKey(Members, on_delete=models.SET_NULL,  max_length=100,null=True, blank=False)
    Reason = models.ForeignKey(PledgeItem, on_delete=models.SET_NULL,  max_length=100, blank=True, null=True)
    Amount_Pledged = models.IntegerField()
    Amount_Paid = models.IntegerField(blank=True, null=True)
    Balance = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.Pledge_Made_By

    @property
    def Total_Amount_Pledged(self):
        return self._foo
        
    #using decorators to archive the calculations
    @property
    def total_pledge_paid(self):
        results = PaidPledges.objects.filter(Pledge_Id=self.id).aggregate(totals=models.Sum("Amount_Paid"))
        if (results['totals']):
            return results["totals"]
        else:
            return 0 
    @property
    def Pledge_Balance(self):
        results=self.Amount_Pledged - self.total_pledge_paid
        return results
    @property
    def updatestatus(self):
        if (self.total_pledge_paid >= self.Amount_Pledged):
            self.Status = self.paid
            self.save()
            return self.Status

        elif (self.total_pledge_paid == 0):
            self.Status = self.unpaid
            self.save()
            return self.Status

        elif (self.total_pledge_paid < self.Amount_Pledged):
            self.Status = self.partial
            self.save()
            return self.Status

        else:
            return self.Status    


class PaidPledges(Model):
    Reason=models.ForeignKey(PledgeItem, on_delete=models.SET_NULL,  max_length=100, null=True, blank=True)
    Pledge_Id=models.IntegerField(blank=True, null=True)
    Pledge_Made_By = models.ForeignKey(Members, on_delete=models.SET_NULL,null=True,  max_length=100, blank=False)
    Amount_Paid = models.IntegerField(blank=True, null=True)
    Date = models.DateField(null=True, blank=True)

        #x=Pledges.objects.filter(pk=self.Pledge_Id).values_list('pk', flat=True)
        #results=PaidPledges.objects.values('Pledge_Id').annotate(totals=Sum('Amount_Paid')).order_by('Pledge_Id')
        
        #return results['totals']   
         
    
class PledgesReportArchive(Model):
    Status = models.CharField(max_length=150, null=True)
    Pledge_Id = models.IntegerField(null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    Pledge_Made_By = models.ForeignKey(Members, on_delete=models.SET_NULL,  max_length=100, null=True, blank=True)
    Reason = models.CharField(max_length=100, null=True)
    Pledged_Amount=models.IntegerField(null=True, blank=True)
    Amount_Paid = models.IntegerField(null=True, blank=True)
    Balance = models.IntegerField(null=True, blank=True)
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)

    # using decorators
    @property
    def total_pledge_paid(self):
        results = PaidPledges.objects.filter(Pledge_Id=self.Pledge_Id).aggregate(totals=models.Sum("Amount_Paid"))
        if (results['totals']):
            return results["totals"]
        else:
            return 0 
    @property
    def all_pledges_total(self):
        results = PaidPledges.objects.aggregate(totals=models.Sum(self.total_pledge_paid))
        if (results['totals']):
            return results["totals"]
        else:
            return 0 
            
    @property
    def Pledge_Balance(self):
        results=self.Pledged_Amount - self.total_pledge_paid
        return results 
    @property
    def updatestatus(self):
        if (self.total_pledge_paid >= self.Pledged_Amount):
            self.Status = "PAID"
            self.save()
            return self.Status

        elif (self.total_pledge_paid == 0):
            self.Status = "UNPAID"
            self.save()
            return self.Status

        elif (self.total_pledge_paid < self.Pledged_Amount):
            self.Status = "PARTIAL"
            self.save()
            return self.Status
        else:
            return self.Status     
    def __str__(self):
        return 'Pledge_Made_By: {1}  Amount_Paid:{0}'.format(self.Pledge_Made_By, self.Amount_Paid) 

class Slider(models.Model):
    slider_image = models.ImageField(upload_to='sliders/', null=True, blank=False)
    image_title = models.CharField(max_length=100)
    modified = models.DateTimeField(verbose_name="Modified", auto_now=True)
    objects = models.Manager()

    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')

    def __str__(self):
        return self.image_title

class About(models.Model):
    about_image = models.ImageField(upload_to='about/', null=True, blank=False)
    about = models.TextField(max_length=50000 , null=True, blank=True)
    about_title = models.CharField(max_length=100, null=True, blank=True)
    vision_description = models.TextField(max_length=10000000, null=True, blank=True)
    mission_description = models.TextField(max_length=100000000, null=True, blank=True)
    Is_View_on_Web = models.CharField(max_length=20, default='Yes', choices=OPTIONS, null=True, blank=False)
    objects = models.Manager()
    published = PublishedStatusManager()

    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')
        verbose_name = ("About")
        verbose_name_plural = ("About")

    def __str__(self):
        return self.about

    def get_absolute_url(self):
        return reverse('about_detail', args=[self.pk])        


#pages
class PublishedHeaderPageManager(models.Manager):
    def get_queryset(self):
        return super(PublishedHeaderPageManager, self).get_queryset().filter(page_location='Header')


class PublishedFooterPageManager(models.Manager):
    def get_queryset(self):
        return super(PublishedFooterPageManager, self).get_queryset().filter(page_location='Footer')


class Page(models.Model):
    IS = (('Header', 'Header'),
          ('Footer', 'Footer'))
    page_location = models.CharField(max_length=100, default='Header', choices=IS)
    page_title = models.CharField( max_length=100)
    page_description = models.TextField(max_length=300)
    page_image = models.ImageField(upload_to='images/', null=True, blank=False)

    objects = models.Manager()
    header = PublishedHeaderPageManager()
    footer = PublishedFooterPageManager()

    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')

    def __str__(self):
        return self.page_title
#Gallery
class Gallery(models.Model):
    gallery_title = models.CharField( max_length=100)
    note = models.TextField( max_length=300)
    Is_View_on_Web = models.CharField(max_length=20, default='Yes', choices=OPTIONS)

    objects = models.Manager()
    published = PublishedStatusManager()

    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')
        verbose_name = ("Gallery")
        verbose_name_plural = ("Galleries")

    def __str__(self):
        return self.gallery_title        
#Images
class Image(models.Model):
    gallery_title = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=False, null=True)
    gallery_image = models.ImageField( upload_to='images/', null=True, blank=False)
    image_caption = models.CharField( max_length=100)
    Is_View_on_Web = models.CharField(max_length=20, default='Yes', choices=OPTIONS, null=True, blank=False)

    objects = models.Manager()
    published = PublishedStatusManager()

    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')

    def __str__(self):
        return self.image_caption
#News
class News(models.Model):
    news_title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=False)
    news = models.TextField()
    Is_View_on_Web = models.CharField(max_length=20, default='Yes', choices=OPTIONS)
    author = models.CharField(max_length=1003, null=True, blank=True, default="Preacher")
    objects = models.Manager()
    published = PublishedStatusManager()

    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')
        verbose_name = ("News")
        verbose_name_plural = ("News")
        ordering = ['-date']

    def __str__(self):
        return self.news_title

    def get_absolute_url(self):
        return reverse('news_detail', args=[self.pk])        

class Event(models.Model):
    activity =(('Events','Events'), ('Church_Program','Church_Program'))
    Activity_Type = models.CharField(max_length=20, choices=activity, default="Events")
    date = models.DateField(auto_now_add=True)
    event_title = models.CharField(max_length=100, blank=True, null=True)
    event_for = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True, null=True)
    event_place = models.CharField(max_length=100,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    image = models.ImageField(upload_to='images/', null=True ,blank=True)
    note = models.TextField(blank=True)
    Is_View_on_Web = models.CharField(max_length=20, default='Yes', choices=OPTIONS)

    Start_Time = models.TimeField(blank=True, null=True)
    End_Time = models.TimeField(blank=True, null=True)
    Program_Name = models.CharField(max_length=100, blank=True, null=True)
    Day = models.CharField(max_length=20, choices=Week_Days, blank=True, null=True)
   
    objects = models.Manager()
    published = PublishedStatusManager()

    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')
        ordering = ['-date']

    def __str__(self):
        return self.event_title

    def get_absolute_url(self):
        return reverse('event_detail', args=[self.pk])


class PublishedChurchManager(models.Manager):
    def get_queryset(self):
        return super(PublishedChurchManager, self).get_queryset().filter(status='Active')

class EnableFrontendManager(models.Manager):
    def get_queryset(self):
        return super(EnableFrontendManager, self).get_queryset().filter(enable_frontend='Yes')


class Church(models.Model):
    church_vision = models.CharField(max_length=1000, default="vision")
    church_mission = models.CharField(max_length=1000, default='mission')
    maps_embedded_link=models.CharField(max_length=1000, blank=True, null=True)
    church_code = models.CharField(max_length=130, blank=True, null=True)
    church_name = models.CharField(max_length=130)
    address = models.CharField(max_length=130)
    phone = models.CharField(max_length=130)
    registration_date = models.DateField(blank=True, null=True)
    email_address = models.EmailField(max_length=120)
    Post_Office_Box = models.CharField(max_length=130, blank=True, null=True)
    footer = models.CharField(max_length=130, blank=True, null=True)
    enable_frontend = models.CharField(max_length=130, default='Yes', choices=OPTIONS)
    latitude = models.CharField(max_length=130, blank=True, null=True)
    longitude = models.CharField(max_length=130, blank=True, null=True)
    facebook_url = models.URLField(max_length=130, blank=True, null=True)
    twitter_url = models.URLField(max_length=130, blank=True, null=True)
    linkedIn_url = models.URLField(max_length=130, blank=True, null=True)
    google_plus_url = models.URLField(max_length=130, blank=True, null=True)
    youtube_url = models.URLField(max_length=130, blank=True, null=True)
    instagram_url = models.URLField(max_length=130, blank=True, null=True)
    pinterest_url = models.URLField(max_length=130, blank=True, null=True)
    frontend_Logo = models.ImageField(upload_to='logo/', blank=False)
    backend_Logo = models.ImageField(upload_to='logo/', blank=False)
    STATUS = (('Active', 'Active'),
              ('Inactive', 'Inactive'))
    status = models.CharField(max_length=130, blank=True, null=True, default="Active", choices=STATUS)
    objects = models.Manager()
    published = PublishedChurchManager()
    fronted = EnableFrontendManager()
    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')
        ordering = ('church_name',)
        verbose_name = 'church'
        verbose_name_plural = 'churches'

    def __str__(self):
        return self.church_name
class Contact(models.Model):
    name=models.CharField(max_length=1000, blank=True, null=True)
    email = models.CharField(max_length=130, blank=True, null=True)
    phone = models.CharField(max_length=130, blank=True, null=True)
    subject = models.CharField(max_length=130, blank=True, null=True)
    message = models.TextField(max_length=130, blank=True, null=True)
    feedback = models.TextField(max_length=100000, blank=True, null=True)


