from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList

def show_html(request):
  all_data = MyWatchList.objects.all()
  cnt_watched = 0
  for data in all_data:
    if data.watched: cnt_watched += 1
  cnt_not_watched = len(all_data) - cnt_watched
  context = {
    'watchlist': all_data,
    'watched_many': (cnt_watched > cnt_not_watched),
    'name': 'Daniel Christian Mandolang',
    'npm': '2106630006',
  }
  return render(request, 'mywatchlist.html', context)

def show_xml(request):
  all_data = MyWatchList.objects.all()
  return HttpResponse(serializers.serialize('xml',all_data), content_type='application/xml')

def show_json(request):
  all_data = MyWatchList.objects.all()
  return HttpResponse(serializers.serialize('json',all_data), content_type='application/json')

def check_watched(request, id):
  movie = MyWatchList.objects.get(pk=id)
  movie.watched = not movie.watched
  movie.save()
  return redirect('mywatchlist:show_html')