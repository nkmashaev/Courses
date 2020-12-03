from collections import defaultdict

import pytest

import homework6.task02 as task02
from homework6.task01 import instances_counter


# test task1
@pytest.fixture
def user_class_decorated():
    @instances_counter
    class User:
        """User"""

        pass

    return User


def test_instances_counter_add_methods(user_class_decorated):
    assert hasattr(user_class_decorated, "get_created_instances") is True
    assert hasattr(user_class_decorated, "reset_instances_counter") is True


def test_get_created_instances(user_class_decorated):
    assert user_class_decorated.get_created_instances() == 0
    user1, user2 = user_class_decorated(), user_class_decorated()
    assert user1.get_created_instances() == 2
    assert user2.get_created_instances() == 2
    assert user_class_decorated.get_created_instances() == 2


def test_reset_created_instances(user_class_decorated):
    user1, user2 = user_class_decorated(), user_class_decorated()
    assert user1.reset_instances_counter() == 2
    assert user1.reset_instances_counter() == 0
    assert user_class_decorated.reset_instances_counter() == 0
    assert user2.reset_instances_counter() == 0


def test_origin_class_doc(user_class_decorated):
    assert user_class_decorated.__doc__ == "User"


# test task2
def test_raising_error_if_not_hw_given():
    student = task02.Student("Mashaev", "Nikita")
    with pytest.raises(TypeError, match="Error: Expected homework but unknown found!"):
        task02.HomeworkResult(student, "str instead of Homework", "solution")


def test_do_hw_deadline_exception():
    student = task02.Student("Mashaev", "Nikita")
    expired_homework = task02.Homework("Expired", 0)
    with pytest.raises(task02.DeadlineError, match="You are late"):
        student.do_homework(expired_homework, "solution")


def test_do_hw_return_hw_res():
    st = task02.Student("Mashaev", "Nikita")
    hw = task02.Homework("Actual", 1)
    hw_res = st.do_homework(hw, "done")
    assert isinstance(hw_res, task02.HomeworkResult)
    assert hw_res.solution == "done"
    assert hw_res.homework == hw
    assert hw_res.author == st


def test_pass_check():
    st = task02.Student("Mashaev", "Nikita")
    hw = task02.Homework("Actual", 1)
    hw_res = st.do_homework(hw, "2 + 2 = 4")
    assert task02.Teacher.check_homework(hw_res)
    assert hw_res.homework in task02.Teacher.homework_done.keys()


def test_check_same():
    st = task02.Student("Mashaev", "Nikita")
    hw = task02.Homework("Actual", 1)
    hw_res = st.do_homework(hw, "2 + 2 = 4")
    assert len(task02.Teacher.homework_done[hw]) == 0
    task02.Teacher.check_homework(hw_res)
    assert len(task02.Teacher.homework_done[hw]) == 1
    task02.Teacher.check_homework(hw_res)
    assert len(task02.Teacher.homework_done[hw]) == 1


def test_reject_pass():
    st = task02.Student("Mashaev", "Nikita")
    hw = task02.Homework("Actual", 1)
    hw_res = st.do_homework(hw, "2=2")
    assert not task02.Teacher.check_homework(hw_res)
    assert not hw_res.homework in task02.Teacher.homework_done.keys()


def test_reset_results_delete_hw_done_if_nothing_given():
    task02.Teacher.homework_done = defaultdict(list)
    st = task02.Student("Mashaev", "Nikita")
    hw1 = task02.Homework("hw1", 1)
    hw2 = task02.Homework("hw2", 2)
    hw_res1 = st.do_homework(hw1, "2 + 2 = 4")
    hw_res2 = st.do_homework(hw2, "Green Gauss gradient approach")
    task02.Teacher.check_homework(hw_res1)
    task02.Teacher.check_homework(hw_res2)
    assert len(task02.Teacher.homework_done) == 2
    task02.Teacher.reset_results()
    assert len(task02.Teacher.homework_done) == 0


def test_reset_results_delete_def_hw():
    task02.Teacher.homework_done = defaultdict(list)
    st = task02.Student("Mashaev", "Nikita")
    hw1 = task02.Homework("hw1", 1)
    hw2 = task02.Homework("hw2", 2)
    hw_res11 = st.do_homework(hw1, "2 + 2 = 4")
    hw_res12 = st.do_homework(hw1, "2+2=4 ")
    hw_res2 = st.do_homework(hw2, "Green Gauss gradient approach")
    task02.Teacher.check_homework(hw_res11)
    task02.Teacher.check_homework(hw_res12)
    task02.Teacher.check_homework(hw_res2)
    assert len(task02.Teacher.homework_done) == 2
    task02.Teacher.reset_results(hw1)
    assert len(task02.Teacher.homework_done) == 1
    assert len(task02.Teacher.homework_done[hw1]) == 0
