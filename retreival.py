import requests
import base64
from datetime import date, timedelta
import json

def fetch_url(session, captcha):
    toDate = date.today().strftime('%d/%m/%Y')
    fromDate = (date.today() - timedelta(days=10)).strftime('%d/%m/%Y')

    data = {
        'todate': base64.b64encode(toDate.encode()).decode(),
        'fromdate': base64.b64encode(fromDate.encode()).decode(),
        'urg_ord': base64.b64encode(b"0").decode(),
        'casetype': base64.b64encode(b"0").decode(),
        'petres': base64.b64encode(b"0").decode(),
        'partyname': base64.b64encode(b'').decode(),
        'advctname': base64.b64encode(b'').decode(),
        'judgecode': base64.b64encode(b"0").decode(),
        'bench': base64.b64encode(b"A").decode(),
        'rpJudgment': base64.b64encode(b"Y").decode(),
        'pilJudgement': base64.b64encode(b"A").decode(),
        'judgeOrder': base64.b64encode(b"A").decode(),
        'searchText': base64.b64encode(b'undefined').decode(),
        'citationyear': base64.b64encode(b'2025').decode(),
        'citationdigits': base64.b64encode(b'').decode(),
        'captcha': captcha,
        'queryType': 'getRecord',
        'requestType': 'data',
    }

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://hcraj.nic.in",
        "Referer": "https://hcraj.nic.in/cishcraj-jdp/JudgementFilters/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
    }

    url_post = "https://hcraj.nic.in/cishcraj-jdp/judgement-filters/getrecord"

    response = session.post(url_post, data=data, headers=headers)


    json_response = response.json()
       
    return json_response
