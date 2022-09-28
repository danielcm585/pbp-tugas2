release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json && python manage.py loaddata initial_watchlist_data.json && python manage.py tailwind build'

web: gunicorn p\roject_django.wsgi --log-file -
