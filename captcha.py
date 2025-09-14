import requests
import base64
import os
from PIL import Image

def fetch_captcha(session):
    url_post_captcha = 'https://hcraj.nic.in/cishcraj-jdp/causelists/setgetcaptcha?'

    r_captcha = session.post(url_post_captcha)

    json_data = r_captcha.json() #parse json response

    base64_str = json_data['image'] #extract base64 string

    image_data = base64.b64decode(base64_str) #decode base64 string to bytes


    with open('captcha_image.png', 'wb') as f:
        f.write(image_data)

    print("Captcha image saved as captcha_image.png")
    image_path = os.path.abspath('captcha_image.png')
    img = Image.open(image_path)
    img.show()
    
    captcha = input("Enter captcha: ")

    return captcha

if __name__ == "__main__":
    fetch_captcha()