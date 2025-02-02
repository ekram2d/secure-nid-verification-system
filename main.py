import easyocr
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract
import numpy as np
from tabulate import tabulate
import re

def extract_data_with_easyocr(image_path, languages=['en', 'bn']):
    try:
        reader = easyocr.Reader(languages)
        results = reader.readtext(image_path)
        return [text for _, text, _ in results]
    except Exception as e:
        return [f"Error extracting data: {e}"]

def clean_ocr_text(texts):
    cleaned = []
    for text in texts:
        # Remove special characters and fix common OCR errors
        text = re.sub(r'[^a-zA-Z0-9\u0980-\u09FF\s:/.-]', '', text)
        # Fix common OCR misreads
        text = text.replace('7/F', 'T/A').replace('SHIT', 'SHAHID')
        cleaned.append(text.strip())
    return cleaned

def extract_key_fields(texts):
    key_fields = {
        'Name (Bengali)': '',
        'Name (English)': '',
        'Father': '',
        'Mother': '',
        'Date of Birth': '',
        'NID Number': ''
    }

    for text in texts:
        # Bengali name extraction
        if 'নাম:' in text:
            key_fields['Name (Bengali)'] = text.split('নাম:')[-1].strip()

        # English name extraction
        if 'Name:' in text:
            key_fields['Name (English)'] = text.split('Name:')[-1].strip()

        # Father's name extraction
        if 'পিতা:' in text:
            key_fields['Father'] = text.split('পিতা:')[-1].strip()

        # Mother's name extraction
        if 'মাতা:' in text:
            key_fields['Mother'] = text.split('মাতা:')[-1].strip()

        # Date of Birth extraction
        if re.match(r'\d{2} [A-Za-z]{3} \d{4}', text):
            key_fields['Date of Birth'] = text.strip()

        # NID Number extraction
        if 'IDNO:' in text:
            key_fields['NID Number'] = text.split('IDNO:')[-1].strip()

    return key_fields
def verify_images(img1_path, img2_path):
    """Verify if images are identical"""
    try:
        img1 = Image.open(img1_path).convert("RGB")
        img2 = Image.open(img2_path).convert("RGB")

        # Quick size check
        if img1.size != img2.size:
            return (False, "Size mismatch")

        # Pixel comparison
        if list(img1.getdata()) == list(img2.getdata()):
            return (True, "Identical images")

        # Content verification
        text1 = pytesseract.image_to_string(img1, lang='eng')
        text2 = pytesseract.image_to_string(img2, lang='eng')

        return (text1 == text2, "Content matches" if text1 == text2 else "Content differs")

    except Exception as e:
        return (False, f"Verification error: {str(e)}")
def show_extracted_texts(image1_path, image2_path):
    raw_text1 = extract_data_with_easyocr(image1_path)
    raw_text2 = extract_data_with_easyocr(image2_path)

    cleaned_text1 = clean_ocr_text(raw_text1)
    cleaned_text2 = clean_ocr_text(raw_text2)

    key_fields1 = extract_key_fields(cleaned_text1)
    key_fields2 = extract_key_fields(cleaned_text2)

    # Create comparison table
    table_data = [
        ["Name (Bengali)", key_fields1['Name (Bengali)'], key_fields2['Name (Bengali)']],
        # ["Name (English)", key_fields1['Name (English)'], key_fields2['Name (English)']],
        ["Father's Name", key_fields1['Father'], key_fields2['Father']],
        ["Mother's Name", key_fields1['Mother'], key_fields2['Mother']],
        ["Date of Birth", key_fields1['Date of Birth'], key_fields2['Date of Birth']],
        ["NID Number", key_fields1['NID Number'], key_fields2['NID Number']]
    ]

    print("\n=== Cleaned Data Comparison ===")
    print(tabulate(table_data,
                 headers=["Field", "Image 1", "Image 2"],
                 tablefmt="grid",
                 maxcolwidths=[None, 30, 30]))

def display_results(image1_path, image2_path):
    print("\n=== Image Verification ===")
    verification_result = verify_images(image1_path, image2_path)
    status_icon = "✅ valid nid" if  verification_result else "❌ not valid "
    print(f"Verification Status: {status_icon}")
    # print(f"Verification Result: {verification_msg}")
    print(f"\nImage Comparison Result: {verification_result}")

    show_images_comparison(image1_path, image2_path)
    show_extracted_texts(image1_path, image2_path)

if __name__ == "__main__":
    image1_path, image2_path = "nid1.jpg", "decrypted_id_card.jpg"
    display_results(image1_path, image2_path)