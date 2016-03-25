from bs4 import BeautifulSoup

file = open("VNExpress.htm", "rb")
vnexpress = file.read()
vnexpress_string = vnexpress.decode("utf-8")

soup = BeautifulSoup(vnexpress_string, "html.parser")

hot_news_divs = soup.find_all("div", "box_sub_hot_news", "scroll-pane")

for div in hot_news_divs:
    all_a = div.find_all("a")
    i = 1
    for a in all_a:
        print(str(i) + ".", a.contents[0])
        i += 1






