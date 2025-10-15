# Credit Card Statement Parser

https://credit-card-parser.streamlit.app/

<img width="1082" height="799" alt="image" src="https://github.com/user-attachments/assets/cd163c48-19f3-4a50-a364-8ccc8c85f041" />



A simple web application built with Streamlit that parses credit card statements from PDF files and extracts key financial data points.

## Features

- **PDF Upload**: Upload credit card statement PDFs directly through the web interface.
- **Data Extraction**: Automatically extracts the following information:
  - Last 4 digits of the card number
  - Billing cycle start and end dates
  - Payment due date
  - Total balance
  - Minimum payment due
- **Data Display**: Presents extracted data in a clean table format.
- **Raw Text Preview**: Shows a preview of the extracted text for verification.
- **Sample Statements**: Includes sample PDFs from Capital One and Chase for testing.

## Installation

1. Clone or download this repository.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).
3. Upload a credit card statement PDF using the file uploader.
4. View the extracted data in the table below the uploader.
5. Check the raw text preview for additional context.

## Dependencies

- `pdfplumber`: For extracting text from PDF files.
- `PyPDF2`: Additional PDF processing capabilities.
- `streamlit`: Web application framework.
- `pandas`: Data manipulation and table display.


## Notes

- The parser uses regular expressions to identify and extract data, which may not work perfectly for all credit card statement formats.
- Ensure your PDFs are text-based (not image-based) for best results.
- This tool is for personal use and educational purposes; always verify extracted data manually.

## Contributing

Feel free to submit issues or pull requests if you find ways to improve the parsing accuracy or add support for additional credit card providers.
