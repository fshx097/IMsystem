global chat_array
global chat_list

chat_array = []
chat_list = []

def send(message):
    chat_array.append(message)

def pull(place):
    return chat_array[place:]