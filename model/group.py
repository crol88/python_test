class Group:
    def __init__(self, surname=None, name=None, secondname=None, datapicker=None, phone=None, fromwhere=None,
                 filial=None, cbase_id=None):
        self.name = name
        self.surname = surname
        self.secondname = secondname
        self.datapicker = datapicker
        self.phone = phone
        self.fromwhere = fromwhere
        self.filial = filial
        self.cbase_id = cbase_id

    def __repr__(self):
        return f"{self.__class__}: {self.cbase_id}"
