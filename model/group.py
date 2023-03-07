# -*- coding: utf-8 -*-
class Group:
    def __init__(self, surname=None, name=None, secondname=None, birthday=None, phone=None, fromwhere=None,
                 filial=None, cbaseid=None, value=None, login=None, password=None, mail=None, s_time=None,
                 title=None, user_group=None, department=None, e_time=None):
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
        self.e_time = e_time
        self.title = title
        self.user_group = user_group
        self.department = department

    # def __repr__(self):
    #     return f"{self.__class__}: {self.name, self.surname, self.secondname, self.birthday, self.phone, self.fromwhere, self.filial, self.cbaseid, self.value, self.login, self.password, self.mail, self.s_time, self.title, self.user_group, self.department} "
    #
    # def __eq__(self, other):
    #     return (self.cbaseid is None or other.cbaseid is None or self.cbaseid == other.cbaseid) \
    #            and self.name == other.name


class Chair:
    def __init__(self, title=None, sorting=None, department=None, filial=None, s_time=None):
        self.title = title
        self.sorting = sorting
        self.department = department
        self.filial = filial
        self.s_time = s_time
