import random

class Mahasiswa:
    # Constructor untuk membuat objek Mahasiswa
    def __init__(self, nama, jk, tempat_lahir, tgl_lahir, no_telp, alamat, email, warga, fakultas, prodi, db_mahasiswa):
        self.nama = nama
        self.jk = jk
        self.tempat_lahir = tempat_lahir
        self.tgl_lahir = tgl_lahir
        self.no_telp = no_telp
        self.alamat = alamat
        self.email = email
        self.warga = warga
        self.fakultas = fakultas
        self.prodi = prodi
        self.password = tgl_lahir  # Password otomatis menggunakan tanggal lahir
        self.nim = self.__generate_nim(db_mahasiswa) # Private Method Enkapsulasi

    # Private Method untuk generate NIM
    def __generate_nim(self, db_mahasiswa):
        tahun = "26"
        kode_fakultas = {"FTEIC": "8", "TEKNIK": "9", "FEB": "5"}
        kode_prodi = {
            "Teknik Informatika": "6", "Sistem & Teknologi Informasi": "2",
            "Teknik Arsitektur": "1", "Teknik Industri": "7",
            "Manajemen": "3", "Akuntansi": "4"
        }
        
        fak_code = kode_fakultas.get(self.fakultas, "0")
        prod_code = kode_prodi.get(self.prodi, "0")
        
        while True:
            random_num = str(random.randint(100000, 999999))
            candidate_nim = tahun + fak_code + prod_code + random_num
            if candidate_nim not in db_mahasiswa:
                return candidate_nim

def daftar_maba(db_mahasiswa, clear_screen_func):
    clear_screen_func() 
    print("=== PENDAFTARAN MAHASISWA BARU ===")
    nama = input("Nama Lengkap            : ").strip()
    jk = input("Jenis Kelamin (L/P)     : ").strip()
    tempat_lahir = input("Tempat Lahir            : ").strip()
    tgl_lahir = input("Tanggal Lahir (DDMMYYYY): ").strip() 
    no_telp = input("No. Telp                : ").strip()
    alamat = input("Alamat Rumah            : ").strip()
    email = input("Email                   : ").strip()
    warga = input("Kewarganegaraan         : ").strip()
    
    print("\n--- PILIHAN FAKULTAS ---")
    print("1. FTEIC")
    print("2. TEKNIK")
    print("3. FEB")
    pil_fak = input("Pilih Fakultas (1/2/3): ").strip()
    
    fakultas = ""
    prodi = ""
    
    if pil_fak == "1":
        fakultas = "FTEIC"
        print("\n--- PILIHAN PRODI FTEIC ---")
        print("1. Teknik Informatika")
        print("2. Sistem & Teknologi Informasi")
        pil_prod = input("Pilih Prodi (1/2): ").strip()
        if pil_prod == "1":
            prodi = "Teknik Informatika"
        elif pil_prod == "2":
            prodi = "Sistem & Teknologi Informasi"
        else:
            print("\n[-] Pilihan Prodi tidak valid!")
            input("Tekan Enter untuk kembali...")
            return
            
    elif pil_fak == "2":
        fakultas = "TEKNIK"
        print("\n--- PILIHAN PRODI TEKNIK ---")
        print("1. Teknik Arsitektur")
        print("2. Teknik Industri")
        pil_prod = input("Pilih Prodi (1/2): ").strip()
        if pil_prod == "1":
            prodi = "Teknik Arsitektur"
        elif pil_prod == "2":
            prodi = "Teknik Industri"
        else:
            print("\n[-] Pilihan Prodi tidak valid!")
            input("Tekan Enter untuk kembali...")
            return
            
    elif pil_fak == "3":
        fakultas = "FEB"
        print("\n--- PILIHAN PRODI FEB ---")
        print("1. Manajemen")
        print("2. Akuntansi")
        pil_prod = input("Pilih Prodi (1/2): ").strip()
        if pil_prod == "1":
            prodi = "Manajemen"
        elif pil_prod == "2":
            prodi = "Akuntansi"
        else:
            print("\n[-] Pilihan Prodi tidak valid!")
            input("Tekan Enter untuk kembali...")
            return
    else:
        print("\n[-] Pilihan Fakultas tidak valid! Kembali ke menu utama.")
        input("\nTekan Enter untuk kembali...")
        return

    mhs_baru = Mahasiswa(nama, jk, tempat_lahir, tgl_lahir, no_telp, alamat, email, warga, fakultas, prodi, db_mahasiswa)
    # Menyimpan Objek ke dalam Database dictionary
    db_mahasiswa[mhs_baru.nim] = mhs_baru
    
    clear_screen_func()
    print("==================================================")
    print("           PENDAFTARAN BERHASIL DISIMPAN           ")
    print("==================================================")
    print(f"Username (NIM)  : {mhs_baru.nim}")
    print(f"Password        : {mhs_baru.password}")
    print("==================================================")
    print("Harap catat Username dan Password Anda untuk Login.")
    input("\nTekan Enter untuk kembali ke Menu Utama...")