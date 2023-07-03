from category import CategoryDAO
cat_address = "DataBase\categories.txt"

class MedicalTourism:
    def __init__(self) -> None:
        self.cat_DAO = CategoryDAO(cat_address)
        self.categories = self.cat_DAO.read_from_database()

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

    



