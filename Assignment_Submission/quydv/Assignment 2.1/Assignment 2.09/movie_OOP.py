#Classes and functions
class Movie:
    def __init__(self, org_name, trans_name, year, movie_list):
        self.org_name = org_name
        self.trans_name = trans_name
        self.year = year
        self.list = movie_list

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

    def movie_list_append(self):
        return self.list.append(self)


def display_movie_list(movie_list):
    for movie in movie_list:
        print(str.format("Movie#{0}", movie_list.index(movie)+1))
        movie.print()
        print("\n")

def remove_movie(movie, movie_list):
    movie_list.remove(movie)
    return movie_list

def search_movie_by_year(year, movie_list):
    filtered_list = []
    for movie in movie_list:
        if movie.create()["year"] == year:
            filtered_list.append(movie)
    return filtered_list

#List of movie list
m_list = []

#Create and add movie to list
movie1 = Movie("Dawn of Justice", "Công lý thức giấc", 2016, m_list)
movie1.movie_list_append()

movie2 = Movie("Zootopia", "Thành phố động vật", 2016, m_list)
movie2.movie_list_append()

movie3 = Movie("Whiplash", "Tay trống cự phách", 2015, m_list)
movie3.movie_list_append()


#Run and Display
display_movie_list(m_list)
##Removie movie
# remove_movie(movie3, m_list)
# display_movie_list(m_list)
#Search movie by year
movie_in_2016 = search_movie_by_year(2016, m_list)
display_movie_list(movie_in_2016)
