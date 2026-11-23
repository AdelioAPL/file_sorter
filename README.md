# 📁 File Sorter Automation

Proyek otomasi sederhana menggunakan Python untuk merapikan file berdasarkan kategorinya secara otomatis.

---

## Struktur Folder

```text
file-sorter-automation/
├── file_sorter.py          # Skrip utama untuk merapikan file
├── create_dummy_files.py   # Skrip untuk membuat file contoh untuk pengujian aman
├── test_folder/            # Folder simulasi uji coba (dibuat otomatis)
└── README.md
```

---

## Cara Menjalankan

### 1. Buat File Simulasi (Uji Coba Aman)
Jalankan perintah ini di terminal:
```bash
python3 create_dummy_files.py
```
Ini akan membuat folder `test_folder/` berisi berbagai jenis file simulasi (`.pdf`, `.jpg`, `.mp4`, `.zip`, dll).

### 2. Jalankan Skrip Otomasi
```bash
python3 file_sorter.py
```
Semua file di `test_folder/` akan otomatis terkelompokkan ke dalam subfolder (`Dokumen`, `Gambar`, `Video`, dsb).

---

## Menerapkannya ke Folder Downloads Asli
Buka [file_sorter.py](file:///home/adelio-lio/file-sorter-automation/file_sorter.py) lalu ubah:
```python
TARGET_DIR = BASE_DIR / "test_folder"
```
Menjadi:
```python
TARGET_DIR = Path.home() / "Downloads"
```
