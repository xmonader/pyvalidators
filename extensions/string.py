from .. import ValidatingProperty

class Upper(ValidatingProperty):
    ERR_MSG = "all Letters must be uppercase."
    def validate(self, val):
        return all([x.isupper() for x in val])


class Lower(ValidatingProperty):
    ERR_MSG = "all Letters must be lowercase."

    def validate(self, val):
        return all([x.islower() for x in val])
