from django.contrib import admin
from django.urls import path
from .views import TaslViewSet
urlpatterns = [
    path('', TaslViewSet.as_view({'get':'list','post':'create'})),
    path('<int:pk>/', TaslViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
]