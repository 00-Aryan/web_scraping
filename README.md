# Rajasthan High Court Web Scraping & Data Automation

A robust, full-stack Python web scraping and data automation solution designed to extract public judicial records from the Rajasthan High Court (Principal Seat, Jodhpur) website. This project focuses on overcoming advanced server-side validation techniques to retrieve, parse, and structure judgment data into a clean, queryable CSV format.

## Key Achievements & Skills Demonstrated

- **Advanced Network Programming**: Successfully implemented Session Management using the `requests` library to maintain session state across multi-step requests, bypassing anti-scraping measures.
- **Two-Step Parsing**: Developed a highly reliable process to parse complex HTML responses containing embedded JSON data, followed by a secondary Beautiful Soup pass to extract the nested data table.
- **Security Bypass**: Engineered a solution to handle dynamic form validation, including Base64 Encoding/Decoding for date/payload parameters and integrating manual human input for CAPTCHA challenges.
- **Data Pipeline**: Created a clean and modularized workflow for data extraction, attribute capture, and output to a Pandas DataFrame for final Data Persistence to a CSV file.

## 🛠️ Technology Stack

- **Language**: Python 3.x
- **Core Libraries**:
  - `requests`: For handling HTTP requests and Session Management
  - `BeautifulSoup4`: For HTML Parsing and data extraction
  - `pandas`: For data manipulation and saving the final CSV output
  - `base64`, `json`, `datetime`, `os`: For encoding, file handling, and utility functions
  - `Pillow`: For CAPTCHA image display

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- Install required libraries:
```bash
pip install requests beautifulsoup4 pandas Pillow
```

### Execution

1. Run the main script:
```bash
python main.py
```

2. **Solve the CAPTCHA**:
   - The script will automatically open the `captcha_image.png` file on your desktop
   - The terminal will prompt you to `Enter captcha:`
   - Manually type the code from the image into the terminal and press Enter

3. **Output**: The script will execute the search, parse the results, and create the final file:
   - `rajasthan_high_court_judgments.csv` (Contains all structured judgment data)

## ⚙️ Data Extracted & Output Format

The script extracts all visible data from the table, along with hidden primary keys required for document retrieval.

| Column Name | Description | Source |
|------------|-------------|--------|
| Serial No | Sequential index of the record | Table Cell (TD) |
| Case Details | Full case type and parties (e.g., CRLA / 670 / 2016 SANJAY KUMAR Vs. STATE) | Table Cell (TD) |
| Hon'ble Justice | Name(s) of the presiding judge(s) | Table Cell (TD) |
| Order/Judgement Date | The date the judgment was passed (DD-Mon-YYYY) | Table Cell (TD) |
| Case Number | The hidden numeric identifier required for PDF retrieval (`data-caseno`) | Button Attribute |
| Order Number | The hidden order identifier required for PDF retrieval (`data-orderno`) | Button Attribute |
| Case Year | The hidden case year required for PDF retrieval (`data-cyear`) | Button Attribute |
| PDF Name | The generated filename for the corresponding downloaded PDF (`CaseNo_OrderNo_Year.pdf`) | Script-Generated |

## 🚧 Current Status & Future Improvements

**Status**: Core data retrieval and PDF downloading logic is functional and stable.

### Future Work (Bonus Requirement)

- **ML-Powered CAPTCHA Solver**: Implement a local Machine Learning model (e.g., using TensorFlow or scikit-learn) to automatically solve the CAPTCHA image, removing the need for manual input and enabling true end-to-end automation.

## 📄 License

This project is for educational and research purposes only. Please ensure compliance with the Rajasthan High Court's terms of service and applicable laws regarding web scraping.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📧 Contact

For questions or suggestions, please open an issue in this repository.
