import json
from .globalneed import Session_list, Session, User
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def __init__(self):
        super(ChatConsumer, self).__init__()

    def connect(self):
        self.accept()

        # Session_list.append(Session)
        # self.send(text_data=json.dumps({"message": chat_array[self.now:]}))
        # self.now = len(chat_array)

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        print(1)
        text_data_json = json.loads(text_data)
        type = text_data_json["type"]
        session_name = text_data_json["sessionName"]
        #message = text_data_json["message"]
        if type == 'check':
            if session_name not in Session_list.keys():
                newSession = Session(session_name)
                user = User("qhr")
                user.setSocket(self)
                newSession.addMember(user)
                Session_list[session_name] = newSession
            else:
                user = User("qhr")
                user.setSocket(self)
                Session_list[session_name].addMember(user)
        else:
            message = text_data_json["message"]
            for member in Session_list[session_name].member:
                member.addMessage(message)
                member.sendMessage()
