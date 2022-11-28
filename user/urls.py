from django.urls import path
from .views import LoginView, RegisterView, SpecificUserView, UserView

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("register/", RegisterView.as_view()),
    path("user/", UserView.as_view()),
    path("user/<int:id>", SpecificUserView.as_view()),
]
