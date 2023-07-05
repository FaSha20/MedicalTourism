class Form :
    def __init__(self,line) -> None:
        # self.askQuestions()
        # self.user = None
        data = line.split(',')
        self.user = data[0]
        self.tourism = data[1]
        self.duration  = data[2]
        self.level = data[3]
    def setUser(self,user):
        self.user = user

    def to_string(self):
        return '\n'.join([self.user + ',' + self.tourism + ',' + self.duration + ',' + self.level])




class FormDAO:
    def __init__(self,address) -> None:
        self.address = address

    def add_to_database(self, form):
        f = open(self.address, "a")
        f.write(form.to_string()+'\n')
        f.close()

    def read_from_database(self):
        forms = []
        with open(self.address, 'r') as infile:
            data = infile.readlines()
            for line in data:
                line = line[:-1]
                forms.append(Form(line))
        return forms