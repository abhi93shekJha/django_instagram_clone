from django.http import HttpResponse
from django.shortcuts import render
from .models import User, UserProfile
from .forms import RegistrationForm

# Views will contain the business logics, i.e. methods
def index(request):
    # this function receives HttpRequest object
    # this object contains the information about the request,
    # a web browser sends these information,
    # or we send it from postman
    
    # http://127.0.0.1:8000/users/index/?q1=Ak&q2=Kumar%20Jha
    # %20 for space

    all_params = request.GET
    message = f"{all_params['q1'] + ' '  + all_params['q2']}"
    
    q1 = request.GET.get('q1', 'default_val')
    q3 = request.GET.get('q3', 'default_val')
    
    message = message + ' ' + q1 + ' ' + q3 
    
    return HttpResponse(message)

# http://127.0.0.1:8000/users/index?q="Ak"&q="Kumar%2Jha"
# above one will have a list in q

def home_page(request):
    # gets out the first row
    user_data = User.objects.all()
    return render(request, 'users/home.html', {"data":user_data})


def register(request):
    form = RegistrationForm()
    errors = []
    message = ""
    
    if request.method == "POST":
        # this line will directly get in the inputs in a form object
        form = RegistrationForm(request.POST)
        # below line will automatically validata, according the created model object (ex.-max_length, not null etc)
        if form.is_valid():
            user = form.save(commit=False) # do not save the data directly to database, b/c of commit=False
            user.save()   # this will save to DB
            message = "New use created!!"
        else:
            errors = form.errors
            
    context = {
        'form': form,
        'errors': errors,
        'message': message
    }
    return render(request, 'users/registration.html', context)
