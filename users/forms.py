from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

CATEGORY = (
    ('','Choose...'),
    ('EMP', 'Employer'),
    ('EME','Employee'), 
)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    category =forms.ChoiceField(choices=CATEGORY)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'category', 'password1', 'password2']