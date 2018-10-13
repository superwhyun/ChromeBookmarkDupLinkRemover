
#
# Pre-requisites
#   - pip3 install beautifulsoup4
# Steps
    # 0. In bookmark editor of chrome, put high-priority links/folders at the front of the bookmark bar
    # 1. export bookmark from chrome
    # 2. python app.py
    # 3. import new bookmark to chrome
# simple.
#


import subprocess
from bs4 import BeautifulSoup as bs


bookmark_filename = "bookmark.html"
bookmark_clean_filename = "bookmark_clean.html"


linkdic = dict()
def is_duplicated(link, desc):
    if(linkdic.get(link) is None and desc is not None):
        print("updating dic for ", link, desc)
        # linkdic.update({link, 'desc'})
        linkdic[link] = desc
        return False
    elif(linkdic.get(link) is not None):
        return True


fd = open(bookmark_clean_filename, 'w')
cnt=1
with open(bookmark_filename) as file:
        for line in file:
            # print(cnt, " line ")
            soup = bs(line)
            links = soup.findAll('a')

            if(len(links)==0):
                fd.write(line)
            else:
                for link in links:
                    if(is_duplicated(link.get('href'), link.string)):
                        # print(link.string, ":", link.get('href'))
                        # print('Duplicated')
                        pass
                    else:
                        fd.write(line)
            cnt=cnt+1

print("completed")                                  
fd.close()





        