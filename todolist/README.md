# Todolist Style (CSS)

### Apa perbedaan inline, internal, dan external CSS?
Perbedaan utama dari ketiga CSS tersebut adalah penempatan CSS style pada template. Pada inline CSS, stylesheet ditempatkan langsung pada tags ditargetkan. Pada internal CSS, stylesheet masih ditempatkan pada file `.html` namun diletakkan pada tags `<style>`. Pada external CSS, stylesheet ditulis pada file `.css` yang terpisah dari file html dan dikoneksikan menggunakan tags `<link>`. 

Masing-masing penempatan memiliki kelebihan dan kekurangan masing-masing. Inline CSS membuat file html menjadi panjang dan sulit, internal CSS relatif lebih baik dan rapi dibandingkan inline CSS, namun file html tetap panjang. Sedangkan pada external CSS, stylesheet berada pada file terpisah yang membuat file html lebih pendek dan mudah dibaca.

### Jelaskan tags HTML5!
- `<p>...</p>` merupakan tags untuk membentuk sebuah paragraph pada laman web.
- `<h1>...</h1>`, `<h2>...</h2>`, dsb merupakan tags yang digunakan untuk membentuk judul atau header.
- `<b>...</b>` merupakan tags untuk menebalkan font (bold).
- `<i>...</i>` merupakan tags untuk memiringkan font (italic).
- `<u>...</u>` merupakan tags untuk menggarisbawah font (underline).
- `<nav>...</nav>` merupakan tags yang digunakan untuk membuat navigation bar.
- `<div>...</div>` merupakan tags untuk mengemas beberapa elemen menjadi sebuah section atau division.
- `<input>` merupakan tags untuk membuat sebuah field yang dapat menerima input user.
- `<form>...</form>` merupakan tags untuk mengemas beberapa input menjadi sebuah form.
- `<a>...</a>` merupakan tags untuk membuat link ke laman lain, dsb.

### Jelaskan tipe-tipe CSS selector!
- `tags { ... }` merupakan selector terhadap semua tags dengan jenis yang ditargetkan.
- `.class { ... }` merupakan selector berdasarkan class untuk mentargetkan beberapa section dengan class yang bersesuaian.
- `#id { ... }` merupakan selector berdasarkan id untuk mentargetkan beberapa section dengan id yang bersesuaian.

### Implementasi checklist
- Setup tailwind css pada django dengan menggunakan module `django-tailwind` dengan mengikuti langkah-langkah [di sini](https://django-tailwind.readthedocs.io/en/latest/installation.html).
- Menerapkan kustomisasi style pada tags-tags html pada django template menggunakan tailwind untuk menciptakan design laman website yang menarik.
- Menambahkan class dengan tipe `hover:...` untuk menciptakan efek khusus saat suatu section di-*hover* oleh mouse.
- Menambahkan class dengan tipe `md:...`, `lg:...`, dsb untuk menciptakan laman website yang responsive terhadap ukuran layar.