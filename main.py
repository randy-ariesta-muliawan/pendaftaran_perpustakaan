from os import system

import views
from models import user, contact


contact.load_nama()
user_respon = ""
while user_respon != "7":

	views.print_menu()
	user_respon = input("RESPON : ").upper()
	if user_respon == 'F':
		views.tentang_kami()
	else:
		user.cek_respon_user(user_respon)

else:
	system("cls")
	print("Sampai Jumpa...")