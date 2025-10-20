# CSV Reader — Pembaca CSV Otomatis

Aplikasi kecil untuk membaca file CSV dengan dua metode: menggunakan `pandas` atau modul standar `csv`.

**Bahasa**: Python

---

## Ringkasan

Proyek ini adalah skrip sederhana yang memperlihatkan dua cara membaca file CSV:

* `csv_pandas(tujuan, file)`: membaca CSV menggunakan `pandas.read_csv()` dan menampilkan `DataFrame`.
* `csv_csv(tujuan, file)`: membaca CSV menggunakan modul standar `csv` dan mencetak setiap baris sebagai string.

Skrip menampilkan menu sederhana untuk memilih cara pembacaan.

---

## Fitur

* Pilih antara pembacaan dengan `pandas` (lebih kuat, menampilkan tabel) atau modul `csv` bawaan (ringan, baris demi baris).
* Penanganan error dasar (directory tidak ada, file tidak ditemukan, exception saat membaca).

---

## Prasyarat

* Python 3.8+ (direkomendasikan)
* Paket `pandas` (hanya diperlukan jika menggunakan opsi 1)

Instal `pandas` bila belum ada:

```bash
pip install pandas
```

---

## Struktur proyek (contoh)

```
project-root/
├─ reader.py        # skrip utama (kode yang kamu kirimkan)
├─ README.md        # file dokumentasi ini
└─ data/
   └─ email.csv     # contoh file CSV
```

---

## Cara pakai

1. Siapkan file CSV (misal `email.csv`) di folder yang akan kamu gunakan, contoh di `D:\automationandscripting`.
2. Jalankan skrip:

```bash
python reader.py
```

3. Ikuti instruksi: pilih `1` untuk membaca dengan `pandas` atau `2` untuk membaca dengan `csv`.

Contoh input ketika diminta:

```
Jadi mau pilih mana?(1/2): 1
```

---

## Contoh `email.csv` sederhana

```
email,name
alice@example.com,Alice
bob@example.com,Bob
```

Catatan: Gunakan encoding UTF-8 jika memungkinkan.

---

## Penjelasan singkat fungsi

* `csv_pandas(tujuan, file)`:

  * Mengecek apakah direktori `tujuan` ada.
  * Menggabungkan path dan memanggil `pd.read_csv()`.
  * Mencetak `DataFrame` ke console.

* `csv_csv(tujuan, file)`:

  * Mengecek apakah direktori `tujuan` ada.
  * Membuka file dengan encoding `utf-8` dan menggunakan `csv.reader`.
  * Mencetak setiap baris (menggabungkan kolom dengan `, `).

---

## Saran perbaikan / fitur tambahan

* Validasi path dan proteksi agar tidak menunjuk ke direktori berbahaya.
* Menambahkan argumen baris perintah (CLI) menggunakan `argparse` untuk fleksibilitas.
* Menambahkan opsi `--delimiter` untuk mendukung delimiter lain (mis. `;`).
* Menambahkan logging (modul `logging`) alih-alih `print` untuk penggunaan produksi.
* Menambahkan unit test untuk kedua fungsi.
* Memeriksa encoding file dan mencoba fallback (`latin-1`) bila `utf-8` gagal.

---

## Keamanan

Jangan jalankan skrip yang memodifikasi atau menghapus file penting sistem. Pastikan direktori tujuan hanya berisi file data yang aman.

---

## Kontribusi

Jika ingin menyumbang perbaikan, ajukan pull request atau buka issue dengan penjelasan singkat.

---

## Lisensi

MIT License. Silakan gunakan dan modifikasi sesuai kebutuhan.

---

## Kontak

Jika butuh penjelasan lebih lanjut atau mau ditambahkan fitur tertentu, beri tahu aku dan aku bantu modifikasi README atau kodenya.
