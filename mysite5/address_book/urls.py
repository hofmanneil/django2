from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>',views.display_contact, name='contact'),
    path('person_list',views.create_contact, name='new_contact'),


]
