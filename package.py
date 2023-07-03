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
        self.cost = self.calc_cost()
        

    def get_required_docs(self):
        if int(self.category) == COSMETIC:
            self.required_docs.append("History of cosmetic surgery")
        elif int(self.category) == HEART:
            self.required_docs.append("History of heart attack")
        return ','.join(self.required_docs)
    
    def calc_adaptation(self, form_string):
        score = 0
        ts , d, l =  form_string.split()
        d = int(d)
        if ts == self.has_tourism_side:
            score += 10
        if self.duration - d < 10 : 
            score += (5 - self.duration + d)
        if l == self.level:
            score += 5
        return score

    def to_string(self):
        return '\n'.join(["Package ID: "+ str(self.id), "Has tourism side: "+ self.has_tourism_side,
                          "Travel duration: "+ str(self.duration), "Travel level: "+self.level,
                          "Approximate cost: "+ str(self.cost) + "$"])
    
    def is_match(self, id):
        return (id == self.id)
    
    def calc_cost(self):
        cost = (self.duration * 10)
        if(self.level == "luxury"):
            cost += 1000
        elif(self.level == "midrange"):
            cost += 500
        else:
            cost += 200
        if(self.has_tourism_side):
            cost += 700
        return cost

    
        


        
    