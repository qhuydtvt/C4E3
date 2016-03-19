##class person:
##    def __init__(self,a,b):
##        self.name=''
##        self.age=-1
##    def print(self,a,b):
##        print('name: ',self.name)
##        print('age: ', self.age)
##
##p=person("Minh",18)
##p.name='Minh Ham'
##p.age=16
##p.print("Minh",18)

class display_movie:
    def __init__(self):
        self.org_name=''
        self.trans_name=''
        self.year=1
    def print(self):
        print('Orighinal name: ',self.org_name)
        print('Translated name: ',self.trans_name)
        print('Year: ',self.year)

class display_movie_list:
    def __init__(self,m_list):
        self.m_list=''
        self.display_movie=''
    def print(self,m_list):
        idx=1
        for movie in m_list:
            print(str.format('Movie# {0}',idx))
            self.display_movie(movie)
            idx+=1

class search_movie_by_year:
    def __init__(self,m_list,year):
        self.search_movie_by_year=''
        self.year=1
        self.m_list=''
    def print(self,m_list,year):
        n=[]
        for i in m_list:
            if i['year']==year:
                n.append(i)
            return (n)
        
