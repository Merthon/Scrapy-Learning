from scrapyd_api import ScrapydAPI

Scrapyd = ScrapydAPI('http://127.0.0.1:6800')

#调用方法实现对应接口的操作
egg = open('project.egg','rb')
Scrapyd.add_version('project', 'v1', egg)