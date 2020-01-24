from django.utils.timezone import now
from datetime import datetime
from django.db import models
from django.db.models import Model
from django.db.models import Sum
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import PermissionsMixin

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
        ('Admin','Admin'),('Secretary','Secretary')      
    )
    username = models.CharField(max_length=30, unique=True)
    Role = models.CharField(max_length=250, choices=roles)
    full_name =  models.ForeignKey('Members', on_delete=models.PROTECT, max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)  # can login
    is_staff = models.BooleanField(default=False)  # staff user non superuser
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FILEDS = []
    objects = UserManager()
    def __str__(self):
        return self.full_name
class Sundry(Model):
    reason=(
        ('Lunch','Lunch'),('Upkeep','Upkeep'),('Airtime/Data','Airtime/Data')      
    )
    Date = models.DateField(null=True, blank=True)
    Payment_Made_To = models.CharField(max_length=100, blank=False)
    Reason_For_Payment = models.CharField(max_length=250, choices=reason)
    Amount = models.IntegerField(default=0)
    def __str__(self):
        return self.Payment_Made_To

class Offerings(Model):
    services = (('Home Cell Service','Home Cell Service'),('Youth Service','Youth Service'),('Wednesday Service','Wednesday Service'),
        ('Bible Study Service','Bible Study Service'),('Friday Overnight','Friday Overnight'),('SundayFirst Service','Sunday First Service'),
        ('Sunday Second Service','Sunday Second Service'),('Sunday Third Service','Sunday Third Service'),
        )
    Date = models.DateField(null=True, blank=True)
    Total_Offering = models.IntegerField(default=0)
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
    Amount = models.IntegerField(default=0)
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
    Amount = models.IntegerField(default=0)

    def __str__(self):
        return 'Name:{0}, Reason:{1}, Amount: {2}'.format(self.Payment_Made_To, self.Reason_For_Payment, self.Amount)

##########################################
# REPORT ARCHIVING MODELS AFTER SUBMISSION #
##########################################

class ExpensesReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Name = models.CharField(max_length=100, default='Name', null=True)
    Amount = models.FloatField(default=0.0, null=True)
    Reason = models.CharField(max_length=100,null=True)
    month = models.CharField(max_length=100,null=True)
    year = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1} Reason:{2} Amount:{0}'.format(self.Name,self.Reason, self.Amount)

class GeneralExpensesReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Name = models.CharField(max_length=100, default='Name', null=True)
    Amount = models.FloatField(default=0.0, null=True)
    Reason = models.CharField(max_length=100,null=True)
    month = models.CharField(max_length=100,null=True)
    year = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1} Reason:{2} Amount:{0}'.format(self.Name,self.Reason, self.Amount)        
class SundryReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Name = models.CharField(max_length=100, default='Name', null=True)
    Amount = models.FloatField(default=0.0, null=True)
    Reason = models.CharField(max_length=100,null=True)
    month = models.CharField(max_length=100,null=True)
    year = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1} Reason:{2} Amount:{0}'.format(self.Name,self.Reason, self.Amount)

class AllowanceReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Staff = models.CharField( max_length=100,null=True)
    Month = models.CharField(max_length=100,null=True)
    Amount = models.IntegerField(default=0)
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1}  Amount:{0}'.format(self.Staff, self.Amount)

class OfferingsReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Service = models.CharField( max_length=100,null=True)
    Amount = models.IntegerField(default=0)
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1}  Amount:{0}'.format(self.Day, self.Amount)  
        
class Members(models.Model):
    sex=(('Female','Female'),('Male','Male'))
    status=(('Married','Married'),('Single','Single'),('Divorced','Divorced'),('Widower','Widower'),('Widow','Widow'))
    marriage=(('Church_Marriage','Church_Marriage'),('Customary','Customary'),('Legal','Legal'),('Cohabiting','Cohabiting'))
    education=(('Masters','Master'),('Degree','Degree'),('Diploma','Diploma'),('Certificate','Certificate'),('None','None'),
        ('Still_Studying','Still_Studying'),('Primary_Graduate','Primary_Graduate'),('O_Level_Graduate','O_Level_Graduate'),('A_Level_Graduate','A_Level_Graduate'))
    employment=(('Employed','Employed'),('Unemployed','Unemployed'))
    cell=(
        ('Church Zone','Church Zone'),('Kabira Zone','Kabira Zone'),('Kafunda Zone','Kafunda Zone'),('Lugoba Zone','Lugoba Zone') ,('Katooke Zone','Katooke Zone'),
        ('Kazo Zone','Kazo Zone'),('Gombolola Zone','Gombolola Zone'),('Kawaala Zone','Kawaala Zone'),('Bombo Rd Zone','Bombo Rd Zone')
        )

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
    Ministry_Involved_In=models.CharField(max_length=100,null=True,blank=True)
    Name_Of_Next_Of_Kin=models.CharField(max_length=100,null=True,blank=True)
    Contact_Of_Next_Of_Kin=models.CharField(max_length=100,null=True,blank=True)
    Residence_Of_Next_Of_Kin=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.First_Name + ' ' + self.Second_Name
    @property
    def full_name(self):
        return self.First_Name + ' ' + self.Second_Name
    
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
    rol=(('Security','Security'),('Secretary','Secretary'),('Church-Welfare','Church-Welfare'))
    sex=(('Male','Male'),('Female','Female'))
    education=(('Masters','Master'),('Degree','Degree'),('Diploma','Diploma'),('Certificate','Certificate'))
    rel =(('Born Again','Born Again'),('Others','Others'))
    member=(('Yes','Yes'),('No','No'))
    UCC_Bwaise_Member=models.CharField(max_length=100, choices=member,blank=True, null=True)
    Church_Member=models.ForeignKey(Members, on_delete=models.PROTECT, max_length=100, null=True, blank=True)
    First_Name=models.CharField(max_length=100,blank=True,null=True)
    Second_Name=models.CharField(max_length=100,blank=True,null=True)
    Gender=models.CharField(max_length=100, choices=sex, null=True)
    Date_Of_Birth=models.DateField(null=True, blank=True)
    Education_Level=models.CharField(max_length=100, choices=education,null=True)
    Residence=models.CharField(max_length=100,null=True)
    Telephone=models.CharField(max_length=100,null=True)
    Photo=models.ImageField(upload_to='avatars/', blank=False)
    Faith=models.CharField(max_length=100, choices=rel, null=True)
    Date_of_paying_salary = models.DateField(null=True, blank=True)
    Month_being_cleared = models.DateField(null=True, blank=True)
    Salary_Amount = models.IntegerField(default=0)
    Role = models.CharField(max_length=200, choices=rol, blank=True, null=True)
    Date_of_employment=models.DateField(null=False, blank=False)
    End_of_contract=models.DateField(null=False, blank=False)
    @property
    def total_salary_paid(self):
        current_month = datetime.now().month
        current_year = datetime.now().year
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
    Salary_Amount = models.IntegerField(default=0)
    Month_being_cleared = models.DateField(null=True, blank=True)
    Date_of_paying_salary = models.DateField(null=True, blank=True)
    @property
    def basic_salary(self):
        staffs=StaffDetails.objects.filter(id=self.Salary_Id)
        for i in staffs:
            salary=i.Salary_Amount
            return salary
    
    @property
    def total_salary_paid(self):
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
    Thanks_Giving_By = models.ForeignKey(Members, on_delete=models.PROTECT, max_length=100, null=True, blank=True)
    Amount = models.IntegerField(default=0)
    Service=models.CharField(max_length=100, choices=services, blank=False)
    def __str__(self):
        return self.Thanks_Giving_By
class ThanksGivingReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Thanks_Giving_By = models.ForeignKey(Members, on_delete=models.PROTECT, max_length=100, null=True, blank=True)
    Amount = models.IntegerField(default=0)
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
    Seed_Made_By = models.ForeignKey(Members, on_delete=models.PROTECT, max_length=100, null=True, blank=True)
    Amount = models.IntegerField(default=0)
    Service=models.CharField(max_length=100, choices=services, blank=False)
    def __str__(self):
        return self.Seed_Made_By  
class Donations(Model):
    Date = models.DateField(null=True, blank=True)
    Donated_By = models.CharField(max_length=100, null=True, blank=True)
    Amount = models.IntegerField(default=0)
    Reason=models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.Donated_By


class SeedsReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Seed_Made_By = models.ForeignKey(Members, on_delete=models.PROTECT, max_length=100, null=True, blank=True)
    Amount = models.IntegerField(default=0)
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)

class DonationsReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Reason = models.CharField(max_length=100, null=True, blank=True)
    Amount = models.IntegerField(default=0)
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)

class Tithes(Model):
    services = (('Home Cell Service','Home Cell Service'),('Youth Service','Youth Service'),('Wednesday Service','Wednesday Service'),
        ('Bible Study Service','Bible Study Service'),('Friday Overnight','Friday Overnight'),('SundayFirst Service','Sunday First Service'),
        ('Sunday Second Service','Sunday Second Service'),('Sunday Third Service','Sunday Third Service'))
    Date = models.DateField(null=True, blank=True)
    Tithe_Made_By = models.ForeignKey(Members, on_delete=models.PROTECT, max_length=100, null=True, blank=True)
    Amount = models.IntegerField(default=0)
    Service=models.CharField(max_length=100, choices=services, blank=False)
    def __str__(self):
        return self.Tithe_Made_By

class TithesReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Tithe_Made_By = models.ForeignKey(Members, on_delete=models.PROTECT, max_length=100, null=True, blank=True)
    Amount = models.IntegerField(default=0)
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)
    def __str__(self):
        return 'Name: {1}  Amount:{0}'.format(self.Tithe_Made_By, self.Amount)
class SalariesPaidReportArchive(models.Model):
    Salary_Id = models.CharField(max_length=200,null=True, blank=True)
    Name = models.CharField(max_length=200,null=True, blank=True)
    Salary_Amount = models.IntegerField(default=0)
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
    Name =  models.ForeignKey(Members, on_delete=models.PROTECT, max_length=100, null=True, blank=True)
    Month = models.CharField(max_length=12,choices=months, blank=False)
    Amount = models.IntegerField(default=0)
    def __str__(self):
        return self.Name 
#PLEDGES MODEL
class PledgeItem(Model):
    Date = models.DateField(blank=True, null=True)
    Item_That_Needs_Pledges = models.CharField(max_length=100, blank=True, null=True)
    Amount_Needed = models.IntegerField(default=0, blank=True, null=True)
    Pledge_Deadline = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.Item_That_Needs_Pledges

    @property
    def Total_Amount_Pledged(self):
        print(self.Item_That_Needs_Pledges)
        results = Pledges.objects.filter(Reason__Item_That_Needs_Pledges=self.Item_That_Needs_Pledges).aggregate(totals=models.Sum("Amount_Pledged"))
        print(results)
        if (results['totals']):
            return results["totals"]
        else:
            return 0 
    @property
    def Pledge_Amount_Remaining(self):
        results=self.Amount_Needed-self.Total_Amount_Pledged
        return results
              
class Pledges(Model):
    paid = 'PAID'
    partial = 'PARTIAL'
    unpaid = 'UNPAID'
    state = ((paid, 'Paid'), (partial, 'Partial'), (unpaid, 'Unpaid'))
    Status=models.CharField(max_length=100, choices=state, null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    Pledge_Made_By = models.ForeignKey(Members, on_delete=models.PROTECT, max_length=100, blank=False)
    Reason = models.ForeignKey(PledgeItem, on_delete=models.PROTECT, max_length=100, blank=True, null=True)
    Amount_Pledged = models.IntegerField(default=0)
    Amount_Paid = models.IntegerField(default=0, blank=True, null=True)
    Balance = models.IntegerField(default=0, blank=True, null=True)
    Amount_In_Words = models.CharField(max_length=500, blank=False)
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
    Reason=models.CharField(max_length=100, blank=True, null=True)
    Pledge_Id=models.CharField(max_length=100, blank=True, null=True)
    Pledge_Made_By = models.ForeignKey(Members, on_delete=models.PROTECT, max_length=100, blank=False)
    Amount_Paid = models.IntegerField(default=0, blank=True, null=True)
    Date = models.DateField(null=True, blank=True)

class PledgesReportArchive(Model):
    Status = models.CharField(max_length=150, null=True)
    Pledge_Id = models.IntegerField(null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    Pledge_Made_By = models.ForeignKey(Members, on_delete=models.PROTECT, max_length=100, null=True, blank=True)
    Reason = models.CharField(max_length=100, null=True)
    Pledged_Amount=models.IntegerField(default=0)
    Amount_Paid = models.IntegerField(default=0)
    Balance = models.IntegerField(default=0)
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
