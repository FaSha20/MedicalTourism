COSMETIC = 1
HEART = 2

class Package:
    counter = 0
    def __init__(self, category, info) -> None:
        Package.counter += 1
        info_list = info.split()
        self.id = Package.counter
        self.category = category
        self.has_tourism_side = info_list[0]
        self.duration = int(info_list[1])
        self.level = info_list[2]
        self.required_docs =  ["Identity card", "Passport"]

    def get_reguired_docs(self):
        if self.category == COSMETIC:
            self.required_docs.append("History of cosmetic surgery")
        elif self.category == HEART:
            self.required_docs.append("History of heart attack")
        return ','.join(self.required_docs)
    
    def calc_adoption(self, form_string):
        score = 0
        ts , d, l =  form_string.split()
        d = int(d)
        if ts == self.has_tourism_side:
            score += 1
        if self.duration - d < 5 : 
            score += (5 - self.duration + d)
        if l == self.level:
            score += 1

    def to_string(self):
        return ' '.join([self.has_tourism_side, str(self.duration), self.level])
        
    