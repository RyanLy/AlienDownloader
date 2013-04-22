import urllib, re
from urlparse import urlparse
var = raw_input("Enter your URL to the subreddit: ")
o = urlparse(var)
if o.scheme == '':
    var = "".join(("http://", var))
source = urllib.urlopen(var).read()
a = 0
while len(source) <= 12000:
    source = urllib.urlopen(var).read()
    a = a+1
    if a == 100:
        break
m = source.find('id=\'header-img\'',0)
if m == -1:
    print("Sorry!  Unable to find the image. Please check if link is valid or try again.")
else:
    m = source.find('"',m)
    n = source.find('"',m+1)
    link = source[m+1:n]
    urllib.urlretrieve(link, 'Alien.jpg')
    print("Your file has been downloaded into the same directory as this program.")
    print("The file is named alien.jpg")
raw_input("Press enter to quit: ")
