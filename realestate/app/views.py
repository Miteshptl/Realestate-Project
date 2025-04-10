from django.shortcuts import render, redirect, HttpResponse,  get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Project, Upcoming, ProjectImage, UpcomingImage, Appointment
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta


# Create your views here.
def index(req):
    properties=Project.objects.all()
    up=Upcoming.objects.all()
    context={"properties":properties,"up":up}
    return render(req,"index.html",context)

def about(req):
    return render(req,"about.html")

def contact(req):
    return render(req,"contact.html")



def registered(request):
    projects = Project.objects.all()  # Retrieve all projects from the database
    return render(request, "registered.html", {"projects": projects})

# Display a list of all upcoming projects
def upcoming(request):
    upcoming_projects = Upcoming.objects.all()  # Retrieve all upcoming projects
    return render(request, "upcoming.html", {"upcoming_projects": upcoming_projects})

def projectpage(request, project_id):
    project = get_object_or_404(Project, project_id=project_id)
    # Fetch all images related to this project
    project_images = ProjectImage.objects.filter(project=project)
    return render(request, "projectpage.html", {
        "project": project,
        "project_images": project_images  # Pass the images to the template
    })

def upcomingdetail(request, upcoming_project_id):
    upcoming = get_object_or_404(Upcoming, upcoming_project_id=upcoming_project_id)
    # Fetch all images related to this upcoming project
    upcoming_images = UpcomingImage.objects.filter(upcoming_project=upcoming)
    return render(request, "upcomingdetail.html", {
        "upcoming": upcoming,
        "upcoming_images": upcoming_images  # Pass the images to the template
    })


def generate_time_slots():
    start_time = datetime.strptime('10:00 AM', '%I:%M %p')
    end_time = datetime.strptime('7:00 PM', '%I:%M %p')
    slots = []
    while start_time < end_time:
        slots.append(start_time.strftime('%I:%M %p'))  # Format time as 'HH:MM AM/PM'
        start_time += timedelta(hours=2)  # Increment by 2 hours
    return slots





from django.shortcuts import render
from datetime import datetime
from .models import Appointment  # Assuming you have an Appointment model

def book_appointment(req):
    time_slots = generate_time_slots()
    today = datetime.today()

    if req.method == 'POST':
        service_name = req.POST.get('service_name')
        service_description = req.POST.get('service_description')
        service_fee = req.POST.get('service_fee')
        appointment_date = req.POST.get('appointment_date')
        selected_time_slot = req.POST.get('time_slot')

        try:
            appointment_datetime = datetime.strptime(
                f"{appointment_date} {selected_time_slot}", 
                '%Y-%m-%d %I:%M %p'
            )
        except ValueError:
            # Invalid date/time format
            return render(req, 'book_appointment.html', {
                'time_slots': time_slots,
                'today': today,
                'error': "Invalid date or time format. Please try again.",
                'form_data': req.POST
            })

        appointment = Appointment(
            user=req.user,
            service_name=service_name,
            service_description=service_description,
            service_fee=service_fee,
            date=appointment_datetime,
            phone=req.POST.get('phone'),
            email=req.POST.get('email'),
            message=req.POST.get('message', ''),
        )
        appointment.save()
        req.session['appointment_id'] = appointment.id
        return render(req, 'book_success.html')

    return render(req, 'book_appointment.html', {
        'time_slots': time_slots,
        'today': today
    })


def success(request):
    appointment_id = request.session.get('appointment_id')
    appointment = None
    if appointment_id:
        appointment = Appointment.objects.filter(id=appointment_id).first()

    return render(request, 'book_uccess.html', {'appointment': appointment})


def user_appointments(req):
    appointments = Appointment.objects.filter(user=req.user) 
    return render(req, 'Appointments.html', {'appointments': appointments})


















def commercial(req):
    if req.method=="GET":
        allproducts=Upcoming.objects.filter(type_of_project__exact="Commercial")
        print(allproducts)
        context={'allproducts':allproducts}
        return render(req,'upcoming.html',context)
    else:
        allproducts=Project.objects.all()
        print(allproducts)
        context={'allproducts':allproducts}
        return render(req,'upcoming.html',context)

def residential(req):
    if req.method=="GET":
        allproducts=Upcoming.objects.all()
        # allproducts=Product.productmanager.electronics_list()
        allproducts=Upcoming.objects.filter(type_of_project__exact="Residential")
        print(allproducts)
        context={'allproducts':allproducts}
        return render(req,'upcoming.html',context)
    else:
        allproducts=Upcoming.objects.all()
        print(allproducts)
        context={'allproducts':allproducts}
        return render(req,'upcoming.html',context)
































































































































































































# def upcoming(req):
#     return render(req,"upcoming.html")

# def registered(req):
#     return render(req,"registered.html")

def validate_password(password):
    if len(password)<8:
        raise ValidationError("Password must be at least 8 characters long")
    if not any(char.isdigit() for char in password):
        raise ValidationError("Password must contain at least one digit")
    if not any(char.isupper() for char in password):
        raise ValidationError("Password must contain at least one uppercase letter")
    if not any(char.islower() for char in password):
        raise ValidationError("Password must contain at least one lowercase letter")
    if not any(char in ['!','@','#','$','%','^','&','*','(',')'] for char in password):
        raise ValidationError("Password must contain at least one special character")

# signup view to be created
#  signin view to be created 

def signup(req):
    print(req.method)
    context={}
    if req.method=="GET":
        return render(req,"signup.html")
    else:
        print(req.method)
        uname=req.POST.get("uname")
        upass=req.POST.get("upass")
        ucpass=req.POST.get("ucpass")
        print(uname,upass,ucpass)
        
        try:
            validate_password(upass)
        except ValidationError as e:
            context["error"]=str(e)
            return render(req,"signup.html",context)
        
        if uname=="" or upass=="" or ucpass=="":
            context["error"]="All fields are required"
            return render(req,"signup.html",context)
        elif upass!=ucpass:
            context["error"]="Passwords do not match"
            return render(req,"signup.html",context)
        elif uname.isdigit():
            context["error"]="Enter Valid Full Name"
            return render(req,"signup.html",context)
        elif upass == uname:
            context["error"]="Password cannot be same as Username"
            return render(req,"signup.html",context)
        else:
            try:
                userdata=User.objects.create(username=uname,password=upass)
                userdata.set_password(upass)
                userdata.save()
                print(User.objects.all())
                return redirect("signin")
            except:
                print("User already exists")
                context["error"]="Username already exists"
                return render(req,"signup.html",context)

        
def signin(req):
    if req.method=="POST":
        uname=req.POST.get("uname")
        upass=req.POST.get("upass")
        context={}
        print(uname,upass)
        if uname==""or upass=="":
            context["error"]="All fields are required"
            return render(req,"{% url 'signin' %}",context)
        else:
            userdata=authenticate(username=uname,password=upass)
            if userdata is not None:
                login(req,userdata)
                return redirect("/")
            else:
                context["error"]="Invalid credentials"
                return render(req,"signin.html",context)
    else:
        return render(req,"signin.html")

def userlogout(req):
    logout(req)
    return redirect("/")

def request_password_reset(req):
    if req.method=="GET":
        return render(req,"request_password_reset.html")
    else:
        uname=req.POST.get("uname")
        context={}
        try:
            userdata=User.objects.get(username=uname)
            return redirect("reset_password",uname=userdata.username)
        except User.DoesNotExist:
            context["error"]="User does not exist"
            return render(req,"request_password_reset.html",context)

def reset_password(req,uname):
    userdata=User.objects.get(username=uname)
    if req.method=="GET":
        return render(req,"reset_password.html",{"uname":uname})
    else:
        upass=req.POST.get("upass")
        ucpass=req.POST.get("ucpass")
        context={}
        userdata=User.objects.get(username=uname)
        try:
            if uname=="" or upass=="" or ucpass=="":
                context["error"]="All fields are required"
                return render(req,"reset_password.html",context)
            elif upass!=ucpass:
                context["error"]="Passwords do not match"
                return render(req,"reset_password.html",context)
            else:
                validate_password(upass)
                userdata.set_password(upass)
                userdata.save()
                return redirect("signin")
            
        except ValidationError as e:
            context["error"]=str(e)
            return render(req,"reset_password.html",context)