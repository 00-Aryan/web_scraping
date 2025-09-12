import requests
from bs4 import BeautifulSoup
import base64

url_get = 'https://hcraj.nic.in/cishcraj-jdp/JudgementFilters/'

url_post_captcha = 'https://hcraj.nic.in/cishcraj-jdp/causelists/setgetcaptcha?'

# url_post = 'https://hcraj.nic.in/cishcraj-jdp/judgement-filters/getrecord'

# base_url = requests.get(url_get)
r_captcha = requests.post(url_post_captcha)



# payload = {
#     'fromdate': '',
#     'todate': '' ,
#     'rpJudgment' : '' ,
#     'captcha' : '' 
# }

# with open('file1.html' , 'w' ,encoding="utf-8") as f:
#     f.write(r.text)


json_data = r_captcha.json() #parse json response

base64_str = r_captcha['image'] #extract base64 string

image_data = base64.b64decode(base64_str) #decode base64 string to bytes
with open('captcha_image.png', 'wb') as f:
    f.write(image_data)
