from pathlib import Path

# Membuat dummy files untuk pengujian aman
BASE_DIR = Path(__file__).resolve().parent
TEST_DIR = BASE_DIR / "test_folder"

DUMMY_FILES = [
    "laporan_keuangan.xlsx",
    "proposal_proyek.pdf",
    "catatan_meeting.docx",
    "foto_liburan.jpg",
    "logo_transparan.png",
    "rekaman_audio.mp3",
    "video_tutorial.mp4",
    "backup_database.zip",
    "setup_aplikasi.deb",
    "data_mentah.csv",
    "arsip_lama.tar.gz",
    "file_aneh.xyz",
]


def generate_dummies():
    TEST_DIR.mkdir(exist_ok=True)
    for filename in DUMMY_FILES:
        file_path = TEST_DIR / filename
        file_path.write_text(f"Ini adalah konten dummy untuk {filename}\n")
    print(f"Berhasil membuat {len(DUMMY_FILES)} file dummy di: {TEST_DIR}")


if __name__ == "__main__":
    generate_dummies()
