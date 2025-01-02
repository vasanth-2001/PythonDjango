from django.shortcuts import render
from .models import UserProfile
from .forms import Profileform
from django.views.generic.edit import CreateView

# Create your views here.
class ProfileCreateView(CreateView):
    model=UserProfile
    template_name="profile/createprofile.html"
    fields="__all__"