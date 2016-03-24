class Movie:
    def __init__(self,o,t,y):
        self.org = o
        self.trans = t
        self.year = y
        self.list = []
    def create_movie(self):
        m = {
            'org_name': self.org,
            'trans_name': self.trans,
            'year': self.year
        }
        return m
    def display_movie(self, m):
        print("Original name: ",m['org_name'])
        print("Translated name: ",m["trans_name"])
        print("Year: ",m['year'])
        print()
    def movie_list(self,n):
        movie = n
        self.list.append(movie)
        print(self.list)
        return self.list
    def display_movie_list(self, m_list):
        for i in m_list:
            print("Movie#", m_list.index(i)+1)
            print("Original name: ",i['org_name'])
            print("Translated name: ",i["trans_name"])
            print("Year: ",i['year'])
            print()
    def remove_movie(self,m_list,movie):
        m_list.remove(movie)
    def search_movie_by_year(self, m_list, year):
        n = []
        for i in m_list:
            if i['year']==year:
                n.append(i)
        print(n)
        return n

m = Movie("HG","Dau truong sinh tu",2016)
m.create_movie()
m.display_movie(m.create_movie())
m.movie_list(m.create_movie())

n = Movie("abc","cde",2016)
c = n.create_movie()
a = m.movie_list(c)

m.display_movie_list(a)

m.remove_movie(a,c)
m.display_movie_list(a)

d = Movie("Little Door Gods", "Tieu Mon Than", 2015)
e = Movie("Break point", "Ranh gioi chet", 2015)
m.movie_list(d.create_movie())
a = m.movie_list(e.create_movie())

print("------------------")
m.search_movie_by_year(a,2015)

