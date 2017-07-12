from .. import ValidatingProperty

class Int(ValidatingProperty):
    def validate(self, val):
        try:
            int(val)
        except: 
            return False
        else:
            return True


class Float(ValidatingProperty):
    def validate(self, val):
        try:
            float(val)
        except: 
            return False
        else:
            return True

