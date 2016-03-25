from bs4 import BeautifulSoup
import urllib.request
import xlwt

vnexpress_url = "http://vnexpress.net"

web_page = urllib.request.urlopen(vnexpress_url)
html = web_page.read()
html_string = html.decode("utf-8")

soup = BeautifulSoup(html_string, "html.parser")

hot_news_divs = soup.find_all("div", "box_sub_hot_news", "scroll-pane")

for div in hot_news_divs:
    all_a = div.find_all("a")
    for n in range(0, len(all_a) - 3):
        print(str(n+1) + ".", all_a[n].contents[0])

wb = xlwt.Workbook()
ws = wb.add_sheet("VNExpress_hot_news")

for hot_news in hot_news_divs:
    for i in range(len(all_a) - 3):
        ws.write(i, 0, str(i+1) + "." + hot_news.find_all("a")[i].contents[0])
    # r = 0
    # for a in hot_news.find_all("a"):
    #     ws.write(r, 0, a.contents[0])
    #     r += 1

wb.save("VNExpress.xls")
