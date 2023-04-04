import json

global chat_array
global chat_list
import snowflake.client
import time


# 消息类
class Message:
    def __init__(self, user, message):
        # self.uuid = snowflake.client.get_guid()
        self.user = user
        self.time = time.time()
        self.message = message


# 用户类
class User:
    def __init__(self, username):
        # self.uuid = snowflake.client.get_guid()
        self.username = username
        self.messageArray = []
        self.socket = None
        self.p = 0

    def setSocket(self, socket):
        self.socket = socket

    def addMessage(self, message):
        self.messageArray.append(message)

    def sendMessage(self):
        self.socket.send(text_data=json.dumps({"message": self.messageArray[self.p:]}))
        self.p = len(self.messageArray)

# 会话类
class Session:
    def __init__(self, roomName):
        self.member = []
        self.roomName = roomName

    def addMember(self, member):
        self.member.append(member)


Session_list = {}


def send(message):
    chat_array.append(message)


def pull(place):
    return chat_array[place:]
