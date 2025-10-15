import socket

HOST = "127.0.0.1"
PORT = 8088

def handle_request(request):
    headers = request.split("\r\n")
    cookie = None
    for h in headers:
        if h.startswith("Cookie:"):
            cookie = h.split(":", 1)[1].strip()
    if cookie:
        body = f"<h1>Welcome back, {cookie}!</h1>"
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n"
        response += f"Content-Length: {len(body)}\r\n"
        response += "\r\n" + body
    else:
        body = "<h1>Welcome, new user!</h1>"
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n"
        response += "Set-Cookie: User123\r\n"
        response += f"Content-Length: {len(body)}\r\n"
        response += "\r\n" + body
    return response

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Serving on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            request = conn.recv(1024).decode()
            if not request:
                continue
            response = handle_request(request)
            conn.sendall(response.encode())

