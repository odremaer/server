import socket
from views import *
import os
from dotenv import load_dotenv




project_folder = os.path.expanduser('.')
load_dotenv(os.path.join(project_folder, '.env'))

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')


URLS = {
    '/': index,
    '/blog': blog
}


def get_postvalue(request):
    parsed = request.split('=')
    return parsed[-1]


# method and url (/ or /blog)
def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]

    return (method, url)


def generate_headers(method, url):
    if method == 'POST':
        return ('HTTP/1.1 200 OK\n\n', 200)
    if not method == 'GET':
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)

    if not url in URLS:
        return ('HTTP/1.1 404 Not found\n\n', 404)

    return ('HTTP/1.1 200 OK\n\n', 200)


def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><p>Not found</p>'
    if code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    return URLS[url]()



def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)
    print(get_postvalue(request)) # type str
    return (headers + body).encode()



def run():
    serv_sock = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)
    serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # для предотвращение ошибки с занятым адресом
    serv_sock.bind(('{}'.format(HOST), int(PORT)))
    serv_sock.listen()

    while True:
        client_sock, client_address = serv_sock.accept()
        request = client_sock.recv(1024)
        print(request)
        print(len(request))
        print('Connected by ', client_address)
        if len(request) != 0:
            response = generate_response(request.decode('utf-8'))
            client_sock.sendall(response)
        client_sock.close()


if __name__ == '__main__':
    run()
