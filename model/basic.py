class Basic:
    def __init__(self, surname=None, name=None, secondname=None, birthday=None):
        self.name = name
        self.surname = surname
        self.secondname = secondname
        self.birthday = birthday

    def __repr__(self):
        return f"{self.__class__}: {self.name, self.birthday, self.surname, self.secondname}"

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname \
               and self.secondname == other.secondname and self.birthday == other.birthday
