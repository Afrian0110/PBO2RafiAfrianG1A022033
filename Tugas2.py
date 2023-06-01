class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NPM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)


class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa ")
        for mahasiswa in self.DaftarMahasiswa:
            print("- Nama:", mahasiswa.nama, ", NPM:", mahasiswa.nim)


class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print( jurusan.NamaJurusan)


universitas_xyz = Universitas("XYZ University")

daftar_jurusan = ["-Sistem Informasi", "-Teknik Elektro", "-Teknik Informatika\n"]

for nama_jurusan in daftar_jurusan:
    jurusan_baru = Jurusan(nama_jurusan)
    universitas_xyz.tambah_jurusan(jurusan_baru)

universitas_xyz.tampilkan_daftar_jurusan()

jurusan_baru.tampilkan_daftar_mahasiswa()

daftar_mahasiswa_per_jurusan = {}

jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa yang akan ditambahkan: "))

for i in range(jumlah_mahasiswa):
    print(f"\nMasukkan data untuk Mahasiswa ke-{i+1}:")
    nama = input("Nama Mahasiswa: ")
    nim = input("NPM Mahasiswa: ")
    nama_jurusan = input("Jurusan Mahasiswa: ")

    if nama_jurusan in daftar_mahasiswa_per_jurusan:
        jurusan = daftar_mahasiswa_per_jurusan[nama_jurusan]
    else:
        jurusan = Jurusan(nama_jurusan)
        daftar_mahasiswa_per_jurusan[nama_jurusan] = jurusan

    mahasiswa_baru = Mahasiswa(nama, nim, jurusan)
    jurusan.tambah_mahasiswa(mahasiswa_baru)

print("\nDaftar mahasiswa per jurusan:")
for nama_jurusan, jurusan in daftar_mahasiswa_per_jurusan.items():
    print("\nJurusan:", nama_jurusan)
    jurusan.tampilkan_daftar_mahasiswa()


