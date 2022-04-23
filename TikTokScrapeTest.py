from TkScrapper import TkScrapper
from SaveDB import SaveDB
from datetime import datetime

search_dt= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
search_kw = "@naomineo"
print("Begin Scrapping video. keyword: {} datetime: {}".format(search_kw, search_dt))

## Step1: scrape data
scrapper = TkScrapper()
v_count = 10
video_info_list = scrapper.search_video(keyword= search_kw, count= v_count)

print("Success! search video info of keyword: {}".format(search_kw))

## For testing only: read data from json
# json_path = "data/search_user_video_info_naomineo_20220417.json"
# with open(json_path, 'r') as fh:
#     video_info_list = json.load(fh)
#
# print("Success! read video_info_list")


## Step2: save data to db
search_info = dict(search_dt= search_dt, search_kw = search_kw)
saveDb = SaveDB()
saveDb.connect_db()
saveDb.save_search_video_data(search_info, video_info_list)
print("DONE!")