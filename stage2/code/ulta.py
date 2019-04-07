import urllib.request as ulb
import random
import re

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]
def geturl(url):
    response = ulb.Request(url)
    response.add_header('User-Agent', random.choice(my_headers))
    fp = ulb.urlopen(response)
    return fp.read().decode('utf-8')
result=[]
for i in range(0,17):
    print(i)
    url='https://www.ulta.com/makeup-face?N=26y3&No='+str(i*96)+'&Nrpp=96'
    f=geturl(url)
    fi= open('../html/ulta-face-'+str(i)+'.html','w',encoding='utf-8')
    fi.write(f)
    fi.close()
    pattern=re.compile(r'<div class="productQvContainer".*?<a id="qvButton"',re.S)
    basic_content = re.finditer(pattern,f)
    t=0
    for j in basic_content:
        t+=1
        r=[]
        d1=re.search(r'<label class="sr-only">(.*?) out of 5 stars</label>',j.group(),re.S)
        d2=re.search(r'<h4 class="prod-title">[ \r\n\t]*<a href="(.*?)">[ \r\n\t]*(.*?)</a>',j.group(),re.S)
        d3=re.search(r'<p class="prod-desc">[ \r\n\t]*<a href="(.*?)">[ \r\n\t]*(.*?)</a>',j.group(),re.S)
        d4=re.search(r'<span class="regPrice">[ \r\n\t]*(.*?)</span>',j.group(),re.S)
        d5=re.search(r'<span class="pro-new-price">[ \r\n\t]*(.*?)</span>',j.group(),re.S)
        d6=re.search(r'<span class="pcViewMore"> &nbsp; (.*?)&nbsp',j.group(),re.S)
        r.append('\''+d3.group(2)+'\'')
        r.append('\''+d2.group(2)+'\'')
        if d4!=None:
            r.append(d4.group(1))
        elif d5!=None:
            r.append(d5.group(1))
        else:
            r.append('NA')
        if d6!=None:
            r.append(d6.group(1))
        else:
            r.append('0')
        if d1!=None:
            r.append(d1.group(1))
        else:
            r.append('NA')
        a=','.join(r)+'\n'
        result.append(a)
    print(t)
for i in range(0,3):
    print(i)
    url='https://www.ulta.com/mens-fragrance?N=26wf&No='+str(i*96)+'&Nrpp=96'
    f=geturl(url)
    fi= open('../html/ulta-mens-fragrance-'+str(i)+'.html','w',encoding='utf-8')
    fi.write(f)
    fi.close()
    pattern=re.compile(r'<div class="productQvContainer".*?<a id="qvButton"',re.S)
    basic_content = re.finditer(pattern,f)
    t=0
    for j in basic_content:
        t+=1
        r=[]
        d1=re.search(r'<label class="sr-only">(.*?) out of 5 stars</label>',j.group(),re.S)
        d2=re.search(r'<h4 class="prod-title">[ \r\n\t]*<a href="(.*?)">[ \r\n\t]*(.*?)</a>',j.group(),re.S)
        d3=re.search(r'<p class="prod-desc">[ \r\n\t]*<a href="(.*?)">[ \r\n\t]*(.*?)</a>',j.group(),re.S)
        d4=re.search(r'<span class="regPrice">[ \r\n\t]*(.*?)</span>',j.group(),re.S)
        d5=re.search(r'<span class="pro-new-price">[ \r\n\t]*(.*?)</span>',j.group(),re.S)
        d6=re.search(r'<span class="pcViewMore"> &nbsp; (.*?)&nbsp',j.group(),re.S)
        r.append('\''+d3.group(2)+'\'')
        r.append('\''+d2.group(2)+'\'')
        if d4!=None:
            r.append(d4.group(1))
        elif d5!=None:
            r.append(d5.group(1))
        else:
            r.append('NA')
        if d6!=None:
            r.append(d6.group(1))
        else:
            r.append('0')
        if d1!=None:
            r.append(d1.group(1))
        else:
            r.append('NA')
        a=','.join(r)+'\n'
        result.append(a)
    print(t)
for i in range(0,8):
    print(i)
    url='https://www.ulta.com/makeup-eyes-eyeshadow?N=26yf&No='+str(i*96)+'&Nrpp=96'
    f=geturl(url)
    fi= open('../html/ulta-eyeshadow-'+str(i)+'.html','w',encoding='utf-8')
    fi.write(f)
    fi.close()
    pattern=re.compile(r'<div class="productQvContainer".*?<a id="qvButton"',re.S)
    basic_content = re.finditer(pattern,f)
    t=0
    for j in basic_content:
        t+=1
        r=[]
        d1=re.search(r'<label class="sr-only">(.*?) out of 5 stars</label>',j.group(),re.S)
        d2=re.search(r'<h4 class="prod-title">[ \r\n\t]*<a href="(.*?)">[ \r\n\t]*(.*?)</a>',j.group(),re.S)
        d3=re.search(r'<p class="prod-desc">[ \r\n\t]*<a href="(.*?)">[ \r\n\t]*(.*?)</a>',j.group(),re.S)
        d4=re.search(r'<span class="regPrice">[ \r\n\t]*(.*?)</span>',j.group(),re.S)
        d5=re.search(r'<span class="pro-new-price">[ \r\n\t]*(.*?)</span>',j.group(),re.S)
        d6=re.search(r'<span class="pcViewMore"> &nbsp; (.*?)&nbsp',j.group(),re.S)
        r.append('\''+d3.group(2)+'\'')
        r.append('\''+d2.group(2)+'\'')
        if d4!=None:
            r.append(d4.group(1))
        elif d5!=None:
            r.append(d5.group(1))
        else:
            r.append('NA')
        if d6!=None:
            r.append(d6.group(1))
        else:
            r.append('0')
        if d1!=None:
            r.append(d1.group(1))
        else:
            r.append('NA')
        a=','.join(r)+'\n'
        result.append(a)
    print(t)
for i in range(0,8):
    print(i)
    url='https://www.ulta.com/womens-fragrance?N=26wn&No='+str(i*96)+'&Nrpp=96'
    f=geturl(url)
    fi= open('../html/ulta-women-fragrance-'+str(i)+'.html','w',encoding='utf-8')
    fi.write(f)
    fi.close()
    pattern=re.compile(r'<div class="productQvContainer".*?<a id="qvButton"',re.S)
    basic_content = re.finditer(pattern,f)
    t=0
    for j in basic_content:
        t+=1
        r=[]
        d1=re.search(r'<label class="sr-only">(.*?) out of 5 stars</label>',j.group(),re.S)
        d2=re.search(r'<h4 class="prod-title">[ \r\n\t]*<a href="(.*?)">[ \r\n\t]*(.*?)</a>',j.group(),re.S)
        d3=re.search(r'<p class="prod-desc">[ \r\n\t]*<a href="(.*?)">[ \r\n\t]*(.*?)</a>',j.group(),re.S)
        d4=re.search(r'<span class="regPrice">[ \r\n\t]*(.*?)</span>',j.group(),re.S)
        d5=re.search(r'<span class="pro-new-price">[ \r\n\t]*(.*?)</span>',j.group(),re.S)
        d6=re.search(r'<span class="pcViewMore"> &nbsp; (.*?)&nbsp',j.group(),re.S)
        r.append('\''+d3.group(2)+'\'')
        r.append('\''+d2.group(2)+'\'')
        if d4!=None:
            r.append(d4.group(1))
        elif d5!=None:
            r.append(d5.group(1))
        else:
            r.append('NA')
        if d6!=None:
            r.append(d6.group(1))
        else:
            r.append('0')
        if d1!=None:
            r.append(d1.group(1))
        else:
            r.append('NA')
        a=','.join(r)+'\n'
        result.append(a)
    print(t)

print(result)
f=open('../result/ulta-face.csv','w',encoding='utf-8')
f.writelines(result)
f.close()



