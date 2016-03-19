movie_list = [
    {"org_name": "Dawn of Justice",
     "trans_name": "Cong ly thuc giac",
     "year": "2016",
     "quality": "HD"
        },
    {"org_name": "Captain America: Civil War",
     "trans_name": "Doi truong My: Noi chien",
     "year": "2016",
     "quality": "HD"
        }
    ]

def print_movie():
    for i in range(len(movie_list)):
        print(str.format("{0}. {1} ({2}) {3}\n{4}\n", i + 1, movie_list[i]["org_name"], movie_list[i]["year"], movie_list[i]["quality"], movie_list[i]["trans_name"]))
print_movie()

def add_movie():
    org_name = input("Original name: ")
    trans_name = input("Movie name translated into Vietnamese: ")
    year = input("Release in year: ")
    quality = input("Quality: ")
    movie_list.append({"org_name": org_name, "trans_name": trans_name, "year": year, "quality": quality})
    print_movie()

def edit_movie():
    edit_movie = input("Which movie do you want to edit?")
    for i in range(len(movie_list)):
        if edit_movie == movie_list[i]["org_name"] or edit_movie == movie_list[i]["trans_name"]:
            edit_info = input("Which info you want to edit (original name, translated name, year or quality)?")
            if edit_info == "original name":
                edit_info = "org_name"
            elif edit_info == "translated name":
                edit_info = "trans_name"
            new_info = input("Please enter your correction: ")
            movie_list[i][edit_info] = new_info
    print_movie()
    
def remove_movie():
    remove_movie = input("Which movie do you want to remove?")
    for movie in movie_list:
        if remove_movie == movie["org_name"] or remove_movie == movie["trans_name"]:
            movie_list.remove(movie)
    print_movie()

action = input("What do you want (add/edit/remove) movie? ")
if action == "add":
    add_movie()
elif action == "edit":
    edit_movie()
elif action == "remove":
    remove_movie()
