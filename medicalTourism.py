from category import CategoryDAO
from reservation import ReservationDAO, Reservation

cat_address = "DataBase\categories.txt"
res_address = "DataBase\reservation.txt"

class MedicalTourism:
    def __init__(self) -> None:
        self.cat_DAO = CategoryDAO(cat_address)
        self.res_DAO = ReservationDAO(res_address)
        self.categories = self.cat_DAO.read_from_database()
        self.reservations = []

    def show_all_categories(self):
        cats_string = ""
        for c in self.categories:
            cats_string += (c.to_string())
        return cats_string
    
    def find_category_by_id(self, cat_id):
        for c in self.categories:
            if c.is_match(cat_id):
                return c
        return None
    
    def find_package_by_id(self, pack_id):
        for c in self.categories:
            found_pack = c.find_package_by_id(pack_id)
            if found_pack:
                return found_pack
        return None
    
    def add_reservation(self, wanted_package, documents):
        new_reservation = Reservation(wanted_package, documents)
        self.reservations.append(new_reservation)
        return new_reservation

    



