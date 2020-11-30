def instances_counter(cls):
    class WithCounter(cls):
        """
        With Counter
        """

        numb_of_inst = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__class__.numb_of_inst += 1

        @classmethod
        def get_created_instances(cls):
            return cls.numb_of_inst

        @classmethod
        def reset_instances_counter(cls):
            to_return, cls.numb_of_inst = cls.numb_of_inst, 0
            return to_return

    WithCounter.__doc__ = cls.__doc__
    return WithCounter


@instances_counter
class User:
    """
    User
    """

    pass


if __name__ == "__main__":
    User.get_created_instances()
    User.__doc__
    user, _, _ = User(), User(), User()
    user.get_created_instances()
    user.reset_instances_counter()
