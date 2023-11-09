from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('analysis/', views.analysis, name='analysis'),
    path('predictions/', views.predictions, name='predictions'),
    path('<pk>/', views.object_chart, name='chart'),
     path('<pk>/chart/', views.object_chart_js, name='js-chart'),
    path('delete/<pk>/', views.delete, name='delete'),

]




