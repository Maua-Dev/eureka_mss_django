"""
URL configuration for eureka_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from app.views.delivery_views import DeliveryViews
from app.views.task_views import TaskViews
from app.views.project_views import ProjectViews
from app.views.user_views import UserViews

urlpatterns = [
    # TaskViews
    path('get_all_tasks', TaskViews.get_all_tasks, name='get_all_tasks'),
    
    # ProjectViews
    path('create_project', ProjectViews.create_project, name='create_project'),
    path('update_project', ProjectViews.update_project, name='update_project'),
    path('get_project', ProjectViews.get_project, name='get_project'),
    path('get_projects_by_role', ProjectViews.get_projects_by_role, name='get_projects_by_role'),
    
    # DeliveryViews
    path('create_delivery', DeliveryViews.create_delivery, name='create_delivery'),
    path('get_deliveries', DeliveryViews.get_deliveries, name='get_deliveries'),
    
    # UserViews
    path('get_all_students', UserViews.get_all_students, name='get_all_students'),
    path('get_all_professors', UserViews.get_all_professors, name='get_all_professors')
    
]
