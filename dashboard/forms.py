from django import forms
from .models import *
from captcha.fields import ReCaptchaField
from django.forms import Textarea, TextInput, ChoiceField
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, MonthPickerInput  

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()

class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ('slider_image', 'image_title')

class SpendForm(forms.ModelForm):
    class Meta:
        model=Spend
        fields=('Date','Payment_Made_To','Reason_For_Payment','Amount')
        widgets = {
            'Date': DatePickerInput(),
            
        } 
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
        raise ValidationError("This email is already used.")

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

class PledgesCashedOutForm(forms.ModelForm):
    class Meta:
        model=PledgesCashedOut
        fields=('Date','Item_That_Needs_Pledges','Amount_Needed','Item_Id','Amount_Cashed_Out')
        widgets = {'Date': DatePickerInput(),
          'Item_That_Needs_Pledges': TextInput(attrs={'placeholder': 'Item'}),} 

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
        fields=('Date_Of_Birth','First_Name','Second_Name','Gender','Church_Member','UCC_Bwaise_Member',
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
        fields = ('Status','Amount_Paid','Balance','Date','Pledge_Made_By','Reason','Amount_Pledged')
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
class ThanksGivingForm(forms.ModelForm):
    class Meta:
        model=ThanksGiving
        fields = ('Date','Thanks_Giving_By','Amount','Service')
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
class DonationsForm(forms.ModelForm):
    class Meta:
        model=Donations
        fields = ('Date','Donated_By','Amount','Reason')
        widgets = {
            'Date': DatePickerInput(),
            'Donated_By': TextInput(attrs={'placeholder': 'e.g. Church, Place or Person'}),
        } 
        labels = {
            'Donated_By': 'Received From',
        }
class MembersForm(forms.ModelForm):
    class Meta:
        model= Members
        fields = ('More_Info','Is_View_on_Web','Group','Initials','First_Name','Second_Name','Telephone','Residence','Gender', 'Home_Cell','Photo','Marital_Status','Marriage_Kind',
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
            'Item_That_Needs_Pledges': TextInput(attrs={'placeholder': 'Item'}),
          }                
class PledgesReportArchiveForm(forms.ModelForm):
    class Meta:
        model= PledgesReportArchive
        fields = ('Status','Pledge_Id','Date','Pledge_Made_By','Reason', 'Amount_Paid') 
        widgets = {
            'Date': DatePickerInput(),
        }  

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('about_title','about', 'about_image','vision_description','mission_description','Is_View_on_Web')

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
        fields = ('news_title', 'image', 'news', 'Is_View_on_Web')

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
                  'address', 'phone', 'registration_date', 'email_address', 'Post_Office_Box',
                  'footer', 'enable_frontend', 'latitude','longitude', 'facebook_url', 'twitter_url', 
                  'linkedIn_url', 'google_plus_url', 'youtube_url','instagram_url','pinterest_url', 
                  'status', 'frontend_Logo', 'backend_Logo')

        widgets = {
            'church_name': TextInput(attrs={'placeholder': 'Church Name'}),
            'church_code': TextInput(attrs={'placeholder': 'Church Code'}),
            'address': TextInput(attrs={'placeholder': 'Address'}),
            'phone': TextInput(attrs={'placeholder': 'Phone'}),
            'email_address': TextInput(attrs={'placeholder': 'Email'}),
            'fax': TextInput(attrs={'placeholder': 'Fax'}),
            'footer': TextInput(attrs={'placeholder': 'Footer'}),
            'registration_date': DatePickerInput(),
        }
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'subject','message','feedback')