from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
  path('', home, name='home'),
  path('create-task/', create_task, name='create_task'),
  path('login/', login_user, name='login'),
  path('register/', register_user, name='register'),
  path('logout/', logout_user, name='logout'),
]