import requests
import base64


url_post_captcha = 'https://hcraj.nic.in/cishcraj-jdp/causelists/setgetcaptcha?'

r_captcha = requests.post(url_post_captcha)




json_data = r_captcha.json() #parse json response

base64_str = json_data['image'] #extract base64 string

image_data = base64.b64decode(base64_str) #decode base64 string to bytes
with open('captcha_image.png', 'wb') as f:
    f.write(image_data)
