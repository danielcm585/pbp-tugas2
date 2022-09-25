from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
  path('', home, name='home'),
  path('create-task/', create_task, name='create_task'),
  path('create/', create, name='create'),
  path('mark-done/<int:id>', mark_done, name='mark_done'),
  path('delete/<int:id>', delete, name='delete'),
  path('login/', login_user, name='login'),
  path('register/', register_user, name='register'),
  path('logout/', logout_user, name='logout'),
]