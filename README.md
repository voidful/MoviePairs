**Get Conversation Pairs from movie subtitle( 獲取電影對白 )**  
- put all srt file into data directory  
- Run main.py  
- Output pair.txt  

**Crawler subtitle from zimuku**  

Before you start :  

Install scrapy
```
yum install libffi-devel  
yum install openssl-devel  
pip install scrapy  
```
Config spider  
Edit subtitle/subtitle_crawler/spiders/subtitle_spider.py
```
start_urls = [
 links to crawler
]
```
 - get links form subtitle/preprocess/generate_zhimuku_link.py

document of scrapy :  
http://scrapy-chs.readthedocs.io/zh_CN/latest/

How To Use:  
 - cd to subtitle directory  
 - Then run : ```scrapy crawl shareditor```