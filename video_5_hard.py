
class Video:
    def __init__(self, title, duration, adult_mode = False, second = 0):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.second = second



#ur = UrTube()
#v1 = Video('Лучший язык программирования 2024 года', 200)
#v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#print(v1.title, v1.adult_mode, v2.title, v2.adult_mode)