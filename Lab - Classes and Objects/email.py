class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}'


email_list = []
while True:
    command = input().split()
    if command[0] == 'Stop':
        break
    sender = command[0]
    receiver = command[1]
    content = command[2]
    info = Email(sender, receiver, content)
    email_list.append(info)
index = [int(num) for num in input().split(', ')]

for i in index:
    email_list[i].send()

for email in email_list:
    print(email.get_info())
