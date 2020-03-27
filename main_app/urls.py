from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wish/add', views.WishCreate.as_view() , name="add_wish"),
    path('wish/delete/<int:wish_id>', views.delete_wish , name="delete_wish"),
]