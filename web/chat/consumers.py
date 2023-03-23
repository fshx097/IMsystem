import json
from .globalneed import chat_list,chat_array
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def __init__(self):
        super(ChatConsumer, self).__init__()
        self.now = 0

    def connect(self):
        self.accept()
        chat_list.append(self)
        self.send(text_data=json.dumps({"message": chat_array[self.now:]}))
        self.now = len(chat_array)

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        #需要对chat_array上锁？
        chat_array.append(message)
        print(chat_array)
        for i in chat_list:
            i.send(text_data=json.dumps({"message": chat_array[i.now:]}))
            i.now = len(chat_array)