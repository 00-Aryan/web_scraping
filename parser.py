from bs4 import BeautifulSoup
import base64
import os
import json

def parse_html(json_data):
    html_content = json_data.get("html", "")
    soup = BeautifulSoup(html_content, 'html.parser')

    table = soup.find('table')
    if not table:
        print("No table found in the HTML content.")
        return []

    rows = table.find('tbody').find_all('tr')
    judgements_data = []

    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 1:
            serial_no = cols[0].get_text(strip=True)
            case_details = cols[1].get_text(" ", strip=True)
            honable_justice = cols[2].get_text(strip=True)
            order_judgement_date = cols[3].get_text(strip=True)

            buttons = cols[-1].find_all('button')
            caseno, orderno, cyear = "", "", ""
            if buttons:
                caseno = buttons[0].get("data-caseno")
                orderno = buttons[0].get("data-orderno")
                cyear = buttons[0].get("data-cyear")

            row_data = {
                "Serial No": serial_no,
                "Case Details": case_details,
                "Hon'ble Justice": honable_justice,
                "Order/Judgement Date": order_judgement_date,
                "Case No": caseno,
                "Order No": orderno,
                "Case Year": cyear,
            }
            judgements_data.append(row_data)

    return judgements_data


def download_pdfs(judgements_data, session):
    os.makedirs("pdfs", exist_ok=True)

    for case in judgements_data:
        caseno = case["Case No"]
        orderno = case["Order No"]
        cyear = case["Case Year"]

        if not caseno or not orderno or not cyear:
            print(f"Skipping case due to missing data: {case}")
            continue

        data = {
            "fileyear": base64.b64encode(cyear.encode()).decode(),
            "filename": base64.b64encode(f"{caseno}_{orderno}.pdf".encode()).decode()
        }

        url = "https://hcraj.nic.in/cishcraj-jdp/DwonloadOrdJud.php"
        r = session.post(url, data=data)

        if r.text != "NAN":
            file_url = f"https://hcraj.nic.in/cishcraj-jdp/{r.text}"
            pdf_response = session.get(file_url)


            filename = os.path.join("pdfs", f"{caseno}_{orderno}_{cyear}.pdf")
            with open(filename, "wb") as f:
                f.write(pdf_response.content)
        else:
            print(f"⚠️ No file found for {caseno}")
