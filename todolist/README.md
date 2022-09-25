# Todolist

Untuk mengakses aplikasi klik di [sini](https://pbp-tugas2-daniel.herokuapp.com/todolist/)

#### Akun dummy:
- Username: `dummy1`, Password: `pass12345`
- Username: `dummy2`, Password: `pass12345`

### Apa kegunaan `{% csrf_token %}` pada element `<form>`?
- CSRF (kependekan dari Cross-Site Request Forgery) adalah suatu serangan sederhana terhadap suatu web. Untuk mencegah serangan tersebut, dikembangkanlah CSRF Token yang berfungsi sebagai validator dari suatu HTTP Request. Suatu request akan diproses jika dan hanya jika request tersebut memiliki token yang valid.

### Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
- Sesuai fungsinya, CSRF Token merupakan token yang digunakan oleh server untuk mengenali apakah suatu request meruapakan serangan CSRF atau bukan. Oleh karena itu, tanpa adanya CSRF Token, request yang dikirimkan akan dianggap dianggap sebagai suatu serangan oleh server, sehingga request tersebut akan ditolak.

### Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? 
- Tags `<form>` meruapakan tags pada HTML yang dapat digunakan untuk menerima dan mengumpulkan data dari pengguna. Adapun generator seperti `{{ form.as_table }}` hanyalah fasilitas yang dimiliki Django Template Language untuk membentuk form dalam bentuk tabel. Oleh karena itu, tentu saja elemen `<form>` dapat dibuat secara manual.

### Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
- Buat class `Form` pada `models.py` yang digenerate langsung dari model yang terkait.
- Buat tags `<form>` pada `template.html` dengan method `POST` dan action merujuk ke suatu route, kemudian implementasikan fungsi pada `views.py` untuk men-*handle* request tersebut.
- Letakan semua komponen input di dalam tags `<form>`.
- Pada fungsi views, dapatkan data input yang dimasukkan ke dalam form dengan membuat instance `Form` dari `request.POST` yang diterima.

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
- Data yang di-input user akan diterima dan diatur oleh tags `<form>` pada perangkat client.
- Saat user men-*trigger* input yang bertipe `"submit"`, client akan mengirim request `POST` ke server sesuai route yang terhubung pada atribut `action` dari form tersebut.
- Seperti biasa, request yang diterima akan di-*parse* dan di-*handle* oleh fungsi views yang bersesuaian.
- Data yang diterima dari form dapat diakses oleh server dengan mengkonversi data tersebut menjadi sebuah instance `Form`.
- Data tersebut kemudian digunakan untuk membuat sebuah instance baru dari suatu model yang ada, kemudian disimpan ke database.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Buat sebuah aplikasi `todolist` dengan menjalankan perintah `python3 manage.py startapp todolist`, kemudian daftarkan aplikasi tersebut pada `project-django/settings.py` dan `project_django/urls.py`.
- Buat class `Task` pada `todolist/models.py`, kemudian buat route-route pada `todolist/urls.py` beserta dengan fungsi-fungsi yang bersesuaian pada `todolist/views.py`.
- Buat template untuk page-page yang diperlukan pada `todolist/templates/`.
- Kaitkan fungsi pada `todolist/views.py` dengan model `User` yang sudah disediakan Django.
- Atur halaman `login` dan `register`, kemudian kunci halaman `/todolist/` dan `/todolist/create-task` agar hanya dapat diakses oleh user yang sudah login.
- Tambahkan sebuah `BooleanField` pada `Task`, kemudian tambahkan 3 kolom pada `todolist/templates/todolist.html` untuk menampilkan status pengerjaan sebuah task, menandai suatu task sudah dikerjakan, dan menghapus suatu task.
- Buat route dan fungsi yang sesuai untuk menandai dan menghapus suatu task, kemudian hubungkan dengan tombol pada template.