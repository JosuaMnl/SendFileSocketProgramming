import socket
import base64

SERVICE_IP="127.0.0.1"
SERVICE_PORT=5006
BUFFER_SIZE=2048

SEPARATOR_DATA = "<###>"
global fw

#membuat socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#melakukan binding socket
sock.bind((SERVICE_IP, SERVICE_PORT))

print("Menunggu kiriman pesan")
while True:
	data, addr = sock.recvfrom(BUFFER_SIZE)
	print("Pesan diterima dari", addr)

	protocolLenString=int.from_bytes(data[:2],'big')
	protocolStart=2
	protocolEnd=protocolStart + protocolLenString
	comModeProtocol=data[protocolStart:protocolEnd].decode('ascii')

	if comModeProtocol=="FILESEND":
		processLenString=int.from_bytes(data[protocolEnd:(protocolEnd+2)],'big')
		processStart=protocolEnd+2
		processEnd=processStart+processLenString
		comModeProcess=data[processStart:processEnd].decode('ascii')

		if comModeProcess=='HEAD':
			dataLenString=int.from_bytes(data[processEnd:(processEnd+2)],'big')
			dataStart=processEnd+2
			dataEnd=dataStart+dataLenString
			dataString=data[dataStart:dataEnd].decode('ascii')
			nama,ukuran = dataString.split(SEPARATOR_DATA)
			print("menerima head dengan nama",nama,"ukuran",int(ukuran))
			fw = open('tesBaru.txt','wb')
		elif comModeProcess=='TAIL':
			print("pengiriman selesai")
			fw.close()
			sock.close()
			break
		elif comModeProcess=='DATA':
			dataLenString=int.from_bytes(data[processEnd:(processEnd+2)],'big')
			dataStart=processEnd+2
			dataEnd=dataStart+(len(data)-dataStart)
			pieceNumber=dataLenString
			pieceData=data[dataStart:dataEnd]
			print("pengiriman data ke-",dataLenString)
			fw.write(pieceData)
		else:
			print("Service dihentikan karena bukan pengiriman file")
			break
