class Movie:
    def __init__(self, org_name, trans_name, year):
        self.org_name = org_name
        self.trans_name = trans_name
        self.year = year
                    
    def create(self):
        movie = {
        "org_name": self.org_name,
        "trans_name": self.trans_name,
        "year": self.year
        }
        return movie
    
    def print(self):
        print("Original name:", self.org_name)
        print("Translated name:", self.trans_name)
        print("Year:", self.year)

movie1 = Movie("Dawn of Justice", "Cong ly thuc giac", 2016)
movie2 = Movie("Zootopia", "Thanh pho dong vat", 2016)
movie3 = Movie("Kungfu Panda 3", "Cong phu gau truc 3", 2016)
movie4 = Movie("The Revenant", "Nguoi ve tu coi chet", 2015)

##class Movie_list:
##    def __init__(self):
##        self = []      
##        
##    def movie_list_append(self, movie):
##        self.append(movie)
##
##    def display_movie_list(movie_list):
##        for movie in movie_list:
##            print(str.format("Movie#{0}", movie_list.index(movie) + 1))
##            movie.print()
##            print("\n")
##
##m_list = Movie_list()
##m_list.movie_list_append(movie1)
##display_movie_list(m_list)
        
m_list = []
m_list.append(movie1)
m_list.append(movie2)
m_list.append(movie3)
m_list.append(movie4)

def display_movie_list(movie_list):
    for movie in movie_list:
        print(str.format("Movie#{0}", movie_list.index(movie) + 1))
        movie.print()
        print("\n")

print("Print initial movie list:")
display_movie_list(m_list)
m_list.remove(movie3)
print("Print movie list after removing Kungfu Panda 3:")
display_movie_list(m_list)

def search_movie_by_year(movie_list, year):
    filtered_list = []
    for movie in movie_list:
        if year == movie.create()["year"]:
            filtered_list.append(movie)
    return filtered_list

movie_in_2016 = search_movie_by_year(m_list, 2016)
print("Print movie in 2016:")
display_movie_list(movie_in_2016)
            
