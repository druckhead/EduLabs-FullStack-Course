
class IncompatibleFileTypeError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)


class IncompatibleCsvHeaders(Exception):
    def __init__(self, lhs_header, rhs_header):
        self.lhs_header = lhs_header
        self.rhs_header = rhs_header
        self.msg = f"Error: lhs={self.lhs_header} and rhs={self.rhs_header} posses different headers"
        super().__init__(self.msg)


class InvalidFileExtension(Exception):
    def __init__(self, msg: str):
        self.msg = msg
        super().__init__(self.msg)
