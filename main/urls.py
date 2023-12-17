from django.urls import path

from main import views
from django.contrib import admin
urlpatterns = [
    path('', views.index, name='home'),
    path('clubs', views.clubs, name='clubs'),
    path('participants', views.participants, name='participants'),
    path('rings', views.rings, name='rings'),
    path('experts', views.experts, name='experts'),
    path('participants/<int:pk>', views.ParticipantReport.as_view(), name='participantreport'),
    path('clubs/<int:pk>', views.clubReport, name='clubreport'),
]