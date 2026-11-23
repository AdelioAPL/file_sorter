import os
import shutil
from pathlib import Path

# Folder yang ingin dirapikan
# Secara default diarahkan ke folder 'test_folder' di dalam proyek ini agar aman diuji coba
BASE_DIR = Path(__file__).resolve().parent
TARGET_DIR = BASE_DIR / "test_folder"

# Pemetaan kategori berdasarkan ekstensi file
EXTENSIONS_MAP = {
    "Dokumen": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Gambar": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Video": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Arsip": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Installer": [".exe", ".deb", ".dmg", ".pkg", ".appimage"],
}


def sort_files(target_path: Path):
    if not target_path.exists():
        print(f"Folder target '{target_path}' tidak ditemukan!")
        return

    print(f"=== Memulai perapian folder: {target_path} ===")
    moved_count = 0

    for item in target_path.iterdir():
        # Jangan pindahkan folder (hanya proses file biasa)
        if item.is_dir():
            continue

        file_ext = item.suffix.lower()
        moved = False

        # Cek kategori
        for category, extensions in EXTENSIONS_MAP.items():
            if file_ext in extensions:
                dest_dir = target_path / category
                dest_dir.mkdir(exist_ok=True)

                dest_file = dest_dir / item.name
                shutil.move(str(item), str(dest_file))
                print(f"[✓] {item.name} -> {category}/")
                moved = True
                moved_count += 1
                break

        # Jika ekstensi tidak terdaftar dan punya ekstensi
        if not moved and file_ext != "":
            dest_dir = target_path / "Lainnya"
            dest_dir.mkdir(exist_ok=True)
            dest_file = dest_dir / item.name
            shutil.move(str(item), str(dest_file))
            print(f"[?] {item.name} -> Lainnya/")
            moved_count += 1

    print(f"\nSelesai! Total file berhasil dipindahkan: {moved_count}")


if __name__ == "__main__":
    sort_files(TARGET_DIR)
