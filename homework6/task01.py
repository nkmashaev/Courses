def instances_counter(cls):
    cls.instance_counter = 0
    cls_init = cls.__init__

    def cls_init_with_counter(self, *args, **kwargs):
        cls_init(self, *args, **kwargs)
        self.__class__.instance_counter += 1

    @classmethod
    def get_created_instances(cls):
        return cls.instance_counter

    @classmethod
    def reset_instances_counter(cls):
        res = cls.instance_counter
        cls.instance_counter = 0
        return res

    cls.__init__ = cls_init_with_counter
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls


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
