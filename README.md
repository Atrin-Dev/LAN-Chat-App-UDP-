# LAN-Chat-App-UDP-
A simple communication-aware LAN chat application with a GUI built using **Tkinter** and **UDP sockets** in Python. It features a retry mechanism, periodic heartbeat messages, and support for extensions like encryption and multi-language versions.

---

## 📦 Features

- 💬 Real-time messaging over local network
- 🪟 Intuitive GUI with message history
- 🔁 Retry mechanism for reliable UDP communication
- 💓 Periodic heartbeat to maintain presence awareness

---

## 🧠 Architecture Overview

- `chat_ui.py` — Graphical User Interface (GUI) using `Tkinter`.
- `udp_chat.py` — Networking logic using `socket` and threading.
- `main.py` — Entry point that connects UI and backend.
- `config.py` — Central configuration for IP addresses, ports, retry settings, etc.

---

## 🏃 Getting Started

### ✅ Requirements

- Python 3.6+
- Works on Windows, macOS, and Linux

### 📂 Installation

```bash
git clone https://github.com/Atrin-Dev/lan-chat-udp.git
cd lan-chat-udp

