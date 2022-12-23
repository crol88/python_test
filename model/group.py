# -*- coding: utf-8 -*-
class Group:
    def __init__(self, surname=None, name=None, secondname=None, birthday=None, phone=None, fromwhere=None,
                 filial=None, cbaseid=None, value=None, login=None, password=None, mail=None, s_time=None, title=None):
        self.name = name
        self.surname = surname
        self.secondname = secondname
        self.birthday = birthday
        self.phone = phone
        self.fromwhere = fromwhere
        self.filial = filial
        self.cbaseid = cbaseid
        self.value = value
        self.login = login
        self.password = password
        self.mail = mail
        self.s_time = s_time
        self.title = title

    def __repr__(self):
        return f"{self.__class__}: {self.cbaseid, self.name, self.value}"

    def __eq__(self, other):
        return (self.cbaseid is None or other.cbaseid is None or self.cbaseid == other.cbaseid) \
               and self.name == other.name


class Chair:
    def __init__(self, title=None, sorting=None, department=None, filial=None, s_time=None):
        self.title = title
        self.sorting = sorting
        self.department = department
        self.filial = filial
        self.s_time = s_time
