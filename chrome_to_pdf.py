import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def html_to_pdf(html_file, pdf_file):
    # Get absolute path
    html_path = os.path.abspath(html_file)
    pdf_path = os.path.abspath(pdf_file)
    
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # Set PDF print options
    appState = {
        "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": ""
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2,
        "isLandscapeEnabled": False,
        "isHeaderFooterEnabled": False
    }
    
    chrome_options.add_experimental_option('prefs', {
        'printing.print_preview_sticky_settings.appState': appState,
        'savefile.default_directory': os.path.dirname(pdf_path)
    })
    chrome_options.add_argument('--print-to-pdf=' + pdf_path)
    
    try:
        # Initialize Chrome driver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Load HTML file
        driver.get('file://' + html_path)
        
        # Wait for page to fully load
        time.sleep(2)
        
        # Print to PDF
        print_options = {
            'landscape': False,
            'displayHeaderFooter': False,
            'printBackground': True,
            'paperWidth': 8.27,  # A4 width in inches
            'paperHeight': 11.69,  # A4 height in inches
            'marginTop': 0.4,
            'marginBottom': 0.4,
            'marginLeft': 0.4,
            'marginRight': 0.4,
            'pageRanges': '1-'
        }
        
        # Use Chrome Dev Tools Protocol to print to PDF
        result = driver.execute_cdp_cmd('Page.printToPDF', print_options)
        
        # Save the PDF
        with open(pdf_path, 'wb') as f:
            f.write(bytes(result['data'], 'base64'))
        
        print(f"Successfully converted {html_file} to {pdf_path}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    html_to_pdf("vista_cfp.html", "vista_cfp.pdf") 