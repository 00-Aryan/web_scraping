from bs4 import BeautifulSoup
import re
import json
import base64
import os



def parse_html(json_data, session):
    html_content = json_data.get("html", "")
    soup = BeautifulSoup(html_content, 'html.parser')

    table = soup.find('table')
    if not table:
        print("No table found in the HTML content.")
        return

    rows = table.find('tbody').find_all('tr')

    for row in rows:    
        cols = row.find_all('td')
        serial_no = cols[0].get_text(strip=True)
        case_details = cols[1].get_text(" ", strip=True)
        honable_justice = cols[2].get_text(strip=True)
        order_judgement_date = cols[3].get_text(strip=True)

        
        buttons = cols[-1].find_all('button')

        for btn in buttons:
            caseno = btn.get("data-caseno")
            orderno = btn.get("data-orderno")
            cyear = btn.get("data-cyear")

            
            data = {
                "fileyear": base64.b64encode(cyear.encode()).decode(),
                "filename": base64.b64encode(f"{caseno}_{orderno}.pdf".encode()).decode()
            }

            url = "https://hcraj.nic.in/cishcraj-jdp/DwonloadOrdJud.php"
            r = session.post(url, data=data)

            if r.text != "NAN":
                file_url = f"https://hcraj.nic.in/cishcraj-jdp/{r.text}"

                pdf_response = session.get(file_url)
                if pdf_response.status_code == 200:

                    os.makedirs("pdfs", exist_ok=True)
                    filename = os.path.join("pdfs", f"{caseno}_{orderno}_{cyear}.pdf")

                    with open(filename, "wb") as f:
                        f.write(pdf_response.content)
                else:
                    print(f"Failed to download PDF for {caseno}")
            else:
                print(f"No file found for {caseno}")