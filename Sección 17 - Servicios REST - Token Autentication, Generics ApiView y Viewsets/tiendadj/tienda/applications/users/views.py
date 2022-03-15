from django.shortcuts import render

# 
# Django import
from django.views.generic import TemplateView

class LoginUser(TemplateView): 
    template_name = "users/login.html"
    