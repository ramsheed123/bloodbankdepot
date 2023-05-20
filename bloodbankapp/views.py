from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from .forms import RegistrationForm
from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Registration
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.http import HttpResponse


from datetime import datetime

@login_required(login_url='adminlogin')
def edit_registration_view(request, registration_id):
    registration = get_object_or_404(Registration, id=registration_id)

    if request.method == 'POST':
        # Update the contact with the new information
        registration.name = request.POST['name']
        registration.email = request.POST['email']
        registration.phone = request.POST['phone']
        registration.ward_numbers = request.POST['ward']

        # Handle the last_donation_date field
        last_donation_date = request.POST['last_donation_date']
        try:
            last_donation_date = datetime.strptime(last_donation_date, '%Y-%m-%d').date()
        except ValueError:
            # Handle the case where an invalid date format is entered
            return HttpResponse('Invalid date format')

        registration.last_donation_date = last_donation_date

        registration.weight = request.POST['weight']

        # Handle the dob field
        dob = request.POST['dob']
        try:
            dob = datetime.strptime(dob, '%Y-%m-%d').date()
        except ValueError:
            # Handle the case where an invalid date format is entered
            return HttpResponse('Invalid date format')

        registration.dob = dob

        registration.save()
        return redirect('admin-contact')
    else:
        context = {
            'registration': registration,
            'registration_id': registration_id,
        }
        return render(request, 'admin/edit_registration.html', context)



@login_required(login_url='adminlogin')
def delete_registration(request, registration_id):
    registration = get_object_or_404(Registration, id=registration_id)
    registration.delete()
    return redirect('admin-contact')

    
@login_required(login_url='/')
def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            gender = form.cleaned_data['gender']
            dob = form.cleaned_data['dob']
            weight = form.cleaned_data['weight']
            blood_group = form.cleaned_data['blood_group']
            
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            last_donation_date = form.cleaned_data['last_donation_date']
            ward_numbers = form.cleaned_data['ward_numbers']  # Get the value of ward_numbers from the form

            # Check conditions for specific fields
            errors = []

            if not name.isalpha():
                form.add_error('name', 'Name should only contain alphabetic characters.')

            if dob >= date.today():
                form.add_error('dob', 'Date of birth should be in the past.')

            if not weight.isnumeric() or not (50 <= int(weight) <= 150):
                form.add_error('weight', 'Weight should be a numeric value between 50 and 150.')

            try:
                validate_email(email)
            except ValidationError:
                form.add_error('email', 'Please enter a valid email address.')

            if not phone.isnumeric() or len(phone) != 10:
                form.add_error('phone', 'Phone number should be a 10-digit numeric value.')

            if Registration.objects.filter(phone=phone).exists():
                form.add_error('phone', 'This phone number is already registered.')

            if not form.errors:
                registration = form.save(commit=False)
                registration.last_donation_date = last_donation_date
                registration.ward_numbers = ward_numbers  # Set the value of ward_numbers for the registration
                registration.save()
                return redirect('registration_success')  # Redirect to the success page

    else:
        form = RegistrationForm()

    return render(request, 'index.html', {'form': form})

# Other views remain unchanged


# Other views remain unchanged





def registration_success(request):
    return render(request, 'registration_success.html')



@login_required(login_url='adminlogin')
def admin_contact_view(request):
    search_query = request.GET.get('search')
    blood_group_query = request.GET.get('blood_group')
    ward_query = request.GET.get('ward')

    registrations = Registration.objects.all()

    if search_query:
        registrations = registrations.filter(
            Q(name__icontains=search_query) |
            Q(ward_numbers__icontains=search_query) 
            
        )

    if blood_group_query:
        registrations = registrations.filter(blood_group=blood_group_query)

    if ward_query:
        registrations = registrations.filter(ward__icontains=ward_query)

    context = {
        'registrations': registrations,
        'search_query': search_query,
        'blood_group_query': blood_group_query,
        'ward_query': ward_query,
    }
    return render(request, 'admin/contact.html', context)




def admin_contact(request):
    # Get the data from the database.
    registrations = Registration.objects.all()

    # Render the admin contact.html page with the data.
    context = {'registrations': registrations}
    return render(request, 'admin/contact.html', context)

def adminclick_view(request):
    if request.user.is_authenticated:
        return redirect('admin-dashboard')
    return redirect('adminlogin')


def afterlogin_view(request):
    return redirect('admin-dashboard')


@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    registrations = Registration.objects.all().order_by('-id')  # Retrieve all registrations ordered by the latest ID
    context = {'registrations': registrations}
    return render(request, 'admin/dashboard.html', context)


def admin_404(request):
    return HttpResponseNotFound('<h1>Page not found</h1>')




  # Import the Contact model


def registration(request):
    if request.method == 'POST':
        # Get the form data
        name = request.POST['name']
        gender = request.POST['gender']
        dob = request.POST['dob']
        weight = request.POST['weight']
        blood_group = request.POST['blood_group']
        
        email = request.POST['email']
        phone = request.POST['phone']
        ward_numbers = request.POST['ward_numbers']
    
    

        # Create a new Registration object and save it to the database
        registration = Registration(
            name=name,
            gender=gender,
            dob=dob,
            weight=weight,
            blood_group=blood_group,
           
            email=email,
            phone=phone,
            ward_numbers=ward_numbers,
       
        )
        registration.save()

       

    else:
        # Render the registration form page
        return render(request, 'index.html')


