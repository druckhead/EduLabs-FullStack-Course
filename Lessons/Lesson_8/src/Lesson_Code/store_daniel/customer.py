class Customer:
    def __init__(self, name: str, address: str, id_number: str, phone: str, email: str | None = None):
        self._name = name
        self._address = address
        self._id_number = id_number
        self._phone = phone
        self._email = email

    @property
    def get_name(self) -> str:
        return self._name

    @property
    def get_address(self) -> str:
        return self._address

    @property
    def get_id_num(self) -> str:
        return self._id_number

    @property
    def get_phone(self) -> str:
        return self._phone

    @property
    def get_email(self) -> str | None:
        return self._email

    def __str__(self):
        return f"<Customer Details>\n" \
               f"Customer Name: {self._name}\n" \
               f"Customer Address: {self._address}\n" \
               f"Customer Phone: {self._phone}\n"

    def __repr__(self):
        return f"<Customer {self._name}>"
