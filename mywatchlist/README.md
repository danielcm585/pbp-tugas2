# Watchlist

To access the app click [here](https://pbp-tugas2-daniel.herokuapp.com/mywatchlist/html)

## Difference between JSON, XML, and HTML
---

JSON, XML, and HTML are some formats that are used in Django to represent the response to the user. HTML responses show datas by rendering it in a browser, while XML and JSON are *self-descriptive* language to represent datas to the users.

### XML 

XML stands for *eXtensible Markup Language*. XML format uses tags that are similar to tags that HTML use. The datas will provide the data information inside the specified tags.

XML format example:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<shoe>
  <size>42</size>
  <brand>Nike</brand>
  <type>Air Force 1</type>
  <colorway>Triple White</colorway>
</shoe>
```

### JSON 

JSON stands for *JavaScript Object Notation*. JSON format is the format Javascript actually use to represent objects. It is also similary to Python's dictionary notation.

JSON format example:
```json
"shoe": {
  "size": 42,
  "brand": "Nike",
  "type": "Air Force 1",
  "colorway": "Triple White"
}
```

### HTML

HTML stands for *HyperText Markup Language*. It is a markup language that is used to be rendered in browsers. HTML is commonly used along with CSS to style those HTML tags.

## Data Delivery in Platform Based Programming
---

Data delivery in platform based programming is used to communicate between client and server. Clients can send their requests to the server using any kind of devices such as mobile, tablet, or desktop devices. The request sent in either JSON or XML format. The server will accept the requests and send responses based on the request made by the client. The response will also be sent in either JSON, XML, or HTML format.

## Implementation
---

### Initialization

- Create a virtual environment using `python3 -m venv env`.
- Run the virtual environment using `source env/bin/activate`.
- Install all requirements using `pip install -r requirements.txt`.

### Create New App

- Create `mywatchlist` app using `python manage.py startapp mywatchlist`.
- Include `'mywatchlist'` to the `INSTALLED_APPS` in `project_django/settings.py`.

### Configure Routes

- Add `path('mywatchlist', include('mywatchlist.urls'))` to `urlpatters` in `project_django/urls`.
- Add more routes to `mywatchlist/urls.py` to get HTML, XML, or JSON requests.
- Create functions in `mywatchlist/views.py` to handle those routes and connect them to the routes.

### Create Model

- Create a model called `MyWatchList` in `mywatchlist/models.py`.
- Put some data fields with the precise data type to the class containing the required information.
- Make migration using `python3 manage.py makemigrations mywatchlist` and then `python3 manage.py migrate mywatchlist`.
- Create `mywatchlist/fixtures/initial_watchlist_data.json` containing initial data to load.
- Load the initial data using `python3 manage.py loaddata initial_watchlist_data.json`.

## Testing
---

Testing the application via Postman. The screenshots below show the result of the tests.

- [HTML](https://pbp-tugas2-daniel.herokuapp.com/mywatchlist/html)
![HTML](../static/html.png?raw=true)
- [XML](https://pbp-tugas2-daniel.herokuapp.com/mywatchlist/xml)
![XML](../static/xml.png?raw=true)
- [JSON](https://pbp-tugas2-daniel.herokuapp.com/mywatchlist/json)
![JSON](../static/json.png?raw=true)