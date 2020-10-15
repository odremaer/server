import socket
import signal
import sys

# def cb_sigint_handler(signum, stack):
#     global is_interrupted
#     print("SIGINT received")
#     is_interrupted = True
#
# is_interrupted = False
# signal.signal(signal.SIGINT, cb_sigint_handler)
URLS = {
    '/': 'hello index',
    '/blog': 'hello blog'
}


def parse_request(request):
    parsed = request.split(' ')
    print(parsed[0], parsed[1])
    method = parsed[0]
    url = parsed[1]
    return (method, url)


def generate_headers(method, url):
    if not method == 'GET':
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)

    if not url in URLS:
        return ('HTTP/1.1 404 Not found\n\n', 404)

    return ('HTTP/1.1 200 OK\n\n', 200)


def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    return (headers + 'hello world').encode()



def run():
    serv_sock = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)
    serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # для предотвращение ошибки с занятым адресом
    serv_sock.bind(('localhost', 8080))
    #PORT HOST
    serv_sock.listen()

    while True:
        client_sock, client_addr = serv_sock.accept()
        #client_address
        request = client_sock.recv(1024)
        print(request)
        print()
        print('Connected by ', client_addr)

        response = generate_response(request.decode('utf-8'))

        client_sock.sendall(response)
        client_sock.close()


if __name__ == '__main__':
    run()