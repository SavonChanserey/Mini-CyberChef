# Project Title: Mini-CyberChef

# Description
Mini-CyberChef is a python cryptography tool that got inspired from cyberchef for encoding and decoding text. Users can use specific operation such as base64, hex, xor and more or use the magic function that automatic analyze the ciphertext related to. 

# Project Structure

Mini-CyberChef/<br>
│── gui/<br>
│   └── app.py                 # Main GUI<br>
│<br>
│── operations/<br>
│   ├── bacon.py<br>
│   ├── base32.py<br>
│   ├── base45.py<br>
│   ├── base58.py<br>
│   ├── base62.py<br>
│   ├── base64.py<br>
│   ├── base85.py<br>
│   ├── base92.py<br>
│   ├── binary.py<br>
│   ├── hexadecimal.py          
│   ├── magic.py          
│   ├── rot13.py<br> 
│   ├── rot47.py   
│   ├── vigenere.py    
│   └── xor.py<br>       
│<br>
│── README.md<br>
│── requirements.txt<br>
│── docs/<br>
│   └── Savon_Chanserey_G2_Report.pdf<br>
│   └── Savon_Chanserey_G2_Report.docx<br>

# Installation/setup instructions

1. Clone the Repository:
   git clone https://github.com/SavonChanserey/Mini-CyberChef.git

2. Install dependencies:
   pip install -r requirements.txt<br>
   <br>
   Note: In requirements.txt include pyperclip (clipboard copy support), Pillow (GUI images/icons support)

3. Run the application
   python3 gui/app.py



# Usage examples

# Dependencies or libraries



