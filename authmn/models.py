from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user         = models.OneToOneField(User)
    team_name    = models.CharField(max_length=20,help_text='please choose a unique team name')
    college_name = models.CharField(max_length=20,help_text= '(Please enter your college name,all your team members must be from the same college)')
    
    team_leader  = models.CharField(max_length=20,help_text='(Please enter the name of your Team leader,your team should contain atleast one member and five members at maximum)')
    team_leader_mobilenumber = models.CharField(max_length=12,help_text = '(Please enter your team Mobilenumber)')
    team_leader_email = models.EmailField(max_length=40)
    
    member_2     = models.CharField(max_length=20,blank=True,help_text='(If you have more than one member in your team,please fill their names)')
    mobilenumber_2           = models.CharField(max_length=12,blank=True,help_text='(You can enter your team member mobilenumber other than team leader mobilenumber,but it is optional)')
    email_2           = models.EmailField(max_length=40,blank=True,help_text='(You can enter your team member email_id other than team leader email,but it is optional)')
    
    member_3     = models.CharField(max_length=20,blank=True,help_text='(If you have more than one member in your team,please fill their names)')
    mobilenumber_3           = models.CharField(max_length=12,blank=True)
    email_3           = models.EmailField(max_length=40,blank=True)
    
    member_4     = models.CharField(max_length=20,blank=True,help_text='(If you have more than one member in your team,please fill their names)')
    mobilenumber_4           = models.CharField(max_length=12,blank=True)
    email_4           = models.EmailField(max_length=40,blank=True)
    
    member_5     = models.CharField(max_length=20,blank=True,help_text='(If you have more than one member in your team,please fill their names)')
    mobilenumber_5           = models.CharField(max_length=12,blank=True)
    email_5           = models.EmailField(max_length=40,blank=True)
    
    team_id = models.CharField(max_length=10)
    want_accommodation = models.BooleanField(default=False)
    accomodation_for_boys = models.IntegerField(default=0, help_text='Number of male members in your team')
    accomodation_for_girls = models.IntegerField(default=0, help_text='Number of female members in your team')
    
    
    def __unicode__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = "Teams"
