# PBO2RafiAfrianG1A022033
# Tugas2PBO
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurus
# Penjelasan :
Kelas Mahasiswa:
Kelas ini memiliki tiga atribut yaitu nama, nim, dan jurusan.
> Metode __init__ digunakan sebagai konstruktor untuk menginisialisasi objek Mahasiswa dengan nama, nim, dan jurusan yang diberikan.
> Metode tampilkan_info digunakan untuk menampilkan informasi mahasiswa seperti nama, nim, dan nama jurusan.


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
# Penjelasan :
Kelas Jurusan:

Kelas ini memiliki dua atribut yaitu NamaJurusan dan DaftarMahasiswa.
> Metode __init__ digunakan sebagai konstruktor untuk menginisialisasi objek Jurusan dengan nama jurusan yang diberikan dan membuat daftar mahasiswa yang awalnya kosong.
> Metode tambah_mahasiswa digunakan untuk menambahkan objek Mahasiswa ke dalam daftar mahasiswa pada jurusan tertentu.
> Metode tampilkan_daftar_mahasiswa digunakan untuk menampilkan daftar mahasiswa yang terdaftar pada jurusan tersebut.


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
# Penjelasan :
Kelas Universitas:

Kelas ini memiliki dua atribut yaitu NamaUniversitas dan DaftarJurusan.
> Metode __init__ digunakan sebagai konstruktor untuk menginisialisasi objek Universitas dengan nama universitas yang diberikan dan membuat daftar jurusan yang awalnya kosong.
> Metode tambah_jurusan digunakan untuk menambahkan objek Jurusan ke dalam daftar jurusan pada universitas tertentu.
> Metode tampilkan_daftar_jurusan digunakan untuk menampilkan daftar jurusan yang terdapat di universitas tersebut.


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
# Penjelasan :
Setelah mendefinisikan kelas-kelas di atas, kode selanjutnya melakukan hal berikut:

> Membuat objek universitas_xyz dari kelas Universitas dengan nama "XYZ University".
> Membuat daftar jurusan dalam bentuk list daftar_jurusan.
> Untuk setiap nama jurusan dalam daftar_jurusan, membuat objek jurusan_baru dari kelas Jurusan dengan nama jurusan tersebut, dan menambahkannya ke universitas_xyz menggunakan metode tambah_jurusan.
> Menampilkan daftar jurusan di universitas menggunakan metode tampilkan_daftar_jurusan pada universitas_xyz.
> Menampilkan daftar mahasiswa pada jurusan_baru menggunakan metode tampilkan_daftar_mahasiswa.
> Menerima input jumlah mahasiswa yang akan ditambahkan.
> Dalam loop sebanyak jumlah_mahasiswa, menerima input data untuk setiap mahasiswa (nama, npm, dan nama jurusan).
> Jika jurusan sudah ada dalam daftar_mahasiswa_per_jurusan, menggunakan objek jurusan yang sudah ada. Jika belum, membuat objek jurusan baru dari kelas Jurusan dan menambahkannya ke daftar_mahasiswa_per_jurusan.
>Membuat objek mahasiswa_baru dari kelas Mahasiswa dengan data yang diinputkan, dan menambahkannya ke da


# Output Yang Dihasil kan 
Daftar Jurusan di Universitas XYZ University
-Sistem Informasi
-Teknik Elektro
-Teknik Informatika

Daftar Mahasiswa
Masukan dengan input dari youser 
Masukkan jumlah mahasiswa yang akan ditambahkan: 3

Masukkan data untuk Mahasiswa ke-1:
Nama Mahasiswa: Afrian
NPM Mahasiswa: G1A022033
Jurusan Mahasiswa: Teknik Informatika

Masukkan data untuk Mahasiswa ke-2:
Nama Mahasiswa: Yaya
NPM Mahasiswa: G1A022002
Jurusan Mahasiswa: Teknik Informatika

Masukkan data untuk Mahasiswa ke-3:
Nama Mahasiswa: Bedul
NPM Mahasiswa: G1E033099
Jurusan Mahasiswa: Teknik Elektro

Tampilan setelahh youser menginput daftar mahasiswa
Daftar mahasiswa per jurusan:
> Jurusan: Teknik Informatika
Daftar Mahasiswa
- Nama: Afrian , NPM: G1A022033
- Nama: Yaya , NPM: G1A022002

> Jurusan: Teknik Elektro
Daftar Mahasiswa
- Nama: Bedul , NPM: G1E033099
