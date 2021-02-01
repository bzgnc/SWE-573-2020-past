from django.urls import path
from reddimental import views
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('analyze_sentiment/', views.analyze_sentiment, name="analyze_sentiment"),
    path('accounts/', include('accounts.urls'))
]

