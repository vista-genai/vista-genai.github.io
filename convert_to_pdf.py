import sys
from weasyprint import HTML

def html_to_pdf(html_file, pdf_file):
    HTML(html_file).write_pdf(pdf_file)
    print(f"Successfully converted {html_file} to {pdf_file}")

if __name__ == "__main__":
    html_to_pdf("vista_cfp.html", "vista_cfp.pdf") 