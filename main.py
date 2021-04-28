# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#!/usr/bin/python
# -*- coding: utf-8 -*-

# from bs4 import BeautifulSoup, element
# import requests, re, os, configparser, codecs
#
# # html_file = '/Users/yan/Desktop/wechat.html'
# cfg_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'latest_wechat.cfg')
# config = None
# platforms_all = [u'Mac平台', u'iOS平台', u'Android平台', u'Windows平台', u'Web 微信', u'Windows Phone平台', u'Symbian平台', u'Series 平台', u'BlackBerry平台']
# platforms_app = [u'iOS平台', u'Android平台']
#
#
# def request_wechat_update():
#     r = requests.get('https://weixin.qq.com/cgi-bin/readtemplate?lang=zh_CN&t=weixin_faq_list')
#     if r.status_code == 200:
#         # print r.content
#         return r.content
#
#
# def parse_html(content):
#     if not content:
#         return
#     data_map = {}
#     # soup = BeautifulSoup(open(html_file), features="lxml")
#     soup = BeautifulSoup(content, 'lxml')
#     res = soup.select("h2")
#     # print res
#     for x in res:
#         if x.string in platforms_all:
#             platform_data = []
#             ul = [y for y in x.next_sibling.next_sibling if type(y) == element.Tag]
#             for li in ul:
#                 single_data = []
#                 li_info = [y for y in li.contents if type(y) == element.Tag]
#                 content = li_info[0].string
#                 link = li_info[0].attrs['href']
#                 date = li_info[1].string
#                 single_data.extend([content, link, date])
#                 if check_update(x.string.encode('utf-8'), [s.encode('utf-8') for s in single_data]):
#                     platform_data.append([s.encode('utf-8') for s in single_data])
#                 else:
#                     break
#             if platform_data:
#                 data_map[x.string.encode('utf-8')] = platform_data
#     # print data_map
#     if not data_map:
#         print '无新版本'
#     return data_map
#
#
# def get_config():
#     global config
#     if not config:
#         config = configparser.ConfigParser()
#         config.read(cfg_file, encoding='utf-8')
#         # config.read_file(codecs.open(cfg_file, 'r', 'utf8'))
#
#
# # 和已有最新版本的数据对比，如果相同，则没有最新版本，返回False；如果不同，则有最新版本，返回True
# def check_update(platform, platform_data):
#     platform = platform.decode('utf-8')
#     content = config.get(platform, u'content')
#     link = config.get(platform, u'link')
#     date = config.get(platform, u'date')
#     old_latest_data = [x.encode('utf-8') for x in [content, link, date]]
#     hasUpdate = False
#     for i in range(3):
#         if platform_data[i] != old_latest_data[i]:
#             hasUpdate = True
#             break
#     return hasUpdate
#
#
# def update_cfg(data_map):
#     if not data_map:
#         print 'NO DATA_MAP when update_cfg()'
#         return
#     for x, y in data_map.iteritems():
#         x = x.decode('utf-8')
#         config.set(x, u'content', y[0][0])
#         config.set(x, u'link', y[0][1])
#         config.set(x, u'date', y[0][2])
#     with codecs.open(cfg_file, 'wb', encoding='utf-8') as cf:
#         config.write(cf)
#
#
# def generate_message(data_map):
#     if not data_map:
#         print 'NO DATA_MAP when generate_message()'
#         return
#     msg = ''
#     if len(data_map) > 0:
#         msg += '微信有新版本啦\n------------------------\n'
#         for x, y in data_map.iteritems():
#             if x.decode('utf-8') in platforms_app:    # 目前只发送iOS和Android平台的更新信息
#                 for single_data in y:
#                     version = re.search(r'\d+(.\d+){0,}', single_data[0]).group(0)
#                     link = 'https://weixin.qq.com' + single_data[1].replace('amp;', '')
#                     msg += '%s：V%s（%s） %s\n' % (x, version, single_data[2], link)
#     msg += '\n\n更多版本请查看：https://weixin.qq.com/cgi-bin/readtemplate?lang=zh_CN&t=weixin_faq_list'
#     print 'msg:', msg
#     return msg
#
#
# def send_msg_to_group(msg):
#     if not msg:
#         print 'NO MESSAGE GENERATED when send_msg_to_group()'
#         return
#     # url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c0dedd3e-3e49-4b9f-a899-360d4eb47314'   # debug
#     url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=46fa5f84-e34e-48df-9e5b-11d85227ae82'  # QA&开发 group
#     headers = {'Content-Type': 'application/json'}
#     data = {
#         "msgtype": "text",
#         "text": {
#             "content": msg
#         }
#     }
#     r = requests.post(url, headers=headers, json=data)
#     print r.content
#
#
# def process():
#     get_config()
#     content = request_wechat_update()
#     data_map = parse_html(content)
#     msg = generate_message(data_map)
#     send_msg_to_group(msg)
#     update_cfg(data_map)
#
#
# if __name__ == '__main__':
#     process()

print("hello")
