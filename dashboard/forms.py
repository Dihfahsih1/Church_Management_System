from dal import autocomplete
import os
import fleep
from django import forms
from .models import *
from django.forms import Textarea, TextInput, ChoiceField
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, MonthPickerInput 
from captcha.fields import CaptchaField

from functools import partial
 
class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ('slider_image', 'image_title')


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('Is_View_on_Web','email','username','Role','full_name','is_active','is_staff','is_superuser')
        widgets = {
            'Date': DatePickerInput(),
            
        } 
class UserEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email:
            return email
        try:
            user = User.objects.get(email=email)
            if user.email == self.instance.email:
                return email
        except User.DoesNotExist:
            return email
        return "This email is already used."

class ExpendituresForm(forms.ModelForm):
    class Meta:
        model=Expenditures
        fields=('Notes','Member_Name','Other_Expenditure','Reason_filtering','Archived_Status','Date',
        'Payment_Made_To','Main_Expense_Reason','General_Expenses_Reason','Petty_Cash_Reason','Amount')
        widgets = {
            'Other_Expenditure': TextInput(attrs={'placeholder': 'any other expense'}),
            'Amount': TextInput(attrs={'placeholder': 'Shs.'}),
            'Date': DatePickerInput(),
            'Member_Name': autocomplete.ModelSelect2(url='auto-complete',
            attrs={'data-placeholder': 'Type here the name....', 'data-minimum-input-length': 3})
        }                 
class RevenuesForm(forms.ModelForm):
    class Meta:
        model=Revenues
        fields=('Envag_Or_Missions_Amount','Building_Amount','Love_Offering_Amount','Thanks_Giving_Amount','Member_Id','General_Offering_Amount','Tithe_Amount','Seed_Amount','Bills_Amount','Other_Notes','Other_Sources','Revenue_filter','Archived_Status','Date','Member_Name'
        ,'Service','Amount')
        widgets = {
            'Date': DatePickerInput(),
            'Other_Sources': TextInput(attrs={'placeholder': 'e.g lwaki olimulamu missions'}),
            'Other_Notes': TextInput(attrs={'placeholder': 'Something like title'}),
        }                 

class PledgesCashedOutForm(forms.ModelForm):
    class Meta:
        model=PledgesCashedOut
        fields=('Date','Item_That_Needs_Pledges','Amount_Needed','Item_Id','Amount_Cashed_Out')
        widgets = {'Date': DatePickerInput(),
          'Item_That_Needs_Pledges': TextInput(attrs={'placeholder': 'Item'}),} 

class StaffDetailsForm(forms.ModelForm):
    class Meta:
        model=StaffDetails
        fields=('Date_Of_Birth','First_Name','Second_Name','Gender','Church_Member','UCC_Bwaise_Member',
            'Education_Level','Residence','Telephone','Photo','Faith',
            'Date_of_paying_salary','Month_being_cleared','Salary_Amount',
            'Role','Date_of_employment','End_of_contract')
        widgets = {
             'Church_Member' : autocomplete.ModelSelect2(url='auto-complete',
            attrs={'data-placeholder':'Type here the name....', 'data-minimum-input-length':3}),
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

class PledgesForm(forms.ModelForm):
    class Meta:
        model=Pledges
        fields = ('Pledge_Made_By_Visitor','is_church_member','Archived_Status','Status','Amount_Paid','Balance','Date','Pledge_Made_By','Reason','Amount_Pledged')
        widgets = {
            'Date': DatePickerInput(),
            'Pledge_Made_By': autocomplete.ModelSelect2(url='auto-complete', attrs={
            'data-placeholder': 'Type here Member name....', 'data-minimum-input-length': 3}),

        }

class CashFloatForm(forms.ModelForm):
    class Meta:
        model=CashFloat
        fields = ('Date','Amount','Notes','TopUpAmount')
        widgets = {
            'Date': DatePickerInput(),
        } 
class UpdatePledgesForm(forms.ModelForm):
    class Meta:
        model=Pledges
        fields = ('Date','is_church_member', 'Pledge_Made_By_Visitor','Pledge_Made_By', 'Reason')
        widgets = {

            'Date': DatePickerInput(),
            'Amount_Paid': TextInput(attrs={'placeholder': 'Shs.'}),
        }  

class MembersForm(forms.ModelForm):
    #captcha = CaptchaField()
    class Meta:
        model= Members
        fields = ('More_Info','Is_View_on_Web','Email','Group','Initials','First_Name','Second_Name','Telephone',
            'Residence','Gender', 'Home_Cell','Photo','Marital_Status','Marriage_Kind',
            'Education_Level','Profession','Type_of_Work','Place_of_Work','Country','County','Parish','District',
            'Sub_County', 'Village','Date_Of_Salvation','Date_Of_Joining_UCC_Bwaise','Ministry_Involved_In', 'Spouse','Children',
            'Name_Of_Next_Of_Kin','Contact_Of_Next_Of_Kin','Residence_Of_Next_Of_Kin','Date_Of_Birth','is_active')
        is_active = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
        widgets = {
            'Date_Of_Birth': DatePickerInput(),
            'Date_Of_Joining_UCC_Bwaise': DatePickerInput(),
            'Date_Of_Salvation': DatePickerInput(),             
          } 
        labels = {
            'Spouse': 'Your Marriage Partner',
            'More_Info':'Brief intro about the member',
            'Children': 'The names of member \'s children'
        }
        


class VisitorsForm(forms.ModelForm):
    class Meta:
        model=Visitors
        fields = ('Date','First_Name','Second_Name','Telephone','Address','Church')
        widgets = {
            'Date': DatePickerInput(),
          }   
class PledgeItemsForm(forms.ModelForm):
    class Meta:
          model = PledgeItem
          fields = ('Archived_Status','Item_That_Needs_Pledges','Amount_Needed','Pledge_Deadline','Date')
          widgets = {
            'Date': DatePickerInput(),
            'Pledge_Deadline': DatePickerInput(),
            'Item_That_Needs_Pledges': TextInput(attrs={'placeholder': 'Item'}),
          }                


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('banner','church_details','about_title','about', 'about_image','core_values','vision_description','mission_description','Is_View_on_Web')

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('page_location', 'page_title', 'page_description', 'page_image')

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('gallery_title', 'note', 'Is_View_on_Web')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('gallery_title', 'gallery_image', 'image_caption','Is_View_on_Web')   
                                           
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('news_title', 'image','audio_file', 'news', 'Is_View_on_Web')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('start_date', 'project_title', 'project_leader', 'image', 'project_description', 'Is_View_on_Web')
        widgets = {
            'start_date': DatePickerInput(),
            'project_leader': autocomplete.ModelSelect2(url='auto-complete', attrs={
                'data-placeholder': 'Type here the name....', 'data-minimum-input-length': 1})
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_title', 'event_for', 'event_place', 'from_date', 'to_date', 'image', 'note',
                  'Is_View_on_Web', 'Start_Time', 'End_Time', 'Program_Name', 'Day','Activity_Type')

        widgets = {
            'from_date': DatePickerInput(),
            'to_date': DatePickerInput(),
            'Start_Time': TimePickerInput(),
            'End_Time': TimePickerInput(),
        }
        
class churchForm(forms.ModelForm):
    class Meta:
        model = Church
        fields = ('church_vision','church_mission','maps_embedded_link','church_name', 'church_code', 
                  'address', 'phone','status', 'Church_Logo',
                   'registration_date', 'email_address', 'Post_Office_Box',
                  'footer', 'enable_frontend', 'latitude','longitude', 'facebook_url', 'twitter_url', 
                  'linkedIn_url', 'google_plus_url', 'youtube_url','instagram_url','pinterest_url', 
                  )

        widgets = {
            'church_name': TextInput(attrs={'placeholder': 'Church Name'}),
            'church_code': TextInput(attrs={'placeholder': 'Church Code'}),
            'address': TextInput(attrs={'placeholder': 'Address'}),
            'phone': TextInput(attrs={'placeholder': 'Phone'}),
            'email_address': TextInput(attrs={'placeholder': 'Email'}),
            'footer': TextInput(attrs={'placeholder': 'Footer'}),
            'registration_date': DatePickerInput(),

        }
class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'subject','message','feedback')
        #form for ministries 
class MinistryForm(forms.ModelForm):
    class Meta:
        model = Ministry
        fields = ('name', 'leader', 'photos', 'details','Is_View_on_Web')
class AnnualConferenceForm(forms.ModelForm):
    class Meta:
        model = AnnualConference
        fields = ('start_date', 'end_date', 'estimated_budget', 'conference_theme','conference_report')
        widgets={
        'start_date':DatePickerInput(),
        'end_date' :DatePickerInput()
        }
class LwakiOliMulamuForm(forms.ModelForm):
    class Meta:
        model = LwakiOliMulamu
        fields = ('date','location','which_type','conference_theme','title','preachers','embedded_video','image','audio_file','day','details')
        widgets={
        'date':DatePickerInput(),
        }
class NewConvertForm(forms.ModelForm):
    class Meta:
        model = NewConvert
        fields = ('is_church_member', 'born_again_before', 'First_Name', 'Second_Name', 'Telephone', 'Date_Of_Salvation', 'member_name')
        widgets={
            'Date_Of_Salvation':DatePickerInput(),
            'member_name': autocomplete.ModelSelect2(url='auto-complete',
            attrs={'data-placeholder': 'Type here the name....', 'data-minimum-input-length': 3})
        }