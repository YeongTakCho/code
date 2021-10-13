html_doc="""
<html>
    <head>
    </head>
        <body>
            <p> hello </p>
            <p> good day </p>
        </body>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser') # <- html_doc은 파싱할 문서고, 'html.parser'는 파싱 방식이에요.

for p in soup.find_all('p'):
    print(p)