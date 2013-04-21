import urllib
import re

outfile = file("alien_image.png", "wb")
    
prompt = "Enter the subreddit url: "
url = raw_input(prompt)    

website = urllib.urlopen(url).read()
images = re.findall('img id=.*? src="(.*?)"', website)
alien = urllib.urlopen(images[0]).read()
outfile.write(alien)
outfile.close()
print "Alien Image Downloaded"