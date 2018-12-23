import urllib.reques
import lxml.html
from mastodon import Mastodon
from bs4 import BeautifulSoup


# Setup Mastodon with tokens

mastodon = Mastodon(
	access_token = 'token.secret',
	api_base_url = 'your_instance_url_here'
)

# Follow the random link generator and grab the redirected URL

with urllib.request.urlopen("http://yokai.com/?redirect_to=random") as random;
	URL = random.geturl()

# Format the redirect page using BeautifulSoup for scraping

soup = BeautifulSoup(urllib.request.urlopen(URL), 'lxml')

# Define the title of the page

title = soup.title.string

# Locate the first image in the page and download it for posting

image_source = soup.find_all('img')[0].get('src')

image = urllib.request.urlretrieve(image_source, "image.png")

# Define the name of the Yokai based on the title of the page, strip out trailing words

yokainame = title.replace(' – Yokai.com', '')

# Create the status to be posted

status = ("The Yōkai of the day is " + yokainame + ".\n \nArt and information by Matthew Meyer.\n" + "\n" + URL)

# Generate the dictionary for the downloaded picture to prepare it for upload

media = mastodon.media_post("image.png")

# Post the status

mastodon.status_post(status, media_ids = media)
