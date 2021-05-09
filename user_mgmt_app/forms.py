from django.forms import ModelForm
from user_mgmt_app.models import Registered_users

class RegisterForm(ModelForm):
   class Meta:
       model = Registered_users
       fields = ['username', 'email']