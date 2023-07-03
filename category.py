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
        return "Category id: " + self.id + "\n" + "About category: " +  self.info + "\n---------------\n"
    
    def is_match(self, id):
        return (id == self.id)
    
    def find_package_by_id(self, pack_id):
        for p in self.packages:
            if p.is_match(pack_id):
                return p
        return None
    
    def find_max_adaptation(self, form):
        max = 0
        best_package = None
        for p in self.packages:
            pa = p.calc_adaptation(form)
            if  pa > max:
                max = pa
                best_package = p
        return best_package

class CategoryDAO:
    def __init__(self, address) -> None:
        self.cat_address = address

    def read_from_database(self):  
        cats = []      
        with open(self.cat_address, 'r') as infile:
            data = infile.readlines()
            for line in data:
                line = line[:-1]
                cats.append(Category(line))
        return cats
    
    # def add_to_database(self, cat):
    #     cat_info = ','.join([cat.id, cat.info, len(cat.packages), ])
    #     f = open(self.cat_address, "a")
    #     f.write(cat_info)
    #     f.close()

            