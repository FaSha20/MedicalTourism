from package import Package

class Category:
    def __init__(self, data) -> None:
        all_info = data.split(',')
        self.id = all_info[0]
        self.info = all_info[1]
        self.packages = []
        for i in range(int(all_info[2])):
            p1 = Package(self.id, all_info[3+i])
            self.packages.append(p1)
    def to_string(self):
        return ' '.join([self.id, self.info])

class CategoryDAO:
    def __init__(self, address) -> None:
        self.cat_address = address

    # def add_to_database(self, cat):
    #     cat_info = ','.join([cat.id, cat.info, len(cat.packages), ])
    #     f = open(self.cat_address, "a")
    #     f.write(cat_info)
    #     f.close()

    def read_from_database(self):  
        cats = []      
        with open(self.cat_address, 'r') as infile:
            data = infile.readlines()
            for line in data:
                line = line[:-1]
                cats.append(Category(line))
        return cats
            