import subprocess
import sys
import os

def generate_pdf(html_file, pdf_file):
    """
    Converts an HTML file to a PDF using Google Chrome's headless mode.
    """
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    
    if not os.path.exists(chrome_path):
        print("Error: Google Chrome not found at the specified path.")
        return

    if not os.path.exists(html_file):
        print(f"Error: HTML file not found at {html_file}")
        return

    html_file_abs = os.path.abspath(html_file)
    pdf_file_abs = os.path.abspath(pdf_file)

    command = [
        chrome_path,
        '--headless',
        '--disable-gpu',
        '--no-pdf-header-footer',
        '--print-to-pdf=' + pdf_file_abs,
        f'file://{html_file_abs}'
    ]

    try:
        print(f"Generating PDF for: {html_file}")
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"Successfully created PDF: {pdf_file_abs}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating PDF:")
        print(f"Command: {' '.join(e.cmd)}")
        print(f"Return code: {e.returncode}")
        print(f"Output:\n{e.stdout}")
        print(f"Error Output:\n{e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_final_pdf.py <input_html_file> <output_pdf_file>")
        sys.exit(1)
    
    input_html = sys.argv[1]
    output_pdf = sys.argv[2]
    
    generate_pdf(input_html, output_pdf) 