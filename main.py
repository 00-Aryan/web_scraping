import retreival
import captcha
import parser
import requests
import json

def main():
    s = requests.Session()

    captcha_text = captcha.fetch_captcha(s)
    json_data = retreival.fetch_url(s, captcha_text)
    judgements_data = parser.parse_html(json_data)
    with open("judgements.json", "w", encoding="utf-8") as f:
        json.dump(judgements_data, f, ensure_ascii=False, indent=2)
    
    parser.download_pdfs(judgements_data, s)

    

if __name__ == "__main__":
    main()
