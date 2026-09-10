from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


class Signup(CreateView):
    form_class=UserCreationForm
    template_name="signup.html"
    success_url="login"