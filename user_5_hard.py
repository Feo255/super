
class User:
    def __init__(self):
        self.list_data = []
        self.data = {}

    def u_add(self, nickname, password, age):
        self.data['nickname'] = nickname
        self.data['password'] = password
        self.data['age'] = age
        self.list_data.append(self.data)








