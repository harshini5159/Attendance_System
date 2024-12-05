"""
URL configuration for demoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import  settings
from django.contrib import admin
from django.urls import path
from Authentication.views import login_page,signup,home,logout_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_page,name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',logout_page,name='logout'),

    path('home/',home,name="home"),
    # path('hello/',demo,name="demo"),
    # path('project/',home1,name="project"),
]

urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)