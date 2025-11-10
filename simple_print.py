import os
import subprocess
import tempfile
import time

# Path to the HTML file
html_file = os.path.abspath("vista_cfp.html")
pdf_file = os.path.abspath("vista_cfp.pdf")

# Check if Google Chrome exists
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if os.path.exists(chrome_path):
    try:
        print(f"Attempting to convert {html_file} to {pdf_file} using Chrome...")
        # Use Chrome to print to PDF
        cmd = [
            chrome_path,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--print-to-pdf=" + pdf_file,
            "file://" + html_file
        ]
        
        # Run the command
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(timeout=30)
        
        if process.returncode == 0:
            print(f"Successfully converted {html_file} to {pdf_file}")
        else:
            print(f"Error: {stderr.decode('utf-8')}")
            
    except Exception as e:
        print(f"Error: {e}")
else:
    print("Google Chrome not found. Please install Chrome or use another method.") 