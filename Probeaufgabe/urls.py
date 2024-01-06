from django.urls import path

from . import views
from . views import probe_view_funktion

urlpatterns = [
    path('', views.probe_view_funktion, name="probe_view_funktion"),
    path('newstudent', views.new_student, name="new_student")

]