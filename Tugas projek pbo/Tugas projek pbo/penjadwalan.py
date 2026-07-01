class KRS:
    JADWAL_PAKET = {
        "Teknik Informatika": [
            {"matkul": "Dasar Pemrograman", "sks": 3},
            {"matkul": "Kalkulus I", "sks": 3},
            {"matkul": "Pengantar Teknologi Informasi", "sks": 2}
        ],
        "Sistem & Teknologi Informasi": [
            {"matkul": "Dasar-Dasar Sistem Informasi", "sks": 3},
            {"matkul": "Matriks & Ruang Vektor", "sks": 3},
            {"matkul": "Manajemen Bisnis Pengantar", "sks": 2}
        ],
        "Teknik Arsitektur": [
            {"matkul": "Pengantar Studio Perancangan", "sks": 4},
            {"matkul": "Estetika Bentuk", "sks": 2},
            {"matkul": "Sejarah & Teori Arsitektur I", "sks": 2}
        ],
        "Teknik Industri": [
            {"matkul": "Pengantar Teknik Industri", "sks": 2},
            {"matkul": "Fisika Dasar I", "sks": 3},
            {"matkul": "Kalkulus I", "sks": 3}
        ],
        "Manajemen": [
            {"matkul": "Pengantar Manajemen", "sks": 3},
            {"matkul": "Matematika Ekonomi", "sks": 3},
            {"matkul": "Pengantar Bisnis", "sks": 3}
        ],
        "Akuntansi": [
            {"matkul": "Pengantar Akuntansi I", "sks": 3},
            {"matkul": "Matematika Ekonomi", "sks": 3},
            {"matkul": "Mikroekonomi Pengantar", "sks": 3}
        ]
    }

    @classmethod
    def tampilkan_krs(cls, prodi):
        print("\n==============================================")
        print(f" PAKET KRS SEMESTER 1 - {prodi.upper()} ")
        print("==============================================")
        
        # mengambil daftar matkul berdasarkan prodi 
        matkul_list = cls.JADWAL_PAKET.get(prodi.strip(), [])
        
        if not matkul_list:
            print("Belum ada jadwal mata kuliah.")
            print("==============================================\n")
            return

        total_sks = 0
        for i, item in enumerate(matkul_list, 1):
            print(f"{i}. {item['matkul']} ({item['sks']} SKS)")
            total_sks += item['sks']
            
        print("==============================================")
        print(f" TOTAL SKS YANG DIAMBIL: {total_sks} SKS")
        print("==============================================\n")