from django.urls import path
from .views import HomePage
app_name = "intro"
urlpatterns = [
    path('',HomePage.as_view(),name = 'intro')
]