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
│   ├── hexadecimal_decode.py<br>
│   ├── hexadecimal_encode.py<br>
│   ├── magic.py<br>
│   ├── rot13.py<br>
│   ├── rot47.py<br>
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
   git clone https://github.com/SavonChanserey/Mini-CyberChef.git<br>
   cd path/to/Mini-CyberChef<br>

2. Create a Virtual Environment:<br>
   python3 -m venv venv<br>

3. Activate the Virtual Environment
   - For macOS/Linux:<br> source venv/bin/activate<br>
   - For Window:<br> venv\Scripts\activate<br>
   
4. Install dependencies:
   pip install -r requirements.txt<br>
   <br>

5. Run the application:
   python3 main.py

**Note:** If you want to exit virtual environment: deactivate

# Usage examples

**Decode Base64:**<br>
- Input: SGVsbG8gd29ybGQh<br>
- Drag "From Base64" → "RUN RECIPE"<br>
- Output: Hello world!<br>

**Auto-detect encoding**<br>
- Input: ;K_$aOB (Base92-encoded "Hello")<br>
- Drag "Magic"<br>
- Output: [Base92] Hello

**Hash a string**<br>
- Input: password123<br>
- Drag "SHA256" → "RUN RECIPE"<br>
- Output: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
  
# Dependencies or libraries

- Python standard library — used for the GUI (Tkinter)<br>

- Listed in requirements.txt:<br>
   base58 — enables Base58 encode/decode operations<br>
   base45 — enables Base45 encode/decode operations<br>
   base92 — enables Base92 encode/decode operations<br>


