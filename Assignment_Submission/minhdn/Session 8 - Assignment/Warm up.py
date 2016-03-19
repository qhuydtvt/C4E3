#
def display_movie(m):
    print("Original name:", m["org_name"])
    print("Translated name:", m["trans_name"])
    print("Year:", m["year"])
    print()

def creat_movie(org_name, trans_name, year):
    return {
        "org_name": org_name,
        "trans_name": trans_name,
        "year": year
        }

movie0 = creat_movie("The hunger game", "Đấu trường sinh tử", 2016)
display_movie(movie0)

#
##def display_movie_list(m_list):
##    i = 1
##    for movie in m_list:
##        print(str.format("Movie#{0}", i))
##        display_movie(movie)
##        i += 1

def display_movie_list(m_list):
    for i in range(len(m_list)):
        print(str.format("Movie#{0}", i+1))
        display_movie(m_list[i])

movie_list = []
movie0 = creat_movie("The hunger game", "Đấu trường sinh tử", 2016)
movie1 = creat_movie("Little door gods", "Tiểu môn thần", 2015)

movie_list.append(movie0)
movie_list.append(movie1)
display_movie_list(movie_list)

#
def remove_movie(m_list, movie):
    m_list.remove(movie)

##movie0 = creat_movie("The hunger game", "Đấu trường sinh tử", 2016)
##movie1 = creat_movie("Little door gods", "Tiểu môn thần", 2015)
##movie_list = [movie0, movie1]

remove_movie(movie_list, movie0)
display_movie_list(movie_list)

#
def search_movie_by_year(m_list, year):
    lis = []
    for i in range(len(m_list)):
        if year == m_list[i]["year"]:
            lis.append(m_list[i])
    return lis

##    return_list = []
##    for m in m_list:
##        if m[ "year"] == year:
##            return_list.append(m)
##    return return_list

##movie_list = []
##movie_list.append(creat_movie("The hunger games", "Đấu trường sinh tử", 2016))
##movie_list.append(creat_movie("Little Door Gods", "Tiểu Môn Thần", 2015))
movie_list.append(creat_movie("Break point", "Ranh giới chết", 2015))

movie_in_2015 = search_movie_by_year(movie_list, 2015)
display_movie_list(movie_in_2015)
            
            


