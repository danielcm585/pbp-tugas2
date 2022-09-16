from django.urls import path
from mywatchlist.views import *

app_name = 'mywatchlist'

urlpatterns = [
  path('html/', show_html, name='show_html'),
  path('xml/', show_xml, name='show_xml'),
  path('json/', show_json, name='show_json'),
  path('check/<int:id>', check_watched, name='check_watched'),
]