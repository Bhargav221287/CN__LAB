import socket
def main():
    while True:
        try:
            num = int(input("Enter an integer between 1 and 100: "))
            if 1 <= num <= 100:
                break
            else:
                print("Please enter a number in the valid range.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    client_name = "Bhargav"
    server_host = "10.21.17.101"
    server_port = 9999      
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((server_host, server_port))
            message = f"{client_name}|{num}"
            sock.sendall(message.encode())
            data = sock.recv(1024).decode()
            server_name, server_num_str = data.split("|")
            server_num = int(server_num_str)
            print("\n--- Communication Summary ---")
            print(f"Client’s name    : {client_name}")
            print(f"Server’s name    : {server_name}")
            print(f"Client’s integer : {num}")
            print(f"Server’s integer : {server_num}")
            print(f"Sum              : {num + server_num}")
    except Exception as e:
        print("Error:", e)
if __name__ == "__main__":
    main()

