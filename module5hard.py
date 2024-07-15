from time import sleep

class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname: str, password: str, age: int):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует.')
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Поздравляем, {nickname}! Успешная регистрация.')

    def log_out(self):
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user

    def add(self, *new_video):
        for i in new_video:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, search_word: str):
        search_result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                search_result.append(video.title)
        return search_result

    def watch_video(self, name_film: str):
        if self.current_user is not None:
            if self.current_user.age > 18:
                for i in self.videos:
                    if name_film == i.title:
                        for j in range(0, i.duration + 1):
                            print(j, end=' ')
                            sleep(1)
                        print(f'Конец видео')
            else:
                print(f'Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            print(f'Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 15)
v2 = Video('Для чего девушкам парень программист?', 12, True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('ЛУЧШИЙ'))
print(ur.get_videos('ПрОг'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('Liza', 'Fgg567', 10)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('Evgen', 'Ghj098', 37)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('Liza', 'Erttyd444', 45)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')