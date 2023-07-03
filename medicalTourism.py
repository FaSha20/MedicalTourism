from category import CategoryDAO
from reservation import ReservationDAO, Reservation

cat_address = "DataBase\Categories.txt"
res_address = "DataBase\Reservation.txt"

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
        raise Exception("The entered category ID is not valid")
    
    def find_package_by_id(self, pack_id):
        for c in self.categories:
            found_pack = c.find_package_by_id(pack_id)
            if found_pack:
                return found_pack
        raise Exception("The entered package ID is not valid") 
    
    def add_reservation(self, wanted_package, documents):
        new_reservation = Reservation(wanted_package, documents)
        return new_reservation
    
    def finalize_res(self, reservation, card_info):
        reservation.pay(card_info)
        self.reservations.append(reservation)
        self.res_DAO.add_to_database(reservation)
        return reservation.to_string()

    



