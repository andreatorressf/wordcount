
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home),
   path('countthewords/',views.count,  name='count'),
  
]
