import requests
from bs4 import BeautifulSoup
import pdfkit
import os
import time
import re

# Base URL of the novel's website
base_url = "https://novelfire.docsachhay.net/book/overgeared/chapter-"

# Directory to save chapters as PDFs
output_dir = "light_novel_pdfs"
os.makedirs(output_dir, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

path_to_wkhtmltopdf = r"C:\Programming\wkhtmltopdf\bin\wkhtmltopdf.exe"  # Adjust path as needed
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

options = {
    'enable-local-file-access': None,
    'encoding': 'UTF-8',  # Ensure proper encoding
    'margin-top': '1mm',     # Remove top margin
    'margin-right': '0mm',   # Remove right margin
    'margin-bottom': '0mm',  # Remove bottom margin
    'margin-left': '0mm',    # Remove left margin
}

# Pattern to match unwanted strings
patternGoogle = re.compile(r"Google", re.IGNORECASE)
patternPatreon = re.compile(r"Patreon", re.IGNORECASE)

# Iterate over each chapter link
for chapter in range (2000, 2001):
    scraped_url = base_url + str(chapter)
    print(f"Chapter={chapter}, URL={scraped_url}")
    
    # Fetch the chapter page
    chapter_response = requests.get(scraped_url, headers=headers)

    chapter_soup = BeautifulSoup(chapter_response.content, 'html.parser')
    
    # Extract the HTML content of the chapter
    content_html = chapter_soup.select_one("div#content")  # Update selector

    # Iterate through all elements within the parent
    for element in content_html.find_all():  # Finds all descendants
        if element.string:  # Check if the string matches the pattern
            stringedElement = str(element.string)
            if patternPatreon.search(stringedElement):
                element.decompose()  # Remove the element if it 
            if patternGoogle.search(stringedElement):
                element.decompose()  # Remove the element if it 

    if content_html is None:
        print(f"Failed to scrape chapter={chapter}. Skipping..")
        continue


    # Convert to string for PDF conversion
    html_content = f"""
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="C:/Programming/Projects/scraping-overgeared/style.css">
            <title>Overgeared | Chapter {chapter}</title>
        </head>
        <body>
            <h3>Chapter {chapter}</h1>
            {content_html.prettify()}
        </body>
    </html>
    """

    # Save as PDF
    pdf_file = f"{output_dir}/{chapter}.pdf"
    pdfkit.from_string(html_content, pdf_file, configuration=config, options=options)

    time.sleep(1)  # Delay to avoid being blocked