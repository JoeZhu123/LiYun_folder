# -*- coding:utf-8 -*-
# http://www.math.pku.edu.cn/teachers/lidf/docs/textrick/index.htm

import urllib2
import re
import os
import csv

'''
csvfile = file('sample.csv', 'rb')
reader = csv.reader(csvfile)
code_list=[]
line_num=0
for line in reader:
    line_num=line_num+1
    if line_num>150 and line_num<301:
        code_list.append(line)
        print line[0]
csvfile.close()
'''
'''
url_list=[]
True_Or_False=1
while(True_Or_False):
    url = raw_input("请输入url\n")
    if url!='q':
        url_list.append(url)
    else:
        True_Or_False=0

for url in url_list:
    print url
'''
# open the url and read
def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    page.close()
    return html

def readHtml(htmlName):
    file_object=open(htmlName)
    try:
        all_the_text = file_object.read()
    finally:
        file_object.close()
    return all_the_text
#    print len(all_the_text)
#f = open('/Users/joe/Documents/'+htmlName, 'wb')
#    f.write(all_the_text)
#    f.close()

def getContent(html):
    reg=r'<li><div class="t1".*?><font>(.*?)</font></div><div class="t2".*?><font>(.*?)</font></div><div class="t3"><dd><span class="d1".*?><a href="(.*?)" target="_blank">(.*?)<img .*?>.*?</a></span><span class="d3">(.*?)</span></dd></div></li>'
    content_re=re.compile(reg)
    content_list=re.findall(content_re,html)
    for content in content_list:
        print content[0]
        print content[1]
        print content[2]
        print content[3]
        print content[4]

# compile the regular expressions and find
# all stuff we need
def getUrl(html):
    reg = r'(?:href|HREF)="?((?:http://)?.+?\.pdf)'
    url_re = re.compile(reg)
    url_lst = re.findall(url_re,html)
    return(url_lst)

def getFile(url,stockcode):
    file_name = stockcode+'_'+url.split('/')[4]+'_'+url.split('/')[5]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        
        f.write(buffer)
    f.close()
    print "Sucessful to download" + " " + file_name

html=readHtml('002099.html')
getContent(html)
'''
root_url = 'http://www.math.pku.edu.cn/teachers/lidf/docs/textrick/'

raw_url = 'http://www.math.pku.edu.cn/teachers/lidf/docs/textrick/index.htm'

html = getHtml(raw_url)
url_lst = getUrl(html)

url_lst=['http://www.cninfo.com.cn/cninfo-new/disclosure/szse/bulletin_detail/true/1200024187?announceTime=2014-07-02',
         'http://www.cninfo.com.cn/cninfo-new/disclosure/szse/bulletin_detail/true/1200024188?announceTime=2014-07-02',
         'http://www.cninfo.com.cn/cninfo-new/disclosure/szse/bulletin_detail/true/61201538?announceTime=2012-07-02%2006:30',
         'http://www.cninfo.com.cn/cninfo-new/disclosure/szse/bulletin_detail/true/61201539?announceTime=2012-07-02%2006:30',
         'http://www.cninfo.com.cn/cninfo-new/disclosure/szse/bulletin_detail/true/59618605?announceTime=2011-07-01%2006:30',
         'http://www.cninfo.com.cn/cninfo-new/disclosure/szse/bulletin_detail/true/59618606?announceTime=2011-07-01%2006:30',
         'http://www.cninfo.com.cn/cninfo-new/disclosure/szse/bulletin_detail/true/59618607?announceTime=2011-07-01%2006:30',
         'http://www.cninfo.com.cn/cninfo-new/disclosure/szse/bulletin_detail/true/59618608?announceTime=2011-07-01%2006:30',
         'http://www.cninfo.com.cn/cninfo-new/disclosure/szse/bulletin_detail/true/59618609?announceTime=2011-07-01%2006:30',
         'http://www.cninfo.com.cn/cninfo-new/disclosure/szse/bulletin_detail/true/59509955?announceTime=2011-06-03%2006:30',
         'http://www.cninfo.com.cn/cninfo-new/disclosure/szse/bulletin_detail/true/59479951?announceTime=2011-05-27%2006:30',
         'http://www.cninfo.com.cn/cninfo-new/disclosure/szse/bulletin_detail/true/59421429?announceTime=2011-05-12%2011:46',
         'http://www.cninfo.com.cn/cninfo-new/disclosure/szse/bulletin_detail/true/58302589?announceTime=2010-08-14%2006:30']

root_url = 'http://www.cninfo.com.cn/finalpage/'
new_url_lst=[]
for url in url_lst:
    result0 = re.findall(".*/(.*)?announceTime.*",url)
    print result0[0].strip('?')
    if('%' in url):
        result1 = re.findall(".*=(.*)%.*",url)
        print result1[0]
    else:
        result1 = re.findall(".*=(.*)",url)
        print result1[0]
    new_url_lst.append(root_url+result1[0]+'/'+result0[0].strip('?')+'.PDF')

for url in new_url_lst:
    print url
'''