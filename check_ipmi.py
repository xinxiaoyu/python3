import urllib.parse
import http.cookiejar
import re
import subprocess
import time
from datetime import date

url = "http://"
postdata =urllib.parse.urlencode({
"account":"",
"password":""
}).encode('utf-8')

req = urllib.request.Request(url, postdata)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 
2.X MetaSr 1.0')

cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)

file = opener.open(req)
data = file.read()
file = open("/tmp/3.html", "wb")
file.write(data)
file.close()

today = date.today().strftime('%Y-%m-%d')

ap1 = "http:"
data2 = urllib.request.urlopen(ap1).read()
fhandle = open("/tmp/ap1"+today+".html", "wb")
fhandle.write(data2)
fhandle.close()

file_count = open('/tmp/ap1'+today+'.html', 'r')
for line in file_count:
    count = re.findall(r'count": (\d+), "next_url', line)
file_count.close()

count_int = int(count[0])
page_start = 1

fhandle1 = open("/tmp/ap1"+today+".html", "wb")

while page_start < count_int:
    ap1_page = ""
    data3 = urllib.request.urlopen(ap1_page).read()
    fhandle1.write(data3)
    page_start += 30
    time.sleep(1)

fhandle1.close()

fhandler1_split = subprocess.Popen(['sed', '-i', 's/asset_role/asset_role\\n/g', '/tmp/ap1'+today+'.html'])
fhandler1_split.wait()

ap1_file = open('/tmp/ap1'+today+'.html', 'r')

ip_host = []

for line1 in ap1_file:
    iphost = re.findall(r'drac_ip": "?(.+?)"?, "public_ip.*?hostname": (.+?)?, "source', line1)
    ip_host += iphost

ap1_file.close()

for ip in ip_host:
    p = subprocess.Popen(['sudo', 'nmap', '-sU', '-oN=/mydata/log'+today+'.txt','--append-output', '-p623', ip[0]])
    p.wait()
    print(ip[0])
