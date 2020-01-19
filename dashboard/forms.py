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
class GeneralExpensesForm(forms.ModelForm):
    class Meta:
        model=GeneralExpenses
        fields=('Date','Payment_Made_To','Expense_Reason','Amount')
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
        fields=('Date_Of_Birth','First_Name','Second_Name','Gender',
            'Education_Level','Residence','Telephone','Photo','Faith',
            'Date_of_paying_salary','Month_being_cleared','Salary_Amount',
            'Role','Date_of_employment','End_of_contract')
        widgets = {
             'Month_being_cleared' :MonthPickerInput(),
             'Date_Of_Birth': DatePickerInput(),
            'Date_of_paying_salary': DatePickerInput(),
            'Date_of_employment': DatePickerInput(),
            'End_of_contract': DatePickerInput(),
        }
class SalariesPaidForm(forms.ModelForm):
    class Meta:
        model = SalariesPaid
        fields = ('Salary_Id','Name','Salary_Amount','Month_being_cleared','Date_of_paying_salary')
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
        fields = ('Reason','Pledge_Made_By','Amount_Paid','Date')
        widgets = {
            'Date': DatePickerInput(),
            
        }  

class PaidPledgesForm(forms.ModelForm):
    class Meta:
        model=PaidPledges
        fields = ('Reason','Pledge_Id','Pledge_Made_By','Amount_Paid','Date')
        widgets = {
            'Date': DatePickerInput(),
        }              
class TithesForm(forms.ModelForm):
    class Meta:
        model=Tithes
        fields = ('Date','Tithe_Made_By','Amount','Service')
        widgets = {
            'Date': DatePickerInput(),
        } 
class SeedsForm(forms.ModelForm):
    class Meta:
        model=Seeds
        fields = ('Date','Seed_Made_By','Amount','Service')
        widgets = {
            'Date': DatePickerInput(),
        } 

class MembersForm(forms.ModelForm):
    class Meta:
        model= Members
        fields = ('First_Name','Second_Name','Telephone','Residence','Gender', 'Home_Cell','Photo','Marital_Status','Marriage_Kind',
            'Education_Level','Profession','Type_of_Work','Place_of_Work','Country','County','Parish','District','Sub_County',
            'Village','Date_Of_Salvation','Date_Of_Joining_UCC_Bwaise','Ministry_Involved_In','Name_Of_Next_Of_Kin',
            'Contact_Of_Next_Of_Kin','Residence_Of_Next_Of_Kin','Date_Of_Birth')
        widgets = {
            'Date_Of_Birth': DatePickerInput(),
            'Date_Of_Joining_UCC_Bwaise': DatePickerInput(),
            'Date_Of_Salvation': DatePickerInput()
          } 

class VisitorsForm(forms.ModelForm):
    class Meta:
        model=Visitors
        fields = ('First_Name','Second_Name','Telephone','Address','Church')
class PledgeItemsForm(forms.ModelForm):
    class Meta:
          model = PledgeItem
          fields = ('Item_That_Needs_Pledges','Amount_Needed','Pledge_Deadline','Date')
          widgets = {
            'Date': DatePickerInput(),
            'Pledge_Deadline': DatePickerInput(),
          }                
class PledgesReportArchiveForm(forms.ModelForm):
    class Meta:
        model= PledgesReportArchive
        fields = ('Status','Pledge_Id','Date','Pledge_Made_By','Reason', 'Amount_Paid') 
        widgets = {
            'Date': DatePickerInput(),
        }                