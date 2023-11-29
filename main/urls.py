from django.urls import path
from main import views


urlpatterns = [
    path('', views.main_page, name='main'),
    path('home/', views.home_view, name='home'),
    path('list/', views.list_view, name='list'),
    path('listing/<str:id>/', views.listing_view, name='listing'),
    path('listing/<str:id>/edit', views.edit_view, name='edit'),
    path('listing/<str:id>/like', views.like_listing_view, name='like_listing'),
    path('listing/<str:id>/enquire', views.enquire_listing_using_email, name='enquire_listing'),
]
