class movie:
    def __init__(self,ori,trans,year):
        self.ori = ori
        self.trans = trans
        self.year = year
    def foot(self):
        print('Gobble')
    def say(self):
        pass
    
    
m = movie('Secret', 'Bi Mat Khong The Noi', 2015)
if(not(hasattr(m , 'Secret'))):
    setattr(m,'Secret', ('Bi Mat Khong The Noi' ))
    setattr(m,'Secret',('Bi Mat Khong The Noi' , 2015))
print('Original name : ', m.ori)
print('Translated name : ', m.trans)
print('Year : ', m.year)

        
