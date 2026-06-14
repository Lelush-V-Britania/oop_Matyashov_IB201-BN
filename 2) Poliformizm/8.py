class Person:
    def __init__(self, name, patronymic, surname, phones):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.phones = phones

    def get_phone(self):
        if 'private' in self.phones:
            return self.phones['private']
        else:
            return None

    def get_name(self):
        return self.surname + " " + self.name + " " + self.patronymic

    def get_work_phone(self):
        if 'work' in self.phones:
            return self.phones['work']
        else:
            return None

    def get_sms_text(self):
        return "Уважаемый " + self.name + " " + self.patronymic + "! Примите участие в нашем беспроигрышном конкурсе для физических лиц"

class Company:
    def __init__(self, name, comp_type, phones, *employees):
        self.name = name
        self.comp_type = comp_type
        self.phones = phones
        self.employees = employees

    def get_phone(self):
        if 'contact' in self.phones:
            return self.phones['contact']
        for emp in self.employees:
            phone = emp.get_work_phone()
            if phone is not None:
                return phone
        return None

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return "Для компании " + self.name + " есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для " + self.comp_type

def send_sms(*args):
    for obj in args:
        phone = obj.get_phone()
        if phone is not None:
            print("Отправлено СМС на номер " + phone + " с текстом: " + obj.get_sms_text())
        else:
            print("Не удалось отправить сообщение абоненту: " + obj.get_name())