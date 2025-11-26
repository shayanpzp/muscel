# workout/urls.py
from django.urls import path
from . import views

app_name = "workout"

urlpatterns = [
    path("", views.home, name="home"),
    path("questionnaire/", views.questionnaire, name="questionnaire"),
    path("bmi-result/", views.bmi_result, name="bmi_result"),
    path("choose-program/", views.choose_program, name="choose_program"),
    path("price/", views.price, name="price"),
]