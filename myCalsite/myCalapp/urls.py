from django.urls import path, include
from . import views

urlpatterns = [
    #path('<int:page>/', views.index),
    #path('month/<int:page>/', views.index), <--will be doing something like this
    path('', views.index),
    #path('events/', views.events_view),
]
