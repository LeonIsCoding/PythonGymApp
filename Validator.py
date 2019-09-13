class Validator:
    @staticmethod
    def isempty(value):
        value = value.strip()
        if not value:
            return True
        return False

    @staticmethod
    def isexerciselevelunselected(value):
        if value == -1:
            return True
        return False
