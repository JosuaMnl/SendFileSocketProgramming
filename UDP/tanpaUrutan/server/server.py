import socket
import base64

global fw
SERVICE_IP="127.0.0.1"
SERVICE_PORT=5005
BUFFER_SIZE=2048

file_name="fotoBaru.jpg"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVICE_IP, SERVICE_PORT))

print("Menunggu kiriman pesan")
fw = open(file_name,'wb')
while True:
	data, addr = sock.recvfrom(BUFFER_SIZE)
	print("Pesan diterima dari", addr)

	if not data:
		print("pengiriman selesai")
		fw.close()
		sock.close()
		break

	fw.write(data)
	print("menerima potongan data")
