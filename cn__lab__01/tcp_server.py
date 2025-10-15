import socket
def main():
    server_name = "Server of John Q. Smith"
    server_integer = 42 
    host = "0.0.0.0" 
    port = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"{server_name} listening on {host}:{port}...")
        while True:
            client_socket, client_addr = server_socket.accept()
            with client_socket:
                print(f"\nConnection from {client_addr}")
                data = client_socket.recv(1024).decode()
                if not data:
                    continue
                try:
                    client_name, client_num_str = data.split("|")
                    client_num = int(client_num_str)
                except Exception:
                    print("Invalid client message format. Closing connection.")
                    continue
                if not (1 <= client_num <= 100):
                    print(f"Invalid integer received ({client_num}). Terminating server.")
                    return 
                print("\n--- Communication Summary ---")
                print(f"Client’s name    : {client_name}")
                print(f"Server’s name    : {server_name}")
                print(f"Client’s integer : {client_num}")
                print(f"Server’s integer : {server_integer}")
                print(f"Sum              : {client_num + server_integer}")
                response = f"{server_name}|{server_integer}"
                client_socket.sendall(response.encode())
if __name__ == "__main__":
    main()

