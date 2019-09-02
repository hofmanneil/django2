from django.shortcuts import render

# view to signup
#view to login
def login_view(request):
     return render(request,'accounts/login.html')               #request = the request   templates/login   where i am finding it

#Change your Template to have a form
#when submitting make sure catch data
#https://docs.djangoproject.com


def signup_view(request):
    return render(request,'signup/login.html')
