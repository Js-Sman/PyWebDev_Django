from django.urls import path
from . import views  # Nötig um von hier aus auf die verschiedenen views zu routen


urlpatterns = [
    path('quadratzahlen/<str:base_number>', views.quadratzahlen, name="quadratzahlen"),
]