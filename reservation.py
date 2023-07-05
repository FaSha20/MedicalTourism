from payment import Payment

class Reservation:
    def __init__(self, package, docs) -> None:
        self.package = package
        self.docs = docs
        self.status = "PRIMARY"
        self.total_cost = self.calc_total_cost()
        self.payment = None
        self.supporter = None
        self.user = None

    def calc_total_cost(self):
        # add %10 tax
        return self.package.calc_cost() * 1.1
    
    def pay(self, card_password):
        self.payment = Payment(self.total_cost, card_password)
        self.payment.start_transaction()
        self.status = "FINAL"
        
    def to_string1(self):
        if self.payment :
            py = self.payment.to_string()
        else:
            py = "Nothing was paid."
        return '\n'.join(["# Package Info:\n"+self.package.to_string(), "\n# Documents:\n"+self.docs,
                          "\n# Status:\n"+self.status, "\n# Final Cost:\n"+str(self.total_cost)+"$", 
                          "\n# Payment:\n "+py])
    def to_string(self):
        if self.payment :
            py = self.payment.to_string()
        else:
            py = "Nothing was paid."
        return '\n'.join(["# Supporter:\n" + self.supporter +"\n# User:\n"+ self.user+"\n# Package Info:\n"+self.package.to_string(), "\n# Documents:\n"+self.docs,
                          "\n# Status:\n"+self.status, "\n# Final Cost:\n"+str(self.total_cost)+"$", 
                          "\n# Payment:\n "+py])
    
    def setUser(self,username):
        self.user = username

    def setSuppoerter(self,supporter):
        self.supporter = supporter

class ReservationDAO:
    def __init__(self, address) -> None:
        self.res_address = address 

    def add_to_database(self, reservation):
        f = open(self.res_address, "a")
        f.write(reservation.to_string()+"\n\n")
        f.close()