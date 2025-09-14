import requests
import base64
from datetime import date, timedelta


def fetch_url(session, captcha):

    toDate = date.today().strftime('%d/%m/%Y')
    fromDate = (date.today() - timedelta(days=10)).strftime('%d/%m/%Y')
    # url_get = 'https://hcraj.nic.in/cishcraj-jdp/JudgementFilters/'
 

    # base_url =session.get(url_get)
    # print(base_url.headers) 

    # with open('base_url.html' , 'w' ,encoding="utf-8") as f:
    #     f.write(base_url.text)
    # print("file created as base_url.html")

    data = {
       'todate' : base64.b64encode(toDate.encode('utf-8')).decode('utf-8'),
       'fromdate' : base64.b64encode(fromDate.encode('utf-8')).decode('utf-8'),
       'urg_ord': base64.b64encode(b"0").decode('utf-8'),
       'casetype':  base64.b64encode(b"0").decode('utf-8'),
       'petres':  base64.b64encode(b"0").decode('utf-8'),
       'partyname':base64.b64encode(b'').decode('utf-8'),
       'advctname':base64.b64encode(b'').decode('utf-8'),
       'judgecode': base64.b64encode(b"0").decode('utf-8'),
       'bench':  base64.b64encode(b"A").decode('utf-8'),
       'rpJudgment' : base64.b64encode(b"Y").decode('utf-8'),
       'pilJudgement': base64.b64encode(b"A").decode('utf-8'),
       'judgeOrder':base64.b64encode(b"A").decode('utf-8'),
       'searchText':base64.b64encode(b'undefined').decode('utf-8'),
       'citationyear' :base64.b64encode(b'2025').decode('utf-8'),
       'citationdigits':base64.b64encode(b'').decode('utf-8'),
       'captcha': captcha,
       'queryType':'getRecord',
       'requestType':'data',
   }

    url_post = 'https://hcraj.nic.in/cishcraj-jdp/judgement-filters/getrecord'

    response = session.post(url_post , data=data)
    print(response.status_code)
    print(response.headers) 

    with open('response.html' , 'w' ,encoding="utf-8") as f:
        f.write(response.text)    
    print("file created as response.html")

    
# if __name__ == "__main__":
#     fetch_url()

