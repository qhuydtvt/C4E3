class Movie:
    def print(self):
        print("Original name:", self.name)
        print("Translated name:", self.trans)
        print("Year:", self.year)
 
    def __init__(self, n, t, y):
        self.name = n
        self.trans = t
        self.year = y

                 
Movie1= Movie("The hunger games", "Dau truong sinh tu", 2016)
Movie1.print()
Movie2= Movie("Little door gods", "Tieu mon than", 2015)
movie_list = [Movie1,Movie2]
i=1
for m in movie_list:
    print(str.format("Movie #{0}",i))
    m.print()
    i=i+1

Movie3= Movie("Break point", "Ranh gioi chet", 2015)
Movie_list2 = [Movie1,Movie2,Movie3]

