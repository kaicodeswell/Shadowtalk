# 🟣 ShadowTalk - LAN Chat System

A simple, real-time chat system built with Python using sockets and threading. ShadowTalk allows two users on the same network (LAN) to chat privately through a clean terminal interface.

---

## 💡 Features

- 🖥️ Host or Join a chat server easily
- 💬 Real-time message exchange
- 🔐 Exit chat with confirmation prompt
- 🧹 Clear chat history with `/clearhistory`
- 🛑 Graceful exit with `/exit` or `Ctrl+C`
- 🧠 Threaded design for smooth experience

---

## 📸 Preview

🔷 Welcome to ShadowTalk - LAN Chat System 🔷

1️⃣ Host a Chat Server

2️⃣ Join a Chat Server

3️⃣ Exit 🚪


---

## ⚙️ How It Works

- One device **hosts** the server.
- Another device on the **same Wi-Fi or LAN** **joins** using the same IP & port.
- Both users can type and receive messages in real-time.

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.x
- Devices connected to the same Wi-Fi/LAN (for actual LAN use)

### 🧪 Run It

- Clone or download this repo.
-  Open terminal in the project directory.
-  Run:
python shadowtalk.py

- Choose to host or join a chat.

# 📝 Available Commands
Command	Action

`/exit`	Exit the chat safely

`/clearhistory`	Clear terminal chat history

`Ctrl+C`	Also exits safely with message

# 🙋‍♂️ Why ShadowTalk?
ShadowTalk was made to learn basic networking with Python and create a practical tool to chat over local networks securely and simply — no server setup, no fluff.

# 📁 File Structure

shadowtalk.py     #Main script

# 📚 Learnings
This project helps you understand:

Socket programming

Threading for concurrency

Command-line interaction

Graceful exits & input validation

# 📜 License
This project is open-source and available under the MIT License.

# 🧠 Author
Made with ❤️ by [kai]
