import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)  # Хэширование пароля
        self.age = age

    def __str__(self):
        return f'User(nickname - {self.nickname}, age - {self.age})'

    def __repr__(self):
        return self.__str__()

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'Video(title={self.title}, duration={self.duration}s, adult_mode={self.adult_mode})'

    def __repr__(self):
        return self.__str__()

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        password_hash = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == password_hash:
                self.current_user = user
                return
        print('Неверный логин или пароль')

    def register(self, nickname, password, age):
        password_hash = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password_hash, age)
        self.users.append(new_user)
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word = search_word.lower()
        return [video.title for video in self.videos if search_word in video.title.lower()]

    def watch_video(self, video_title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title == video_title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for i in range(video.duration):
                    print(i + 1)
                    time.sleep(1)  
                print('Конец видео')
                video.time_now = 0
                return
        print('Видео не найдено')

# Создание объектов
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))  # ['Лучший язык программирования 2024 года']
print(ur.get_videos('ПРОГ'))  # ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
        
