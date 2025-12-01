# Project Title: Mini-CyberChef

# Description
Mini-CyberChef is a python cryptography tool that got inspired from cyberchef, and that is a lightweight and user-friendly tool that is easy to learn because the tool is simplified. The application has a graphical interface (GUI) that allows the users to encode, decode, and analyze the text without writing any type of code. It also has a magic feature which attempts to automatically find common encodings and tries to decode them.

# Project Structure

Mini-CyberChef/<br>
│<br>
│── main.py<br>
│<br>
│── gui/<br>
│   └── app.py                   # Main GUI<br>
│<br>
│── operations/<br>
│   ├── bacon_decode.py<br>
│   ├── bacon_encode.py<br>
│   ├── base32_decode.py<br>
│   ├── base32_encode.py<br>
│   ├── base45_decode.py<br>
│   ├── base45_encode.py<br>
│   ├── base58_decode.py<br>
│   ├── base58_encode.py<br>
│   ├── base62_decode.py<br>
│   ├── base62_encode.py<br>
│   ├── base64_decode.py<br>
│   ├── base64_encode.py<br>
│   ├── base85_decode.py<br>
│   ├── base85_encode.py<br>
│   ├── base92_decode.py<br>
│   ├── base92_encode.py<br>
│   ├── binary_decode.py<br>
│   ├── binary_encode.py<br>
│   ├── hexadecimal_decode.py<br>
│   ├── hexadecimal_encode.py<br>
│   ├── magic.py<br>
│   ├── rot13.py<br>
│   ├── rot47.py<br>
│   ├── vigenere_decode.py<br>
│   ├── vigenere_encode.py<br>
│   └── xor.py<br>
│<br>
│── README.md<br>
│── requirements.txt<br>
│<br>
│── docs/<br>
│   ├── Savon_Chanserey_G2_Report.pdf<br>
│   └── Savon_Chanserey_G2_Report.docx


# Installation/setup instructions

1. Clone the Repository:
   git clone https://github.com/SavonChanserey/Mini-CyberChef.git

2. Install dependencies:
   pip install -r requirements.txt<br>
   <br>
   Note: In requirements.txt include pyperclip (clipboard copy support), Pillow (GUI images/icons support)

3. Run the application:
   python3 main.py



# Usage examples

# Dependencies or libraries



