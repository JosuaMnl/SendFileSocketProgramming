import socket
import os

SERVICE_IP = "127.0.0.1"
SERVICE_PORT = 5006
BUFFER_SIZE = 2048

file_name="silabus.pdf"
file_size=os.path.getsize(file_name)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
with open(file_name, "rb") as fr:
	while True:
		#baca byte dari berkas
		bytes_read = fr.read(BUFFER_SIZE)
		pesan=bytes_read
		sock.sendto(pesan, (SERVICE_IP, SERVICE_PORT))

		if not bytes_read:#tidak ada lagi bytes yang dibaca
			#mengirim pesan penutup
			fr.close()
			print("Menutup pengiriman file",file_name,"ke", SERVICE_IP)
			break

		#mengirim potongan file
		print("Mengirim potongan file")

sock.close()
