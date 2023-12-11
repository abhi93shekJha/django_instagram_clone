from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={
            "placeholder": "Provide your name",
            "class": "input-fields"
        }
    ), label="Name")
    
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(
        attrs={
            "placeholder": "Provide your email",
            "class": "input-fields"
        }
    ), label="Email")
    
    password = forms.CharField(required=True, widget=forms.widgets.PasswordInput(
        attrs={
            "placeholder": "Provide your password",
            "class": "input-fields"
        }
    ), label="Password")
    
    # this class will automatically use the fields inside User model
    # and show it as form input (we can use this field in html)
    # so above we have used name and email from User, below with 'exclude' keyword
    # we have excluded few fields
    # We have not excluded phone_number which will be shown in form input
    class Meta:
        model = User
        exclude = ('created_on', 'updated_on', 'is_active', )