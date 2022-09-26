class Info:
    def __init__(self, value=None):
        self.value = value

    def __repr__(self):
        return f"{self.__class__}: {self.value}"
