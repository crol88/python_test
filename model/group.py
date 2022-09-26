class Group:
    def __init__(self, surname=None, name=None, secondname=None, birthday=None, phone=None, fromwhere=None,
                 filial=None, cbaseid=None, value=None):
        self.name = name
        self.surname = surname
        self.secondname = secondname
        self.birthday = birthday
        self.phone = phone
        self.fromwhere = fromwhere
        self.filial = filial
        self.cbaseid = cbaseid
        self.value = value

    def __repr__(self):
        return f"{self.__class__}: {self.cbaseid, self.name, self.value}"

    def __eq__(self, other):
        return (self.cbaseid is None or other.cbaseid is None or self.cbaseid == other.cbaseid) \
               and self.name == other.name
