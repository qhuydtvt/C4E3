import urllib3
import json
import certifi
import re

def download_webpage (url):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    r = http.request("GET", url)
    return r.data
def extract_username(url):
	return re.search(r'https://www.facebook.com/([^/?]+)', url).group(1)

def build_post_url ():
    url=input("Nhập trang facebook url của trang đối thủ: ") #nhập rồi sau đó cách một cái
    username=extract_username(url)
    graph_facebook = "https://graph.facebook.com/"
    link_end = "/posts/?key=value&access_token="
    app_id = "1592298727726686"
    app_secret = "93c85459b4a55a1c9316bfe0aebc97c5"
    post_url = graph_facebook+ username+ link_end + app_id + "|" + app_secret
    print (post_url)
    return post_url

content=download_webpage(build_post_url())

decoded_content = content.decode("utf-8")

json_postdata = json.loads(decoded_content) #root
json_fbposts = json_postdata['data']
posts=[]
for each_dictionary_in_list in json_postdata["data"]:
    keys = each_dictionary_in_list.keys()
    for each_key in keys:
        if each_key == "message":
           status=each_dictionary_in_list["message"]
           posts.append(status)
           #id
        #created_time

keywords = ["game", "sự kiện", "trúng thưởng", "quay số", "combo", "tiết kiệm", "lì xì", "event","tặng","miễn phí","Mua 1 tặng", "GIẢM GIÁ",
            "KHUYẾN MÃI", "KHUYẾN MẠI", "SHARE", "TAG", "EVENT"]
text = posts

found_posts = []
for keyword in keywords:
    for post in posts:
        if re.search(keyword, post) and post not in found_posts:
            found_posts.append(post)

for post in found_posts:
    print("************************************************")
    print("/////////////////////////////////////////////////")
    print(post)

