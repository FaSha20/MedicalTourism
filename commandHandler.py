SHOW_ALL_CATEGORIES = 1
RESERVE_PACKAGE = 3
FIND_BEST_PACKAGE = 2
QUIT = 4

class CommandHandler:
    def __init__(self, medical_tourism_system) -> None:
        self.system = medical_tourism_system

    def handle(self, command):
        response = None
        if(command == SHOW_ALL_CATEGORIES):
            response = "--------All categories--------\n" + self.system.show_all_categories()

        elif(command == FIND_BEST_PACKAGE):
            cat_id = input("Enter category ID: ")
            wanted_category = self.system.find_category_by_id(cat_id)
            if(wanted_category == None):
                raise Exception("The entered category ID is not valid")
            has_tourism = input("Please fill the form below base on you priorities: \nDo you want to visit places besides treatment?(yes / no) : ")
            duration = input("How many days can you devote to traveling?(a number) : ")
            level = input("ٌWhat level of travel do you want?(laxury / midrange / economy) : ")
            best_pack = wanted_category.find_max_adaptation(has_tourism + " " + duration + " " + level)
            response = "\n-This is the most similar package we've found:\n" + best_pack.to_string() 

        elif(command == RESERVE_PACKAGE):
            pass


        else:
            raise Exception("Out of bounds.")
        
        return response
        