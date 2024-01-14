from django.contrib import admin
from django.urls import path
from Advitya_app import views
from .views import register_for_activity,handle_activity_registration
from .views import dashboard, custom_login_view
urlpatterns = [
    path("", views.index, name='index'),
    path('SocioTrivia', views.SocioTrivia, name='SocioTrivia'),
    path('Triviareg', views.Triviareg, name='Triviareg'),
    path('Account', views.Account, name='Account'),
    path('contact', views.contact, name='contact'),
    path('event', views.event, name='event'),
    path('sponsor', views.sponsor, name='sponsor'),
    path('schedule', views.schedule, name='schedule'),
    path('login/', custom_login_view, name='custom_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('handle_activity_registration/<int:activity_id>/', handle_activity_registration, name='handle_activity_registration'),
    path('register/<int:activity_id>/', register_for_activity, name='register_for_activity'),
]



    # path('choose', views.choose, name='choose'),
   
    # path('events', views.events_page, name='events_page'),  # New view for displaying events
    # path('register_for_event', views.register_for_event, name='register_for_event'),  # New view for registering for an event

    # path('initial-registration', initial_registration, name='initial_registration'),
    # path('initial-registration', views.initial_registration, name='initial_registration'),




