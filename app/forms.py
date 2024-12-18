from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User        
from django.forms import DateInput, ModelForm, PasswordInput, Select, TextInput
from .models import *

'''
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='enter first_name')
    last_name = forms.CharField(max_length=30, required=False, help_text='enter last_name')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    language = forms.CharField(max_length=30, required=False, help_text='language')
    caste = forms.CharField(max_length=30, required=False, help_text='caste')
    city = forms.CharField(max_length=30, required=False, help_text='city')
    occupation = forms.CharField(max_length=30, required=False, help_text='occupation')
    religion = forms.CharField(max_length=30, required=False, help_text='religion'),
    state = forms.CharField(max_length=30, required=False, help_text='select state'),
    nri = forms.CharField(max_length=30, required=False, help_text='select yes or no'),

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 
                  'city', 'religion', 'language',                  
                  'password1', 'password2', )
'''

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Create a UserUpdateForm to update a username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']
        
# Create a ProfileUpdateForm to update image.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']


class SeekerForm(ModelForm):
    class Meta:
        model = Seeker
        fields = (
            'seeker_name', 'seeker_email', 'seeker_password', 
            'seeker_mobile')

        widgets = {
            'seeker_name': TextInput(),    
            'seeker_password': PasswordInput(),
        }


class FormentryForm(ModelForm):
    
    class Meta:
        model = Seeker

        fields = ( 
            #'seeker_dob', 
            'seeker_gender',
            'seeker_religion', 'seeker_caste', 'seeker_language',
            'seeker_occupation', 'seeker_city', 'seeker_state', 'seeker_country'            
        )       
    
       
        widgets = {
            #'seeker_dob': DateInput(), 
            'seeker_religion': Select(),
            'seeker_city': Select(),            
        }
