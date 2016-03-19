###về nhà chuyển hết toàn bộ các def trong bài warm-up thành class
##
### dùng thư viện xlrd của python để xử lý file excel. sau đó gửi mail hàng loạt cho mọi người
##
##def display_movie(m):
## print("Original name: ", m["org_name"])
## print("Translated name: ", m["trans_name"])
## print("Year: ", m["year"])
## print()
##def create_movie(org_name, trans_name, year):
## return {
## "org_name": org_name,
## "trans_name": trans_name,
## "year": year
## }
##
##
##def display_movie_list(m_list):
##    i=0
##    for movie in m_list:
##        print("Movie#",i+1)
##        display_movie(movie)
##        i=i+1
##movie_list=[]
##movie0 = create_movie("The hunger games", "Đấu trường sinh tử",
##2016)
##movie1 = create_movie("Little Door Gods", "Tiểu Môn Thần", 2015)
##
##def remove_movie(m_list, movie):
##    m_list.remove(movie)
##movie0 = create_movie("The hunger games", "Đấu trường sinh tử",2016)
##movie1 = create_movie("Little Door Gods", "Tiểu Môn Thần", 2015)
##movie_list = [movie0, movie1]
###remove_movie(movie_list, movie0)
###display_movie_list(movie_list)
##
##def search_movie_by_year(m_list, year):
##    list_search =[]
##    for movie in m_list:
##        if movie["year"]==year:
##            list_search.append(movie)
##    return list_search
##movie_list=[]
##movie_list.append(create_movie("The hunger games", "Đấu trường sinh tử", 2016))
##movie_list.append(create_movie("Break point", "Ranh giới chết",2015))
##movie_list.append(create_movie("Little Door Gods", "Tiểu Môn Thần",2015))
##movie_in_2015 = search_movie_by_year(movie_list, 2015)
###display_movie_list(movie_in_2015)



class Movie:
    def __init__(self, org_name, trans_name,year):
        self.org_name = org_name
        self.trans_name = trans_name
        self.year = year 
    def display(self):
        print("Original name: ",self.org_name)
        print("Translated name: ", self.trans_name)
        print("Year: ", self.year)
        print()

movie0 = Movie("The hunger games", "Đấu trường sinh tử",2016)
movie1 = Movie("Little Door Gods", "Tiểu Môn Thần", 2015)

movie_list = [movie0,movie1]

def display_movie_list(m_list):
    for movie in m_list:
        movie.display()

def remove_movie(m_list, movie):
    m_list.remove(movie)

#remove_movie(movie_list, movie0)
#display_movie_list(movie_list)

def search_movie_by_year(m_list, year):
    list_search =[]
    for movie in m_list:
        
        if movie.year==year:
            #print(year)
            list_search.append(movie)
    return list_search


movie0= Movie("The hunger games", "Đấu trường sinh tử", 2016)
movie1= Movie("Break point", "Ranh giới chết",2015)
movie2= Movie("Little Door Gods", "Tiểu Môn Thần",2015)
movie_list=[movie0,movie1,movie2]

movie_in_2015 = search_movie_by_year(movie_list, 2015)
display_movie_list(movie_in_2015)
