from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('teamcreate/',views.teamcreate),
    # path('join/',views.join),
]