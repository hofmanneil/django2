from django.shortcuts import render
from django.http import HttpResponse
from address_book.models import Person
from address_book.models import Buildings
from django.contrib import messages
from django.shortcuts import redirect


def index(request):
    person_list = Person.objects.all()
    print(person_list)
    html_data=render(request,'index.html',{'contacts':person_list})
    return html_data

def index2(request):
    building_list = Buildings.objects.all()
    print(building_list)
    html_data2=render(request,'index.html',{'buildings':building_list})
    return html_data2

def display_contact(request,contact_id):
    return render(
        request,
        'contact.html',
        {'contact':Person.objects.get(pk=contact_id) }
    )
def create_contact(request):
    print('hello')
    if request.method =='POST':
        contact, created = Person.objects.get_or_create(
        email = request.POST.get('email_address'),
        defaults={
            'first_name' : request.POST.get('first_name'),
            'last_name' : request.POST.get('last_name'),
            'phone_number' : request.POST.get('phone_number'),
          },
        )

        if not created:
            message.error(request,"User alraedy exists ")
        else:
            return redirect('index')

# Instead of using get()
    #    if Person.objects.get(email_address=email):
        #    messages.error(request,"contact already exists!!")
        #    pass
        #else:
        #    contact=Person.objects.create(
        #    f
        #)


    return render(request,'new_contact.html')    #return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

    #render(request, 'myapp/index.html', {
    #    'foo': 'bar',
    #}, content_type='application/xhtml+xml')

    #<a href={% url 'new_contact' create_contact %} >
