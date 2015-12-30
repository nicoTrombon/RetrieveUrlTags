import urllib
from bs4 import BeautifulSoup

def main():
    url = raw_input('Enter url:')

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    #Retrieve a list of the anchor tags
    #Each tag is like a dict of HTML attributes

    tags = soup('a')

    for tag in tags:
        print tag.get('href', None)

if __name__ == '__main__':
    main()