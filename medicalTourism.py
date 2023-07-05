from category import CategoryDAO
from reservation import ReservationDAO, Reservation
from customer import CustomerDAO,Customer
from form import Form,FormDAO
from supporter import SupporterDAO,Supporter

cat_address = "DataBase\Categories.txt"
res_address = "DataBase\Reservation.txt"
user_address = "DataBase\\Users.txt"
form_address = "DataBase\Form.txt"
supporter_address = "DataBase\Supporter.txt"

class MedicalTourism:
    def __init__(self) -> None:
        self.cat_DAO = CategoryDAO(cat_address)
        self.res_DAO = ReservationDAO(res_address)
        self.customer_DAO = CustomerDAO(user_address)
        self.form_DAO = FormDAO(form_address)
        self.supporter_DAO = SupporterDAO(supporter_address)
        self.categories = self.cat_DAO.read_from_database()
        self.reservations = []
        self.Users = self.customer_DAO.read_from_database()
        self.Forms = self.form_DAO.read_from_database()
        self.supporters = self.supporter_DAO.read_from_database()
    def isUserCorrect(self,passWord,userName):
        for user in self.Users:
            if user.checkID(userName) :
                if user.checkPass(passWord) :
                    return True
        raise Exception("Wrong username or password.")
    def addForm(self,user,tourism,duration,level):
        newForm = Form(user + ',' + tourism + ',' + duration + ',' + level)
        self.Forms.append(newForm)
        self.form_DAO.add_to_database(newForm)
    def usernameExists(self,username):
        for user in self.Users:
            if user.checkID(username) :
                raise Exception("Username exists!Choose another.")
        return False

    def addUser(self,username,passWord):
        newUser = Customer(username + ',' + passWord)
        self.Users.append(newUser)
        self.customer_DAO.add_to_database(newUser)

    def show_all_categories(self):
        cats_string = ""
        for c in self.categories:
            cats_string += (c.to_string())
        return cats_string
    
    def find_category_by_id(self, cat_id):
        for c in self.categories:
            if c.is_match(cat_id):
                return c
        raise Exception("The entered category ID is not valid\n")
    
    def find_package_by_id(self, pack_id):
        for c in self.categories:
            found_pack = c.find_package_by_id(pack_id)
            if found_pack:
                return found_pack
        raise Exception("The entered package ID is not valid\n") 
    
    def add_reservation(self, wanted_package, documents):
        new_reservation = Reservation(wanted_package, documents)
        return new_reservation
    
    def findSupporter(self):
        for supporter in self.supporters :
            if supporter.getStatus() == "free" :
                supporter.changestatus()
                return supporter.getName()
        raise Exception("No supporter available.\n")
    
    def addSupporterToData(self):
        self.supporter_DAO.emptyFile()
        for supporter in self.supporters :
            self.supporter_DAO.add_to_database(supporter)

    def finalize_res(self, reservation, card_info,username):
        reservation.pay(card_info)
        chosenSupporter = self.findSupporter()
        self.addSupporterToData()
        reservation.setUser(username)
        reservation.setSuppoerter(chosenSupporter)
        self.reservations.append(reservation)
        self.res_DAO.add_to_database(reservation)
        return reservation.to_string()

    



