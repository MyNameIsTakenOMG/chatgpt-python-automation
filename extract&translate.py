

import requests
from bs4 import BeautifulSoup
import html

#url of the webpage
url = 'https://www.example.com'

#make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

#parse the html content
soup = BeautifulSoup(html_content, "lxml")

#find all the headers
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

#translate the headers into spanish
translated_headers = []
for header in headers:
    translated_headers.append(html.unescape(header.text).translate(to='es'))

#save the headers into a html file
with open('headers.html', 'w') as f:
    f.write('<html>\n<head>\n</head>\n<body>\n')
    for header in translated_headers:
        f.write('<p>{}</p>\n'.format(header))
    f.write('</body>\n</html>')