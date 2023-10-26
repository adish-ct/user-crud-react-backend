from django.urls import path
from .views import RegisterView, RetriveUserView, RetriveData

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("profile/", RetriveUserView.as_view()),
    path("data/", RetriveData.as_view()),
]
