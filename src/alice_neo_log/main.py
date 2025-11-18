from email import message
from neo_chat_bot import NeoChatBot
from animal import Animal


def main():
    neo_chat_bot =  NeoChatBot()
    message = input("메세지를 입력하세요: ")
    neo_chat_bot.ask(message)


if __name__ == "__main__":
    main()
