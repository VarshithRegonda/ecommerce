from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about_page/',views.about_page,name="about_page"),
    path('content_page/',views.content_page,name="content_page"),
    path('login/',views.login_page,name='login_apge'),
    path('Register',views.register_page,name='register')
]