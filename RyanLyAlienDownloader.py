import urllib, re
var = raw_input("Enter your URL to the subreddit: ")
if var[0:3] == "www":
    var = "".join(("http://",var))    
elif var[0:6] == "reddit":
    var = "".join(("http://www.",var))
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
raw_input("Press any key and enter to quit: ")
