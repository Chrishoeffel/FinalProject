from django.urls import path
from . import views

app_name ='cal'
urlpatterns = [
    path('', views.index, name='index'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<int:pk>/', views.event, name='event_edit'),
]
