from payment import Payment

class Reservation:
    def __init__(self, package, docs) -> None:
        self.package = package
        self.docs = docs
        self.status = "primary"
        self.total_cost = self.calc_total_cost()
        self.payment = None

    def calc_total_cost(self):
        # add %10 tax
        return self.package.calc_cost() * 1.1
    
    def pay(self, card_password):
        self.payment = Payment(self.total_cost, card_password)
        self.payment.start_transaction()
        

    def to_string(self):
        if self.payment :
            py = self.payment.to_string()
        else:
            py = "nothing"
        return '\n'.join(["# Package Info:\n"+self.package.to_string(), "# Documents:\n"+self.docs,
                          "# Status:\n"+self.status, "# Final Cost:\n"+str(self.total_cost)+"$", 
                          "#Payment:\n "+py])


class ReservationDAO:
    def __init__(self, address) -> None:
        self.res_address = address 

    def add_to_database(self, reservation):
        f = open(self.cat_address, "a")
        f.write(reservation.to_string())
        f.close()