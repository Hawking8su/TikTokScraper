

from TikTokApi import TikTokApi
import json
import os
from datetime import datetime


class TkScrapper:
    ## Write python object to json file
    def write_json(self, json_str="", out_file=""):
        with open(out_file, 'w') as outfile:
            json.dump(json_str, outfile)


    ##  Download user info
    def get_user_info_full(self, username=""):
        with TikTokApi(custom_verify_fp=os.environ.get("verifyFp", None)) as api:
            return api.user(username=username).info_full()


    def download_user_info(self, username=""):
        try:
            user_info = self.get_user_info_full(username)
            out_file = "./data/user_info_{}_{}.json".format(username, datetime.now().strftime("%Y%m%d"))
            self.write_json(user_info, out_file)
            print("Success! user info saved to {}".format(out_file))
        except Exception as e:
            print("Errors:", e)

    ## Download user video info
    ## Note: user.video() is not working, use search.video() instead
    def search_video(self, keyword="", count=10):
        out_video_list = []
        i = 0
        with TikTokApi(custom_verify_fp=os.environ.get("verifyFp", None)) as api:
            for video_info in api.search.videos(keyword, count=count):
                out_video_list.append(video_info.info_full())
                print("Get {} video info".format(i))
                i += 1
                if i >= count: break
        return out_video_list

    def download_video_info(self, keyword = "", count=10):
        try:
            out_video_list = self.search_user_video(keyword, count)
            out_file = "./data/search_user_video_info_{}_{}.json".format(keyword, datetime.now().strftime("%Y%m%d"))
            self.write_json(out_video_list, out_file)
            print("Success! search user video info saved to {}".format(out_file))
        except Exception as e:
            print("Errors:", e)

if __name__ == "__main__":
    # create data folder
    if not os.path.exists('./data'):
        os.makedirs('./data')
    # download user info and save to json
    username = 'naomineo'
    search_kw = "@"+username
    tkScrapper = TkScrapper()
    # tkScrapper.download_user_info(username)
    tkScrapper.download_video_info(username, count = 10)