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

services = (
         ('Unspecified Service','Unspecified Service'),
        ('Home Cell Service','Home Cell Service'),('Youth Service','Youth Service'),('Wednesday Service','Wednesday Service'),
        ('Bible Study Service','Bible Study Service'),('Friday Overnight','Friday Overnight'),('Sunday First Service','Sunday First Service'),
        ('Sunday Second Service','Sunday Second Service'),('Sunday Third Service','Sunday Third Service'),
        )

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
archive = (
    ('ARCHIVED', 'ARCHIVED'),
    ('NOT-ARCHIVED', 'NOT-ARCHIVED'),)

petty=(
        ('Lunch','Lunch'),('Upkeep','Upkeep'),('Airtime/Data','Airtime/Data'),('Other','Other')     
    )
main=(
        ('Water Bills','Water Bills'),('Yaka Bills','Yaka Bills'),
        ('Transport','Transport'), ('Love Offering','Love Offering'),('Medical Bills','Medical Bills'),('Rent','Rent'),
        ('Help','Help'),('Drinks','Drinks'),('Savings','Savings'),
        ('Evangelism','Evangelism')
    )
general = (('Tithe of Tithes','Tithe of Tithes'),('Generator Mechanic','Generator Mechanic'),('Instruments','Servicing Music Instruments'),('Condolences','Condolences'),
        ('Stationery','Stationery'),('Repair','Any Other Repair'),('Purchase','Purchase'),
        ('Renovations','Renovations')
        )
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
roles=(
    ('Admin','Admin'),('Secretary','Secretary') ,('SuperAdmin','SuperAdmin') ,
    ('Building Chair', 'Building Chair'),
   ('Marrieds Leader', 'Marrieds Leader'),
   ('Youth Leader', 'Youth Leader'),
   ('Ordinary', 'Ordinary'), 
   ('Assistant_Admin', 'Assistant_Admin'),
   ('Website Admin', 'Website Admin'),  
)
rol=(('Security','Security'),('Secretary','Secretary'),('Church-Welfare','Church-Welfare'),('Admin','Admin'))
education=(('Masters','Masters'),('Degree','Degree'),('Diploma','Diploma'),('Certificate','Certificate'))
rel =(('Born Again','Born Again'),('Others','Others'))
member=(('Yes','Yes'),('No','No'))
THEMES = (
    ("jazzberry-jam", 'Jazzberry Jam'),
    ("black", 'Black'),
    ("umber", 'Umber'),
    ("medium-purple", 'MediumPurple'),
    ("lime-green", 'LimeGreen'),
    ("rebecca-purple", 'RebeccaPurple'),
    ("radical-red", 'Radical Red'),
    ("dodger-blue", "DodgerBlue"),
    ("maroon", "Maroon"),
    ("dark-orange", "DarkOrange"),
    ("deep-pink", "DeepPink"),
    ("trinidad", "Trinidad"),
    ("slate-gray", "SlateGray"),
    ("light-sea-green", "LightSeaGreen"),
    ("navy-blue", "Navy Blue"),
    ("red", "Red"))

class UserRole(models.Model):
    name = models.CharField(max_length=100, default='Roles', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
    
class Theme(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True, default='slate-gray')
    colour = models.CharField(max_length=40)
    is_active = models.CharField(max_length=10, default='Yes', choices=OPTIONS)
    objects = models.Manager()
    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')
    def __str__(self):
        return self.colour + ' ' + self.name

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
    email = models.EmailField(max_length=255,blank=True, null=True)
    username = models.CharField(max_length=30, unique=True)
    Role = models.CharField(max_length=250, choices=roles, blank=True, null=True)
    full_name =  models.ForeignKey('Members', on_delete=models.SET_NULL,  max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False)  
    is_superuser = models.BooleanField(default=False)
    Is_View_on_Web = models.CharField(max_length=20, default='Yes', choices=OPTIONS,null=True,blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FILEDS = []
    objects = UserManager()
    published = PublishedStatusManager()
    def __str__(self):
        return str(self.full_name)
    @property
    def UserEmail(self):
        get_member=Members.objects.filter(Full_Named=self.full_name)
        for i in get_member:
            if i.Email is not None:
                self.email=i.Email
                self.save()
                return self.email

class Expenditures(Model):
    Date = models.DateField(null=True, blank=True)
    Payment_Made_To = models.CharField(max_length=1000,blank=True, null=True)
    Amount = models.IntegerField(default=0)
    Reason_filtering=models.CharField(max_length=1000, blank=True, null=True)
    Other_Expenditure=models.CharField(max_length=1000, blank=True, null=True)
    Notes=models.CharField(max_length=1000, blank=True, null=True)
    Main_Expense_Reason=models.CharField(max_length=1000, choices=main,blank=True, null=True)
    General_Expenses_Reason=models.CharField(max_length=1000, choices=general, blank=True, null=True)
    Petty_Cash_Reason=models.CharField(max_length=1000, choices=petty, blank=True, null=True)
    Archived_Status= models.CharField(max_length=1000, choices=archive, blank=True, null=True, default='NOT-ARCHIVED')
    Member_Name = models.ForeignKey('Members', on_delete=models.SET_NULL,  max_length=1000, null=True, blank=True)
    def __str__(self):
        return self.Reason_filtering
    
    @property
    def cash_float(self):
        current_month = datetime.now().month
        current_year = datetime.now().year
        Float_Cash=CashFloat.objects.filter(Date__month=current_month, Date__year=current_year ).values('Amount').aggregate(totals=models.Sum("Amount"))
        if (Float_Cash['totals']):
            return Float_Cash["totals"]
        else:
            return 0

    @property
    def expenses_total(self):
        current_month = datetime.now().month
        current_year = datetime.now().year
        total_expenses=Expenditures.objects.filter(Date__month=current_month, Date__year=current_year ).values('Amount').aggregate(totals=models.Sum("Amount"))
        if (total_expenses['totals']):
            return total_expenses["totals"]
        else:
            return 0

    @property
    def salaries_total(self): 
        current_month = datetime.now().month
        current_year = datetime.now().year       
        total_salaries=SalariesPaid.objects.filter(Date_of_paying_salary__month=current_month, Date_of_paying_salary__year=current_year )\
        .values('Salary_Amount').aggregate(totals=models.Sum("Salary_Amount"))
        if (total_salaries['totals']):
            return total_salaries["totals"]
        else:
            return 0

    @property
    def net_float(self):
        results = self.cash_float - (self.expenses_total + self.salaries_total)
        return results


class Revenues(Model):
    Date = models.DateField(null=True, blank=True)
    Service=models.CharField(max_length=100, choices=services, null=True, blank=True)
    Amount = models.IntegerField(default=0, blank=True, null=True)
    General_Offering_Amount = models.IntegerField(default=0, blank=True, null=True)
    Tithe_Amount = models.IntegerField(default=0, blank=True, null=True)
    Seed_Amount = models.IntegerField(default=0, blank=True, null=True)
    Member_Name = models.ForeignKey('Members', on_delete=models.SET_NULL,  max_length=100, null=True, blank=True)
    Archived_Status= models.CharField(max_length=100, choices=archive, blank=True, null=True, default='NOT-ARCHIVED')
    Revenue_filter=models.CharField(max_length=100, blank=True, null=True)
    Other_Sources=models.CharField(max_length=100, blank=True, null=True)
    Other_Notes=models.CharField(max_length=10000, blank=True, null=True)
    def __str__(self):
        return str(self.Revenue_filter)
    class Meta:
        ordering = ['-Date']    
        
class Members(models.Model):
    Archived_Status= models.CharField(max_length=1000, choices=archive, blank=True, null=True, default='NOT-ARCHIVED')
    date = models.DateTimeField(auto_now=True)
    Group = models.CharField(max_length=100, choices=grouping, null=True, blank=True, default="God Is Able")
    Initials=models.CharField(max_length=100, choices=ini,null=True, blank=True)
    First_Name=models.CharField(max_length=100,null=True, blank=True)
    Second_Name=models.CharField(max_length=100,null=True, blank=True)
    Home_Cell=models.CharField(max_length=100, choices=cell,null=True)
    Residence=models.CharField(max_length=100,null=True, blank=True)
    Telephone=models.CharField(max_length=100,null=True, blank=True)
    Email=models.EmailField(null=True, blank=True)
    Photo=models.ImageField(upload_to='avatars/', max_length=10000, null=True, blank=True)
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
    is_active = models.BooleanField(default=False)
    Is_View_on_Web = models.CharField(max_length=20, default='Yes', choices=OPTIONS,null=True,blank=True)
    objects = models.Manager()
    published = PublishedStatusManager()
    Full_Named=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return str(self.First_Name )+ ' ' + str(self.Second_Name)
                  
    @property
    def full_name(self):
        save_this=str(self.First_Name )+ ' ' + str(self.Second_Name)
        self.Full_Named=save_this
        self.save()
        return self.Full_Named
            
    def total_tithe(self):
        current_year = datetime.now().year
        results = Revenues.objects.filter(Member_Name__id=self.id, Revenue_filter='tithes', Date__year=current_year).aggregate(totals=models.Sum("Amount"))
        if (results['totals']):
            return results["totals"]
        else:
            return 0    
    class Meta:
        ordering = ['First_Name']
class Ministry(models.Model):
    name = models.CharField(max_length=100, unique=True)
    leader = models.ForeignKey(Members, on_delete=models.CASCADE, max_length=100)
    details = models.TextField(max_length=10000000, null=True, blank=True)
    photos = models.ImageField(upload_to='avatars/',max_length=10000, blank=True) 
    Is_View_on_Web = models.CharField(max_length=20, default='Yes', choices=OPTIONS,null=True,blank=True)
    objects = models.Manager()
    published = PublishedStatusManager()
    def __str__(self):
        return self.name

class Visitors(models.Model):
    Date = models.DateField(null=True, blank=True)
    Photo=models.ImageField(upload_to='avatars/', max_length=10000, blank=True)
    First_Name=models.CharField(max_length=100, null=True)
    Second_Name=models.CharField(max_length=100, null=True)
    Address=models.CharField(max_length=100, null=True)
    Telephone=models.CharField(max_length=100, null=True)
    Church=models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.First_Name + ' ' + self.Second_Name

class StaffDetails(models.Model):
    UCC_Bwaise_Member=models.CharField(max_length=100, choices=member,blank=True, null=True)
    Church_Member=models.ForeignKey(Members, on_delete=models.SET_NULL,  max_length=100, null=True, blank=True)
    First_Name=models.CharField(max_length=100,blank=True,null=True)
    Second_Name=models.CharField(max_length=100,blank=True,null=True)
    Gender=models.CharField(max_length=100, choices=sex, null=True, blank=True)
    Date_Of_Birth=models.DateField(null=True, blank=True)
    Education_Level=models.CharField(max_length=100, choices=education,null=True, blank=True)
    Residence=models.CharField(max_length=100,null=True, blank=True)
    Telephone=models.CharField(max_length=100,null=True, blank=True)
    Photo=models.ImageField(upload_to='avatars/',max_length=10000, null=True, blank=True)
    Faith=models.CharField(max_length=100, choices=rel, null=True, blank=True)
    Date_of_paying_salary = models.DateField(null=True, blank=True)
    Month_being_cleared = models.CharField(max_length=200,null=True, blank=True)
    Salary_Amount = models.IntegerField()
    Role = models.CharField(max_length=200, choices=rol, blank=True, null=True)
    Date_of_employment=models.DateField(null=True, blank=True)
    End_of_contract=models.DateField(null=True, blank=True)
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
    Month_being_cleared = models.CharField(max_length=200,null=True, blank=True)
    Archived_Status= models.CharField(max_length=1000, choices=archive, blank=True, null=True, default='NOT-ARCHIVED')
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
                balance = a_amount - bal['totals']
                return balance

#PLEDGES MODEL
class PledgeItem(Model):
    Date = models.DateField(blank=True, null=True)
    Item_That_Needs_Pledges = models.CharField(max_length=100, unique=True)
    Amount_Needed = models.IntegerField(blank=True, null=True)
    Pledge_Deadline = models.DateField(blank=True, null=True)
    Archived_Status = models.CharField(max_length=100, blank=True, null=True, choices=archive, default="NOT-ARCHIVED")
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
        results = self.Amount_Needed - self.Total_Amount_Pledged
        return results
        
    #total money paid for a particular item
    @property
    def Item_money_received(self):
        results=Pledges.objects.filter(Reason__Item_That_Needs_Pledges=self.Item_That_Needs_Pledges).aggregate(totals=models.Sum("Amount_Paid"))
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
    def __str__(self):
        return self.Item_That_Needs_Pledges

class Pledges(Model):
    op = (('YES', 'YES'), ('NO','NO'))
    paid = 'PAID'
    partial = 'PARTIAL'
    unpaid = 'UNPAID'
    is_church_member=models.CharField(max_length=100, choices=op, default='YES', null=True, blank=True)
    state = ((paid, 'Paid'), (partial, 'Partial'), (unpaid, 'Unpaid'))
    Status=models.CharField(max_length=100, choices=state, null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    Pledge_Made_By_Visitor = models.ForeignKey(Visitors, on_delete=models.SET_NULL,  max_length=100,null=True, blank=True)
    Pledge_Made_By = models.ForeignKey(Members, on_delete=models.SET_NULL,  max_length=100,null=True, blank=True)
    Reason = models.ForeignKey(PledgeItem, on_delete=models.SET_NULL,  max_length=100, blank=True, null=True)
    Amount_Pledged = models.IntegerField(default=0,blank=True, null=True)
    Amount_Paid = models.IntegerField(default=0,blank=True, null=True)
    Balance = models.IntegerField(blank=True, null=True)
    Archived_Status= models.CharField(max_length=100, choices=archive, blank=True, null=True, default='NOT-ARCHIVED')
    #create this per transaction made or recorded
    DateOfPayment = models.DateField(null=True, blank=True)
    NameOfPledgee = models.CharField(max_length=100,blank=True, null=True)
    AmountBeingPaid = models.IntegerField(default=0,blank=True, null=True)
    PledgeItem = models.CharField(max_length=100,blank=True, null=True)
    def __str__(self):
        if self.Pledge_Made_By:
            return self.Archived_Status
        
        return self.Archived_Status

    @property 
    def Pledge_Balance(self):
        results=self.Amount_Pledged - self.Amount_Paid
        self.Balance=results
        self.save()
        return self.Balance
    
    @property
    def updatestatus(self):
        if (self.Pledge_Balance <= 0):
            self.Status = self.paid
            self.save()
            return self.Status

        elif (self.Amount_Paid == 0):
            self.Status = self.unpaid
            self.save()
            return self.Status

        elif (self.Amount_Paid < self.Amount_Pledged):
            self.Status = self.partial
            self.save()
            return self.Status

        else:
            return self.Status 
         
class Slider(models.Model):
    slider_image = models.ImageField(upload_to='sliders/', max_length=10000,null=True, blank=False)
    image_title = models.CharField(max_length=100)
    modified = models.DateTimeField(verbose_name="Modified", auto_now=True)
    objects = models.Manager()
    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')

    def __str__(self):
        return self.image_title

class About(models.Model):
    about_image = models.ImageField(upload_to='about/',max_length=10000, null=True, blank=True)
    banner = models.ImageField(upload_to='about/',max_length=10000, null=True, blank=True)
    about = models.TextField(max_length=50000 , null=True, blank=True)
    about_title = models.CharField(max_length=100, null=True, blank=True)
    core_values = models.TextField(max_length=10000000, null=True, blank=True)
    church_details = models.TextField(max_length=10000000, null=True, blank=True)
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
        return self.vision_description or self.mission_description or self.core_values

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
    page_image = models.ImageField(upload_to='images/', max_length=10000,null=True, blank=False)
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
    date = models.DateField(auto_now_add=True)
    objects = models.Manager()
    published = PublishedStatusManager()
    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')
        verbose_name = ("Gallery")
        verbose_name_plural = ("Galleries")
        ordering = ['-id']

    def __str__(self):
        return self.gallery_title        
#Images
class Image(models.Model):
    gallery_title = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=False, null=True)
    gallery_image = models.ImageField( upload_to='images/', max_length=10000,null=True, blank=False)
    image_caption = models.TextField( max_length=100000)
    date = models.DateField(auto_now_add=True)
    Is_View_on_Web = models.CharField(max_length=20, default='Yes', choices=OPTIONS, null=True, blank=False)
    objects = models.Manager()
    published = PublishedStatusManager()
    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')
        ordering = ['-gallery_image']

    def __str__(self):
        return self.image_caption
#News   
class News(models.Model):
    news_title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', max_length=10000, null=True, blank=True)
    audio_file = models.FileField(upload_to='audios/',max_length=10000, null=True, blank=True)
    news = models.TextField(null=True, blank=True)
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
    image = models.ImageField(upload_to='images/',max_length=10000, null=True ,blank=True)
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

#Church-Projects
class Project(models.Model):
    project_title = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/',max_length=10000, null=True, blank=False)
    project_description = models.TextField()
    project_leader = models.ForeignKey('Members', on_delete=models.CASCADE,null=True, blank=True)
    Is_View_on_Web = models.CharField(max_length=20, default='Yes', choices=OPTIONS)
    objects = models.Manager()
    published = PublishedStatusManager()

    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')
        verbose_name = ("Projects")
        verbose_name_plural = ("Projects")
        ordering = ['-start_date']

    def __str__(self):
        return self.project_title

    def get_absolute_url(self):
        return reverse('project_detail', args=[self.pk])
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
    Church_Logo = models.ImageField(upload_to='logo/',max_length=10000, blank=False)
    STATUS = (('Active', 'Active'), ('Inactive', 'Inactive'))
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
    def __str__(self):
        return self.name

class CashFloat(models.Model):
    Date = models.DateField(null=True, blank=True)
    Amount = models.IntegerField(default=0)
    Notes = models.TextField(max_length=100000, blank=True, null=True)
    def __int__(self):
        return self.Amount

#for testing purposes

class Testing(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)

class AnnualConference(models.Model):
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    estimated_budget = models.IntegerField(default=0,blank=True, null=True)
    conference_theme = models.CharField(max_length=500, blank=True, null=True)
    conference_report = models.TextField(max_length=100000, blank=True, null=True)
    def __str__(self):
        return self.conference_theme
class NewConvert(models.Model):
    is_church_member = models.CharField(max_length=100, choices=OPTIONS, default="No", blank=True, null=True)
    born_again_before = models.CharField(max_length=100, choices=OPTIONS, default="No", blank=True, null=True)
    First_Name=models.CharField(max_length=100,null=True, blank=True)
    Second_Name=models.CharField(max_length=100,null=True, blank=True)
    Telephone=models.CharField(max_length=100,null=True,blank=True)
    Date_Of_Salvation=models.DateField(null=True,blank=True)
    member_name = models.ForeignKey(Members, on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return self.member_name or self.First_Name + ' ' + self.Second_Name

