from django import forms
from .models import *
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, MonthPickerInput, DateTimePickerInput   


class SpendForm(forms.ModelForm):
    class Meta:
        model=Spend
        fields=('Date','PaymentMadeTo','ReasonForPayment','Amount','AmountInWords')

class SundryForm(forms.ModelForm):
    class Meta:
        model=Sundry
        fields=('Date','PaymentMadeTo','Amount','AmountInWords','ReasonForPayment')

class SalaryForm(forms.ModelForm):
    class Meta:
        model=Salary
        fields = ('Date','Name','Month','Amount','AmountInWords')

class StaffDetailsForm(forms.ModelForm):
    class Meta:
        model=StaffDetails
        fields=('image','FistName','SecondName','Salary','Role','Duties','Sex','Contact')

class OfferingsForm(forms.ModelForm):
    class Meta:
        model=Offerings
        fields = ('Date','DayOfTheWeek','TotalOffering','AmountInWords')
class PledgesForm(forms.ModelForm):
    class Meta:
        model=Pledges
        fields = ('Amount_Paid','Balance','Date','Pledge_Made_By','Reason','Amount_Pledged','Amount_In_Words')
        widgets = {
            'Date': DatePickerInput(),
        }
class UpdatePledgesForm(forms.ModelForm):
    class Meta:
        model=Pledges
        fields = ('Amount_Paid','Date')
        widgets = {
            'Date': DatePickerInput(),
        }  

class PaidPledgesForm(forms.ModelForm):
    class Meta:
        model=PaidPledges
        fields = ('Name','Member_id','Amount_Paid','Date')
        widgets = {
            'Date': DatePickerInput(),
        }              
class TithesForm(forms.ModelForm):
    class Meta:
        model=Tithes
        fields = ('Date','DayOfTheWeek','TitheMadeBy','Amount','AmountInWords')

class MembersForm(forms.ModelForm):
    class Meta:
        model= Members
        fields = ('First_Name','Second_Name','Telephone','Address')

class VisitorsForm(forms.ModelForm):
    class Meta:
        model=Visitors
        fields = ('First_Name','Second_Name','Telephone','Address','Church')        