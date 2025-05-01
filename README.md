# Submission_Fundamental_Pemrosesan_Data
# ETL Pipeline - Fashion Product

Proyek ini adalah implementasi ETL (Extract, Transform, Load) pipeline sederhana yang mengambil data produk dari website [Fashion Studio Dicoding](https://fashion-studio.dicoding.dev/), membersihkan data, lalu menyimpan hasilnya ke Google Sheets API dan PostgreSQL.

---

## Cara Menjalankan ETL Pipeline
1. Pastikan semua dependency sudah terinstall dengan menjalankan:

    ```bash
    pip install -r requirements.txt
    ```

2. Jalankan pipeline ETL dengan perintah berikut:

    ```bash
    python main.py
    ```

---

## Cara Menjalankan Unit Test
Untuk memastikan semua fungsi berjalan dengan benar, jalankan unit test menggunakan perintah dibawah ini:

```bash
pytest tests/
```

Jika ingin melihat hasil lebih rinci, gunakan opsi perintah ini `-v`:

```bash
pytest tests/ -v
```

---

## Cara Menjalankan Test Coverage
Untuk memeriksa seberapa besar kode telah diuji oleh unit test, jalanakan perintah dibawah ini :

1. Jalankan test coverage:

    ```bash
    pytest tests/ --cov=tests --cov-report=term-missing
    ```

2. Hasilnya akan menampilkan persentase cakupan kode yang diuji di setiap file.

---

## 📄 Struktur Proyek
```
submit pemrosesan data/
 ├── .coverage
 ├── data_bersih.csv
 ├── main.py
 ├── project-pemrosesan-data-284-3ff50f58e05b.json
 ├── requirements.txt
 ├── susbmission.txt
 ├── tests
 │ ├── test_extract.py
 │ ├── test_load.py
 │ ├── test_transform.py
 │ ├── __pycache__
 │ │ ├── test_extract.cpython-313-pytest-8.3.5.pyc
 │ │ ├── test_load.cpython-313-pytest-8.3.5.pyc
 │ │ ├── test_transform.cpython-313-pytest-8.3.5.pyc
 ├── utils
 │ ├── extract.py
 │ ├── load.py
 │ ├── transform.py
 │ ├── __pycache__
 │ │ ├── extract.cpython-313.pyc
 │ │ ├── load.cpython-313.pyc
 │ │ ├── transform.cpython-313.pyc
```

---

## URL Google Sheets
Melihat hasil data yang sudah diekstrak dan dibersihkan di Google Sheets melalui tautan berikut:

[ini adalah hasil Google Sheets - scrapping_submission_pemrosesan_data](https://docs.google.com/spreadsheets/d/1iB08iXSlxkY_oG-sSGMUtQF-bTWJoXE41akyrZgPv2A)

---

✅ **Proyek ini telah melalui pengujian menyeluruh dengan cakupan (coverage) lebih dari 90% di semua unit test.**
![image](https://github.com/user-attachments/assets/d01dcc63-4edb-44ea-81cf-454800724493)
