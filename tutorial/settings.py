# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
#mysql数据库配置
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'my_base'         #数据库名字，请修改
MYSQL_USER = 'root'             #数据库账号，请修改 
MYSQL_PASSWD = 'root'         #数据库密码，请修改

MYSQL_PORT = 3306               #数据库端口，在dbhelper中使用


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1.1
REDIRECT_ENABLED = False
DOWNLOAD_TIMEOUT = 15
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.8',
    'referer': 'https://www.sina.com/',
    'Connection': 'keep-alive',
    'Cookie': 'U_TRS1=000000a2.d9696925.5b5036dc.2976d88a; UOR=www.baidu.com,down.tech.sina.com.cn,; vjuids=-16fe3e761.164b1564fb8.0.1dd854685ee34; SINAGLOBAL=182.18.19.162_1531983583.108820; SGUID=1537177861595_51316365; U_TRS2=000000a2.c9804a5e.5ba222ee.5c287ebd; Apache=182.18.19.162_1537352430.199410; ULV=1537511823768:10:5:3:182.18.19.162_1537352430.199410:1537352429995; SUB=_2AkMs9p2pf8NxqwJRmP4QzWzgaIp1wwzEieKaqmxyJRMyHRl-yD9kqkMftRB6B3azRgAeihOsiLr-P_Zq910nlN2_EAM_; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhQFdcHJ-.IA7rM9gvwRGre; CNZZDATA5581074=cnzz_eid%3D860730700-1538202970-%26ntime%3D1538202970; CNZZDATA5581080=cnzz_eid%3D382120531-1538199338-%26ntime%3D1538199338; CNZZDATA1264476941=1547431245-1538203104-%7C1538203104; lxlrtst=1538273011_o; lxlrttp=1538731187; vjlast=1538981684; bdshare_firstime=1538982319652; ArtiFSize=14; CNZZDATA5581086=cnzz_eid%3D1883505522-1534743571-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1538983576; CNZZDATA5399792=cnzz_eid%3D345060771-1534745091-http%253A%252F%252Ftech.sina.com.cn%252F%26ntime%3D1538986670; UM_distinctid=16652d0841c7b8-0bd336581b5773-47e1039-1fa400-16652d0841d841'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'tutorial.pipelines.TutorialPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
