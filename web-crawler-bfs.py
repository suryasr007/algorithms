import queue

class WebCrawler(object):
    def __init__(self):
        self.q = queue.Queue()
        self.discoveredWebsiteList = list()

    def discover_web(self, root):
        self.queue.add(root);
        self.discoveredWebsiteList.append(root)

        while not q.empty():
            current_url = q.get()
            raw_html = read_url(current_url)

    


    def read_url(url):
