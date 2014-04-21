import urllib, re
from urlparse import urlparse
var = raw_input("Enter the name of your subreddit: ")
o = urlparse(var)
if o.scheme == '':
    var = "".join(("http://reddit.com/r/", var))
source = urllib.urlopen(var).read()
while source[-7:] != '</html>':
    source = urllib.urlopen(var).read()
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
