import socket

serv_sock = socket.socket(socket.AF_INET,      # задамем семейство протоколов 'Интернет' (INET)
                          socket.SOCK_STREAM,  # задаем тип передачи данных 'потоковый' (TCP)
                          proto=0)             # выбираем протокол 'по умолчанию' для TCP, т.е. IP
print(type(serv_sock))                         # <class 'socket.socket'>