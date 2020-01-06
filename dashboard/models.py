from django.utils.timezone import now
from datetime import datetime
from django.db import models
from django.db.models import Model
from django.db.models import Sum
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget

class StaffDetails(models.Model):
    image = models.ImageField(upload_to="media", default="Photo")
    FistName= models.CharField(max_length=150,blank=False)
    SecondName = models.CharField(max_length=150,blank=False)
    Salary = models.IntegerField(default=0)
    Role = models.CharField(max_length=20, default="MALE", blank=False)
    Duties = models.CharField(max_length=1000, blank=False)
    choices=(
        ('Male','Male'),
        ('Female', 'Female'))
    Sex = models.CharField(max_length=7, default="MALE", blank=False, choices=choices)
    Contact = models.CharField(max_length=100, default="Tel or Email")
    def __str__(self):
        return self.FistName + ' ' + self.SecondName

class Sundry(Model):
    Date = models.DateField(null=True, blank=True)
    Payment_Made_To = models.CharField(max_length=100, blank=False)
    Reason_For_Payment = models.CharField(max_length=250)
    Amount = models.IntegerField(default=0)
    def __str__(self):
        return self.Payment_Made_To

class Offerings(Model):
    services = (('Home Cell Service','Home Cell Service'),('Youth Service','Youth Service'),('Wednesday Service','Wednesday Service'),
        ('Bible Study Service','Bible Study Service'),('Friday Overnight','Friday Overnight'),('SundayFirst Service','Sunday First Service'),
        ('Sunday Second Service','Sunday Second Service'),('Sunday Third Service','Sunday Third Service'))
    Date = models.DateField(null=True, blank=True)
    Total_Offering = models.IntegerField(default=0)
    Service=models.CharField(max_length=100, choices=services, blank=False)
    def __str__(self):
        return self.Total_Offering

class Spend(models.Model):
    reason=(
        ('Church Renovations','Church Renovations'),('Water Bills','Water Bills'),('Electricity','Electricity Bills'),
        ('Lwaki Oli Mulamu Conference','Lwaki Oli Mulamu Conference')
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
class SundryReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Name = models.CharField(max_length=100, default='Name', null=True)
    Amount = models.FloatField(default=0.0, null=True)
    Reason = models.CharField(max_length=100,null=True)
    month = models.CharField(max_length=100,null=True)
    year = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1} Reason:{2} Amount:{0}'.format(self.Name,self.Reason, self.Amount)

class SalaryReportArchive(models.Model):
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
    cell=(
        ('Church Zone','Church Zone'),('Kabira Zone','Kabira Zone'),('Kafunda Zone','Kafunda Zone'),('Lugoba Zone','Lugoba Zone') ,('Katooke Zone','Katooke Zone'),
        ('Kazo Zone','Kazo Zone'),('Gombolola Zone','Gombolola Zone'),('Kawaala Zone','Kawaala Zone'),('Bombo Rd Zone','Bombo Rd Zone')
        )
    First_Name=models.CharField(max_length=100,null=True)
    Second_Name=models.CharField(max_length=100,null=True)
    Home_Cell=models.CharField(max_length=100, choices=cell,null=True)
    Residence=models.CharField(max_length=100,null=True)
    Telephone=models.CharField(max_length=100,null=True)
    Photo=models.ImageField(upload_to='avatars/', blank=False)

    def __str__(self):
        return self.First_Name + ' ' + self.Second_Name
    @property
    def full_name(self):
        return self.First_Name + ' ' + self.Second_Name
    
class Visitors(models.Model):
    First_Name=models.CharField(max_length=100, null=True)
    Second_Name=models.CharField(max_length=100, null=True)
    Address=models.CharField(max_length=100, null=True)
    Telephone=models.CharField(max_length=100, null=True)
    Church=models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.First_Name + ' ' + self.Second_Name

class Tithes(Model):
    Date = models.DateField(null=True, blank=True)
    Tithe_Made_By = models.ForeignKey(Members, on_delete=models.CASCADE, max_length=100, null=True, blank=True)
    Amount = models.IntegerField(default=0)
    def __str__(self):
        return self.Tithe_Made_By
        
class TithesReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Tithe_Made_By = models.ForeignKey(Members, on_delete=models.CASCADE, max_length=100, null=True, blank=True)
    Amount = models.IntegerField(default=0)
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1}  Amount:{0}'.format(self.Tithe_Made_By, self.Amount)

class Salary(models.Model):

    months = (
        ('January','January'),('February','February'),('March', 'March'),('April', 'April')
        ,('May','May'),('June', 'June'),('July', 'July'),('August','August'),
        ('September', 'September'),('October', 'October'),('November','November'),('December', 'December')
    )
    Date = models.DateField(null=True, blank=True)
    Name =  models.ForeignKey(Members, on_delete=models.CASCADE, max_length=100, null=True, blank=True)
    Month = models.CharField(max_length=12,choices=months, blank=False)
    Amount = models.IntegerField(default=0)
    def __str__(self):
        return self.Name 
        #PLEDGES MODEL
class Pledges(Model):
    paid = 'PAID'
    partial = 'PARTIAL'
    unpaid = 'UNPAID'
    state = ((paid, 'Paid'), (partial, 'Partial'), (unpaid, 'Unpaid'))
    Status=models.CharField(max_length=100, choices=state, null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    Pledge_Made_By = models.ForeignKey(Members, on_delete=models.CASCADE, max_length=100, blank=False)
    Reason = models.CharField(max_length=100, null=True)
    Amount_Pledged = models.IntegerField(default=0)
    Amount_Paid = models.IntegerField(default=0, blank=True, null=True)
    Balance = models.IntegerField(default=0, blank=True, null=True)
    Amount_In_Words = models.CharField(max_length=500, blank=False)
    def __str__(self):
        return self.Pledge_Made_By
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
    Pledge_Id=models.CharField(max_length=100, blank=True, null=True)
    Pledge_Made_By = models.ForeignKey(Members, on_delete=models.CASCADE, max_length=100, blank=False)
    Amount_Paid = models.IntegerField(default=0, blank=True, null=True)
    Date = models.DateField(null=True, blank=True)


class PledgesReportArchive(Model):
    Status = models.CharField(max_length=150, null=True)
    Pledge_Id = models.IntegerField(null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    Pledge_Made_By = models.ForeignKey(Members, on_delete=models.CASCADE, max_length=100, null=True, blank=True)
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
        PledgesReportArchive.objects.all().delete()
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
