import socket
import threading
import sys
import os

# Automatically detect local IP for server
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return '127.0.0.1'

PORT = 5000
username = ""

# Function to receive messages
def receive_messages(conn):
    while True:
        try:
            msg = conn.recv(1024).decode("utf-8")
            if msg:
                print(f"\n💬 {msg}\n📝 You: ", end="")
            else:
                break
        except:
            print("\n⚠️ Connection closed.")
            conn.close()
            break

# Function to send messages
def send_messages(conn):
    while True:
        try:
            msg = input("📝 You: ")
        except KeyboardInterrupt:
            print("\n❌ Interrupted. Exiting...")
            conn.send(f"{username} left the chat.".encode("utf-8"))
            conn.close()
            sys.exit()

        if msg.lower() == "/exit":
            try:
                confirm_exit = input("❓ Are you sure you want to exit the chat? (yes/no): ").strip().lower()
                if confirm_exit == "yes":
                    print("👋 Bye!")
                    conn.send(f"{username} left the chat.".encode("utf-8"))
                    conn.close()
                    sys.exit()
                elif confirm_exit == "no":
                    continue
                else:
                    print("⚠️ Please enter a valid response (yes/no).")
                    continue
            except KeyboardInterrupt:
                print("\n❌ Interrupted. Exiting...")
                conn.send(f"{username} left the chat.".encode("utf-8"))
                conn.close()
                sys.exit()
        elif msg.lower() == "/clearhistory":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("🧹 Chat history cleared.")
            continue

        conn.send(f"{username}: {msg}".encode("utf-8"))

# Start server function
def start_server():
    global username
    try:
        username = input("🪪 Enter your name (host): ").strip() or "Host"
    except KeyboardInterrupt:
        print("\n👋 Bye!")
        return

    while True:
        try:
            confirm = input("⚙️ Are you sure you want to host the server? (yes or no): ").strip().lower()
            if confirm == "yes":
                break
            elif confirm == "no":
                print("👋 Bye!")
                return
            else:
                print("⚠️ Please enter a valid response (yes/no).")
        except KeyboardInterrupt:
            print("\n👋 Bye!")
            return

    HOST = get_local_ip()
    print(f"📡 Your IP address is: {HOST}")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"\n🖧 Hosting chat on {HOST}:{PORT}... Waiting for a connection (Ctrl+C to cancel)...")

    try:
        conn, addr = server_socket.accept()
        print(f"✅ Connected with {addr}!")
        threading.Thread(target=receive_messages, args=(conn,)).start()
        send_messages(conn)
    except KeyboardInterrupt:
        print("\n👋 Server shut down by user.")
    except Exception as e:
        print(f"⚠️ Error: {e}")
    finally:
        server_socket.close()

# Join server function
def join_server():
    global username
    try:
        username = input("🪪 Enter your name (client): ").strip() or "Guest"
    except KeyboardInterrupt:
        print("\n👋 Bye!")
        return

    while True:
        try:
            confirm = input("⚙️ Do you want to join a chat server? (yes or no): ").strip().lower()
            if confirm == "yes":
                break
            elif confirm == "no":
                print("👋 Bye!")
                return
            else:
                print("⚠️ Please enter a valid response (yes/no).")
        except KeyboardInterrupt:
            print("\n👋 Bye!")
            return

    host_ip = input("🔌 Enter the host IP address: ").strip()
    print("🔌 Attempting to connect... Type '/exit' anytime to cancel.")
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host_ip, PORT))
        print("✅ Connected to the host!")

        threading.Thread(target=receive_messages, args=(client_socket,)).start()
        send_messages(client_socket)
    except Exception as e:
        print(f"⚠️ Could not connect: {e}")

# Main menu
if __name__ == "__main__":
    print("""
🔷 Welcome to ShadowTalk - LAN Chat System 🔷
1️⃣ Host a Chat Server
2️⃣ Join a Chat Server
3️⃣ Exit 🚪
    """)

    while True:
        try:
            option = input("📌 Choose an option (1/2/3): ").strip()
        except KeyboardInterrupt:
            print("\n👋 Bye! Stay connected.")
            break

        if option == "1":
            start_server()
            break
        elif option == "2":
            join_server()
            break
        elif option == "3":
            print("👋 Bye! Stay connected.")
            break
        else:
            print("⚠️ Invalid option. Try again.")
