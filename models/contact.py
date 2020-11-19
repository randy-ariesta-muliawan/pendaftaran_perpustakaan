from os import system
from json import load, dump

def tambah_buku():

	system("cls")
	print("Menambahkan Buku Baru\nInformasi Buku")

	tanggal_pengembalian = input("Tanggal Pengembalian :")
	nama_buku            = input("Nama Buku            :")
	nama_peminjam_buku   = input("Nama Peminjam Buku   :")
	telp_peminjam_buku   = input("Telp Peminjam Buku   :")
	alamat_peminjam_buku = input("Alamat Peminjam Buku :")

	respon = input(f"Yakin ingin menyimpan {nama_peminjam_buku} ? (IYA/TIDAK) ")

	if respon.upper() == "IYA":
		nama[nama_peminjam_buku] = {
		"tanggal_pengembalian" : tanggal_pengembalian,
		"nama_buku" : nama_buku,
		"nama_peminjam_buku" : nama_peminjam_buku,
		"telp_peminjam_buku" : telp_peminjam_buku,
		"alamat_peminjam_buku" : alamat_peminjam_buku
		}
		save_nama()
		print("Data Tersimpan")
	else:
		print("Batal Tersimpan")
	input("Tekan ENTER untuk kembali ke MENU")

def lihat_semua_buku():

	system("cls")
	print("Daftar Peminjam Buku Yang Telah Tersimpan\n")

	if len(nama) == 0:
		print("Belum ada data yang disimpan saat ini.")

	else:
		#pembalian\n, nama_buku\n, nama_peminjam_buku\n")
		for name in nama:
			#print(name,"|\t|", nama[name]["tanggal_pengembalian"])
			print(f"Tanggal Pengembalian : {nama[name]['tanggal_pengembalian']}")
			print(f"Nama Peminjam Buku   : {name}")
			print(f"Nama Buku            : {nama[name]['nama_buku']}")
			print(f"Telp Peminjam Buku   : {nama[name]['telp_peminjam_buku']}")
			print(f"Alamat Peminjam Buku : {nama[name]['alamat_peminjam_buku']}\n")
	input("Tekan ENTER untuk kembali ke MENU")

def mencari_buku(name):

	#name = input("Masukkan Nama Yang Ingin Dicari : ")

	if name in nama:
		print(" - HASIL YANG KAMI TEMUKAN - \n")
		print(f"Tanggal Pengembalian : {nama[name]['tanggal_pengembalian']}")
		print(f"Nama Peminjam Buku   : {name}")
		print(f"Nama Buku            : {nama[name]['nama_buku']}")
		print(f"Telp Peminjam Buku   : {nama[name]['telp_peminjam_buku']}")
		print(f"Alamat Peminjam Buku : {nama[name]['alamat_peminjam_buku']}\n")
		return True
	else:
		print(f"Nama {name} Tidak Dapat Kami Temukan. ")
		return False

	#input("Tekan ENTER untuk kembali ke MENU")

def tampilan_mencari_buku():
	system("cls")
	print("Pencarian Kontak")
	names = input("Masukkan Nama Yang Ingin Dicari : ")
	mencari_buku(names)
	input("Tekan ENTER untuk kembali ke MENU")

def menghapus_buku_dari_daftar():

	system("cls")
	print("Menghapus Data Buku")
	name = input("Nama Peminjam Yang Akan Dihapus : ")

	if name in nama:
		print(f" - BERIKUT ADALAH DATA DARI PEMINJAM ( {name} ) -")
		print(f"Tanggal Pengembalian : {nama[name]['tanggal_pengembalian']}")
		print(f"Nama Peminjam Buku   : {name}")
		print(f"Nama Buku            : {nama[name]['nama_buku']}")
		print(f"Telp Peminjam Buku   : {nama[name]['telp_peminjam_buku']}")
		print(f"Alamat Peminjam Buku : {nama[name]['alamat_peminjam_buku']}")
		respon = input("Yakin Ingin Dihapus (IYA/TIDAK) : ")

		if respon.upper() == "IYA":
			del nama[name]
			save_nama()
			print(f"Peminjam Dengan Nama {name} Telah Dihapus.")

		else:
			print(f"Batal Menghapus Nama Peminjam ( {name} )")

	else:
		print(f"Nama {name} Tidak Ditemukan ")

	input("Tekan ENTER untuk kembali ke MENU")
	save_nama()

def mengedit_tanggal_pengembalian(name):
	print("INFORMASI YANG AKAN DIPERBARUI")
	print("DATA LAMA")
	print(f"Tanggal Pengembalian\t:{nama[name]['tanggal_pengembalian']}")
	new_tanggal = input(f"Tanggal Pengembalian Akan Diubah Menjadi : ")
	nama[name]["tanggal_pengembalian"] = new_tanggal
	save_nama()
	print("Data Berhasil Diperbarui.")
	mencari_buku(name)
	save_nama()

def mengedit_nama_buku(name):
	print("INFORMASI YANG AKAN DIPERBARUI")
	print("DATA LAMA")
	print(f"Buku\t:{nama[name]['nama_buku']}")
	new_buku = input("Masukkan Nama Buku Yang Baru : ")
	nama[name]["Informasi Buku"] = new_buku
	save_nama()
	print("Data Berhasil Diperbarui.")
	mencari_buku(name)
	save_nama()

def mengedit_telp_peminjam_buku(name):
	print("INFORMASI YANG AKAN DIPERBARUI")
	print("DATA LAMA")
	print(f"Telp\t:{name[nama]['telp_peminjam_buku']}")
	new_telp = input("Masukkan Nomor Telepon Yang Baru : ")
	name[nama]["telp_peminjam_buku"] = new_telp
	save_nama()
	print("Data Berhasil Diperbarui.")
	mencari_buku(name)
	save_nama()

def mengedit_alamat_peminjam_buku(name):
	print("INFORMASI YANG AKAN DIPERBARUI")
	print("DATA LAMA")
	print(f"Alamat Peminjam Buku\t:{nama[name]['alamat_peminjam_buku']}")
	new_alamat = input("Masukkan Alamat Yang Baru : ")
	nama[name]["alamat_peminjam_buku"] = new_alamat
	save_nama()
	print("Data Berhasil Diperbarui.")
	mencari_buku(name)

def mengedit_nama_kontak(name):
	print("INFORMASI YANG AKAN DIPERBARUI")
	print("DATA LAMA")
	print(f"Nama\t:{name}")
	new_nama = input("Masukkan Nama Baru : ")
	nama[new_nama] = nama[name]
	save_nama()
	print("Data Berhasil Diperbarui.")
	mencari_buku(new_nama)
	save_nama()

def edit_info():
	system("cls")
	print("EDIT INFO")
	names = input("Masukkan Nama Yang Akan Diedit Infonya : ")
	result = mencari_buku(names)
	if result:
		print("EDIT [1] TANGGAL PENGEMBALIAN, [2] NAMA, [3] NAMA BUKU, [4] NOMOR TELEPON, [5] ALAMAT RUMAH")
		respon = input("Pilihan informasi yang akan diedit : ")
		if respon == "1":
			mengedit_tanggal_pengembalian(names)
		elif respon == "2":
			mengedit_nama_kontak(names)
		elif respon == "3":
			mengedit_nama_buku(names)
		elif respon == "4":
			mengedit_telp_peminjam_buku(names)
		elif respon == "5":
			mengedit_alamat_peminjam_buku(names)
		else:
			print("Respon Tidak Valid")
	input("Tekan ENTER untuk kembali ke MENU")


def tentang_kami():
	system("cls")
	print("Aplikasi kami adalah aplikasi perpustakan")
	input("Tekan ENTER untuk kembali ke MENU")

def load_nama():
	with open('data/contact_table.json', 'r') as file:
		nama = load(file)
		return nama
		
def save_nama():
	with open('data/contact_table.json', 'w') as file:
		dump(nama, file)

nama = load_nama()