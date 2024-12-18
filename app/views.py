from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from operator import itemgetter
from .forms import *

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'app/register.html', {'form': form})

@csrf_exempt
def login_in(request):  # as in github
    user = request.user
    if user.is_authenticated:
        return redirect("home")
        
    if request.method == 'POST':
        print('ln 34 in views.login_in.POST')
        formusername = request.POST.get('username')
        formpwd = request.POST.get('password')
        formpwdmp = make_password(formpwd)   
        regdpwd = User.objects.get(username=formusername).password
        checkpassword=check_password(regdpwd, formpwdmp)
        print('ln 44 checkpassword ', checkpassword)
        success = user.check_password(formpwd)
        print('ln 38 success ', success)
        #valid = user.check_password(form.cleaned_data['password'])
        userregd = User.objects.get(username=formusername)
        print('ln 46 userregd ', userregd)
        # User.objects.get(username=formusername).password == request.POST['password'] is True.
        # user = authenticate(username=userregd)#, password=password)
        userregdid = User.objects.get(username=formusername).id 
        print('ln 50 userregdid ', userregdid)
        
        #print('ln 38 user ', user)
        # if user is not None:
        if checkpassword:
            login(request, userregd)
            print('ln 54 login successful user: ', userregd)
            print('ln 55 request.user.id ', request.user.id)
            messages.success(request, ("login successful"))
            return redirect('profile')

    context = {}
    return render(request, 'app/login.html')

def log_out(request):
    logout(request)
    return redirect('home')


@csrf_exempt
def profile(request):
    profile = Profile.objects.get_or_create(user=request.user)
    # profile = Profile.objects.get(pk=request.user.id)
    print('ln 71 request.user.id ', request.user.id)
    if request.method == 'POST':
        print('ln 37 in views.profile')
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   # request.FILES,
                                   instance=request.user.profile,
                                   # instance=profile,
                                   )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        # p_form = ProfileForm(instance=profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'app/profile.html', context)


@csrf_exempt
def edit_profile(request):
    # seeker.id =  request.session['seeker.id']
     
    # seeker=Seeker.objects.get(id=seeker.id)
   
    # profile = seeker.profile
    
    form = ProfileForm()
    if request.method == 'POST':
        # form = ProfileForm(request.POST, instance=profile)
        # form = ProfileForm(request.POST, request.Files)
        form = ProfileForm(request.POST)
        if form.is_valid():
            # form.instance.user = request.user
        
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm()

    return render(request, 'app/edit_profile.html', {'form': form})

def view_profile(request):
    return render(request, 'app/view_profile.html')

def seeprofile(request):
    return render(request, 'app/seeprofile.html')

@csrf_exempt
def signinlogin(request):
    if request.method == 'POST':
        print('ln 220 in views.signinlogin.POST')
        seekerform = SeekerForm(request.POST)
        if seekerform.is_valid():
            print('ln 199 form.is_valid')
            # form.save()
        
            seeker_name = seekerform.cleaned_data.get('seeker_name')  
            seeker_email = seekerform.cleaned_data.get('seeker_email')
            
            seeker_password = seekerform.cleaned_data.get('seeker_password')
            encryptedpassword = make_password(seeker_password)
            print('ln 207 encryptedpassword ', encryptedpassword)
            checkpassword=check_password(request.POST['seeker_password'], encryptedpassword)
            print('ln 209 checkpassword ', checkpassword)
            
            seeker_mobile = seekerform.cleaned_data.get('seeker_mobile')
            print(' name email pwd mobile', seeker_name, seeker_email, seeker_password, seeker_mobile)

            seeker=Seeker(
                seeker_name=seeker_name, seeker_email=seeker_email, seeker_password=encryptedpassword,
                seeker_mobile=seeker_mobile, 
            )
            '''
            seeker_dob=seeker_dob, seeker_gender=seeker_gender,
            seeker_religion=seeker_religion, seeker_caste= seeker_caste, seeker_language= seeker_language, 
            seeker_occupation= seeker_occupation, seeker_city= seeker_city, seeker_state= seeker_state, 
            seeker_country = seeker_country
            '''
        
            seeker.save()
            print('ln 249 seeker: ', seeker)         
            request.session["seeker.id"] = seeker.id
            print("ln 250 request.session['seeker_name']", request.session['seeker.id'] )
            # login(request, user)
            return redirect('edit_profile')
        else:
            print('ln 104 form is invalid')
    else:
        seekerform = SeekerForm()
    return render(request, 'app/signinlogin.html', {'seekerform': seekerform})

def home(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

@csrf_exempt
def app(request):
    return render(request, 'app/app.html')

def assisted_services(request):
    return render(request, 'app/assisted_services.html')

def bride_profile(request):
    return render(request, 'app/bride_profile.html')

def c_list(request):
    seekernamelist = list(Seeker.objects.all().values_list('seeker_name', 'seeker_caste'))
    print('ln 27 seeker ', list(seekernamelist))
    seeker = list(Seeker.objects.filter(seeker_caste='caste1').values
        ('seeker_name', 'seeker_gender', 
         'seeker_religion', 'seeker_caste',
         'seeker_state', 'seeker_country'))
    print('ln 32 seeker_caste ', seeker)   
    context = {
        'seekernamelist': seekernamelist,
        'seeker': seeker
    }
    return render(request, 'app/c_list.html', context)

def city_list(request):
    seekernamelist = list(Seeker.objects.all().values_list('seeker_name', 'seeker_city'))
    print('ln 41 seeker ', list(seekernamelist))
    seeker = list(Seeker.objects.filter(seeker_city='city1').values
        ('seeker_name', 'seeker_gender', 
         'seeker_religion', 'seeker_caste',
         'seeker_state', 'seeker_country'))
    print('ln 46 seeker_city ', seeker)   
    context = {
        'seekernamelist': seekernamelist,
        'seeker': seeker
    }
    return render(request, 'app/city_list.html', context)

def contact(request):
    return render(request, 'app/contact.html')

def faq(request):
    return render(request, 'app/faq.html')

def feedback(request):
    return render(request, 'app/feedback.html')

def footer(request):
    return render(request, 'app/footer.html')

@csrf_exempt
def form_entry(request): 
        
    if request.method == 'POST':
        formentryform = FormentryForm(request.POST)
        seeker.id =  request.session['seeker.id']
        seeker = Seeker.objects.get(id=seeker.id)
        print('ln 71 seeker ', seeker.seeker_email)
        if formentryform.is_valid():
            print('ln 70 form.is_valid')
            formentryform.save()
            #seeker_dob = formentryform.cleaned_data.get('seeker_dob')  
            '''
            seeker_gender = formentryform.cleaned_data.get('seeker_gender') 
            seeker_occupation = formentryform.cleaned_data.get('seeker_occupation')  
            print('ln 75 mobile, dob, gender ', seeker_gender, seeker_occupation)

            seeker_religion = formentryform.cleaned_data.get('seeker_religion')                    
            seeker_caste = formentryform.cleaned_data.get('seeker_caste')   
            seeker_language = formentryform.cleaned_data.get('seeker_language')   
            print('ln 80 religion caste lang ', seeker_religion, seeker_caste, seeker_language)
                            
            seeker_city = formentryform.cleaned_data.get('seeker_city')   
            seeker_state = formentryform.cleaned_data.get('seeker_state')   
            seeker_country = formentryform.cleaned_data.get('seeker_country')   
            print('ln 85 city, state, country ', seeker_city, seeker_state, seeker_country)
         
            seeker=Seeker(
                #seeker_dob=seeker_dob,  
                seeker_gender=seeker_gender, seeker_occupation=seeker_occupation,
                seeker_religion=seeker_religion, seeker_caste=seeker_caste, seeker_language=seeker_language,
                seeker_city=seeker_city, seeker_state=seeker_state, seeker_country=seeker_country,          
                )
            '''
            
            # seeker.save()
            # print('ln 107 seeker: ', seeker)
            
            # login(request, user)
            return redirect('home')
        else:
            print('ln 104 form is invalid')
    else:
        formentryform = FormentryForm()
    return render(request, 'app/form_entry.html', {'formentryform': formentryform})

def groom_profile(request):
    return render(request, 'app/groom_profile.html')

def head(request):
    return render(request, 'app/head.html')

def help(request):
    return render(request, 'app/help.html')

def icons(request):
    return render(request, 'app/icons.html')

def l_list(request):
    seekernamelist = list(Seeker.objects.all().values_list('seeker_name', 'seeker_language'))
    print('ln 82 seeker ', list(seekernamelist))
    seeker = list(Seeker.objects.filter(seeker_language='lang1').values
        ('seeker_name', 'seeker_gender', 
         'seeker_religion', 'seeker_caste',
         'seeker_state', 'seeker_country'))
    print('ln 87 seeker_lang1 ', seeker)   
    context = {
        'seekernamelist': seekernamelist,
        'seeker': seeker
    }
    return render(request, 'app/l_list.html', context)

def matches(request):
    return render(request, 'app/matches.html')

def nri_list(request):
    seekernamelist = list(Seeker.objects.all().values_list('seeker_name', 'seeker_country'))
    print('ln 102 seeker ', list(seekernamelist))
    seeker = list(Seeker.objects.filter(seeker_country='coun1').values
        ('seeker_name', 'seeker_gender', 
         'seeker_religion', 'seeker_caste',
         'seeker_state', 'seeker_country'))
    print('ln 107 seeker_caste ', seeker)   
    context = {
        'seekernamelist': seekernamelist,
        'seeker': seeker
    }
    return render(request, 'app/nri_list.html', context)

def o_list(request):
    seekernamelist = list(Seeker.objects.all().values_list('seeker_name', 'seeker_occupation'))
    print('ln 105 seeker ', list(seekernamelist))
    seeker = list(Seeker.objects.filter(seeker_occupation='occu1').values
        ('seeker_name', 'seeker_gender', 
         'seeker_religion', 'seeker_caste',
         'seeker_state', 'seeker_country'))
    print('ln 110 seeker_occupation ', seeker)   
    context = {
        'seekernamelist': seekernamelist,
        'seeker': seeker
    }
    return render(request, 'app/o_list.html', context)

def privacy_policy(request):
    return render(request, 'app/privacy_policy.html')

def r_list(request):
    seekernamelist = list(Seeker.objects.all().values_list('seeker_name', 'seeker_religion'))
    print('ln 123 seeker ', list(seekernamelist))
    seeker = list(Seeker.objects.filter(seeker_religion='reli1').values
        ('seeker_name', 'seeker_gender', 
         'seeker_religion', 'seeker_caste',
         'seeker_state', 'seeker_country'))
    your_filter = 'reli1'
    print('ln 129 seeker_reli1 ', seeker)   
    context = {
        'seekernamelist': seekernamelist,
        'seeker': seeker,
        'your_filter': your_filter,
    }
 
    return render(request, 'app/r_list.html', context)

def readtxt(request):
    return render(request, 'app/readtxt.html')

def s_list(request):
    seekernamelist = list(Seeker.objects.all().values_list('seeker_name', 'seeker_state'))
    print('ln 142 seeker ', list(seekernamelist))
    seeker = list(Seeker.objects.filter(seeker_state='state1').values
        ('seeker_name', 'seeker_gender', 
         'seeker_religion', 'seeker_caste',
         'seeker_state', 'seeker_country'))
    print('ln 147 seeker_caste ', seeker)   
    context = {
        'seekernamelist': seekernamelist,
        'seeker': seeker
    }
    return render(request, 'app/s_list.html', context)

@csrf_exempt
def search(request):
    return render(request, 'app/search.html')

def sitemap(request):
    return render(request, 'app/sitemap.html')

def terms(request):
    return render(request, 'app/terms.html')

def tips(request):
    return render(request, 'app/tips.html')

def typo(request):
    return render(request, 'app/typo.html')

def writeus(request):
    return render(request, 'app/writeus.html')