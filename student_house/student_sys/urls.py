"""student_sys URL Configuration

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
import os
import sys
from django.contrib import admin
from django.urls import path
sys.path.append(os.path.dirname(sys.path[0]))
from student_house.student.views import index, IndexView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
]
