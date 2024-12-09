import requests
from bs4 import BeautifulSoup
    
# initialize the list of discovered urls
# with the first page to visit
urls = ["https://therealworld.net/"]
    
# until all pages have been visited
while len(urls) != 0:
    # get the page to visit from the list
    current_url = urls.pop()
    print(current_url)
    # crawling logic
    response = requests.get(current_url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    link_elements = soup.select("a[href]")
    for link_element in link_elements:
        url = link_element['href']
        if url.startswith('http') and url not in urls:
            urls.append(url)
