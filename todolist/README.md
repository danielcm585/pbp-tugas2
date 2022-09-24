### Apa kegunaan `{% csrf_token %}` pada element `<form>`?
- CSRF (kependekan dari Cross-Site Request Forgery) adalah suatu serangan sederhana terhadap suatu web. Untuk mencegah serangan tersebut, dikembangkanlah CSRF Token yang berfungsi sebagai validator dari suatu HTTP Request. Suatu request akan diproses jika dan hanya jika request tersebut memiliki token yang valid.

### Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
- Sesuai fungsinya, CSRF Token merupakan token yang digunakan oleh server untuk mengenali apakah suatu request meruapakan serangan CSRF atau bukan. Oleh karena itu, tanpa adanya CSRF Token, request yang dikirimkan akan dianggap dianggap sebagai suatu serangan oleh server, sehingga request tersebut akan ditolak.

### Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? 
- Tags `<form>` meruapakan tags pada HTML yang dapat digunakan untuk menerima dan mengumpulkan data dari pengguna. Adapun generator seperti `{{ form.as_table }}` hanyalah fasilitas yang dimiliki Django Template Language untuk membentuk form dalam bentuk tabel. Oleh karena itu, tentu saja elemen `<form>` dapat dibuat secara manual.

### Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
- 

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
- 

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- 