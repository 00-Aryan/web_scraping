import retreival
import captcha
import requests

def main():
    s = requests.Session()
    url_get = 'https://hcraj.nic.in/cishcraj-jdp/JudgementFilters/'
 

    base_url =s.get(url_get)
    captcha_text = captcha.fetch_captcha(s)
    retreival.fetch_url(s, captcha_text)

    

if __name__ == "__main__":
    main()
