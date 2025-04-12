class MailServer:
    def __init__(self, name):
        self.name = name
        self.mailbox = {}

    def store_mail(self, recipient, message):
        if recipient not in self.mailbox:
            self.mailbox[recipient] = []
        self.mailbox[recipient].append(message)

    def retrieve_mail(self, recipient):
        return self.mailbox.pop(recipient, [])

    def __str__(self):
        return {self.name}


class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user

    def receive_mail(self):
        received_messages = self.server.retrieve_mail(self.user)
        return received_messages

    def send_mail(self, server_list, recipient_server, recipient_user, message):
        if recipient_server not in server_list:
            print(f"Ошибка: Сервер {recipient_server} недоступен.")
            return

        # Найдем нужный сервер и отправим ему письмо
        for server in server_list:
            if server.name == recipient_server:
                server.store_mail(recipient_user, message)
                print(f"Письмо отправлено на {recipient_server} пользователю {recipient_user}.")
                return


# Пример использования
if __name__ == "__main__":
    # Создаем несколько серверов
    server1 = MailServer("mail.ru")
    server2 = MailServer("gmail.com")

    # Список доступных серверов
    server_list = [server1, server2]

    # Создаем клиентов
    client1 = MailClient(server1, "user1@mail.ru")
    client2 = MailClient(server2, "user2@gmail.com")

    # Отправляем и принимаем почту
    client1.send_mail(server_list, "gmail.com", "user2@gmail.com", "Привет, пользователь 2!")
    messages = client2.receive_mail()
    print(f"Пользователь {client2.user} получил письма: {messages}")

    # Проверяем возможность отправки на недоступный сервер
    client1.send_mail(server_list, "kemsu.ru", "user2@mail.com", "Это не должно сработать!")
