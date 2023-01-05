class Person(object):
    def __init__(self, id_num: str, name: str, address: str, phone_num: str, email: str = None):
        self.id_num = id_num
        self.name = name
        self.address = address
        self.email = email
        self.phone_num = phone_num

    def __repr__(self):
        return f"Name: {self.name}\n" \
               f"id: {self.id_num}"