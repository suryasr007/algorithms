import queue
import requests
from bs4 import BeautifulSoup


class WebCrawler(object):
    def __init__(self):
        self.q = queue.Queue()
        self.discoveredWebsiteList = list()

    def discover_web(self, root):
        self.q.put(root)
        self.discoveredWebsiteList.append(root)

        while not self.q.empty():
            current_url = self.q.get()
            raw_html_links = self.read_url(current_url)

            for link in raw_html_links:
                if link not in self.discoveredWebsiteList:
                    self.discoveredWebsiteList.append(link)
                    print(link)
                    self.q.put(link)
                    


    def read_url(self, url):
        try:
            page = requests.get(url)
        except:
            return
        
        if page.status_code != 200:
            return
        
        soup = BeautifulSoup(page.content, 'html.parser')

        all_links = []
        
        for item in soup.find_all('a', href=True):
            if item['href'][:4] == "http":
               all_links.append(item['href']) 
        return all_links