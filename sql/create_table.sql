-- create tables
use tiktokdb;

create table if not exists search_video_info_json (
    id INT NOT NULL AUTO_INCREMENT primary key ,
    search_dt varchar(50) NOT NUll comment 'search datetime',
    search_kw varchar(500) NOT NULL COMMENT 'search keyword',
    result_no INT NOT NULL COMMENT 'result video no',
    result_json TEXT NULL COMMENT 'result json',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)
;

alter table search_video_info_json add constraint
    unique key uk_search_dt_kw_no (search_dt, search_kw, result_no);

-- PK: id
-- UK: search_dt, search_kw, video_no
# todo: add unique key
create table if not exists search_video_info(
    id int not null auto_increment primary key ,
    search_dt varchar(50) not null comment 'search datetime',
    search_kw varchar(500) not null comment 'search keyword',
    result_no int not null comment 'result video no',
    video_id varchar(50) not null,
    video_desc varchar(500) not null,
    create_time bigint not null,
    height int not null,
    width int not null,
    duration int not null,
    author_id varchar(100) not null,
    author_unique_id varchar(200) not null,
    music_id varchar(200) not null,
    music_title varchar(500) not null,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)
;

# todo: add unique key
# drop table if exists search_video_stats;
create table if not exists search_video_stats(
    id int not null auto_increment primary key ,
    search_dt varchar(50) not null comment 'search datetime',
    search_kw varchar(500) not null comment 'search keyword',
    result_no int not null comment 'result video no',
    video_id varchar(50) not null,
    digg_count bigint not null,
    share_count bigint not null,
    comment_count bigint not null,
    play_count bigint not null,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)
;

# show tables;

