from reservation import Reservation
class Customer : 
    def __init__(self,line) -> None:
        user , pas = line.split(',')
        self.passWord = pas
        self.id = user

    def checkID(self,newID):
        if newID == self.id  :
            return True
        else:
            return False
        
    def checkPass(self,newPass):
        if newPass==self.passWord:
            return True
        else : 
            return False
        
    def to_string(self):
        return '\n'.join([self.id + ',' + self.passWord])



class CustomerDAO : 
    def __init__(self,address) -> None:
        self.address = address

    def add_to_database(self, customer):
        f = open(self.address, "a")
        f.write(customer.to_string()+ '\n')
        f.close()

    def read_from_database(self):
        users = []
        with open(self.address, 'r') as infile:
            data = infile.readlines()
            for line in data:
                line = line[:-1]
                users.append(Customer(line))
        return users