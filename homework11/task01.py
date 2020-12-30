class SimplifiedEnum(type):
    def __new__(cls, name, bases, dct):
        enum_ids = f"_{name}__keys"
        enum_dict = {}
        for curr_id in dct[enum_ids]:
            enum_dict[curr_id] = curr_id
        return super(SimplifiedEnum, cls).__new__(
            cls, name, bases, {**dct, **enum_dict}
        )
