from django.urls import path
from watermeter  import views

urlpatterns = [
       path('', views.index, name="index"),

]
