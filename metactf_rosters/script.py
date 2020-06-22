# This script parses a summary class list from Banner to generate the
#   users file for the CTF.  It parses the OdinId from the mailto: field
#   to use as a username and the last 4 digits from the OdinID via a regexp
#   (to use as the password)
from bs4 import BeautifulSoup
import re
html = open("list.html","r").read()
soup = BeautifulSoup(html, 'html.parser')
foo = soup.find_all(href=re.compile("mailto"))
bar = soup.find_all(string=re.compile("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"))
for i in range(len(bar)):
    x=re.split('[@:]',foo[i].attrs['href'])
    y=bar[i][-4:]
    print("{} {}".format(x[1],y))
