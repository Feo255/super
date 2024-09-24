from video_5_hard import Video
from user_5_hard import User

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.curent_user = None
    def add(self, *args):
        self.videos = list(args)
    def register(self, *args):

        db = User()
        db.u_add(args[0], args[1], args[2])
        print(db.list_data)
        nu = {}
        ix = ("nickname", "password", "age")
        i = 0
        for i in range(len(ix)):
            nu[ix[i]] = args[i]
        self.users.append(nu)

    def log_in(self, username, passw):
        k = 0
        for k in range(len(self.users)):
            if self.users[k] == username:
                print(self.users[k])
                print('welcome')





ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.add(v1, v2)

print(ur.videos)

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
print(ur.users)
ur.log_in('vasya_pupkin', 'lolkekcheburek')



