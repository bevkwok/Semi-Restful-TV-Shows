from django.urls import path
from . import views
urlpatterns = [
    path('shows', views.shows),
    path('shows/new', views.new_show),
    path('shows/create', views.create_show),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('update_show', views.update_show),
    path('shows/<int:show_id>', views.display_show),
]