from authmn.forms import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout 
from django.contrib.auth.models import User
from authmn.models import UserProfile
from django.template import RequestContext
from django.shortcuts import *
import datetime, time
#from django.forms.widgets.CheckBoxInput import check_test

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data        
            newuser = User(username = data['team_name'],first_name = data['team_leader'],email = data['team_leader_email'])
            newuser.set_password(data['password'])
#            print ">>>> PASSWD : " , data['password']
            newuser.save()
    #       want_accommodation = check_test(data['want_accommodation'])
            userprofile = UserProfile(
                user = newuser, 
                team_leader = data['team_leader'],  
                team_name = data['team_name'],  
#                team_leader_gender = data['team_leader_gender'],
                team_leader_age = data['team_leader_age'],
                member_2 = data['member_2'],
                member_3 = data['member_3'],
                member_4 = data['member_4'],
                member_5 = data['member_5'],
                team_leader_mobilenumber = data['team_leader_mobilenumber'],
                mobilenumber_2 = data['mobilenumber_2'],
                mobilenumber_3 = data['mobilenumber_3'],
                mobilenumber_4 = data['mobilenumber_4'],
                mobilenumber_5 = data['mobilenumber_5'],
                team_leader_email = data['team_leader_email'],  
                email_2 = data['email_2'],  
                email_3 = data['email_3'],
                email_4 = data['email_4'],
                email_5 = data['email_5'],
                college_name = data['college_name'],
                team_id = "lc"+str(newuser.id), 
#                want_accommodation = data['want_accommodation'], 
#                centre_for_first_round = data['centre_for_first_round'], 
            )
            userprofile.save()
            newuser = User.objects.get(username=data['team_name'])
            newuser.username = userprofile.team_id
            newuser.save()
            user = authenticate(username = newuser.username, password=data['password'])
            auth_login(request, user)
            return redirect('authmn.views.home')
        else:
            form_errors = form.errors
            print form_errors
            
    else:
        form = RegistrationForm()
    return render_to_response('authmn/register.html', locals(),context_instance = RequestContext(request))

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['team_id']
            password = data['password']
            print " >>>>>>>>>>>>> ", username, "  ", password
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('authmn.views.home')
            else:
                user_profile_list = UserProfile.objects.filter(team_name=username)
                if len(user_profile_list) == 1 :
                    user_profile = user_profile_list[0]
                    username = user_profile.user.username
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        auth_login(request, user)
                        return redirect('authmn.views.home')
                    else :
                        
                        error_message="Something unusual happened. We could find your Team Name, but not your Team. Contact the coordinators."
                        login_form = LoginForm()
                        return render_to_response('authmn/login.html', locals(), context_instance = RequestContext(request))
                elif len(user_profile_list) == 0 :
                    error_message="your username and password do not match"
                    login_form = LoginForm()
                    return render_to_response('authmn/login.html', locals(), context_instance = RequestContext(request))
                else :
                    error_message = "We cannot find a distinct team with that team name. Please use your team ID"
                    login_form = LoginForm()
                    return render_to_response('authmn/login.html', locals(), context_instance = RequestContext(request))
                    
    else:
        form=LoginForm()
    return render_to_response('authmn/login.html', locals(), context_instance = RequestContext(request))

def edit_profile(request):
    round_1_form = FirstRoundCentreForm()
    if request.user.is_authenticated():
        try:
            user = User.objects.get(pk=request.user.id)
        except:
            user=None
            auth_logout(request)    
            return redirect('authmn.views.login')
        if user is not None:        
            try:            
                user_profile=UserProfile.objects.get(user__id=user.id)
#                user_profile=UserProfile.objects.get(user=user)
                round_1_form.fields['centre_for_first_round'].initial = user_profile.centre_for_first_round # Set centre from user_profile
            except:
            # this would happen for admin or users created by admin without putting userprofile,so I'm not caring much about this
                return HttpResponse('Sorry you do not have a user profile')         

            
            
        if request.method == 'POST' and len(request.POST) < 10:
            round_1_form = FirstRoundCentreForm(request.POST)
            if round_1_form.is_valid():
                user_profile.centre_for_first_round = round_1_form.cleaned_data['centre_for_first_round']
                print round_1_form.cleaned_data['centre_for_first_round']
                user_profile.save()
                print user_profile.centre_for_first_round
                return redirect('authmn.views.home')
            
        elif request.method == 'POST':
            print user_profile
            form = EditProfileForm(request.POST,instance = user_profile)
            if form.is_valid():
                form.save()
                print form
                return redirect('authmn.views.home')
                #user.first_name=data['first_name']
                #user.last_name=data['last_name']
                #user.save()
                
        else:
            form = EditProfileForm(instance=user_profile)
    else:
        return redirect('authmn.views.login')
    
    return render_to_response('authmn/editprofile.html', locals(), context_instance = RequestContext(request))
    
def edit_user_profile(request):
    registered_no = UserProfile.objects.count()
    if request.user.is_authenticated:
        try:
            user=User.objects.get(pk=request.user.id)
        except:
            user=None
            auth_logout(request)    
            return redirect('authmn.views.login')
        if request.method == 'POST':
            form=EditUserForm(request.POST,instance=user)
            if form.is_valid():
                form.save()
                return redirect('authmn.views.home')
        else:
            form=EditUserForm(instance=user)
    else:
        return redirect('authmn.views.home')
    return render_to_response('edituser.html', locals(), context_instance = RequestContext(request))

def lunar_first_round(request):
    registered_no = UserProfile.objects.count()
    form=FirstRoundCentreForm()
    if request.user.is_authenticated:
        user=request.user
        try:
            userprofile=UserProfile.objects.get(user=user)
        except:
            user=None
            auth_logout(request)    
            return redirect('authmn.views.login')
        if request.method == 'POST':
            form=FirstRoundCentreForm(request.POST)
            if form.is_valid():
                userprofile.centre_for_first_round = form.cleaned_data['centre_for_first_round']
                return redirect('authmn.views.home')
    
    else:
        return redirect('authmn.views.home')
    return render_to_response('firstround.html', locals(), context_instance = RequestContext(request))
                 
def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)
    else:
        return redirect('authmn.views.login')
    return redirect('authmn.views.login')

def home(request):
    #start date, end date and today's date in seconds for the clock
    (startDate, endDate, now) = set_clock_date()
    registered_no = UserProfile.objects.count()
    round_1_form = FirstRoundCentreForm()
    
    if request.user.is_authenticated:
        if request.user.is_superuser: # For admin to see table of users
            users_for_template = UserProfile.objects.all()
            return render_to_response('authmn/admin.html', locals(), context_instance=RequestContext(request))
        
        user = request.user
        try:
            user_profile = UserProfile.objects.get(user=user)
        except:
            user_profile = None
            user = None
            auth_logout(request)

        if user_profile:
            round_1_form = FirstRoundCentreForm()
            round_1_form.fields['centre_for_first_round'].initial = user_profile.centre_for_first_round # Set centre from user_profile
            
            if request.method == 'POST':
                round_1_form = FirstRoundCentreForm(request.POST)
                if round_1_form.is_valid():
                    user_profile.centre_for_first_round = round_1_form.cleaned_data['centre_for_first_round']
                    print round_1_form.cleaned_data['centre_for_first_round']
                    user_profile.save()
                    print user_profile.centre_for_first_round
                    return redirect('authmn.views.home')
            
                
    else:
        user = None


    return render_to_response('authmn/index.html',locals(),context_instance=RequestContext(request))
    
def set_clock_date():
    '''
        returns start date, end date and today in seconds.
        these values are used in the countdown timer.
    '''
    today = datetime.datetime.now()
    startdate = datetime.datetime(2013, 7, 1, 0, 0, 1)
    enddate = datetime.datetime(2013, 9, 22, 23, 59, 59) # 12th Sept Midnight .. i.e. 13th Sept
    
    startdate_sec = time.mktime(startdate.timetuple())
    enddate_sec = time.mktime(enddate.timetuple())
    today_sec = time.mktime(today.timetuple())
    
    return (startdate_sec, enddate_sec, today_sec)
