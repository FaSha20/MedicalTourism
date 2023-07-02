


class CategoryDAO:
    def __init__(self, address) -> None:
        self.cat_address = address

    def add_to_database(self, cat_info):
        f = open(self.cat_address, "a")
        f.write(cat_info)
        f.close()

    def read_from_database(self):
        f = open(self.cat_address, "r")
        return f.read()