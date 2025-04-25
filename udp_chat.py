import socket, threading, time
from config import *

class UDPChat:
    def __init__(self, on_receive_callback):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.bind((LISTEN_IP, LISTEN_PORT))
        self.on_receive_callback = on_receive_callback
        self.running = True

        threading.Thread(target=self.listen_loop, daemon=True).start()
        threading.Thread(target=self.heartbeat_loop, daemon=True).start()

    def send_message(self, msg):
        for attempt in range(RETRY_COUNT):
            try:
                self.sock.sendto(msg.encode(), (TARGET_IP, TARGET_PORT))
                break
            except Exception as e:
                print(f"[Retry {attempt+1}] Failed to send: {e}")
                time.sleep(RETRY_DELAY)

    def listen_loop(self):
        while self.running:
            try:
                data, addr = self.sock.recvfrom(1024)
                msg = f"[{addr[0]}] {data.decode()}"
                self.on_receive_callback(msg)
            except Exception as e:
                print("Listen error:", e)

    def heartbeat_loop(self):
        while self.running:
            self.send_message("💓 heartbeat")
            time.sleep(HEARTBEAT_INTERVAL)

    def stop(self):
        self.running = False
        self.sock.close()
