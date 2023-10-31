from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name='login'),
    path("logout/", views.user_logout, name='logout'),

]

htmx_urlpatterns = [
    path('check-username/', views.check_username, name='check-username'),
    path('check-email/', views.check_email, name='check-email'),
    path('check-password/', views.check_password, name='check-password'),
]

urlpatterns += htmx_urlpatterns 
