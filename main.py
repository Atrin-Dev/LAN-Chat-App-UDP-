from udp_chat import UDPChat
from chat_ui import ChatUI


def main():
    ui = ChatUI(send_callback=lambda msg: chat.send_message(msg))

    chat = UDPChat(on_receive_callback=ui.display_message)

    try:
        ui.run()
    finally:
        chat.stop()


if __name__ == "__main__":
    main()
