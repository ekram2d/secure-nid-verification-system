![verifaction_result](https://github.com/user-attachments/assets/6928e4d9-00a8-45d7-8e39-548fe08fe8a5)

---

# Secure NID Verification System

This project is designed to extract key fields from NID images using Optical Character Recognition (OCR), compare two NID images for verification, and ensure data integrity. The system uses `EasyOCR` for text extraction, cleans up OCR results, compares key fields like Name, Father’s Name, and NID number, and verifies whether two images are identical or contain the same information.

## Features

- **OCR Text Extraction**: Uses `EasyOCR` to extract text from NID images in multiple languages (Bengali and English).
- **Text Cleaning**: Automatically cleans and fixes common OCR misreads.
- **Key Field Extraction**: Extracts fields like Name (Bengali), Father’s Name, Mother’s Name, Date of Birth, and NID Number.
- **Image Comparison**: Verifies if two images are identical or contain the same text.
- **Data Comparison**: Displays a side-by-side comparison of key fields between two NID images.

## Requirements

Before running the script, ensure you have the following libraries installed:

```bash
pip install easyocr matplotlib pytesseract tabulate numpy
```

## Files

- `main.py`: Main Python script containing the logic for OCR extraction, image comparison, and data extraction.
- `nid1.jpg`: Example NID image for testing.
- `decrypted_id_cardS.jpg`: Example image for comparison.

## How to Run in Google Colab

### Step 1: Upload the files to Google Colab
1. Upload the `main.py`, `nid1.jpg`, and `decrypted_id_cardS.jpg` files to your Google Colab environment.

### Step 2: Install Dependencies
Install the required dependencies in the Colab environment:

```python
!pip install easyocr matplotlib pytesseract tabulate numpy
```

### Step 3: Upload Images for Testing
You can upload images directly in Colab using the following code:

```python
from google.colab import files
uploaded = files.upload()
```

### Step 4: Run the Script
After uploading the necessary files and images, run the script to extract and compare data:

```python
!python main.py
```

### Step 5: View Results
- The script will display a side-by-side comparison of the two images.
- It will also print a table comparing the extracted fields between the two images.

## Script Functions

### `extract_data_with_easyocr(image_path, languages=['en', 'bn'])`
- **Purpose**: Extracts text from the provided image using `EasyOCR`.
- **Parameters**: 
  - `image_path`: Path to the image to extract text from.
  - `languages`: List of languages for OCR, default is English and Bengali.
- **Returns**: List of extracted text.

### `clean_ocr_text(texts)`
- **Purpose**: Cleans up the OCR text by removing unwanted characters and fixing common OCR misreads.
- **Parameters**: 
  - `texts`: List of OCR-extracted texts.
- **Returns**: Cleaned text list.

### `extract_key_fields(texts)`
- **Purpose**: Extracts key fields such as Name, Father's Name, Mother's Name, Date of Birth, and NID Number from the OCR text.
- **Parameters**:
  - `texts`: List of cleaned OCR texts.
- **Returns**: Dictionary with extracted fields.

### `verify_images(img1_path, img2_path)`
- **Purpose**: Verifies if two images are identical by checking their pixel values and OCR-extracted content.
- **Parameters**:
  - `img1_path`: Path to the first image.
  - `img2_path`: Path to the second image.
- **Returns**: Tuple containing verification status and message.

### `show_extracted_texts(image1_path, image2_path)`
- **Purpose**: Displays a comparison of the extracted key fields between two images.
- **Parameters**:
  - `image1_path`: Path to the first image.
  - `image2_path`: Path to the second image.
- **Returns**: Printed comparison table.

### `show_images_comparison(img1_path, img2_path)`
- **Purpose**: Displays the two images side-by-side for visual comparison.
- **Parameters**:
  - `img1_path`: Path to the first image.
  - `img2_path`: Path to the second image.
- **Returns**: None (Displays images in a grid).

## Example Output
![verifaction_result](https://github.com/user-attachments/assets/35a2b705-ef57-4b6b-84a9-4845087a0d8a)

After running the script, you will see:

- **Verification status**: Whether the two images are identical or not.
- **Key Fields Comparison**: A table comparing the Name, Father’s Name, Mother’s Name, Date of Birth, and NID Number.
- **Image Comparison**: A side-by-side visual comparison of the two images.

### Example Table Output:
```plaintext
=== Cleaned Data Comparison ===
+---------------------+---------------------+---------------------+
| Field               | Image 1             | Image 2             |
+---------------------+---------------------+---------------------+
| Name (Bengali)      | Shahid              | Shahid              |
| Father's Name       | Akash               | Akash               |
| Mother's Name       | Jahanara            | Jahanara            |
| Date of Birth       | 15 Jul 1995         | 15 Jul 1995         |
| NID Number          | 1234567890123       | 1234567890123       |
+---------------------+---------------------+---------------------+
```



## License

This project is licensed under the MIT License.

---

This `README.md` provides a clear explanation of how to use the project, what the functions do, and how to set it up and run it in Google Colab.
