class Utility:
    @staticmethod
    def round_value(decimal_places, value):
        if decimal_places < 0 or decimal_places > 4:
            return value
        if value <= 0:
            return value

        formattedvalue = round(value, decimal_places)

        return formattedvalue
