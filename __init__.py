
class ValidatingProperty(property):
    ERR_MSG = "Invalid data passed"

    def validate(self, val):
        return True

    def __set__(self, obj, value):
        print("obj {}, property: {} ,and val {} ".format(obj, self.name, value))
        if self.validate(value) is True:
            super().fset(obj, value)
        else:
            raise ValueError("Can't set {}: {}.".format(self.name, self.ERR_MSG))

    def __set_name__(self, obj, name):
        print("setting: obj: {}, name {}".format(obj, name))
        self.name = name
