import random

class Payment:
    def __init__(self, cost, card_password) -> None:
        self.cost = cost
        self.password = card_password
        self.receipt = None

    def start_transaction(self):
        self.check_password_validation()
        self.check_balance()
        self.receipt = "Result: Successfull transaction!\n"+ "cost: "+ str(self.cost) + "\n" 

    def check_password_validation(self):
        if len(self.password) != 4:
            self.receipt = "Result: Unsuccessfull transaction!\n"+ "cost: "+ str(self.cost) + "\n"
            raise Exception("Invalid password!")
    
    def check_balance(self):
        num = random.random()%10
        if(num > 7 ):
            self.receipt = "Result: Unsuccessfull transaction!\n"+ "cost: "+ str(self.cost) + "\n"
            raise Exception("Not enough inventory!")

    def to_string(self):
        return self.receipt
