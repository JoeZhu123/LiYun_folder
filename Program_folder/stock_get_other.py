# -*- coding:utf-8 -*-
# http://www.math.pku.edu.cn/teachers/lidf/docs/textrick/index.htm

import urllib2
import re
import os
import csv
# open the url and read
def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    page.close()
    return html

# compile the regular expressions and find
# all stuff we need
def getUrl(html):
    reg = r'(?:href|HREF)="?((?:http://)?.+?\.pdf)'
    url_re = re.compile(reg)
    url_lst = re.findall(url_re,html)
    return(url_lst)

def getFile(url,stockcode,stockname,announcename,announcetime):
    file_name = stockcode+'_'+stockname+'_'+announcename+'_'+announcetime+'.PDF'
    if os.path.exists(file_name)==False:
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
    else:
        print file_name + " " + "exist"

def readHtml(htmlName):
    file_object=open(htmlName)
    try:
        all_the_text = file_object.read()
    finally:
        file_object.close()
    return all_the_text

def getContent(html):
    reg=r'<li><div class="t1".*?><font>(.*?)</font></div><div class="t2".*?><font>(.*?)</font></div><div class="t3"><dd><span class="d1".*?><a href="(.*?)" target="_blank">(.*?)</a></span><span class="d3">(.*?)</span></dd></div></li>'
    content_re=re.compile(reg)
    content_list=re.findall(content_re,html)
    return content_list

'''
root_url = 'http://www.math.pku.edu.cn/teachers/lidf/docs/textrick/'

raw_url = 'http://www.math.pku.edu.cn/teachers/lidf/docs/textrick/index.htm'

html = getHtml(raw_url)
url_lst = getUrl(html)

http://www.cninfo.com.cn/cninfo-new/disclosure/szse/bulletin_detail/true/59043566?announceTime=2011-02-25%2006:30
'''
'''
csvfile = file('sample.csv', 'rb')
reader = csv.reader(csvfile)
code_list=[]
line_num=0
for line in reader:
    line_num=line_num+1
    if line_num>161 and line_num<301:
        code_list.append(line[0])
#print line[0]
csvfile.close()

print code
'''
'''
    True_Or_False=1
    while(True_Or_False):
    url = raw_input("请输入url\n")
    if url!='q':
    url_lst.append(url)
    else:
    True_Or_False=0
'''

root_url = 'http://www.cninfo.com.cn/finalpage/'

htmlfile=raw_input('请输入htmlfile:\n')
html=readHtml(htmlfile+'.html')

ContentList=getContent(html)
for content in ContentList:
    #print content[0]
    StockCode=content[0]
    #print content[1]
    StockName=content[1]
    FileName=content[1]
    if os.path.exists('/Users/joe/Documents/Stock/'+FileName)==False:
        os.mkdir('/Users/joe/Documents/Stock/'+FileName)
        os.chdir(os.path.join(os.getcwd(),'/Users/joe/Documents/Stock/'+FileName))
    else:
        os.chdir(os.path.join(os.getcwd(),'/Users/joe/Documents/Stock/'+FileName))
    #print content[2]
    result0 = re.findall(".*/(.*)?announceTime.*",content[2])
    if(' ' in content[2]):
        result1 = re.findall(".*=(.*) .*",content[2])
    else:
        result1 = re.findall(".*=(.*)",content[2])
    new_url=root_url+result1[0]+'/'+result0[0].strip('?')+'.PDF'
    #print content[3]
    announceName=content[3]
    #print content[4]
    announceTime=content[4]
    getFile(new_url,StockCode,StockName,announceName,announceTime)





