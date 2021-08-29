"""project_management_tst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#from django.conf.urls import url
from django.urls import path, include
from core import views

urlpatterns = [
    #path('project/', views.home, name='home'),
    
    path('getProjectList', views.ProjectList, name='listProject'),
    path('postProject/', views.ProjectPost, name='addProject'),
    path('putProject/<int:pk>/', views.ProjectPut, name='updProject'),
    path('delProject/<int:pk>/', views.ProjectDel, name='delProject'),
    
    path('', include('project_site.urls')),
   
]
