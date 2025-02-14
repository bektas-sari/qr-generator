# QR Code Generator (Python/Flask)

A simple and elegant web application built with Flask to generate QR codes from user-provided URLs.

## Features
- Enter a URL and generate a QR code instantly.
- Simple and modern UI with HTML & CSS.
- Built with Flask and `qrcode` library.
- Lightweight and easy to deploy.

## Installation

### 1. Clone the repository
```bash
git clone <GITHUB_REPO_URL>
cd qr_generator
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

The application will run on `http://127.0.0.1:5000/`.

## Usage
1. Open the web page.
2. Enter a URL in the input field.
3. Click the "Generate QR Code" button.
4. The QR code will be displayed on the screen.

## Dependencies
- Flask
- qrcode[pil]

## Project Structure
```
qr_generator/
│── static/
│   ├── style.css   # CSS file for styling
│── templates/
│   ├── index.html  # HTML file for UI
│── app.py          # Flask backend
│── requirements.txt
│── README.md
```

## License
This project is licensed under the MIT License.

## Contribution
Feel free to fork and enhance the project. 
Pull requests are welcome!

## Author
Developed by Bektas SARI
GitHub: bektas-sari 
Mail: bektas_sari@gmail.com

