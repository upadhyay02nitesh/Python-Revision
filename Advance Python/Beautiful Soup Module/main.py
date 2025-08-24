# What is BeautifulSoup?

# BeautifulSoup is a Python library used for parsing HTML and XML documents.

# It allows you to extract information from web pages easily.

# Often used in web scraping to get titles, links, tables, etc.


from bs4 import BeautifulSoup

html_doc = """
<html>
  <head><title>My Web Page</title></head>
  <body>
    <h1>Welcome to my website</h1>
    <p class="content">This is a paragraph.</p>
    <a href="https://example.com">Link</a>
  </body>
</html>
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_doc, "html.parser")

# Print the prettified HTML
print(soup.prettify())
# Access title tag
print(soup.title)          # <title>My Web Page</title>
print(soup.title.string)   # My Web Page

# Access first <p> tag
print(soup.p)              # <p class="content">This is a paragraph.</p>
print(soup.p.text)         # This is a paragraph.
print(soup.p['class'])     # ['content']

# Access href attribute of <a> tag
link = soup.a
print(link['href'])        # https://example.com
# Find all <p> tags
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.text)

# Find all links
links = soup.find_all('a')
for a in links:
    print(a['href'])
# Find by class
content = soup.select('.content')  # All elements with class "content"
print(content[0].text)
