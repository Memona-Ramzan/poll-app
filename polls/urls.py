from django.urls import path
from . import views

urlpatterns = [
    path('', views.listining_ques,name="listining_ques"),
    path('voting', views.voting,name="voting"),
]