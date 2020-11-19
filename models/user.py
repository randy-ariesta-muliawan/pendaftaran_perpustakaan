from . import contact

def cek_respon_user(char):
	if char == "1":
		contact.tambah_buku()
	elif char == "2":
		contact.lihat_semua_buku()
	elif char == "3":
		contact.tampilan_mencari_buku()
	elif char == "4":
		contact.menghapus_buku_dari_daftar()
	elif char == "5":
		contact.edit_info()
	elif char == "6":
		contact.tentang_kami()
	elif char == "7":
		pass
	else:
		print("Respon Tidak Valid")
		input("Tekan ENTER untuk kembali ke MENU...")