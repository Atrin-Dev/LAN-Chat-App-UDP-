import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class ChatUI:
    def __init__(self, send_callback):
        self.window = tk.Tk()
        self.window.title("LAN Chat App (UDP)")
        self.send_callback = send_callback

        self.chat_display = ScrolledText(self.window, height=20, width=50, state='disabled')
        self.chat_display.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.window, width=40)
        self.entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))
        self.entry.bind("<Return>", lambda e: self.send_message())

        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=10, pady=(0, 10))

    def send_message(self):
        msg = self.entry.get().strip()
        if msg:
            self.send_callback(msg)
            self.display_message(f"You: {msg}")
            self.entry.delete(0, tk.END)

    def display_message(self, msg):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, msg + "\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

    def run(self):
        self.window.mainloop()
