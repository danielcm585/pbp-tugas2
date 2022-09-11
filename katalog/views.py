from django.shortcuts import render
from katalog.models import CatalogItem


def show_katalog(request):
  data_katalog = CatalogItem.objects.all()
  context = {
    'list_katalog': data_katalog,
    'nama': 'Daniel Christian Mandolang',
    'npm': '2106630006',
  }
  return render(request, 'katalog.html', context)