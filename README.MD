# Website Crawler

This Python script is designed to crawl a website and generate a site map by visiting each page and extracting all links within the same domain. The generated site map can be useful for search engine optimization (SEO) purposes or for understanding the structure of a website.

## Features

Visits each page of the website starting from a specified URL.
Extracts all links found on each page, filtering out external links to other domains.
Generates a site map containing a list of URLs along with the links found on each page.
Checks the status code of each requested page and prints a message if the status code is not 200 (OK).

## Installation

1. Сlone this repository to your local machine. 
2. Make sure you have Python 3 installed. 
3. Download actual chromedriver for your Chrome version and place it in project directory as a file named "chromedriver"
3. Install the required dependencies using pip install -r requirements.txt.

## USAGE

`
python3 main.py <WEBSITE_START_PAGE_URL>
`

## Example

`

`

```console
$ python3 crawl_site.py http://127.0.0.1:8000

Page: http://127.0.0.1:8000
Links on this page:
  - http://127.0.0.1:8000
  - http://127.0.0.1:8000/help/contacts/
Page: http://127.0.0.1:8000/help/contacts/
Links on this page:
  - http://127.0.0.1:8000/
  - http://127.0.0.1:8000/help/contacts/
  - http://127.0.0.1:8000/login/
  - http://127.0.0.1:8000/help/contacts/
Page: http://127.0.0.1:8000/
Links on this page:
  - http://127.0.0.1:8000/
  - http://127.0.0.1:8000/help/contacts/
Page: http://127.0.0.1:8000/login/
Links on this page:
  - http://127.0.0.1:8000/login/
  - http://127.0.0.1:8000/help/contacts/
Links on this page:
  - http://127.0.0.1:8000/
Pages with errors (status code != 200) 
  - http://127.0.0.1:8000/help/contacts/ - 500
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.