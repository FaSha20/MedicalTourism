
SHOW_ALL_CATEGORIES = 1
RESERVE_PACKAGE = 3
FIND_BEST_PACKAGE = 2
QUIT = 4
SIGNUP = "sign up"
SIGNIN = "sign in"

class CommandHandler:
    def __init__(self, medical_tourism_system) -> None:
        self.system = medical_tourism_system
        self.entered_user = None
    
    def customerHndl(self,username,password,command):
        respons = None
        if command == SIGNIN :
            if self.system.isUserCorrect(password,username) :
                self.entered_user = username
                respons = "You have successfully logged in.\n"
        elif command == SIGNUP : 
            if self.system.usernameExists(username) == False :
                self.system.addUser(username,password)
                self.entered_user = username
                respons = "You have successfully signed up.\n"
        else:
            raise Exception("Out of bound choice")
        
        return respons

    def handle(self, command):
        response = None
        if(command == SHOW_ALL_CATEGORIES):
            response = "--------All categories--------\n" + self.system.show_all_categories()

        elif(command == FIND_BEST_PACKAGE):
            cat_id = input("Enter category ID: ")
            wanted_category = self.system.find_category_by_id(cat_id)
          
            while True :
                has_tourism = input("Please fill the form below base on you priorities: \nDo you want to visit places besides treatment?(yes / no) : ")
                if has_tourism != "yes" and has_tourism != "no" :
                    print("Wrong input! Try again.\n")
                else :
                    break
            duration = input("How many days can you devote to traveling?(a number) : ")
            while True :
                level = input("ٌWhat level of travel do you want?(laxury / midrange / economy) : ")
                if level != "laxury" and level != "midrange" and level !="economy" : 
                    print("Wrong input! Try again.\n")
                else :
                    break
            self.system.addForm(self.entered_user,has_tourism,duration,level)
            best_pack = wanted_category.find_max_adaptation(has_tourism + " " + duration + " " + level)
            response = "\n-This is the most similar package we've found:\n" + best_pack.to_string() 

        elif(command == RESERVE_PACKAGE):
            pack_id = int(input("Enter package ID: "))
            wanted_package = self.system.find_package_by_id(pack_id)
           
            rqu_docs = wanted_package.get_required_docs()
            print("To continue reservation, please upload these documents: "+ rqu_docs + "\n(done): ")
            documents = input()
            new_reservation = self.system.add_reservation(wanted_package, documents)
            feedback = input("-This is your reservation: \n"+ new_reservation.to_string1() +"\nDo you want to finalize it? (yes/no): ")
            if feedback == "yes":
                card_info = input("Enter your credit card password (4 digits) : ")
                report = self.system.finalize_res(new_reservation, card_info,self.entered_user)
                response = "\n-Your final Reservation:\n"+ report
            
        else:
            raise Exception("Out of bound choice")
        
        return response
        