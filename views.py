from os import system

def print_menu():

	system("cls")
	menu_tampilan = """
	=-=-=-=-=-=-=-=-=-=-=
	APLIKASI PERPUSTAKAAN
	=-=-=-=-=-=-=-=-=-=-=
	1. Tambah Buku
	2. Lihat Semua Buku
	3. Mencari Buku Berdasarkan Kepemilikannya
	4. Menghapus Buku dari Daftar
	5. Mengedit Informasi Buku
	6. Tentang Kami
	7. Keluar Perpustakaan
	"""

	print(menu_tampilan)
