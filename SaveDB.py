import mysql.connector
import json


class SaveDB:
    '''
    Save TikTok data into Mysql database
    '''
    def __init__(self):
        self.conn = mysql.connector.connection
        self.dbname = "tiktokdb"

    def __del__(self):
        if self.conn:
            self.conn.close()

    def connect_db(self):
        '''
        Connect to Mysql database
        :param connect_str:
        :return:
        '''
        # todo: parse input connect_string
        try:
            self.conn = mysql.connector.connect(
                host= "127.0.0.1",
                port= "3307",
                user= "root",
                passwd= "111222",
                database= self.dbname,
                buffered= True
            )
            print("Success! connect mysql db: {}".format(self.dbname))
        except mysql.connector.Error as error:
            self.conn = None
            print("Failure! connect mysql db: {} - Error: {}".format(self.dbname,error))


    def save_search_video_data(self, search_info = {}, video_info_list=[], stats_only=0):
        '''
        Save video data into related tables.
        :param search_info: dict
        :param video_info_list: list of dict
        :param stats_only: 0-save info and stats, 1- save only stats
        :return:
        '''
        sql_add_video_json = ("INSERT INTO search_video_info_json "
                        "(search_dt, search_kw, result_no, result_json) "
                        "VALUES (%s, %s, %s, %s)")
        sql_add_video_info = ("INSERT INTO search_video_info "
                        "(search_dt, search_kw, result_no, video_id, video_desc, create_time, height, width, duration, author_id, author_unique_id, music_id, music_title) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        sql_add_video_stats = ("INSERT INTO search_video_stats "
                        "(search_dt, search_kw, result_no, video_id, digg_count, share_count, comment_count, play_count) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        video_json_data = []
        video_info_data = []
        video_stats = []
        sno = 0
        for video_info in video_info_list:
            sno += 1
            video_json_data.append(
                (
                    search_info["search_dt"],
                    search_info["search_kw"],
                    sno,
                    json.dumps(video_info)
                )
            )
            if video_info['statusCode'] != 0: continue
            if stats_only == 0:
                video_info_data.append(
                    (
                        search_info["search_dt"],
                        search_info["search_kw"],
                        sno,
                        video_info["itemInfo"]["itemStruct"]["id"],
                        "",
                        # video_info["itemInfo"]["itemStruct"]["desc"], # todo: having trouble saving emoji characters
                        video_info["itemInfo"]["itemStruct"]["createTime"],
                        video_info["itemInfo"]["itemStruct"]["video"]["height"],
                        video_info["itemInfo"]["itemStruct"]["video"]["width"],
                        video_info["itemInfo"]["itemStruct"]["video"]["duration"],
                        video_info["itemInfo"]["itemStruct"]["author"]["id"],
                        video_info["itemInfo"]["itemStruct"]["author"]["uniqueId"],
                        video_info["itemInfo"]["itemStruct"]["music"]["id"],
                        ""
                        # video_info["itemInfo"]["itemStruct"]["music"]["title"] # todo: having trouble saving emoji characters
                    )
                )
            video_stats.append(
                (
                    search_info["search_dt"],
                    search_info["search_kw"],
                    sno,
                    video_info["itemInfo"]["itemStruct"]["id"],
                    video_info["itemInfo"]["itemStruct"]["stats"]["diggCount"],
                    video_info["itemInfo"]["itemStruct"]["stats"]["shareCount"],
                    video_info["itemInfo"]["itemStruct"]["stats"]["commentCount"],
                    video_info["itemInfo"]["itemStruct"]["stats"]["playCount"]
                )
            )

        print("Success! construct input data.")
        try:
            db_cursor = self.conn.cursor()
            db_cursor.executemany(sql_add_video_json, video_json_data)
            self.conn.commit()
            print("Success! execute sql command: {}".format(sql_add_video_json))
            db_cursor.executemany(sql_add_video_info, video_info_data)
            self.conn.commit()
            print("Success! execute sql command: {}".format(sql_add_video_info))
            db_cursor.executemany(sql_add_video_stats, video_stats)
            self.conn.commit()
            print("Success! execute sql command: {}".format(sql_add_video_stats))
        except Exception as error:
            print("Failure! execute sql command. Error: {}".format(error))