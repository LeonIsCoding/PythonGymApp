class Utility:
    @staticmethod
    def roundvalue(decimalplaces, value):
        if decimalplaces < 0 or decimalplaces > 4:
            return value
        if value <= 0:
            return value

        formattedvalue = round(value, decimalplaces)

        return formattedvalue
