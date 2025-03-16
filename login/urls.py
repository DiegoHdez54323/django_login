from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('menu/', menu_view, name='menu'),
    path('add_user/', add_user_view, name='add_user'),
    path('delete_user/<int:user_id>/', delete_user_view, name='delete_user'),
    path('edit_user/', edit_user_view, name='edit_user'),
    path('logout/', logout_view, name='logout'),

]
