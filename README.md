# scraping-light-novels
## DISCLAIMER
The purpose of this project is only to centralize my favourite light novels and make them available offline (by downloading the result). I can guarantee the usage of this project is for personal use only, if someday you find me (not including anyone who forks this repository) abusing this project for commercialization then you can hit me up at cocabc1@gmail.com.

## List of Novels
- [Overgeared](https://novelfire.docsachhay.net/book/overgeared)

## Requirements
- Python 3.X
- [Pdfkit](https://pypi.org/project/pdfkit/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [PyPdf2](https://pypi.org/project/PyPDF2/)
- [Wkhtmltopdf](https://wkhtmltopdf.org/)

## How to Use
- Download/clone this repository.
- Install the necessary language and the libraries.
- Adjust line 20 on `scrape.py` to where you save wkhtmltopdf binary file.
- Adjust line 37 on `scrape.py` to range what chapter you want scrape.
- Run `python scrape.py`
- Adjust line 10 and 11 on `merge.py` accordingly to modify how many chapter in one file and the start of the chapter.
- Run `python merge.py`
