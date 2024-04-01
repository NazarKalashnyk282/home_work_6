from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError('Value error')




class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))
# Додавання телефонів.

    def delete_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]
# Видалення телефонів. 

    def edit_phone(self, old_phone, new_phone):
        self.delete_phone(old_phone)
        self.add_phone(new_phone)
# Редагування телефонів.

    def find_phone(self, phone):
        return phone in [str(p) for p in self.phones]
# Пошук телефону. 

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"




class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
# Додавання записів.
        
    def find_record(self, name):
        return self.data.get(name)
# Пошук записів за іменем.
    
    def delete_record(self, name):
        del self.records[name]
# Видалення записів за іменем. 