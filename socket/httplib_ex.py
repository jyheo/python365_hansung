import httplib  # use import http.client for Python 3
import HTMLParser

conn = httplib.HTTPConnection('www.python.org')
conn.request('GET', '/index.html')
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
#print data1[:1024]
conn.close()

class MyHTMLParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.start_tag = ''
        
    def handle_starttag(self, tag, attrs):
        self.start_tag = tag
        
    def handle_endtag(self, tag):
        self.start_tag = ''
    
    def handle_data(self, data):
        #print "Encountered some data  :", data
        if self.start_tag == 'title':
            print 'TITLE: ', data
        elif self.start_tag == 'h1':
            print 'Heading 1: ', data

parser = MyHTMLParser()
parser.feed(data1)
