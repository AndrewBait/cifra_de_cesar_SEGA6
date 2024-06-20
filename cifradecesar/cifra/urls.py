from django.urls import path
from .views import CifraView

urlpatterns = [
    path('', CifraView.as_view(), name='cifra'),
]
