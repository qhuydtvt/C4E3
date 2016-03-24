class Movie:
    def display_movie(self):
        print("Original name:", self.org)
        print("Translated name:", self.trans)
        print("Year:", self.year)

    def __init__(self, o, t, y):
        self.org = o
        self.trans = t
        self.year = y

movie_list = [
    Movie("The hunger game", "Đấu trường sinh tử", 2016),
    Movie("Little door gods", "Tiểu môn thần", 2015),
    Movie("Break point", "Ranh giới chết", 2015)
]

for movie in movie_list:
        movie.display_movie()

