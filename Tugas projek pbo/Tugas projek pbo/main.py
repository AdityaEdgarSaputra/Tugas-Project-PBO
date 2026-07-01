import os
from pendaftaran import daftar_maba
from penjadwalan import KRS

# Menyimpan sekumpulan objek Mahasiswa yang mendaftar
db_mahasiswa = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') # type: ignore 

def login_mhs():
    clear_screen()
    print("=== LOGIN PORTAL MAHASISWA ===")
    username = input("Username (NIM) : ").strip()
    password = input("Password       : ").strip()
    
    # Memeriksa password dari atribut objek mahasiswa
    if username in db_mahasiswa and db_mahasiswa[username].password == password:
        mhs = db_mahasiswa[username] # Mengambil objek mahasiswa berdasarkan NIM
        
        clear_screen()
        print(f"Selamat datang, {mhs.nama}!")
        print(f"Program Studi: {mhs.prodi}")
        
        # Memanggil method class KRS
        KRS.tampilkan_krs(mhs.prodi)
        input("Tekan Enter untuk keluar dari halaman KRS...")
    else:
        print("\n[-] Login Gagal. NIM atau Password salah / belum terdaftar.")
        input("\nTekan Enter untuk kembali...")

def menu_admin():
    clear_screen()
    print("==================================")
    print("      MENU ADMINISTRATOR          ")
    print("==================================")
    print(f" Total maahasiswa terdaftar: {len(db_mahasiswa)} orang\n")

    statistik = {}
    for mhs in db_mahasiswa.values():
        statistik[mhs.prodi] = statistik.get(mhs.prodi, 0) + 1

    print(" statistik mahasiswa per program studi:")
    if not statistik:
        print(" belum ada yang mendaftar")
    else:
        for prodi, jumlah in statistik.items():
            print(f" - {prodi}: {jumlah} mahasiswa")  

    print("===================================")
    input(" Tekan enter untuk kembali ke mneu utama...")  

def menu_utama():
    while True:
        clear_screen()
        print("==========================================")
        print(" SISTEM INFORMASI AKADEMIK MAHASISWA BARU ")
        print("==========================================")
        print("1. Daftar Mahasiswa Baru")
        print("2. Login Mahasiswa (Cetak KRS)")
        print("3. Menu Admin ")
        print("4. Keluar Program")
        print("==========================================")
        
        pilihan = input("Pilih menu (1/2/3/4): ").strip()
        
        if pilihan == "1":
            daftar_maba(db_mahasiswa, clear_screen)
        elif pilihan == "2":
            login_mhs()
        elif pilihan == "3":
            user_adm = input("masukkan username admin:")
            pass_adm = input("masukkan password admin:")
            if user_adm == "admin" and pass_adm == "admin":
                menu_admin()
            else:
                print("\n[-] Akses ditolak. Akun admin salah.")
                input("Tekan Enter...")
        elif pilihan == "4":
            print("\nTerima kasih. Program selesai.")
            break
        else:
            print("\n[-] Pilihan tidak valid.")
            input("Tekan Enter untuk mengulangi...")

if __name__ == "__main__":
    menu_utama()