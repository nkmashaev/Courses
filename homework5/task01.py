import datetime


class Homework:
    __slots__ = ("__text", "__deadline", "__created")

    def __init__(self, text: str, days: int):
        self.__text = text
        self.__created = datetime.datetime.now()
        self.__deadline = self.created + datetime.timedelta(days=days)

    @property
    def deadline(self):
        if self.is_active():
            return str(self.__deadline - datetime.datetime.now())
        return str(datetime.timedelta(days=0))

    @property
    def text(self):
        return self.__text

    @property
    def created(self):
        return self.__created

    def is_active(self) -> bool:
        return self.__deadline > datetime.datetime.now()


class Student:
    __slots__ = ("last_name", "first_name")

    def __init__(self, last_name: str, first_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def do_homework(hw: Homework) -> Homework:
        if hw.is_active():
            return hw
        print("You are late")


class Teacher:
    __slots__ = ("last_name", "first_name")

    def __init__(self, last_name: str, first_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(name: str, days: int) -> Homework:
        return Homework(name, days)
