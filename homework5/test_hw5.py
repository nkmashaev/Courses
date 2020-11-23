import datetime
import functools

import pytest
import task01
from task02 import print_result


# task01 tests
@pytest.mark.parametrize(
    "expired_hw",
    [
        task01.Homework("Learn function", 0),
        task01.Homework("First homework", -10),
    ],
)
def test_homework_expired(expired_hw):
    assert expired_hw.is_active() == False
    assert expired_hw.deadline == "0:00:00"


def test_homework_name():
    task_name = "Learn function"
    hw = task01.Homework(task_name, 0)
    assert hw.text == task_name


def test_homework_created():
    curr_time = datetime.datetime.now()
    hw = task01.Homework("test", 1)
    creation_time = hw.created
    dt = datetime.timedelta(seconds=1)
    assert (creation_time - curr_time) < dt


@pytest.mark.parametrize(
    "days",
    [
        1,
        5,
    ],
)
def test_homework_deadline(days):
    hw = task01.Homework("test", days)
    assert hw.is_active()
    deadline = hw.created + datetime.timedelta(days=days)
    rest = str(deadline - datetime.datetime.now())
    assert rest[:-6:1] == hw.deadline[:-6:1]  # without ms


@pytest.mark.parametrize(
    ["last_name", "first_name"],
    [
        ("Daniil", "Sharding"),
        ("Roman", "Petrov"),
    ],
)
def test_person_name(last_name, first_name):
    teacher = task01.Teacher(last_name, first_name)
    student = task01.Student(last_name, first_name)
    assert teacher.last_name == last_name
    assert teacher.first_name == first_name
    assert student.last_name == last_name
    assert student.first_name == first_name


def test_student_do_hw_expired(capfd):
    student = task01.Student("Mashaev", "Nikita")
    expired_hw = task01.Homework("Learn functions", 0)
    student.do_homework(expired_hw)
    stdout, stderr = capfd.readouterr()
    assert stdout == "You are late\n"
    assert stderr == ""


def test_student_do_hw_active(capfd):
    student = task01.Student("Mashaev", "Nikita")
    hw = task01.Homework("Learn functions", 1)
    hw_returned = student.do_homework(hw)
    stdout, stderr = capfd.readouterr()
    assert stdout == ""
    assert stderr == ""
    assert isinstance(hw_returned, task01.Homework)
    assert hw_returned is hw


def test_teacher_can_create_hw():
    hw = task01.Teacher.create_homework("Test", 1)
    assert isinstance(hw, task01.Homework)
    assert hw.text == "Test"


# task02 tests
# Has an original function doc string
def test_print_result_origdoc():
    @print_result
    def test_func():
        """test_func docstring"""
        pass

    assert test_func.__doc__ == "test_func docstring"


# Print result of the original function to stdout
# Save original function behavior
def test_print_result_origres(capfd):
    @print_result
    def test_func_sum(*args):
        return functools.reduce(lambda x, y: x + y, args)

    assert test_func_sum([1, 2, 3], [4]) == [1, 2, 3, 4]
    stdout, stderr = capfd.readouterr()
    assert stdout == "[1, 2, 3, 4]\n"
    assert stderr == ""


# Can take original function
# Returned original functions doesn't print the result into
# stdout
def test_print_result_origfunc(capfd):
    @print_result
    def test_func_sum(*args):
        return functools.reduce(lambda x, y: x + y, args)

    orig = test_func_sum.original_func
    assert orig(1, 9, 2, 8, 3, 7, 4, 6, 5) == 45
    stdout, stderr = capfd.readouterr()
    assert stdout == ""
    assert stderr == ""


# Raises exception if private member called
def test_print_result_call_to_private():
    @print_result
    def test_func():
        pass

    with pytest.raises(AttributeError) as execinfo:
        orig = test_func.__original_func
    assert (
        str(execinfo.value) == "'FuncSaver' object has no attribute '__original_func'"
    )
