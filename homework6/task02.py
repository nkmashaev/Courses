import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """Deadline exception"""


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


class HomeworkResult:
    def __init__(self, author, homework, solution: str):
        if not isinstance(homework, Homework):
            raise TypeError("Error: Expected homework but unknown found!")
        self.__author = author
        self.__solution = solution
        self.__homework = homework

    @property
    def author(self):
        return self.__author

    @property
    def solution(self):
        return self.__solution

    @property
    def homework(self):
        return self.__homework


class Person:
    def __init__(self, last_name: str, first_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    def do_homework(self, hw: Homework, solution: str) -> HomeworkResult:
        if hw.is_active():
            return HomeworkResult(self, hw, solution)
        raise DeadlineError("You are late")


class Teacher(Person):
    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(name: str, days: int) -> Homework:
        return Homework(name, days)

    @classmethod
    def check_homework(cls, hw_res: HomeworkResult) -> bool:
        if len(hw_res.solution) <= 5:
            return False
        curr_hw = hw_res.homework
        curr_solution = hw_res.solution
        if all([hw.solution != curr_solution for hw in cls.homework_done[curr_hw]]):
            cls.homework_done[curr_hw].append(hw_res)
        return True

    @classmethod
    def reset_results(cls, hw=None):
        if isinstance(hw, Homework):
            del cls.homework_done[hw]
        else:
            cls.homework_done = defaultdict(list)
