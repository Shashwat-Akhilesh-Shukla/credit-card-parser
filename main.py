import re
import json
import pdfplumber

def parse_credit_card_statement(pdf_path: str):
    """
    Extracts 5 key data points from a credit card statement PDF.
    Returns a dictionary with:
      - card_last4
      - billing_cycle (start, end)
      - payment_due_date
      - total_balance
      - min_payment_due
    """
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    text = text.replace("\r", "").strip()
    RE_DATE = r"(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4})"
    RE_MONEY = r"\$?[\d,]+\.\d{2}"
    data = {}
    match_last4 = re.search(r"(?:ending in|Account(?: Number)?[:\s]*)(?:[Xx\* ]*)(\d{4})", text, re.IGNORECASE)
    data["card_last4"] = match_last4.group(1) if match_last4 else None
    match_cycle = re.search(r"(?:Opening/Closing Date|Statement Period)[^\d]*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\D+(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})", text, re.IGNORECASE)
    data["billing_cycle"] = [match_cycle.group(1), match_cycle.group(2)] if match_cycle else None
    match_due = re.search(r"Payment Due Date[:\s]*(" + RE_DATE + ")", text, re.IGNORECASE)
    data["payment_due_date"] = match_due.group(1) if match_due else None
    match_total = re.search(r"(?:New Balance|Total Balance|Amount Due)[:\s]*\$?([\d,]+\.\d{2})", text, re.IGNORECASE)
    data["total_balance"] = match_total.group(1) if match_total else None
    match_min = re.search(r"Minimum Payment(?: Due)?[:\s]*\$?([\d,]+\.\d{2})", text, re.IGNORECASE)
    data["min_payment_due"] = match_min.group(1) if match_min else None
    data["raw_text_preview"] = text[:300] + "..." if len(text) > 300 else text
    return data



if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python simple_pdf_parser.py <path_to_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    result = parse_credit_card_statement(pdf_path)
    print(json.dumps(result, indent=2))
