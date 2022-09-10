# Katalog

To visit app click [here](https://pbp-tugas2-daniel.herokuapp.com/katalog/)

## Bagan

---

![Bagan](../static/bagan.png?raw=true)
- HTTP request dibuat oleh user.
- Route dari request user akan di-parsing oleh `urls.py` sesuai dengan `urlspattern` yang ada.
- Fungsi akan dijalankan sesuai dengan route yang diberikan user.
- Fungsi akan terhubung dengan `models.py` yang terkait.
- `models.py` akan melakukan query ke Database Management System yang digunakan dan mendapatkan data yang diinginkan.
- Fungsi akan mengembalikan data yang didapat dalam bentuk `.html` sesuai template kepada user.
- File `.html` tersebut akan ditampilkan kepada user sebagai respon dari server.

## Virtual Environment

---

Virtual environment merupakan suatu development environment yang digunakan django untuk memisahkan satu project dengan project lain. Suatu project seringkali memiliki dependencies yang berbeda dengan project lain, pada kasus inilah virtual environment mampu membantu proses pengembangan.

### Mengapa menggunakan virtual environment?

Virtual environment digunakan untuk me-manage Python packages untuk project-project berbeda. Virtual environment dapat mencegah suatu Python package berlaku secara global yang berpotensi menciptakan konflik antar satu program dengan program lain.

### Apakah kita dapat membuat aplikasi Django tanpa virtual environment?

Tentu saja kita tetap dapat membuat aplikasi Django tanpa virtual environment. Namun implementasi seperti ini tidak baik, karena tanpa virtual environment dependencies suatu project diinstall secara global dan berpotensi menciptakan konflik antar satu project dengan project lain.

## Implementasi

---

### Langkah 1

Membuat sebuah fungsi bernama `show_katalog(request)` pada file `katalog/views.py`. Fungsi tersebut menerima request dari user sebagai parameter, kemudian membuat query untuk meminta semua data dari `CatalogItem`. Fungsi kemudian mengembalikan semua data yang didapatkan melalui `katalog/template/katalog.html` dengan `context` yang sesuai.

### Langkah 2

Membuat sebuah `urlpatterns` baru untuk aplikasi `katalog` pada file `katalog/urls.py`. Cantumkan route `'' (root)` yang dihubungkan ke fungsi `show_katalog(request)` pada `katalog/views.py`. Kemudian cantumkan semua route milik aplikasi `katalog` pada `urlpatterns` milik `urls.py`.

### Langkah 3

Sebelum memetakan data ke template, perlu melakukan migration dengan menjalankan perintah `python3 manage.py makemigrations` dan `python3 manage.py migrate` untuk menyesuaikan model dengan table pada database. Kemudian menginput data dummy ke database dengan menjalankan perintah `python3 manage.py loaddata initial_catalog_data.json`

Membuat file `katalog/templates/katalog.html` yang akan bertugas sebagai template yang menampilkan respon dari fungsi `show_katalog(request)` yang berisi data yang diminta. Data tersebut kemudian diakses dan ditampilkan dengan notasi `{{<nama_variabel>}}` pada `katalog/templates/katalog.html`.

### Langkah 4

Membuat file `Procfile` yang berisi command yang harus dijalankan untuk melakukan build dan `.github/workflows/dpt.yml` yang berisi konfigurasi untuk deployment pada heroku.

### Langkah Bonus

Membuat sebuah file `katalog/static/css/style.css` yang bertugas untuk mengatur styling yang akan diaplikasikan pada `katalog/templates/katalog.html`.

Membuat sebuah unit test pada `katalog/test.py` untuk melakukan pengetesan pada `___`, `___`, dan `___`.