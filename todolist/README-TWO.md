# Todolist with AJAX 

## Perbedaan *asynchronous* dan *synchronous programming*
---

Secara umum, *synchronous* berarti operasi-operasi dikerjakan secara terurut. Artinya, pada *synchronous programming* komputer harus menunggu suatu operasi selesai untuk mulai menjalankan operasi berikutnya. Sedangkan *asynchronous* secara umum berarti operasi-operasi dapat dikerjakan secara tidak terurut. Artinya, pada *asynchronous programming* komputer tidak harus menunggu suatu operasi selesai untuk mulai menjalankan operasi berikutnya. Penerapan *asynchronous programming* pada sebuat website sangat tepat, karena user tidak perlu menunggu suatu operasi selesai untuk menjalankan operasi lainnya.

## Penerapan *Event-Driven Programming Paradigm*
---

Yang dimaksud dengan *Event-Driven Programming* adalah suatu paradima dalam pemrograman dimana operasi-operasi yang dijalankan berdasar pada suatu event yang terjadi. Beberapa contoh event yang dimaksud adalah "onClick", "onSubmit", dll. Event-event tersebut akan dihubungkan dengan sebuah fungsi yang akan dijalankan apabila event tersebut terjadi. 

Beberapa contoh penerapan *Event-Driven Programming* pada tugas ini adalah sebagai berikut.

1. On `#drawer-open-button` click
    ```js
    $('#drawer-open-button').click(() => {
      $('#drawer').removeClass('right-[-250px]')
      $('#drawer').addClass('right-0')
    })
    ```
    Pada kasus ini, saat button dengan id `drawer-open-button` di-click, fungsi tersebut akan dijalankan untuk memunculkan `#drawer` yang pada awalnya tersembunyi di kanan layar.

2. On `#drawer-close-button` click
    ```js
    $('#drawer-close-button').click(() => {
      $('#drawer').removeClass('right-0')
      $('#drawer').addClass('right-[-250px]')
    })
    ```
    Fungsi ini merupakan kebalikan dari `#drawer-open-button` yang berfungsi untuk kembali menyembunyikan `#drawer` ke sebelah kanan layar.

3. On `#new-task-open-button` click
    ```js
    $('#new-task-open-button').click(() => {
      $('#new-task-modal').removeClass('hidden')
      $('#drawer').removeClass('right-0')
      $('#drawer').addClass('right-[-250px]')
    })
    ```
    Pada saat button dengan id `new-task-open-button` di-click, `#new-task-modal` akan ditampilkan dan `#drawer` akan ditutup.

4. On `#new-task-close-button` click
    ```js
    $('#new-task-close-button').click(() => {
      $('#new-task-modal').addClass('hidden')
    })
    ```
    Fungsi ini merupakan kebalikan dari `#new-task-open-button` yang berfungsi untuk menyembunyikan `#new-task-modal` kembali.

5. On `#new-task-form` submit
    ```js
    $('#new-task-form').submit((e) => {
      e.preventDefault()
      $.ajax({
        ...
      })
    })
    ```
    Pada saat `#new-task-form` di-submit, fungsi tersebut akan mencegah laman web melakukan refresh dan melakukan AJAX call untuk membuat task baru.

## Penerapan *asynchronous programming* pada AJAX
---

Pada AJAX, *asynchronous programming* dilakukan pada pengiriman request. Pada saat AJAX request dilakukan, request tersebut akan berjalan di background sehingga user masih dapat melakukan operasi lain tanpa harus menunggu request tersebut selesai. Kemudian, setelah request tersebut berhasil dikirim dan berhasil mendapatkan respon, terdapat fungsi yang dihubungkan untuk menangani respon yang didapat.

## Implementasi checklist
---
- Membuat fungsi baru pada `views.py` untuk memperoleh data semua task dalam bentuk json dan menghubungkannya dengan url `/todolist/json`
- Mengganti bagian django template yang bertugas menampilkan semua tugas dengan AJAX get call yang dipanggil saat laman di-load.
- Membuat new task modal pada `todolist.html` dan menghubungkan sebuah fungsi ke tombol untuk memunculkan modal tersebut.
- Membuat fungsi baru pada `views.py` dan menghubungkannya dengan urls `/todolist/add` untuk membuat task baru.
- Membuat fungsi yang akan dijalankan saat new task form di-submit menggunakan AJAX secara *asynchronous*.
- Membuat fungsi yang akan dijalankan saat delete task di-click dan melakukan update pada laman web secara *asynchronous*.