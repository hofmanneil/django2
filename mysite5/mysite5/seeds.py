from faker import Faker
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "address_book.settings")
django.setup()

from address_book.models import Person

def create_new_contact(fake):
    contact,created =Person.objects.get_or_create(
    email=fake.email_address(),
    defaults={
    'first_name' : fake.first_name(),
    'last_name' : fake.last_name(),
    'phone_number' : fake.phone_number(),
    },
    )
return created

def generate_contacts(number_of_contacts):
    fake=Faker()
    for i in range(number_of_contacts):
        create_new_contact(fake)



generate_contacts(100)
