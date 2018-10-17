# import scrapy
# import datetime
# # from scrapy.contrib.loader import ItemLoader
# from tutorial.items import TutorialItem
# # from scrapy.selector import Selector

# class BaidutopSpider(scrapy.Spider):
#     name = "baidu"
#     allowed_domains = ["baidu.com"]
#     start_urls = ['http://top.baidu.com/buzz?b=1&fr=topindex']


#     def parse(self, response):
#         newsSelector = response.xpath('//table[@class="list-table"]/tr')
#         for baiduitem in newsSelector:
#             item = TutorialItem()
#             if len(baiduitem.xpath('td[@class="keyword"]/a[@class="list-title"]/text()').extract())>0:
#                 item['title'] = baiduitem.xpath('td[@class="keyword"]/a[@class="list-title"]/text()').extract()[0]
#                 item['url'] = baiduitem.xpath('td[@class="keyword"]/a[@class="list-title"]/@href').extract()[0]
#                 item['click_reta'] = baiduitem.xpath('td[@class="last"]/span/text()').extract()[0]
#                 item['ctime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#                 item['from_type']  = 1;
#                 print item
#                 # yield item
#                 yield scrapy.Request(item['url'],callback=self.parse_article)
            
            
            
#     def parse_article(self,response):
#         detail = response.xpath('//div[@id="container"]/div[@id="content_left"]/div[@id="1"]/div[@class="c-offset"]/div[@class="c-row"]/a/@href').extract()
#         print detail
#     #     # item = CoolscrapyItem()
#     #     # item['title'] = baiduitem.xpath('td[@class="keyword"]/a[@class="list-title"]/text()').extract()
#     #     url  = detail.xpath('a[@class="list-title"]/@href').extract()[0]
#     #     print url
#     #     # item['click_reta'] = baiduitem.xpath('td[@class="last"]/span/text()').extract()
#     #     # print(item['title'],item['link'],item['posttime'])
#     #     # yield item
#     
import scrapy
import datetime
import json
import MySQLdb  
# from scrapy.contrib.loader import ItemLoader
from tutorial.items import TutorialItem
import sys
import re
import urllib
from urlparse import urlparse
# from scrapy.selector import Selector

class BaidutopSpider(scrapy.Spider):

    name = "sina"
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://www.sina.com.cn/mid/search-list.shtml']

    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='my_base',port=3306,charset='utf8')
        self.cur=conn.cursor()

    def parse(self, response):
        newsSelector = response.xpath('//div[@class="content"]/div[@class="wrap"]/div[@class="cont"]/ul/li')
        for sinaitem in newsSelector:
            item = TutorialItem()
            item['title'] = sinaitem.xpath('div[@class="keyword"]/a/text()').extract()[0]
            item['url'] = sinaitem.xpath('div[@class="keyword"]/a/@href').extract()[0]
            item['click_rate'] = sinaitem.xpath('div[@class="exp"]/em/text()').extract()[0]
            item['ctime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item['from_type']  = 2;
            url = "http://api.search.sina.com.cn/?c=news&q="+item['title']+"&sort=rel&callback=&num=5"
            sql = 'select id from news_rank where title = "'+item['title']+'"';
            self.cur.execute(sql);
            is_exist = self.cur.fetchall()
            if not is_exist:
                sql = "INSERT INTO news_rank(`title`,`url`,`click_rate`,`ctime`,`utime`,`type`) VALUES('"+item['title']+"','"+item['url']+"','"+str(item['click_rate'])+"','"+item['ctime']+"','"+item['ctime']+"','"+str(item['from_type'])+"')"
                info = self.cur.execute(sql)
            else:
                sql = 'UPDATE news_rank SET click_rate = "'+item['click_rate']+'",utime = "'+item['ctime']+'" WHERE title="'+item['title']+'"'
                info = self.cur.execute(sql)
            
            yield scrapy.Request(url,callback=self.parse_article, meta={'title':item['title']}, dont_filter=True)
            
            
            
    def parse_article(self,response):
        if len(response.body)>0 :
            newUrl = json.loads(response.body)['result']['list']
            for newUrlItem in newUrl:
                newUrlItem['domain_url'] = urlparse(newUrlItem['url']).netloc
                if  (re.search('sports',newUrlItem['domain_url']) or re.search('tech',newUrlItem['domain_url']) or re.search('finance',newUrlItem['domain_url']) or re.search('ent',newUrlItem['domain_url']) or re.search('news',newUrlItem['domain_url'])) and not re.search('7x24',newUrlItem['domain_url']):
                    newUrl = response.urljoin(newUrlItem['url'])
                    break
            # print newUrl
            yield scrapy.Request(newUrl,callback=self.parse_newinfo, meta={'title': response.meta['title'],'newUrl':newUrl})
    

    def parse_newinfo(self,response):
        item = TutorialItem()
        item['release_time'] = ''
        item['title'] = ''
        item['content'] = ''
        if re.search('tech',response.meta['newUrl']) or  re.search('ent',response.meta['newUrl']) or re.search('finance',response.meta['newUrl']) or re.search('sports',response.meta['newUrl']) or re.search('news',response.meta['newUrl']):
            if response.xpath('//h1[@id="main_title"]/text()') or response.xpath('//h1[@id="artibodyTitle"]/text()') or response.xpath('//h1[@class="main-title"]/text()') or response.xpath('//h1[@id="j_title"]/text()'):
                #title
                if response.xpath('//h1[@id="artibodyTitle"]/text()'):
                    item['title'] = response.xpath('//h1[@id="artibodyTitle"]/text()').extract()[0]
                elif response.xpath('//h1[@class="main-title"]/text()'):
                    item['title'] = response.xpath('//h1[@class="main-title"]/text()').extract()[0]
                elif response.xpath('//h1[@id="j_title"]/text()'):
                    item['title'] = response.xpath('//h1[@id="j_title"]/text()').extract()[0]
                elif response.xpath('//h1[@id="j_title"]/text()'):
                    item['title'] = response.xpath('//h1[@id="j_title"]/text()').extract()[0]
                elif response.xpath('//h1[@id="main_title"]/text()'):
                    item['title'] = response.xpath('//h1[@id="main_title"]/text()').extract()[0]
                #content
                # if  response.xpath('//div[@id="artibody"]//text()'):
                #     contents = response.xpath('//div[@id="artibody"]')
                # elif response.xpath('//div[@id="article"]//text()'):
                #     contents = response.xpath('//div[@id="article"]')
                if  response.xpath('//div[@id="artibody"]//text()') or response.xpath('//div[@id="article"]'):
                    content = response.body
                    if content.find('id="artibody"') > 0:
                        content = content[content.index('id="artibody"'):]
                    elif content.find('id="article"') > 0:
                        content = content[content.index('id="article"'):]

                    if content.find('article-bottom') > 0:
                        content = content[0:content.index('article-bottom')]
                    if content :
                        patt=re.compile(r'<p>(.*?)</p>|<div class="img_wrapper">(.*?)<span class="img_descr">')
                        group=patt.findall(content)
                        # print group 
                        
                        item['top_img_url'] = ''
                        item['img_num'] = int(0)
                        for info in group:
                            if info[0]:
                                info = str(info[0])
                                pattern = re.compile(r'href="(.*?)"')
                                info = re.sub(pattern,'', info)
                                pattern = re.compile(r"href='(.*?)'")
                                info = re.sub(pattern,'', info)
                                pattern = re.compile(r'onmouseover="(.*?)"')
                                info = re.sub(pattern,'', info)
                            elif info[1]:
                                info = str(info[1])
                                pattern = re.compile(r'style=".*?"')
                                info = re.sub(pattern,'', info)
                            if info.find('<img') < 0:
                                item['content'] = item['content']+'<p>'+ info+'</p>'
                            else:
                                if item['img_num'] == 0:
                                    pattern = re.compile(r'src="(.*?)"')
                                    item['top_img_url']=pattern.findall(info)[0]
                                item['img_num'] = int(item['img_num']) + 1

                                item['content'] = item['content']+info
                #release_time
                if response.xpath('//div[@id="top_bar"]/div/div[@class="date-source"]/span[@class="date"]/text()'):
                    item['release_time'] = response.xpath('//div[@id="top_bar"]/div/div[@class="date-source"]/span[@class="date"]/text()').extract()[0]
                elif response.xpath('//span[@id="pub_date"]/text()'):
                    item['release_time'] = response.xpath('//span[@id="pub_date"]/text()').extract()[0]
                print item['release_time']
                #source
                item['source'] = ''
                if response.xpath('//span[@id="media_name"]/a[@data-sudaclick="media_name"]/text()'):
                    item['source'] = response.xpath('//span[@id="media_name"]/a[@data-sudaclick="media_name"]/text()').extract()[0]
                elif response.xpath('//span[@id="media_name"]/a/text()'):
                    item['source'] = response.xpath('//span[@id="media_name"]/a/text()').extract()[0]
                elif response.xpath('//div[@class="date-source"]/span[contains(@class,"source-nolink")]/a/text()'):
                    item['source'] = response.xpath('//div[@class="date-source"]/span[contains(@class,"source-nolink")]/a/text()').extract()[0]
                elif response.xpath('//div[@id="top_bar"]/div/div[@class="date-source"]/a/text()'):
                    item['source'] = response.xpath('//div[@id="top_bar"]/div/div[@class="date-source"]/a/text()').extract()[0]
                elif response.xpath('//div[@class="page-info"]/span[@class="time-source"]/span/a/text()'):
                    item['source'] = response.xpath('//div[@class="page-info"]/span[@class="time-source"]/span/a/text()').extract()[0]
                elif response.xpath('//div[@id="top_bar"]/div/div[@class="date-source"]/span[@class="source"]/text()'):
                    item['source'] = response.xpath('//div[@id="top_bar"]/div/div[@class="date-source"]/span[@class="source"]/text()').extract()[0]
                elif response.xpath('//div[@id="top_bar"]/div/div[@class="date-source"]/span[@class="source"]/a/text()'):
                    item['source'] = response.xpath('//div[@id="top_bar"]/div/div[@class="date-source"]/span[@class="source"]/a/text()').extract()[0]
                elif response.xpath('//div[@id="top_bar"]/div/div[@class="date-source"]/span[contains(@class,"source")]/text()'):
                    item['source'] = response.xpath('//div[@id="top_bar"]/div/div[@class="date-source"]/span[contains(@class,"source")]/text()').extract()[0]
        
            sql = 'select id from news_rank where title = "'+response.meta['title']+'"';
            self.cur.execute(sql)
            pid = self.cur.fetchall()
            
            if not pid[0][0]:
                return False
            sql = 'select id from news_info where rank_id = "'+str(pid[0][0])+'"'
            self.cur.execute(sql)
            id = self.cur.fetchall()
            item['ctime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if item['release_time'] :
                item['date'] = urllib.unquote(item['release_time'])[0:10]
                item['time'] = urllib.unquote(item['release_time'])[-6:]
                item['date'] = re.sub(r'[^\d\-]','-',item['date'])
                item['release_time'] = item['date']+item['time']
            if not id:
                sql = "insert into news_info(`rank_id`,`title`,`content`,`source`,`release_time`,`ctime`,`top_img_url`,`img_num`) values('"+str(pid[0][0])+"','"+MySQLdb.escape_string(str(item['title']))+"','"+MySQLdb.escape_string(str(item['content']))+"','"+MySQLdb.escape_string(item['source'])+"','"+item['release_time']+"','"+item['ctime']+"','"+MySQLdb.escape_string(str(item['top_img_url']))+"','"+str(item['img_num'])+"')"
                info = self.cur.execute(sql)
                sql = "update news_rank set is_true=1 where id='"+str(pid[0][0])+"'"
                info = self.cur.execute(sql)
            else:
                return True

        # print item

        # detail = response.xpath('//div[@class="result"]/div[@class="box-result clearfix"]/div[@class="r-info r-info2"]/h2/a').extract()
        # print detail
    #     # item = CoolscrapyItem()
    #     # item['title'] = baiduitem.xpath('td[@class="keyword"]/a[@class="list-title"]/text()').extract()
    #     url  = detail.xpath('a[@class="list-title"]/@href').extract()[0]
    #     print url
    #     # item['click_reta'] = baiduitem.xpath('td[@class="last"]/span/text()').extract()
    #     # print(item['title'],item['link'],item['posttime'])
    #     # yield item