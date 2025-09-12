import requests
from bs4 import BeautifulSoup

url_get = 'https://hcraj.nic.in/cishcraj-jdp/JudgementFilters/'

url_post_captcha = 'https://hcraj.nic.in/cishcraj-jdp/causelists/setgetcaptcha?'

# url_post = 'https://hcraj.nic.in/cishcraj-jdp/judgement-filters/getrecord'

# r = requests.get(url_get)
r = requests.post(url_post_captcha)



# payload = {
#     'fromdate': '',
#     'todate': '' ,
#     'rpJudgment' : '' ,
#     'captcha' : '' 
# }

with open('file1.html' , 'w' ,encoding="utf-8") as f:
    f.write(r.text)

