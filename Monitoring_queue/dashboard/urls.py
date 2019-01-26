from django.urls import path
from . import views

urlpatterns = [     
    path('', views.index, name='index'),    
    path('<int:queue_name>/', views.detail, name='detail'),    
    path('<int:queue_name>/results/', views.results, name='results'),    
    path('<int:queue_name>/vote/', views.vote, name='vote'),
]