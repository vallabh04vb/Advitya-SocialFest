from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Activity, UserActivityRegistration, UserActivityRegistrationInitial, UserAccount, ActivityRegistration
from .forms_v import RegistrationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponse
from django.core.mail import send_mail 
# from django.core import mail
from django.contrib import messages


# Views for rendering templates
def index(request):
    return render(request, "index.html")

def SocioTrivia(request):
    return render(request, "events_form.html")

def event(request):
    return render(request, "events.html")

def contact(request):
    return render(request, "contact.html")

def sponsor(request):
    return render(request, "sponsor.html")

def schedule(request):
    return render(request, "schedule.html")

def Triviareg(request):
    return render(request, "events_form.html")

def Account(request):
    if request.method == "POST":
        aname = request.POST.get('name')   
        aemail = request.POST.get('email')   
        aphone = request.POST.get('phone')  
        acollege = request.POST.get('college')   
        aCity = request.POST.get('City')  
        aprofessions = request.POST.getlist('profession')
        
        # print("Received Data:")
        # print("Name:", aname)
        # print("Email:", aemail)
        # print("Phone:", aphone)
        # print("College:", acollege)
        # print("City:", aCity)
        # print("Professions:", aprofessions)

        professions_str = ', '.join(aprofessions)
        account = UserAccount(name=aname, email=aemail, phone=aphone, college=acollege, City=aCity, events=professions_str)
        account.save()

        sub = "Welcome to Advitya: A Serenade of Aspirations | Abhyuday, IIT Bombay"
        msg = """ 

Dear {},

Greetings from Abhyuday, IIT Bombay!

Thank you for registering for Advitya, the eagerly awaited two-day annual fest hosted by Abhyuday, the social body of IIT Bombay. We're delighted to have you as part of this vibrant celebration and are committed to ensuring it becomes a memorable experience for you!

You have successfully registered for the following:
{}

 Event Details: 

 Date: 20th & 21st January
 Venue: IIT Bombay
 Schedule: The exact timings and venues for each specific event/workshop, etc., will be released in the schedule one day before the fest on our social media handles.

If you require accommodation during the fest, kindly fill out the accommodation form available on our website.

Stay updated with the latest news, announcements by following us on our social media platforms:

 Instagram : https://instagram.com/iitbombay_abhyuday
 Twitter : https://twitter.com/Abhyuday_IITB
 Facebook : https://www.facebook.com/abhyuday.iitb/
 Linkedin : https://www.linkedin.com/company/abhyuday-iit-bombay/

For any queries or require assistance, feel free to reach out to us at:

Maharshi
Events and Fellowships Head
9316169020

Sahil
Media and PR Head
8708260409

Thank you once again for joining us for Advitya: A Serenade of Aspirations. We eagerly anticipate your presence and the opportunity to create lasting memories together!

Best Regards,
Team Abhyuday, IITBombay
""".format(aname,professions_str)

        # You can use the following lines to send the email if needed
        send_mail(sub, msg, 'advitya.iitb@gmail.com', [aemail])

        messages.success(request, "You have successfully registered! Please check your registered email for confirmation.")
        return redirect('index')

    return HttpResponse("Method Not Allowed", status=405)

@login_required
def register_for_activity(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    is_registered = False  # Initialize is_registered with False

    if request.method == 'POST':
        # activity_id = request.POST.get('activity_id')
        form = RegistrationForm(request.POST)
        if form.is_valid():
            social_account = request.user.socialaccount_set.first()
            user_email = social_account.extra_data.get('email') if social_account else None

            registration = UserActivityRegistration(
                user=request.user,
                email=user_email, 
                
                name_user=form.cleaned_data['name_user'],
                activity=activity,
                phone_number=form.cleaned_data['phone_number']
            )
            registration.save()
            return redirect('SocioTrivia')
    else:
        social_account = request.user.socialaccount_set.first()
        initial_data = {'email': social_account.extra_data.get('email')} if social_account else {}
        form = RegistrationForm(initial=initial_data)

    # Check if the user is registered for this activity
    is_registered = UserActivityRegistration.objects.filter(user=request.user, activity=activity).exists()

    # Get registration statuses for other activities
    is_registered_activity_1 = UserActivityRegistration.objects.filter(user=request.user, activity_id=1).exists()
    is_registered_activity_2 = UserActivityRegistration.objects.filter(user=request.user, activity_id=2).exists()

    return render(request, 'events.html', {'form': form, 'activity': activity, 'is_registered': is_registered,
                                           'is_registered_activity_1': is_registered_activity_1,
                                           'is_registered_activity_2': is_registered_activity_2})

@login_required
def dashboard(request):
    user_exists = UserActivityRegistrationInitial.objects.filter(user=request.user).exists()

    if user_exists:
        return render(request, 'events.html')
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                registration = form.save(commit=False)
                registration.user = request.user
                registration.save()
                return redirect("event")
        else:
            form = RegistrationForm()

        return render(request, 'initial_registration.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'events.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('dashboard')

custom_login_view = CustomLoginView.as_view()

login_required
def handle_activity_registration(request, activity_id):
    if request.method == "POST":
        # Assuming the activity_id is passed through the form or extracted from the request
        activity_id = request.POST.get('activity_id')

        # Check if the user is registered for this activity
        is_registered = UserActivityRegistration.objects.filter(user=request.user, activity_id=activity_id).exists()

        if not is_registered:
            # Fetch user data from UserAccount
            user_data = get_object_or_404(UserAccount, user=request.user)

            # Create an entry in ActivityRegistration model
            activity_registration = ActivityRegistration(
                user=request.user,
                name_user=user_data.name,
                email=user_data.email,
                phone_number=user_data.phone,
                activity_id=activity_id
            )
            activity_registration.save()

            # Create an entry in UserActivityRegistration model
            user_activity_registration = UserActivityRegistration(
                user=request.user,
                activity_id=activity_id,
                name_user=user_data.name,
                email=user_data.email,
                phone_number=user_data.phone
                # Add other fields as needed
            )
            user_activity_registration.save()

            messages.success(request, "You have successfully registered for the activity!")
        else:
            messages.warning(request, "You are already registered for this activity.")

        return redirect('index')  # Redirect to the desired page after registration

    return HttpResponse("Method Not Allowed", status=405)
