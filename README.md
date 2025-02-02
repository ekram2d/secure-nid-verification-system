

```markdown
# Secure NID Verification System

## Overview
This project focuses on securely processing National ID (NID) images to protect sensitive information such as NID numbers. It uses OCR to extract the ID number, encrypts it using AES-256 encryption, and then modifies the image to hide the original ID number. The encrypted ID number is displayed on the image, and the system also allows decrypting and visualizing the modified image alongside the original.

## Features
- **OCR-based Data Extraction**: Extracts the NID number using EasyOCR.
- **AES-256 Encryption**: Encrypts the NID number to secure sensitive information.
- **Image Modification**: Replaces the NID number in the image with the encrypted ID.
- **Image Visualization**: Displays the original, modified, and decrypted ID card images side by side.
- **File Download**: Allows users to download the processed images.

## Technologies Used
- **Python** for the core logic
- **EasyOCR** for Optical Character Recognition (OCR) to extract the NID number
- **Cryptography** (Fernet) for AES-256 encryption
- **Pillow** for image manipulation
- **Matplotlib** for visualizing images
- **Google Colab** for easy setup and execution

## Running in Google Colab

Follow these steps to run the project in **Google Colab**:

### 1. Open Google Colab
Go to [Google Colab](https://colab.research.google.com/) and create a new notebook or use an existing one.

### 2. Clone the Repository
Clone the GitHub repository into your Colab environment by running this command:

```python
!git clone https://github.com/username/secure-nid-verification-system.git
```

### 3. Navigate to the Project Folder
After cloning, move into the project folder:

```python
%cd secure-nid-verification-system
```

### 4. Install Dependencies
Install the required dependencies by running:

```python
!pip install easyocr pytesseract Pillow cryptography matplotlib
```

### 5. Upload the NID Image
Upload your NID image (`nid1.jpg` or any other image you want to process). You can use this code to upload the image:

```python
from google.colab import files
uploaded = files.upload()
```

### 6. Run the Code
Run the script to process the NID image. The code will perform OCR, encrypt the ID number, modify the image, and visualize the results:

```python
!python main.py
```

The processed images will be saved and automatically downloaded to your local system.

### 7. Download the Processed Images
After running the script, the processed images (`original_id_card.jpg`, `modified_id_card.jpg`, and `decrypted_id_card.jpg`) will be available for download. You can download them using the Colab `files.download()` method:

```python
from google.colab import files

files.download("original_id_card.jpg")
files.download("modified_id_card.jpg")
files.download("decrypted_id_card.jpg")
```

### 8. Visualization
The images will also be displayed side by side, showing:
- The original ID card.
- The modified ID card with the encrypted ID.
- The decrypted image, showing the original NID card.

## Project Structure
```
secure-nid-verification-system/
│
├── main.py                  # Main script for processing NID images
├── nid1.jpg                 # Sample NID image (replace with your own)
├── decrypted_id_card.jpg    # Decrypted ID card image (generated after processing)
├── original_id_card.jpg     # Original NID card image (generated after processing)
└── requirements.txt         # List of required Python packages (optional)
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Notes:
1. **Replace `username`** in the GitHub URL (`https://github.com/username/secure-nid-verification-system.git`) with your actual GitHub username.
2. **Explanation of Workflow**: The README covers the workflow in Google Colab, including cloning the repo, installing dependencies, uploading the NID image, and running the script.
3. **Image Files**: `nid1.jpg`, `decrypted_id_card.jpg`, and others are placeholders, which can be updated as per your actual data.
4. **Visualization**: The script generates and visualizes the images in Colab, displaying them side by side.


