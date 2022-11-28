import socket
import os

SERVICE_IP = "127.0.0.1"
SERVICE_PORT = 5006

SEPARATOR_DATA = "<###>"
BUFFER_SIZE = 2048
BYTES_SIZE = 1024

def convertStringBytes(defineString):
	lenString=len(defineString)
	return lenString.to_bytes(2,'big') + bytes(defineString, 'ascii')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# print(convertStringBytes("FILESEND"))
file_name="tes.txt"
file_size=os.path.getsize(file_name)
#mengirim pesan pembuka
pesan=convertStringBytes("FILESEND") + convertStringBytes("HEAD") \
      + convertStringBytes(file_name + SEPARATOR_DATA + str(file_size))

# print(pesan)
sock.sendto(pesan, (SERVICE_IP, SERVICE_PORT))
print(f"Yang ada HEAD : {pesan}")
print("Memulai pengiriman file",file_name,"ke", SERVICE_IP)


with open(file_name, "rb") as fr:
	i=1
	while True:
		#baca byte dari berkas
		bytes_read = fr.read(BYTES_SIZE)
		print(f"Bytes Read : {bytes_read}")

		if not bytes_read:#tidak ada lagi bytes yang dibaca
			#mengirim pesan penutup
			pesan=convertStringBytes("FILESEND") + convertStringBytes("TAIL")
			print(f"Yang ada TAIL : {pesan}")
			sock.sendto(pesan, (SERVICE_IP, SERVICE_PORT))
			fr.close()
			sock.close()
			print("Menutup pengiriman file",file_name,"ke", SERVICE_IP)
			break

		#mengirim potongan file
		pesan=convertStringBytes("FILESEND") + convertStringBytes("DATA") \
		     + i.to_bytes(2,'big') + bytes_read
		print(f"Yang ada DATA : {pesan}")
		sock.sendto(pesan, (SERVICE_IP, SERVICE_PORT))
		print("Mengirim potongan ke-",i,"dengan ukuran",len(bytes_read),"byte")
		i=i+1
