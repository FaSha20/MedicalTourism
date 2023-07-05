class Supporter : 
    def __init__(self,line):
        self.name ,self.status = line.split(',')

    def getStatus(self) :
        return self.status
    
    def getName(self):
        return self.name
    def changestatus(self) :
        self.status = "full"
    
    def to_string(slef) :
        return '\n'.join([slef.name + ',' + slef.status])



class SupporterDAO : 
    def __init__(self,address) :
        self.address = address
    
    def emptyFile(self):
        f = open(self.address, "w")
        f.close()

    def add_to_database(self, supporter):
        f = open(self.address, "a")
        f.write(supporter.to_string()+'\n')
        f.close()

    def read_from_database(self):
        supporters = []
        with open(self.address, 'r') as infile:
            data = infile.readlines()
            for line in data:
                line = line[:-1]
                supporters.append(Supporter(line))
        return supporters