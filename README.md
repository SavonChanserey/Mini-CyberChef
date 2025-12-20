# Project Title: Mini-CyberChef

# Description
Mini-CyberChef is a python cryptography tool that got inspired from cyberchef, and that is a lightweight and user-friendly tool that is easy to learn because the tool is simplified. The application has a graphical interface (GUI) that allows the users to encode, decode, and analyze the text without writing any type of code. It also has a magic feature which attempts to automatically find common encodings and tries to decode them.

# Project Structure

Mini-CyberChef/<br>
│<br>
│── main.py<br>
│<br>
│── gui/<br>
│   └── app.py                   
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
│   ├── charcode_decode.py<br>
│   ├── charcode_encode.py<br>
│   ├── count_chars.py<br>
│   ├── crc32.py<br>
│   ├── decimal_decode.py<br>
│   ├── decimal_encode.py<br>
│   ├── extracts_ip.py<br>
│   ├── extracts_url.py<br>
│   ├── hexadecimal_decode.py<br>
│   ├── hexadecimal_encode.py<br>
│   ├── html_entity_decode.py<br>
│   ├── html_entity_encode.py<br>
│   ├── lowercase.py<br>
│   ├── magic.py<br>
│   ├── md5.py<br>
│   ├── morsecode_decode.py<br>
│   ├── morsecode_encode.py<br>
│   ├── octal_decode.py<br>
│   ├── octal_encode.py<br>
│   ├── remove_duplicates.py<br>
│   ├── remove_whitespace.py<br>
│   ├── reverse_line.py<br>
│   ├── reverse_strings.py<br>
│   ├── rot13.py<br>
│   ├── rot47.py<br>
│   ├── sha1.py<br>
│   ├── sha256.py<br>
│   ├── sha512.py<br>
│   ├── uppercase.py<br>
│   ├── url_decode.py<br>
│   ├── url_encode.py<br>
│   ├── vigenere_decode.py<br>
│   ├── vigenere_encode.py<br>
│<br>
│── README.md<br>
│── requirements.txt<br>
│<br>
│── docs/<br>
│   ├── Savon_Chanserey_G2_Report.pdf<br>
│   └── Savon_Chanserey_G2_Report.docx


# Installation/setup instructions

1. Clone the Repository:<br>
   - git clone https://github.com/SavonChanserey/Mini-CyberChef.git<br>
   - cd path/to/Mini-CyberChef<br>

2. Create a Virtual Environment:<br>
   - python3 -m venv venv<br>

3. Activate the Virtual Environment
   - For macOS/Linux:<br> source venv/bin/activate<br>
   - For Window:<br> venv\Scripts\activate<br>
   
4. Install dependencies:
   - pip install -r requirements.txt<br>
   
5. Run the application:
   - python3 main.py<br>

To exit virtual environment: 
   - deactivate<br>

# Usage examples

**Base64:**<br>
- Input: SGVsbG8gd29ybGQh<br>
- Operation: From Base64
- Output: Hello world!<br>

**Auto-detect encoding**<br>
- Input: ;K_$aOB<br>
- Operation: Magic<br>
- Output: [Base92] Hello

**Hashing**<br>
- Input: password123<br>
- Drag "MD5" → "RUN RECIPE"<br>
- Output: 42f749ade7f9e195bf475f37a44cafcb

**Binary**<br>
- Loaf file: flag.txt (it contains some binary)<br>
- Operation: From Binary<br>
- Output: CTF{First_Flag}

# Dependencies or libraries

- Python Standard Libraries:<br>
   + Tkinter: Used to Create Graphical User Interface<br>
   + base64: base32, base64, base85 encoding and decoding<br>
   + binascii: Hexadecimal and binary conversions<br>
   + hashlib: Cryptographic hash functions<br>
   + re: Pattern matching for extraction features<br>
   + html: HTML entity encoding and decoding<br>
   + zlib: CRC32 checksum<br>

- External Libraries:<br>
   + base58: enables Base58 encode/decode operations<br>
   + base45: enables Base45 encode/decode operations<br>
   + base92: enables Base92 encode/decode operations<br>

- In requirements.txt:<br>
  + base58<br>
  + base92<br>
  + base45<br>


