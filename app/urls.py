from django.urls import path, re_path
from .views import *
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name ='register'),
    path('login/', login_in, name='login'),   
    path('logout/', log_out, name='logout'),   
    
    path('signinlogin/', signinlogin, name='signinlogin'),  

    path('profile', profile, name='profile'),    
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('seeprofile/', seeprofile, name='seeprofile'), 

    path('bride_profile/', bride_profile, name='bride_profile'),
    path('groom_profile/', groom_profile, name='groom_profile'),

    path('about/', about, name='about'), 
    path('contact/', contact, name='contact'),
    path('head/', head, name='head'),
    path('footer/', footer, name='footer'),

    path('app/', app, name='app'),
    path('assisted_services/', assisted_services , name='assisted_services'),
    path('c_list/', c_list , name='c_list'),
    path('city_list/', city_list, name='city_list'),
    path('faq/', faq, name='faq'),
    path('feedback/', feedback, name='feedback'),
    path('form_entry/', form_entry, name='form_entry'),
    path('help/', help, name='help'),
    path('icons/', icons, name='icons'),
    path('l_list/', l_list, name='l_list'),                                        
    path('matches/', matches, name='matches'),
    path('nri_list/', nri_list, name='nri_list'),
    path('o_list/', o_list, name='o_list'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
    path('r_list/', r_list, name='r_list'),    
    path('readtxt/', readtxt, name='readtxt'),
    path('s_list/', s_list, name='s_list'),
    path('search/', search, name='search'),                                             
    path('sitemap/', sitemap, name='sitemap'),
    path('terms/', terms, name='terms'),
    path('tips/', tips, name='tips'),
    path('typo/', typo, name='typo'),                                                
    path('writeus/', writeus, name='writeus'), 
]
