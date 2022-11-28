import socket
import easygui
import shutil
import random
import os

file = easygui.fileopenbox()
extension = file.split(".")[1]
no = random.getrandbits(8)
fileBaru = f"E:/File Jos/Kuliah/Semester 5/Sistem Terdistribusi dan Komputer Paralel/kirimFileSocketProgramming/UDP/tanpaUrutan/client/fileCopy{no}.{extension}"
shutil.copy(file, fileBaru)

file_size = os.path.getsize(fileBaru)

UDP_IP = input("Masukkan Alamat IP Address yang ingin dikirimi pesan : ")
UDP_PORT = 5005

BUFFER_SIZE = 2048

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
with open(fileBaru, "rb") as fr:
	while True:
		#baca byte dari berkas
		bytes_read = fr.read(BUFFER_SIZE)
		pesan=bytes_read
		sock.sendto(pesan, (UDP_IP, UDP_PORT))

		if not bytes_read:#tidak ada lagi bytes yang dibaca
			#mengirim pesan penutup
			fr.close()
			print("Menutup pengiriman file",fileBaru,"ke", UDP_IP)
			break

		#mengirim potongan file
		print("Mengirim potongan file")

sock.close()