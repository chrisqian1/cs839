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
for i in range(1,86):
    print(i)
    url='https://www.sephora.com/shop/face-makeup?pageSize=12&currentPage='+str(i)
    f=geturl(url)
    fi= open('../html/sephora-face-'+str(i)+'.html','w',encoding='utf-8')
    fi.write(f)
    fi.close()
    pattern=re.compile(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">.*?"StarRating">',re.S)
    basic_content = re.finditer(pattern,f)
    t=0
    for j in basic_content:
        r=[]
        d=re.match(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">(.*?)</span><br/><span data-at="sku_item_name">(.*?)</span></div><div class="css-68u28a"><span data-at="sku_item_price_list" class="css-(.*?)">(.*?)</span>(.*)</div><div class="css-rrjz1n">(.*?)<!-- -->(.*?)</div><div class="css-164r41r"><div aria-label="(.*?) stars" class="css-1adflzz" data-comp="StarRating"',j.group(),re.S)
        if d!=None:
            t+=1
            r.append('\''+d.group(2)+'\'')
            r.append('\''+d.group(1)+'\'')
            r.append(d.group(4))
            r.append(d.group(6))
            r.append(d.group(8))
            a=','.join(r)+'\n'
            result.append(a)
        else:
            d=re.match(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">(.*?)</span><br/><span data-at="sku_item_name">(.*?)</span></div><div class="css-68u28a"><span data-at="sku_item_price_list" class="css-(.*?)">(.*?)</span>(.*)</div><div class="css-164r41r"><div aria-label="(.*?) stars" class="css-1adflzz" data-comp="StarRating"',j.group(),re.S)
            if d!=None:
                t+=1
                r.append('\''+d.group(2)+'\'')
                r.append('\''+d.group(1)+'\'')
                r.append(d.group(4))
                r.append('0')
                r.append(d.group(6))
                a=','.join(r)+'\n'
                result.append(a)
    print(t)
for i in range(1,40):
    print(i)
    url='https://www.sephora.com/shop/cheek-makeup?pageSize=12&currentPage='+str(i)
    f=geturl(url)
    fi= open('../html/sephora-cheek-'+str(i)+'.html','w',encoding='utf-8')
    fi.write(f)
    fi.close()
    pattern=re.compile(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">.*?"StarRating">',re.S)
    basic_content = re.finditer(pattern,f)
    t=0
    for j in basic_content:
        r=[]
        d=re.match(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">(.*?)</span><br/><span data-at="sku_item_name">(.*?)</span></div><div class="css-68u28a"><span data-at="sku_item_price_list" class="css-(.*?)">(.*?)</span>(.*)</div><div class="css-rrjz1n">(.*?)<!-- -->(.*?)</div><div class="css-164r41r"><div aria-label="(.*?) stars" class="css-1adflzz" data-comp="StarRating"',j.group(),re.S)
        if d!=None:
            t+=1
            r.append('\''+d.group(2)+'\'')
            r.append('\''+d.group(1)+'\'')
            r.append(d.group(4))
            r.append(d.group(6))
            r.append(d.group(8))
            a=','.join(r)+'\n'
            result.append(a)
        else:
            d=re.match(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">(.*?)</span><br/><span data-at="sku_item_name">(.*?)</span></div><div class="css-68u28a"><span data-at="sku_item_price_list" class="css-(.*?)">(.*?)</span>(.*)</div><div class="css-164r41r"><div aria-label="(.*?) stars" class="css-1adflzz" data-comp="StarRating"',j.group(),re.S)
            if d!=None:
                t+=1
                r.append('\''+d.group(2)+'\'')
                r.append('\''+d.group(1)+'\'')
                r.append(d.group(4))
                r.append('0')
                r.append(d.group(6))
                a=','.join(r)+'\n'
                result.append(a)
    print(t)
for i in range(1,83):
    print(i)
    url='https://www.sephora.com/shop/eye-makeup?pageSize=12&currentPage='+str(i)
    f=geturl(url)
    fi= open('../html/sephora-eye-'+str(i)+'.html','w',encoding='utf-8')
    fi.write(f)
    fi.close()
    pattern=re.compile(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">.*?"StarRating">',re.S)
    basic_content = re.finditer(pattern,f)
    t=0
    for j in basic_content:
        r=[]
        d=re.match(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">(.*?)</span><br/><span data-at="sku_item_name">(.*?)</span></div><div class="css-68u28a"><span data-at="sku_item_price_list" class="css-(.*?)">(.*?)</span>(.*)</div><div class="css-rrjz1n">(.*?)<!-- -->(.*?)</div><div class="css-164r41r"><div aria-label="(.*?) stars" class="css-1adflzz" data-comp="StarRating"',j.group(),re.S)
        if d!=None:
            t+=1
            r.append('\''+d.group(2)+'\'')
            r.append('\''+d.group(1)+'\'')
            r.append(d.group(4))
            r.append(d.group(6))
            r.append(d.group(8))
            a=','.join(r)+'\n'
            result.append(a)
        else:
            d=re.match(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">(.*?)</span><br/><span data-at="sku_item_name">(.*?)</span></div><div class="css-68u28a"><span data-at="sku_item_price_list" class="css-(.*?)">(.*?)</span>(.*)</div><div class="css-164r41r"><div aria-label="(.*?) stars" class="css-1adflzz" data-comp="StarRating"',j.group(),re.S)
            if d!=None:
                t+=1
                r.append('\''+d.group(2)+'\'')
                r.append('\''+d.group(1)+'\'')
                r.append(d.group(4))
                r.append('0')
                r.append(d.group(6))
                a=','.join(r)+'\n'
                result.append(a)
    print(t)
for i in range(1,52):
    print(i)
    url='https://www.sephora.com/shop/lips-makeup?pageSize=12&currentPage='+str(i)
    f=geturl(url)
    fi= open('../html/sephora-lips-'+str(i)+'.html','w',encoding='utf-8')
    fi.write(f)
    fi.close()
    pattern=re.compile(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">.*?"StarRating">',re.S)
    basic_content = re.finditer(pattern,f)
    t=0
    for j in basic_content:
        r=[]
        d=re.match(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">(.*?)</span><br/><span data-at="sku_item_name">(.*?)</span></div><div class="css-68u28a"><span data-at="sku_item_price_list" class="css-(.*?)">(.*?)</span>(.*)</div><div class="css-rrjz1n">(.*?)<!-- -->(.*?)</div><div class="css-164r41r"><div aria-label="(.*?) stars" class="css-1adflzz" data-comp="StarRating"',j.group(),re.S)
        if d!=None:
            t+=1
            r.append('\''+d.group(2)+'\'')
            r.append('\''+d.group(1)+'\'')
            r.append(d.group(4))
            r.append(d.group(6))
            r.append(d.group(8))
            a=','.join(r)+'\n'
            result.append(a)
        else:
            d=re.match(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">(.*?)</span><br/><span data-at="sku_item_name">(.*?)</span></div><div class="css-68u28a"><span data-at="sku_item_price_list" class="css-(.*?)">(.*?)</span>(.*)</div><div class="css-164r41r"><div aria-label="(.*?) stars" class="css-1adflzz" data-comp="StarRating"',j.group(),re.S)
            if d!=None:
                t+=1
                r.append('\''+d.group(2)+'\'')
                r.append('\''+d.group(1)+'\'')
                r.append(d.group(4))
                r.append('0')
                r.append(d.group(6))
                a=','.join(r)+'\n'
                result.append(a)
    print(t)
for i in range(1,6):
    print(i)
    url='https://www.sephora.com/shop/makeup-remover-skincare?pageSize=12&currentPage='+str(i)
    f=geturl(url)
    fi= open('../html/sephora-makeup-remover-'+str(i)+'.html','w',encoding='utf-8')
    fi.write(f)
    fi.close()
    pattern=re.compile(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">.*?"StarRating">',re.S)
    basic_content = re.finditer(pattern,f)
    t=0
    for j in basic_content:
        r=[]
        d=re.match(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">(.*?)</span><br/><span data-at="sku_item_name">(.*?)</span></div><div class="css-68u28a"><span data-at="sku_item_price_list" class="css-(.*?)">(.*?)</span>(.*)</div><div class="css-rrjz1n">(.*?)<!-- -->(.*?)</div><div class="css-164r41r"><div aria-label="(.*?) stars" class="css-1adflzz" data-comp="StarRating"',j.group(),re.S)
        if d!=None:
            t+=1
            r.append('\''+d.group(2)+'\'')
            r.append('\''+d.group(1)+'\'')
            r.append(d.group(4))
            r.append(d.group(6))
            r.append(d.group(8))
            a=','.join(r)+'\n'
            result.append(a)
        else:
            d=re.match(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">(.*?)</span><br/><span data-at="sku_item_name">(.*?)</span></div><div class="css-68u28a"><span data-at="sku_item_price_list" class="css-(.*?)">(.*?)</span>(.*)</div><div class="css-164r41r"><div aria-label="(.*?) stars" class="css-1adflzz" data-comp="StarRating"',j.group(),re.S)
            if d!=None:
                t+=1
                r.append('\''+d.group(2)+'\'')
                r.append('\''+d.group(1)+'\'')
                r.append(d.group(4))
                r.append('0')
                r.append(d.group(6))
                a=','.join(r)+'\n'
                result.append(a)
    print(t)
for i in range(1,9):
    print(i)
    url='https://www.sephora.com/shop/nails-makeup?pageSize=12&currentPage='+str(i)
    f=geturl(url)
    fi= open('../html/sephora-nails-'+str(i)+'.html','w',encoding='utf-8')
    fi.write(f)
    fi.close()
    pattern=re.compile(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">.*?"StarRating">',re.S)
    basic_content = re.finditer(pattern,f)
    t=0
    for j in basic_content:
        r=[]
        d=re.match(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">(.*?)</span><br/><span data-at="sku_item_name">(.*?)</span></div><div class="css-68u28a"><span data-at="sku_item_price_list" class="css-(.*?)">(.*?)</span>(.*)</div><div class="css-rrjz1n">(.*?)<!-- -->(.*?)</div><div class="css-164r41r"><div aria-label="(.*?) stars" class="css-1adflzz" data-comp="StarRating"',j.group(),re.S)
        if d!=None:
            t+=1
            r.append('\''+d.group(2)+'\'')
            r.append('\''+d.group(1)+'\'')
            r.append(d.group(4))
            r.append(d.group(6))
            r.append(d.group(8))
            a=','.join(r)+'\n'
            result.append(a)
        else:
            d=re.match(r'<span class="css-ktoumz OneLinkNoTx" data-at="sku_item_brand">(.*?)</span><br/><span data-at="sku_item_name">(.*?)</span></div><div class="css-68u28a"><span data-at="sku_item_price_list" class="css-(.*?)">(.*?)</span>(.*)</div><div class="css-164r41r"><div aria-label="(.*?) stars" class="css-1adflzz" data-comp="StarRating"',j.group(),re.S)
            if d!=None:
                t+=1
                r.append('\''+d.group(2)+'\'')
                r.append('\''+d.group(1)+'\'')
                r.append(d.group(4))
                r.append('0')
                r.append(d.group(6))
                a=','.join(r)+'\n'
                result.append(a)
    print(t)
print(result)
f=open('../result/sephora.csv','w',encoding='utf-8')
f.writelines(result)
f.close()




