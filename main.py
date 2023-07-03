from commandHandler import CommandHandler,  QUIT
from medicalTourism import MedicalTourism



class Main:
    def __init__(self) -> None:
        pass
    def greeting(self):
        print("Hello :)\nWelcome to our Medical Tourism world !")  
        
    def run(self):
        mt = MedicalTourism()
        ch = CommandHandler(mt)

        while True:
            choice = int(input("""
    What do you want to do?
    1) See all Medical Categories 
    2) Find appropriate package
    3) Reserve a Package
    4) Quit
    Your choice :  """))
            if (choice == QUIT):
                print("\nbye bye ^^\n")
                break

            try:
                response = ch.handle(choice)
                print(response)
                
            except Exception as e:
                print("ERROR: ", e)
            

if __name__=="__main__":
    system = Main()
    system.greeting()
    system.run()
        