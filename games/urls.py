from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/',views.play,name='play'),
    path('guess/',views.guess,name='guess'),
]
