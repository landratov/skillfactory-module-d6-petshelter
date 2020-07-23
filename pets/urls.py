from django.urls import path

from .views import PetList, PetDetail, Index, Contacts

app_name = 'pets'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('pets/', PetList.as_view(), name='pets'),
    path('pets/<str:pk>', PetDetail.as_view(), name='pet_detail'),
    path('contacts/', Contacts.as_view(), name='contacts')
]