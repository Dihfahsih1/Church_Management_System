from django.utils.timezone import now
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


class Salary(models.Model):

    months = (
        ('January','January'),('February','February'),('March', 'March'),('April', 'April')
        ,('May','May'),('June', 'June'),('July', 'July'),('August','August'),
        ('September', 'September'),('October', 'October'),('November','November'),('December', 'December')
    )
    Date = models.DateField(null=True, blank=True)
    Name = models.CharField(max_length=100, blank=False)
    Month = models.CharField(max_length=12,choices=months, blank=False)
    Amount = models.IntegerField(default=0)
    AmountInWords = models.CharField(max_length=500, blank=False)
    def __str__(self):
        return self.Name

class Sundry(Model):
    Date = models.DateField(null=True, blank=True)
    PaymentMadeTo = models.CharField(max_length=100, blank=False)
    ReasonForPayment = models.CharField(max_length=250)
    Amount = models.IntegerField(default=0)
    AmountInWords = models.CharField(max_length=500, blank=False)
    def __str__(self):
        return self.PaymentMadeTo

class Offerings(Model):
    Date = models.DateField(null=True, blank=True)
    DayOfTheWeek =  models.CharField(max_length=100, blank=False)
    TotalOffering = models.IntegerField(default=0)
    AmountInWords = models.CharField(max_length=500, blank=False)
    def __str__(self):
        return self.DayOfTheWeek

class Tithes(Model):
    Date = models.DateField(null=True, blank=True)
    DayOfTheWeek = models.CharField(max_length=100, blank=False)
    TitheMadeBy = models.CharField(max_length=100, blank=False)
    Amount = models.IntegerField(default=0)
    AmountInWords = models.CharField(max_length=500, blank=False)
    def __str__(self):
        return self.TitheMadeBy

class Spend(models.Model):
    reason=(
        ('Mechanic','Car Repairing'),('WaterBills','Water Bills'),('Electricity','Electricity Bills'),('URA','Paying Revenue')
    )
    Date = models.DateField(null=True, blank=True)
    PaymentMadeTo = models.CharField(max_length=100,blank=False)
    ReasonForPayment = models.CharField(max_length=100, choices=reason)
    Amount = models.IntegerField(default=0)
    AmountInWords = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return 'Name:{0}, Reason:{1}, Amount: {2}'.format(self.PaymentMadeTo, self.ReasonForPayment, self.Amount)

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
    Day = models.CharField( max_length=100,null=True)
    Amount = models.IntegerField(default=0)
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1}  Amount:{0}'.format(self.Day, self.Amount)

class TithesReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Name = models.CharField( max_length=100,null=True)
    Day = models.CharField(max_length=100, null=True)
    Amount = models.IntegerField(default=0)
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'Name: {1}  Amount:{0}'.format(self.Name, self.Amount)


        
class Members(models.Model):
    First_Name=models.CharField(max_length=100,null=True)
    Second_Name=models.CharField(max_length=100,null=True)
    Address=models.CharField(max_length=100,null=True)
    Telephone=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.First_Name + ' ' + self.Second_Name

class Visitors(models.Model):
    First_Name=models.CharField(max_length=100, null=True)
    Second_Name=models.CharField(max_length=100, null=True)
    Address=models.CharField(max_length=100, null=True)
    Telephone=models.CharField(max_length=100, null=True)
    Church=models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.First_Name + ' ' + self.Second_Name

        #PLEDGES MODEL
class Pledges(Model):
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
        results = PaidPledges.objects.filter(Member_id=self.Pledge_Made_By_id).aggregate(totals=models.Sum("Amount_Paid"))
        if (results['totals']):
            return results["totals"]
        else:
            return 0 
    @property
    def Pledge_Balance(self):
        results=self.Amount_Pledged - self.total_pledge_paid
        return results 

class PaidPledges(Model):
    Name = models.CharField(max_length=100, blank=False)
    Member_id = models.CharField(max_length=100, blank=False)
    Amount_Paid = models.IntegerField(default=0, blank=True, null=True)
    Date = models.DateField(null=True, blank=True)

class PledgesReportArchive(models.Model):
    Date = models.DateField(null=True, blank=True)
    Name = models.CharField( max_length=100,null=True)
    Reason = models.CharField(max_length=100, null=True)
    Pledged_Amount=models.IntegerField(default=0)
    Amount_Paid = models.IntegerField(default=0)
    Balance = models.IntegerField(default=0)
    archivedmonth = models.CharField(max_length=100,null=True)
    archivedyear = models.CharField(max_length=100,null=True)
    #using decorators
    @property
    def total_pledge_paid(self):
        results = PaidPledges.objects.filter(Member_id=self.Pledge_Made_By_id).aggregate(totals=models.Sum("Amount_Paid"))
        if (results['totals']):
            return results["totals"]
        else:
            return 0 
    @property
    def Pledge_Balance(self):
        results=self.Amount_Pledged - self.total_pledge_paid
        return results 

    def __str__(self):
        return 'Name: {1}  Amount:{0}'.format(self.Name, self.Amount)    
