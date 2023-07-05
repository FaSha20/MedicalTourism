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

        while True :
            entered = input("Do you want to sign up/sign in ? ")
            if entered == "sign in" or entered == "sign up": 
                    print("Enter your username and password :")
                    username = input("Username : ")
                    passWord = input("PassWord : ")
                    try:
                        respons = ch.customerHndl(username,passWord,entered)
                        print(respons)
                        break
                    except Exception as e:
                        print("ERROR: ", e)
                        continue
            else :
                print("Wrong input. Try agian.\n")
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
        