from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:pk>', views.one_listing, name='listing'),
    path('search', views.search, name='search')
]