from django.urls import path
from .views import ResisterView, UserView

urlpatterns = [
    path('resiter/', ResisterView.as_view()),
    path('user/', UserView.as_view()),
]