"""WebDev_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

"""
Das hier ist die Hauptseite. Von hier aus wird auf alle anderen Applikationen geroutet.
Die URL's die hier im path() angegeben werden, führen zu der URL datei der entsprechenden Applikation.
"""
urlpatterns = [
    path('demo/', include('PyWebDev_DemoApplikation.urls')),
    path("admin/", admin.site.urls),
    path("accounts/", include('django.contrib.auth.urls')),

]
