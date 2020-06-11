# -*- coding: utf-8 -*-

# Scrapy settings for ksshopdata project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ksshopdata'

SPIDER_MODULES = ['ksshopdata.spiders']
NEWSPIDER_MODULE = 'ksshopdata.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Linux; Android 5.1.1; SM-N960F Build/JLS36C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.12.1620(0x27000C50) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm32'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'ERROR'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
     'Host': 'wxmini-api.uyouqu.com',
     'Connection': 'keep-alive',
     'charset': 'utf-8',
     'Accept-Encoding': 'gzip,compress,br,deflate',
     'content-type':'application/json',
     'Referer': 'https: // servicewechat.com / wx79a83b1a1e8a7978 / 180 / page - frame.html',
     'cookie': 'clientid=13; client_key=f60ac815; kpn=WECHAT_SMALL_APP; kpf=OUTSIDE_ANDROID_H5; mod=OPPO%20R11%20Plus; sys=Android%205.1.1; wechatVersion=7.0.12; language=zh_CN; brand=OPPO; sid=kuaishou.wechat.app; appId=ks_wechat_small_app_2; nickName=PROFILE_SERVICE_ERROR; did=wxo_558dae2672ec2e3548b624e5bdece03bbbc0; session_key=12306be52b2a470e76d27868a2da6993b82793d01ae84745d110efacf79b2bcc4efa6214e5718c091a159c9cda8695c6abae1a129ea034f7525d4a5a84dede9c4d20c07375b922203147158e2759360df6bd2d3c74de2447d1b8c9f71431b113764f7bb59c922f3328053001; eUserStableOpenId=12301959e67267097bf94fac63db9cc8e600cfb354de4dacef43ff58327d6b159df7027a0ca052a49b1a5633bfe1db0a20051a12e5b554d4fc5e41c18a1a8186ab16f889eca52220b0cdbf0b4c770f4b3f63a83f33f28c65eac29c9b14a4cf1a7f9777544ec0079228053001; openId=o5otV4y-tyHkwMicfHlCxfwIkoAI; kuaishou.wechat.app_st=ChZrdWFpc2hvdS53ZWNoYXQuYXBwLnN0ErABRsUKFrtDyxUUb9jxNftoBec8z0-GJE5oyLP-x36NtaF5wGlLQJbwUItM1DlBL2A2NLodtWHK0VQXEZIdi4DSJcZIpxcVcQFN2BW3RFNJOVrbCeCsKJveMPuRR6lRcfcI-CHhhDRZ69NpuY87poZJqjwwKftW_OUZEinZoGGOQotfbWkEJEXpEzyrofpY2iTXgXej7pKI1jjE3tcTXgWRPUHxaXDJzjNUspdWJcIF1lsaEiRcmuVR6UkRsKIU7rO5fOHsOyIgzbh8FtXetqriR4XmFZ6V-uJeKouSguWmR5StgPy4l-ooBTAB; passToken=ChNwYXNzcG9ydC5wYXNzLXRva2VuEpABi-7EYeJTsB_ezSKwj-tsvZ39kA0UN5FBgGUcLtpNJoyoezhqW_rcQYhBsOFmjfd6_MVrSeBSCky57f6yhvMwlgkBt8MNE-5qG0ShlRZFcUBAiSPiwD2chWmMELjLbVXbJCpQF53cYxPhpSSR86079dpLb73g8vf1XZYdXsDboMh9soK5pixM2yHIagiW0vDyGhLv-WrnmatNH5LaZ_0SJ8u4-rIiIDfnjyJY6Ockre5_lX8X5SG6tWEGiHPdMKOdr83byUloKAUwAQ; userId=1674679743; unionid=PROFILE_SERVICE_ERROR'

}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ksshopdata.middlewares.KsshopdataSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ksshopdata.middlewares.KsshopdataDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'ksshopdata.pipelines.KsshopdataPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
