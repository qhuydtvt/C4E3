class movie:
    def __init__(self, org_name,trans_name,year):
        self.org_name = org_name
        self.trans_name= trans_name
        self.year= year
    def display_movie(self):
        print(" Original name: ", self.org_name)
        print("Translated name: ", self.trans_name)
        print("Year: ", self.year)
class movie_list:
    def __init__(self,my_list):
        self.my_list=''
    def display_movielist(self,m_list):
        idx=1
        for movie in m_list:
            print(str.format('Movie#{0}',idx))
            movie.display_movie()
            idx=idx+1
    def search_movie_bt_year(self,m_list,year):
        L=[]
        for movie in m_list:
            if movie.year==year:
                L.append(movie)
        return L
        

a=[movie('the hunger game','dau truong sinh tu',2015),
              movie('litle door gods','tieu mon than',2014),
              movie('break point','ranh gioi chet',2015)]
p1=movie_list(a) 
p1.display_movielist(a)
k= p1.search_movie_bt_year(a,2014)
p1.display_movielist(k)
