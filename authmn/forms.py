from django import forms
from authmn.models import *
from captcha.fields import ReCaptchaField
from lunar.settings import RECAPTCHA_PUBLIC_KEY,RECAPTCHA_PRIVATE_KEY
from django.contrib.auth.models import User

class BaseUserForm(forms.ModelForm):
#   first_name = forms.CharField(max_length=20)
#   last_name  = forms.CharField(max_length=20)
    class Meta:
        model = UserProfile
    
#   def clean_first_name(self):
#       if not self.cleaned_data['first_name'].replace(' ','').isalpha():
#           raise forms.ValidationError(u'Names cannot contain anything other than alphabets.')
#       else:
#           return self.cleaned_data['first_name']
    
#   def clean_last_name(self):
#       if not self.cleaned_data['last_name'].replace(' ','').isalpha():    
#           raise forms.ValidationError(u'names cannot contain anything other than alphabets.')
#       else:
#           return self.cleaned_data['last_name']

    def clean_team_leader_mobilenumber(self):
        if (len(self.cleaned_data['team_leader_mobilenumber'])!=10 or \
           self.cleaned_data['team_leader_mobilenumber'][0] != '7' and \
           self.cleaned_data['team_leader_mobilenumber'][0] != '8' and \
           self.cleaned_data['team_leader_mobilenumber'][0] != '9' or \
           not self.cleaned_data['team_leader_mobilenumber'].isdigit()):
            raise forms.ValidationError(u'Enter a valid mobile number')
        if UserProfile.objects.filter(team_leader_mobilenumber=self.cleaned_data['team_leader_mobilenumber']):          
            raise forms.ValidationError(u'This mobile number is already registered')
        else:
            return self.cleaned_data['team_leader_mobilenumber']
        
    def clean_team_leader_age(self):
        if (self.cleaned_data['team_leader_age']<12 or self.cleaned_data['team_leader_age']>80):
            raise forms.ValidationError('please enter acceptable age between 12 to 80')
        else:
            return self.cleaned_data['team_leader_age']

class RegistrationForm(BaseUserForm):
#   captcha = ReCaptchaField(
#           public_key = RECAPTCHA_PUBLIC_KEY,
#           private_key = RECAPTCHA_PRIVATE_KEY,
#           attrs = {'theme':'clean'}
#           )
#   team_id       = forms.CharField(max_length=20,help_text='(Your team name will be your username,so please choose a unique team name)' )

    password        = forms.CharField(max_length=20,widget=forms.PasswordInput)
    password_again  = forms.CharField(max_length=20,widget=forms.PasswordInput,help_text='please enter the same password which you have entered above')
#   want_accommodation = forms.BooleanField(widget=forms.CheckboxInput,required=False)
    class Meta(BaseUserForm.Meta):
        fields =('team_name','password','password_again','team_leader','team_leader_age','team_leader_mobilenumber','team_leader_email',
'member_2','member_3','member_4','member_5','mobilenumber_2','mobilenumber_3','mobilenumber_4','mobilenumber_5',
'email_2','email_3','email_4','email_5','college_name', 'centre_for_first_round')
    
    def clean_team_name(self):
        if User.objects.filter(username=self.cleaned_data['team_name']):
            raise forms.ValidationError('This team name is already used by others,so please use any other team name')
        else:
            return self.cleaned_data['team_name']

    def clean_team_leader_email(self):
        if User.objects.filter(email=self.cleaned_data['team_leader_email']):
            raise forms.ValidationError('This email_id is already registered,use another')
        else:
            return self.cleaned_data['team_leader_email']
    def clean_password_again(self):
        if self.cleaned_data['password'] != self.cleaned_data['password_again']:
            raise forms.ValidationError('please enter the same password you have entered above or else enter different password')
        else:
            return self.cleaned_data['password_again']

class LoginForm(forms.Form):
    #captcha = ReCaptchaField(
    #       public_key = RECAPTCHA_PUBLIC_KEY,
    #       private_key = RECAPTCHA_PRIVATE_KEY,
    #       attrs = {'theme':'clean'}
    #       )
    
    team_id   =  forms.CharField(max_length = 20, widget = forms.TextInput(attrs = {'placeholder': 'Team ID'}))#, help_text='(Enter your team id)')
    password   =  forms.CharField(max_length = 20, widget = forms.PasswordInput(attrs = {'placeholder': 'Password'}))#, help_text='(Enter your password)')
    
class EditProfileForm(forms.ModelForm):

    class Meta:
        model=UserProfile
        widgets = {
            'user': forms.HiddenInput(),
        }
#           fields = ('first_name','last_name','gender','age','mobilenumber','college_name','branch')
        exclude = ('team_id', 'want_accommodation', 'center_for_first_round', 'accomodation_for_boys', 'accomodation_for_girls')
    
class EditUserForm(forms.ModelForm):
#   first_name=forms.CharField(max_length=20)
#   last_name=forms.CharField(max_length=20)
    class Meta:
        model=User
        widgets = {
    #       'groups'            : forms.HiddenInput(blank=True),
            'is_staff'          : forms.HiddenInput(),
            'is_active'         : forms.HiddenInput(),
            'is_superuser'      : forms.HiddenInput(),
            'date_joined'       : forms.HiddenInput(),
            'last_login'        : forms.HiddenInput(),
            'team_id'        : forms.HiddenInput(),
    #       'user_permissions'  : forms.HiddenInput(blank=True)
            }
        exclude = ('groups', 'user_permissions','password','first_name','last_name','email', 'team_id')

class FirstRoundCentreForm(forms.Form):
    centre_for_first_round=forms.ChoiceField(required=True,choices=[('A', 'IIT Madras'), ('B', 'IIT Delhi'), ('C','VJIT')])

    
    
    
