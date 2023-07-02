from commandHandler import CommandHandler

class MedicalTourism:
    def __init__(self) -> None:
        pass
    def greeting(self):
        print("""Hello :)\nWelcome to our Medical Tourism world !\nWhat do you want to do?
            1) See all Medical Categories 
            2) Reserve a Package
            3) Find appropriate package
            """)  
    def run(self):

        ch = CommandHandler()

        while True:
            choice = int(input("Your choice :  "))
            ch.handle(choice)


if __name__=="__main__":
    system = MedicalTourism()
    system.greeting()
    system.run()
        