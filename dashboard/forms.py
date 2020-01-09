from django import forms
from .models import *
from django.forms import Textarea, TextInput, ChoiceField
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, MonthPickerInput, DateTimePickerInput   


class SpendForm(forms.ModelForm):
    class Meta:
        model=Spend
        fields=('Date','Payment_Made_To','Reason_For_Payment','Amount')
        widgets = {
            'Date': DatePickerInput(),
            
        } 
class SundryForm(forms.ModelForm):
    class Meta:
        model=Sundry
        fields=('Date','Payment_Made_To','Amount','Reason_For_Payment')
        widgets = {
            'Date': DatePickerInput(),
            
        } 
class AllowanceForm(forms.ModelForm):
    class Meta:
        model=Allowance
        fields = ('Date','Name','Month','Amount')
        widgets = {
            'Date': DatePickerInput(),
            
        } 
class StaffDetailsForm(forms.ModelForm):
    class Meta:
        model=StaffDetails
        fields=('Date','Name','Salary_Amount','Role','Date_of_employment','End_of_contract')
        widgets = {
             'Date': DatePickerInput(),
            'Date_of_employment': DatePickerInput(),
            'End_of_contract': DatePickerInput(),
        }
class SalariesPaidForm(forms.ModelForm):
    class Meta:
        model = SalariesPaid
        fields = ('Name','Salary_Amount','Date')
class OfferingsForm(forms.ModelForm):
    class Meta:
        model=Offerings
        fields = ('Date','Total_Offering','Service')
        widgets = {
            'Date': DatePickerInput(),
        }
class PledgesForm(forms.ModelForm):
    class Meta:
        model=Pledges
        fields = ('Status','Amount_Paid','Balance','Date','Pledge_Made_By','Reason','Amount_Pledged','Amount_In_Words')
        widgets = {
            'Date': DatePickerInput(),
        }
class UpdatePledgesForm(forms.ModelForm):
    class Meta:
        model=Pledges
        fields = ('Pledge_Made_By','Amount_Paid','Date')
        widgets = {
            'Date': DatePickerInput(),
            
        }  

class PaidPledgesForm(forms.ModelForm):
    class Meta:
        model=PaidPledges
        fields = ('Pledge_Id','Pledge_Made_By','Amount_Paid','Date')
        widgets = {
            'Date': DatePickerInput(),
        }              
class TithesForm(forms.ModelForm):
    class Meta:
        model=Tithes
        fields = ('Date','Tithe_Made_By','Amount')
        widgets = {
            'Date': DatePickerInput(),
        } 

class MembersForm(forms.ModelForm):
    class Meta:
        model= Members
        fields = ('First_Name','Second_Name','Telephone','Residence', 'Home_Cell','Photo')

class VisitorsForm(forms.ModelForm):
    class Meta:
        model=Visitors
        fields = ('First_Name','Second_Name','Telephone','Address','Church')

class PledgesReportArchiveForm(forms.ModelForm):
    class Meta:
        model= PledgesReportArchive
        fields = ('Status','Pledge_Id','Date','Pledge_Made_By','Reason', 'Amount_Paid') 
        widgets = {
            'Date': DatePickerInput(),
        }                